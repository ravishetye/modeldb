# -*- coding: utf-8 -*-

import datetime
import glob
import inspect
import json
import numbers
import os
import re
import string
import subprocess
import sys
import threading
import time

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value, ListValue, Struct, NULL_VALUE

from ..external import six
from ..external.six.moves.urllib.parse import urljoin  # pylint: disable=import-error, no-name-in-module

from .._protos.public.modeldb import CommonService_pb2 as _CommonService

try:
    import pandas as pd
except ImportError:  # pandas not installed
    pd = None

try:
    import tensorflow as tf
except ImportError:  # TensorFlow not installed
    tf = None

try:
    import ipykernel
except ImportError:  # Jupyter not installed
    pass
else:
    try:
        from IPython.display import Javascript, display
        try:  # Python 3
            from notebook.notebookapp import list_running_servers
        except ImportError:  # Python 2
            import warnings
            from IPython.utils.shimmodule import ShimWarning
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=ShimWarning)
                from IPython.html.notebookapp import list_running_servers
            del warnings, ShimWarning  # remove ad hoc imports from scope
    except ImportError:  # abnormally nonstandard installation of Jupyter
        pass


try:
    import numpy as np
except ImportError:  # NumPy not installed
    np = None
    BOOL_TYPES = (bool,)
else:
    BOOL_TYPES = (bool, np.bool_)

_GRPC_PREFIX = "Grpc-Metadata-"

_VALID_HTTP_METHODS = {'GET', 'POST', 'PUT', 'DELETE'}
_VALID_FLAT_KEY_CHARS = set(string.ascii_letters + string.digits + '_-/')

THREAD_LOCALS = threading.local()
THREAD_LOCALS.active_experiment_run = None

SAVED_MODEL_DIR = "/app/tf_saved_model/"

# TODO: remove this in favor of _config_utils when #635 is merged
HOME_VERTA_DIR = os.path.expanduser(os.path.join('~', ".verta"))


class Connection:
    def __init__(self, scheme=None, socket=None, auth=None, max_retries=0, ignore_conn_err=False):
        """
        HTTP connection configuration utility struct.

        Parameters
        ----------
        scheme : {'http', 'https'}, optional
            HTTP authentication scheme.
        socket : str, optional
            Hostname and port.
        auth : dict, optional
            Verta authentication headers.
        max_retries : int, default 0
            Maximum number of times to retry a request on a connection failure. This only attempts retries
            on HTTP codes {502, 503, 504} which commonly occur during back end connection lapses.
        ignore_conn_err : bool, default False
            Whether to ignore connection errors and instead return successes with empty contents.

        """
        self.scheme = scheme
        self.socket = socket
        self.auth = auth
        # TODO: retry on 404s, but only if we're sure it's not legitimate e.g. from a GET
        self.retry = Retry(total=max_retries,
                           backoff_factor=1,  # each retry waits (2**retry_num) seconds
                           method_whitelist=False,  # retry on all HTTP methods
                           status_forcelist=(502, 503, 504),  # only retry on these status codes
                           raise_on_redirect=False,  # return Response instead of raising after max retries
                           raise_on_status=False)  # return Response instead of raising after max retries
        self.ignore_conn_err = ignore_conn_err


class Configuration:
    def __init__(self, use_git=True, debug=False):
        """
        Client behavior configuration utility struct.

        Parameters
        ----------
        use_git : bool, default True
            Whether to use a local Git repository for certain operations.

        """
        self.use_git = use_git
        self.debug = debug


class LazyList(object):
    # number of items to fetch per back end call in __iter__()
    _ITER_PAGE_LIMIT = 100

    def __init__(self, conn, conf, msg, endpoint, rest_method):
        self._conn = conn
        self._conf = conf
        self._msg = msg  # protobuf msg used to make back end calls
        self._endpoint = endpoint
        self._rest_method = rest_method

    def __getitem__(self, index):
        if isinstance(index, int):
            # copy msg to avoid mutating `self`'s state
            msg = self._msg.__class__()
            msg.CopyFrom(self._msg)
            msg.page_limit = 1
            if index >= 0:
                # convert zero-based indexing into page number
                msg.page_number = index + 1
            else:
                # reverse page order to index from end
                msg.ascending = not msg.ascending  # pylint: disable=no-member
                msg.page_number = abs(index)

            response_msg = self._call_back_end(msg)

            records = self._get_records(response_msg)
            if (not records
                    and msg.page_number > response_msg.total_records):  # pylint: disable=no-member
                raise IndexError("index out of range")
            id_ = records[0].id

            return self._create_element(id_)
        else:
            raise TypeError("index must be integer, not {}".format(type(index)))

    def __iter__(self):
        # copy msg to avoid mutating `self`'s state
        msg = self._msg.__class__()
        msg.CopyFrom(self._msg)
        msg.page_limit = self._ITER_PAGE_LIMIT
        msg.page_number = 0  # this will be incremented as soon as we enter the loop

        seen_ids = set()
        total_records = float('inf')
        while msg.page_limit*msg.page_number < total_records:  # pylint: disable=no-member
            msg.page_number += 1  # pylint: disable=no-member

            response_msg = self._call_back_end(msg)

            total_records = response_msg.total_records

            ids = self._get_ids(response_msg)
            for id_ in ids:
                # skip if we've seen the ID before
                if id_ in seen_ids:
                    continue
                else:
                    seen_ids.add(id_)

                yield self._create_element(id_)

    def __len__(self):
        # copy msg to avoid mutating `self`'s state
        msg = self._msg.__class__()
        msg.CopyFrom(self._msg)
        msg.page_limit = msg.page_number = 1  # minimal request just to get total_records

        response_msg = self._call_back_end(msg)

        return response_msg.total_records

    def _call_back_end(self, msg):
        data = proto_to_json(msg)

        if self._rest_method == "GET":
            response = make_request(
                self._rest_method,
                self._endpoint.format(self._conn.scheme, self._conn.socket),
                self._conn, params=data,
            )
        elif self._rest_method == "POST":
            response = make_request(
                self._rest_method,
                self._endpoint.format(self._conn.scheme, self._conn.socket),
                self._conn, json=data,
            )
        raise_for_http_error(response)

        response_msg = json_to_proto(response.json(), msg.Response)
        return response_msg

    def _get_ids(self, response_msg):
        return (record.id for record in self._get_records(response_msg))

    def _get_records(self, response_msg):
        """Get the attribute of `response_msg` that is not `total_records`."""
        raise NotImplementedError

    def _create_element(self, id_):
        """Instantiate element to return to user."""
        raise NotImplementedError


def make_request(method, url, conn, **kwargs):
    """
    Makes a REST request.

    Parameters
    ----------
    method : {'GET', 'POST', 'PUT', 'DELETE'}
        HTTP method.
    url : str
        URL.
    conn : Connection
        Connection authentication and configuration.
    **kwargs
        Parameters to requests.request().

    Returns
    -------
    requests.Response

    """
    if method.upper() not in _VALID_HTTP_METHODS:
        raise ValueError("`method` must be one of {}".format(_VALID_HTTP_METHODS))

    if conn.auth is not None:
        # add auth to `kwargs['headers']`
        kwargs.setdefault('headers', {}).update(conn.auth)

    with requests.Session() as s:
        s.mount(url, HTTPAdapter(max_retries=conn.retry))
        try:
            response = s.request(method, url, **kwargs)
        except (requests.exceptions.BaseHTTPError,
                requests.exceptions.RequestException) as e:
            if not conn.ignore_conn_err:
                raise e
        else:
            if response.ok or not conn.ignore_conn_err:
                return response
        # fabricate response
        response = requests.Response()
        response.status_code = 200  # success
        response._content = six.ensure_binary("{}")  # empty contents
        return response


def raise_for_http_error(response):
    """
    Raises a potential HTTP error with a back end message if provided, or a default error message otherwise.

    Parameters
    ----------
    response : :class:`requests.Response`
        Response object returned from a `requests`-module HTTP request.

    Raises
    ------
    :class:`requests.HTTPError`
        If an HTTP error occured.

    """
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        try:
            reason = response.json()['message']
        except (ValueError,  # not JSON response
                KeyError):  # no 'message' from back end
            six.raise_from(e, None)  # use default reason
        else:
            # replicate https://github.com/psf/requests/blob/428f7a/requests/models.py#L954
            if 400 <= response.status_code < 500:
                cause = "Client"
            elif 500 <= response.status_code < 600:
                cause = "Server"
            else:  # should be impossible here, but sure okay
                cause = "Unexpected"
            message = "{} {} Error: {} for url: {}".format(response.status_code, cause, reason, response.url)
            six.raise_from(requests.HTTPError(message, response=response), None)


def is_hidden(path):  # to avoid "./".startswith('.')
    return os.path.basename(path.rstrip('/')).startswith('.') and path != "."


def find_filepaths(paths, extensions=None, include_hidden=False, include_venv=False):
    """
    Unravels a list of file and directory paths into a list of only filepaths by walking through the
    directories.

    Parameters
    ----------
    paths : str or list of str
        File and directory paths.
    extensions : str or list of str, optional
        What files to include while walking through directories. If not provided, all files will be
        included.
    include_hidden : bool, default False
        Whether to include hidden files and subdirectories found while walking through directories.
    include_venv : bool, default False
        Whether to include Python virtual environment directories.

    Returns
    -------
    filepaths : set

    """
    if isinstance(paths, six.string_types):
        paths = [paths]
    paths = list(map(os.path.expanduser, paths))

    if isinstance(extensions, six.string_types):
        extensions = [extensions]
    if extensions is not None:
        # prepend period to file extensions where missing
        extensions = map(lambda ext: ext if ext.startswith('.') else ('.' + ext), extensions)
        extensions = set(extensions)

    filepaths = set()
    for path in paths:
        if os.path.isdir(path):
            for parent_dir, dirnames, filenames in os.walk(path):
                if not include_hidden:
                    # skip hidden directories
                    dirnames[:] = [dirname for dirname in dirnames if not is_hidden(dirname)]
                    # skip hidden files
                    filenames[:] = [filename for filename in filenames if not is_hidden(filename)]
                if not include_venv:
                    exec_path_glob = os.path.join(parent_dir, "{}", "bin", "python*")
                    dirnames[:] = [dirname for dirname in dirnames if not glob.glob(exec_path_glob.format(dirname))]
                for filename in filenames:
                    if extensions is None or os.path.splitext(filename)[1] in extensions:
                        filepaths.add(os.path.join(parent_dir, filename))
        else:
            filepaths.add(path)
    return filepaths


def proto_to_json(msg):
    """
    Converts a `protobuf` `Message` object into a JSON-compliant dictionary.

    The output preserves snake_case field names and integer representaions of enum variants.

    Parameters
    ----------
    msg : google.protobuf.message.Message
        `protobuf` `Message` object.

    Returns
    -------
    dict
        JSON object representing `msg`.

    """
    return json.loads(json_format.MessageToJson(msg,
                                                including_default_value_fields=True,
                                                preserving_proto_field_name=True,
                                                use_integers_for_enums=True))


def json_to_proto(response_json, response_cls, ignore_unknown_fields=True):
    """
    Converts a JSON-compliant dictionary into a `protobuf` `Message` object.

    Parameters
    ----------
    response_json : dict
        JSON object representing a Protocol Buffer message.
    response_cls : type
        `protobuf` `Message` subclass, e.g. ``CreateProject.Response``.
    ignore_unknown_fields : bool, default True
        Whether to allow (and ignore) fields in `response_json` that are not defined in
        `response_cls`. This is for forward compatibility with the back end; if the Client protos
        are outdated and we get a response with new fields, ``True`` prevents an error.

    Returns
    -------
    google.protobuf.message.Message
        `protobuf` `Message` object represented by `response_json`.

    """
    return json_format.Parse(json.dumps(response_json),
                             response_cls(),
                             ignore_unknown_fields=ignore_unknown_fields)


def to_builtin(obj):
    """
    Tries to coerce `obj` into a built-in type, for JSON serialization.

    Parameters
    ----------
    obj

    Returns
    -------
    object
        A built-in equivalent of `obj`, or `obj` unchanged if it could not be handled by this function.

    """
    # jump through ludicrous hoops to avoid having hard dependencies in the Client
    cls_ = obj.__class__
    obj_class = getattr(cls_, '__name__', None)
    obj_module = getattr(cls_, '__module__', None)

    # booleans
    if isinstance(obj, BOOL_TYPES):
        return True if obj else False

    # NumPy scalars
    if obj_module == "numpy" and obj_class.startswith(('int', 'uint', 'float', 'str')):
        return obj.item()

    # scientific library collections
    if obj_class == "ndarray":
        return obj.tolist()
    if obj_class == "Series":
        return obj.values.tolist()
    if obj_class == "DataFrame":
        return obj.values.tolist()
    if obj_class == "Tensor" and obj_module == "torch":
        return obj.detach().numpy().tolist()
    if tf is not None and isinstance(obj, tf.Tensor):  # if TensorFlow
        try:
            return obj.numpy().tolist()
        except:  # TF 1.X or not-eager execution
            pass

    # strings
    if isinstance(obj, six.string_types):  # prevent infinite loop with iter
        return obj
    if isinstance(obj, six.binary_type):
        return six.ensure_str(obj)

    # dicts and lists
    if isinstance(obj, dict):
        return {to_builtin(key): to_builtin(val) for key, val in six.viewitems(obj)}
    try:
        iter(obj)
    except TypeError:
        pass
    else:
        return [to_builtin(val) for val in obj]

    return obj


def python_to_val_proto(raw_val, allow_collection=False):
    """
    Converts a Python variable into a `protobuf` `Value` `Message` object.

    Parameters
    ----------
    raw_val
        Python variable.
    allow_collection : bool, default False
        Whether to allow ``list``s and ``dict``s as `val`. This flag exists because some callers
        ought to not support logging collections, so this function will perform the typecheck on `val`.

    Returns
    -------
    google.protobuf.struct_pb2.Value
        `protobuf` `Value` `Message` representing `val`.

    """
    # TODO: check `allow_collection` before `to_builtin()` to avoid unnecessary processing
    val = to_builtin(raw_val)

    if val is None:
        return Value(null_value=NULL_VALUE)
    elif isinstance(val, bool):  # did you know that `bool` is a subclass of `int`?
        return Value(bool_value=val)
    elif isinstance(val, numbers.Real):
        return Value(number_value=val)
    elif isinstance(val, six.string_types):
        return Value(string_value=val)
    elif isinstance(val, (list, dict)):
        if allow_collection:
            if isinstance(val, list):
                list_value = ListValue()
                list_value.extend(val)  # pylint: disable=no-member
                return Value(list_value=list_value)
            else:  # isinstance(val, dict)
                if all([isinstance(key, six.string_types) for key in val.keys()]):
                    struct_value = Struct()
                    struct_value.update(val)  # pylint: disable=no-member
                    return Value(struct_value=struct_value)
                else:  # protobuf's fault
                    raise TypeError("struct keys must be strings; consider using log_artifact() instead")
        else:
            raise TypeError("unsupported type {}; consider using log_attribute() instead".format(type(raw_val)))
    else:
        raise TypeError("unsupported type {}; consider using log_artifact() instead".format(type(raw_val)))


def val_proto_to_python(msg):
    """
    Converts a `protobuf` `Value` `Message` object into a Python variable.

    Parameters
    ----------
    msg : google.protobuf.struct_pb2.Value
        `protobuf` `Value` `Message` representing a variable.

    Returns
    -------
    one of {None, bool, float, int, str}
        Python variable represented by `msg`.

    """
    value_kind = msg.WhichOneof("kind")
    if value_kind == "null_value":
        return None
    elif value_kind == "bool_value":
        return msg.bool_value
    elif value_kind == "number_value":
        return int(msg.number_value) if msg.number_value.is_integer() else msg.number_value
    elif value_kind == "string_value":
        return msg.string_value
    elif value_kind == "list_value":
        return [val_proto_to_python(val_msg)
                for val_msg
                in msg.list_value.values]
    elif value_kind == "struct_value":
        return {key: val_proto_to_python(val_msg)
                for key, val_msg
                in msg.struct_value.fields.items()}
    else:
        raise NotImplementedError("retrieved value type is not supported")


def unravel_key_values(rpt_key_value_msg):
    """
    Converts a repeated KeyValue field of a protobuf message into a dictionary.

    Parameters
    ----------
    rpt_key_value_msg : google.protobuf.pyext._message.RepeatedCompositeContainer
        Repeated KeyValue field of a protobuf message.

    Returns
    -------
    dict of str to {None, bool, float, int, str}
        Names and values.

    """
    return {key_value.key: val_proto_to_python(key_value.value)
            for key_value
            in rpt_key_value_msg}


def unravel_artifacts(rpt_artifact_msg):
    """
    Converts a repeated Artifact field of a protobuf message into a list of names.

    Parameters
    ----------
    rpt_artifact_msg : google.protobuf.pyext._message.RepeatedCompositeContainer
        Repeated Artifact field of a protobuf message.

    Returns
    -------
    list of str
        Names of artifacts.

    """
    return [artifact.key
            for artifact
            in rpt_artifact_msg]


def unravel_observation(obs_msg):
    """
    Converts an Observation protobuf message into a more straightforward Python tuple.

    This is useful because an Observation message has a oneof that's finicky to handle.

    Returns
    -------
    str
        Name of observation.
    {None, bool, float, int, str}
        Value of observation.
    str
        Human-readable timestamp.

    """
    if obs_msg.WhichOneof("oneOf") == "attribute":
        key = obs_msg.attribute.key
        value = obs_msg.attribute.value
    elif obs_msg.WhichOneof("oneOf") == "artifact":
        key = obs_msg.artifact.key
        value = "{} artifact".format(_CommonCommonService.ArtifactTypeEnum.ArtifactType.Name(obs_msg.artifact.artifact_type))
    return (
        key,
        val_proto_to_python(value),
        timestamp_to_str(obs_msg.timestamp),
    )


def unravel_observations(rpt_obs_msg):
    """
    Converts a repeated Observation field of a protobuf message into a dictionary.

    Parameters
    ----------
    rpt_obs_msg : google.protobuf.pyext._message.RepeatedCompositeContainer
        Repeated Observation field of a protobuf message.

    Returns
    -------
    dict of str to list of tuples ({None, bool, float, int, str}, str)
        Names and observation sequences.

    """
    observations = {}
    for obs_msg in rpt_obs_msg:
        key, value, timestamp = unravel_observation(obs_msg)
        observations.setdefault(key, []).append((value, timestamp))
    return observations


def validate_flat_key(key):
    """
    Checks whether `key` contains invalid characters.

    To prevent bugs with querying (which allow dot-delimited nested keys), flat keys (such as those
    used for individual metrics) must not contain periods.

    Furthermore, to prevent potential bugs with the back end down the line, keys should be restricted
    to alphanumeric characters, underscores, and dashes until we can verify robustness.

    Parameters
    ----------
    key : str
        Name of metadatum.

    Raises
    ------
    ValueError
        If `key` contains invalid characters.

    """
    for c in key:
        if c not in _VALID_FLAT_KEY_CHARS:
            raise ValueError("`key` may only contain alphanumeric characters, underscores, dashes,"
                             " and forward slashes")


def generate_default_name():
    """
    Generates a string that can be used as a default entity name while avoiding collisions.

    The generated string is a concatenation of the current process ID and the current Unix timestamp,
    such that a collision should only occur if a single process produces two of an entity at the same
    nanosecond.

    Returns
    -------
    name : str
        String generated from the current process ID and Unix timestamp.

    """
    return "{}{}".format(os.getpid(), str(time.time()).replace('.', ''))


class UTC(datetime.tzinfo):
    """UTC timezone class for Python 2 timestamp calculations"""
    def utcoffset(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return datetime.timedelta(0)


def timestamp_to_ms(timestamp):
    """
    Converts a Unix timestamp into one with millisecond resolution.

    Parameters
    ----------
    timestamp : float or int
        Unix timestamp.

    Returns
    -------
    int
        `timestamp` with millisecond resolution (13 integer digits).

    """
    num_integer_digits = len(str(timestamp).split('.')[0])
    return int(timestamp*10**(13 - num_integer_digits))


def ensure_timestamp(timestamp):
    """
    Converts a representation of a datetime into a Unix timestamp with millisecond resolution.

    If `timestamp` is provided as a string, this function attempts to use pandas (if installed) to
    parse it into a Unix timestamp, since pandas can interally handle many different human-readable
    datetime string representations. If pandas is not installed, this function will only handle an
    ISO 8601 representation.

    Parameters
    ----------
    timestamp : str or float or int
        String representation of a datetime or numerical Unix timestamp.

    Returns
    -------
    int
        `timestamp` with millisecond resolution (13 integer digits).

    """
    if isinstance(timestamp, six.string_types):
        try:  # attempt with pandas, which can parse many time string formats
            return timestamp_to_ms(pd.Timestamp(timestamp).timestamp())
        except NameError:  # pandas not installed
            six.raise_from(ValueError("pandas must be installed to parse datetime strings"),
                           None)
        except ValueError:  # can't be handled by pandas
            six.raise_from(ValueError("unable to parse datetime string \"{}\"".format(timestamp)),
                           None)
    elif isinstance(timestamp, numbers.Real):
        return timestamp_to_ms(timestamp)
    elif isinstance(timestamp, datetime.datetime):
        if six.PY2:
            # replicate https://docs.python.org/3/library/datetime.html#datetime.datetime.timestamp
            seconds = (timestamp - datetime.datetime(1970, 1, 1, tzinfo=UTC())).total_seconds()
        else:  # Python 3
            seconds = timestamp.timestamp()
        return timestamp_to_ms(seconds)
    else:
        raise TypeError("unable to parse timestamp of type {}".format(type(timestamp)))


def timestamp_to_str(timestamp):
    """
    Converts a Unix timestamp into a human-readable string representation.

    Parameters
    ----------
    timestamp : int
        Numerical Unix timestamp.

    Returns
    -------
    str
        Human-readable string representation of `timestamp`.

    """
    num_digits = len(str(timestamp))
    return str(datetime.datetime.fromtimestamp(timestamp*10**(10 - num_digits)))


def now():
    """
    Returns the current Unix timestamp with millisecond resolution.

    Returns
    -------
    now : int
        Current Unix timestamp in milliseconds.

    """
    return timestamp_to_ms(time.time())


def get_python_version():
    """
    Returns the version number of the locally-installed Python interpreter.

    Returns
    -------
    str
        Python version number in the form "{major}.{minor}.{patch}".

    """
    return '.'.join(map(str, sys.version_info[:3]))


def save_notebook(notebook_path=None, timeout=5):
    """
    Saves the current notebook on disk and returns its contents after the file has been rewritten.

    Parameters
    ----------
    notebook_path : str, optional
        Filepath of the Jupyter Notebook.
    timeout : float, default 5
        Maximum number of seconds to wait for the notebook to save.

    Returns
    -------
    notebook_contents : file-like
        An in-memory copy of the notebook's contents at the time this function returns. This can
        be ignored, but is nonetheless available to minimize the risk of a race condition caused by
        delaying the read until a later time.

    Raises
    ------
    OSError
        If the notebook is not saved within `timeout` seconds.

    """
    if notebook_path is None:
        notebook_path = get_notebook_filepath()
    modtime = os.path.getmtime(notebook_path)

    display(Javascript('''
    require(["base/js/namespace"],function(Jupyter) {
        Jupyter.notebook.save_checkpoint();
    });
    '''))

    # wait for file to be modified
    start_time = time.time()
    while time.time() - start_time < timeout:
        new_modtime = os.path.getmtime(notebook_path)
        if new_modtime > modtime:
            break
        time.sleep(0.01)
    else:
        raise OSError("unable to save notebook")

    # wait for file to be rewritten
    timeout -= (time.time() - start_time)  # remaining time
    start_time = time.time()
    while time.time() - start_time < timeout:
        with open(notebook_path, 'r') as f:
            contents = f.read()
        if contents:
            return six.StringIO(contents)
        time.sleep(0.01)
    else:
        raise OSError("unable to read saved notebook")


def get_notebook_filepath():
    """
    Returns the filesystem path of the Jupyter notebook running the Client.

    This implementation is from https://github.com/jupyter/notebook/issues/1000#issuecomment-359875246.

    Returns
    -------
    str

    Raises
    ------
    OSError
        If one of the following is true:
            - Jupyter is not installed
            - Client is not being called from a notebook
            - the calling notebook cannot be identified

    """
    try:
        connection_file = ipykernel.connect.get_connection_file()
    except (NameError,  # Jupyter not installed
            RuntimeError):  # not in a Notebook
        pass
    else:
        kernel_id = re.search('kernel-(.*).json', connection_file).group(1)
        for server in list_running_servers():
            response = requests.get(urljoin(server['url'], 'api/sessions'),
                                    params={'token': server.get('token', '')})
            if response.ok:
                for session in response.json():
                    if session['kernel']['id'] == kernel_id:
                        relative_path = session['notebook']['path']
                        return os.path.join(server['notebook_dir'], relative_path)
    raise OSError("unable to find notebook file")


def get_script_filepath():
    """
    Returns the filesystem path of the Python script running the Client.

    This function iterates back through the call stack until it finds a non-Verta stack frame and
    returns its filepath.

    Returns
    -------
    str

    Raises
    ------
    OSError
        If the calling script cannot be identified.

    """
    for frame_info in inspect.stack():
        module = inspect.getmodule(frame_info[0])
        if module is None or module.__name__.split('.', 1)[0] != "verta":
            filepath = frame_info[1]
            if os.path.exists(filepath):  # e.g. Jupyter fakes the filename for cells
                return filepath
            else:
                break  # continuing might end up returning a built-in
    raise OSError("unable to find script file")


def is_org(workspace_name, conn):
    response = make_request(
        "GET",
        "{}://{}/api/v1/uac-proxy/organization/getOrganizationByName".format(conn.scheme, conn.socket),
        conn, params={'org_name': workspace_name},
    )

    return response.status_code != 404
