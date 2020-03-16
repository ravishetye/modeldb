# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/public/modeldb/versioning/Dataset.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ....public.modeldb.versioning import Enums_pb2 as protos_dot_public_dot_modeldb_dot_versioning_dot_Enums__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/public/modeldb/versioning/Dataset.proto',
  package='ai.verta.modeldb.versioning',
  syntax='proto3',
  serialized_options=b'P\001ZIgithub.com/VertaAI/modeldb/protos/gen/go/protos/public/modeldb/versioning',
  serialized_pb=b'\n.protos/public/modeldb/versioning/Dataset.proto\x12\x1b\x61i.verta.modeldb.versioning\x1a,protos/public/modeldb/versioning/Enums.proto\"\x90\x01\n\x0b\x44\x61tasetBlob\x12\x38\n\x02s3\x18\x01 \x01(\x0b\x32*.ai.verta.modeldb.versioning.S3DatasetBlobH\x00\x12<\n\x04path\x18\x02 \x01(\x0b\x32,.ai.verta.modeldb.versioning.PathDatasetBlobH\x00\x42\t\n\x07\x63ontent\"t\n\x18PathDatasetComponentBlob\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\x04\x12\x1f\n\x17last_modified_at_source\x18\x03 \x01(\x04\x12\x0e\n\x06sha256\x18\x04 \x01(\t\x12\x0b\n\x03md5\x18\x05 \x01(\t\"\\\n\x0fPathDatasetBlob\x12I\n\ncomponents\x18\x01 \x03(\x0b\x32\x35.ai.verta.modeldb.versioning.PathDatasetComponentBlob\"]\n\x16S3DatasetComponentBlob\x12\x43\n\x04path\x18\x01 \x01(\x0b\x32\x35.ai.verta.modeldb.versioning.PathDatasetComponentBlob\"X\n\rS3DatasetBlob\x12G\n\ncomponents\x18\x01 \x03(\x0b\x32\x33.ai.verta.modeldb.versioning.S3DatasetComponentBlob\"\x90\x01\n\x0b\x44\x61tasetDiff\x12\x38\n\x02s3\x18\x01 \x01(\x0b\x32*.ai.verta.modeldb.versioning.S3DatasetDiffH\x00\x12<\n\x04path\x18\x02 \x01(\x0b\x32,.ai.verta.modeldb.versioning.PathDatasetDiffH\x00\x42\t\n\x07\x63ontent\"\xe6\x01\n\x18PathDatasetComponentDiff\x12\x46\n\x06status\x18\x01 \x01(\x0e\x32\x36.ai.verta.modeldb.versioning.DiffStatusEnum.DiffStatus\x12@\n\x01\x41\x18\x02 \x01(\x0b\x32\x35.ai.verta.modeldb.versioning.PathDatasetComponentBlob\x12@\n\x01\x42\x18\x03 \x01(\x0b\x32\x35.ai.verta.modeldb.versioning.PathDatasetComponentBlob\"\\\n\x0fPathDatasetDiff\x12I\n\ncomponents\x18\x01 \x03(\x0b\x32\x35.ai.verta.modeldb.versioning.PathDatasetComponentDiff\"]\n\x16S3DatasetComponentDiff\x12\x43\n\x04path\x18\x01 \x01(\x0b\x32\x35.ai.verta.modeldb.versioning.PathDatasetComponentDiff\"X\n\rS3DatasetDiff\x12G\n\ncomponents\x18\x01 \x03(\x0b\x32\x33.ai.verta.modeldb.versioning.S3DatasetComponentDiffBMP\x01ZIgithub.com/VertaAI/modeldb/protos/gen/go/protos/public/modeldb/versioningb\x06proto3'
  ,
  dependencies=[protos_dot_public_dot_modeldb_dot_versioning_dot_Enums__pb2.DESCRIPTOR,])




_DATASETBLOB = _descriptor.Descriptor(
  name='DatasetBlob',
  full_name='ai.verta.modeldb.versioning.DatasetBlob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s3', full_name='ai.verta.modeldb.versioning.DatasetBlob.s3', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='ai.verta.modeldb.versioning.DatasetBlob.path', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='content', full_name='ai.verta.modeldb.versioning.DatasetBlob.content',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=126,
  serialized_end=270,
)


_PATHDATASETCOMPONENTBLOB = _descriptor.Descriptor(
  name='PathDatasetComponentBlob',
  full_name='ai.verta.modeldb.versioning.PathDatasetComponentBlob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='ai.verta.modeldb.versioning.PathDatasetComponentBlob.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='ai.verta.modeldb.versioning.PathDatasetComponentBlob.size', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_modified_at_source', full_name='ai.verta.modeldb.versioning.PathDatasetComponentBlob.last_modified_at_source', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sha256', full_name='ai.verta.modeldb.versioning.PathDatasetComponentBlob.sha256', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='md5', full_name='ai.verta.modeldb.versioning.PathDatasetComponentBlob.md5', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=388,
)


_PATHDATASETBLOB = _descriptor.Descriptor(
  name='PathDatasetBlob',
  full_name='ai.verta.modeldb.versioning.PathDatasetBlob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='components', full_name='ai.verta.modeldb.versioning.PathDatasetBlob.components', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=482,
)


_S3DATASETCOMPONENTBLOB = _descriptor.Descriptor(
  name='S3DatasetComponentBlob',
  full_name='ai.verta.modeldb.versioning.S3DatasetComponentBlob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='ai.verta.modeldb.versioning.S3DatasetComponentBlob.path', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=577,
)


_S3DATASETBLOB = _descriptor.Descriptor(
  name='S3DatasetBlob',
  full_name='ai.verta.modeldb.versioning.S3DatasetBlob',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='components', full_name='ai.verta.modeldb.versioning.S3DatasetBlob.components', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=579,
  serialized_end=667,
)


_DATASETDIFF = _descriptor.Descriptor(
  name='DatasetDiff',
  full_name='ai.verta.modeldb.versioning.DatasetDiff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s3', full_name='ai.verta.modeldb.versioning.DatasetDiff.s3', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='ai.verta.modeldb.versioning.DatasetDiff.path', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='content', full_name='ai.verta.modeldb.versioning.DatasetDiff.content',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=670,
  serialized_end=814,
)


_PATHDATASETCOMPONENTDIFF = _descriptor.Descriptor(
  name='PathDatasetComponentDiff',
  full_name='ai.verta.modeldb.versioning.PathDatasetComponentDiff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ai.verta.modeldb.versioning.PathDatasetComponentDiff.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='A', full_name='ai.verta.modeldb.versioning.PathDatasetComponentDiff.A', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='B', full_name='ai.verta.modeldb.versioning.PathDatasetComponentDiff.B', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=817,
  serialized_end=1047,
)


_PATHDATASETDIFF = _descriptor.Descriptor(
  name='PathDatasetDiff',
  full_name='ai.verta.modeldb.versioning.PathDatasetDiff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='components', full_name='ai.verta.modeldb.versioning.PathDatasetDiff.components', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1049,
  serialized_end=1141,
)


_S3DATASETCOMPONENTDIFF = _descriptor.Descriptor(
  name='S3DatasetComponentDiff',
  full_name='ai.verta.modeldb.versioning.S3DatasetComponentDiff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='ai.verta.modeldb.versioning.S3DatasetComponentDiff.path', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1143,
  serialized_end=1236,
)


_S3DATASETDIFF = _descriptor.Descriptor(
  name='S3DatasetDiff',
  full_name='ai.verta.modeldb.versioning.S3DatasetDiff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='components', full_name='ai.verta.modeldb.versioning.S3DatasetDiff.components', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1238,
  serialized_end=1326,
)

_DATASETBLOB.fields_by_name['s3'].message_type = _S3DATASETBLOB
_DATASETBLOB.fields_by_name['path'].message_type = _PATHDATASETBLOB
_DATASETBLOB.oneofs_by_name['content'].fields.append(
  _DATASETBLOB.fields_by_name['s3'])
_DATASETBLOB.fields_by_name['s3'].containing_oneof = _DATASETBLOB.oneofs_by_name['content']
_DATASETBLOB.oneofs_by_name['content'].fields.append(
  _DATASETBLOB.fields_by_name['path'])
_DATASETBLOB.fields_by_name['path'].containing_oneof = _DATASETBLOB.oneofs_by_name['content']
_PATHDATASETBLOB.fields_by_name['components'].message_type = _PATHDATASETCOMPONENTBLOB
_S3DATASETCOMPONENTBLOB.fields_by_name['path'].message_type = _PATHDATASETCOMPONENTBLOB
_S3DATASETBLOB.fields_by_name['components'].message_type = _S3DATASETCOMPONENTBLOB
_DATASETDIFF.fields_by_name['s3'].message_type = _S3DATASETDIFF
_DATASETDIFF.fields_by_name['path'].message_type = _PATHDATASETDIFF
_DATASETDIFF.oneofs_by_name['content'].fields.append(
  _DATASETDIFF.fields_by_name['s3'])
_DATASETDIFF.fields_by_name['s3'].containing_oneof = _DATASETDIFF.oneofs_by_name['content']
_DATASETDIFF.oneofs_by_name['content'].fields.append(
  _DATASETDIFF.fields_by_name['path'])
_DATASETDIFF.fields_by_name['path'].containing_oneof = _DATASETDIFF.oneofs_by_name['content']
_PATHDATASETCOMPONENTDIFF.fields_by_name['status'].enum_type = protos_dot_public_dot_modeldb_dot_versioning_dot_Enums__pb2._DIFFSTATUSENUM_DIFFSTATUS
_PATHDATASETCOMPONENTDIFF.fields_by_name['A'].message_type = _PATHDATASETCOMPONENTBLOB
_PATHDATASETCOMPONENTDIFF.fields_by_name['B'].message_type = _PATHDATASETCOMPONENTBLOB
_PATHDATASETDIFF.fields_by_name['components'].message_type = _PATHDATASETCOMPONENTDIFF
_S3DATASETCOMPONENTDIFF.fields_by_name['path'].message_type = _PATHDATASETCOMPONENTDIFF
_S3DATASETDIFF.fields_by_name['components'].message_type = _S3DATASETCOMPONENTDIFF
DESCRIPTOR.message_types_by_name['DatasetBlob'] = _DATASETBLOB
DESCRIPTOR.message_types_by_name['PathDatasetComponentBlob'] = _PATHDATASETCOMPONENTBLOB
DESCRIPTOR.message_types_by_name['PathDatasetBlob'] = _PATHDATASETBLOB
DESCRIPTOR.message_types_by_name['S3DatasetComponentBlob'] = _S3DATASETCOMPONENTBLOB
DESCRIPTOR.message_types_by_name['S3DatasetBlob'] = _S3DATASETBLOB
DESCRIPTOR.message_types_by_name['DatasetDiff'] = _DATASETDIFF
DESCRIPTOR.message_types_by_name['PathDatasetComponentDiff'] = _PATHDATASETCOMPONENTDIFF
DESCRIPTOR.message_types_by_name['PathDatasetDiff'] = _PATHDATASETDIFF
DESCRIPTOR.message_types_by_name['S3DatasetComponentDiff'] = _S3DATASETCOMPONENTDIFF
DESCRIPTOR.message_types_by_name['S3DatasetDiff'] = _S3DATASETDIFF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DatasetBlob = _reflection.GeneratedProtocolMessageType('DatasetBlob', (_message.Message,), {
  'DESCRIPTOR' : _DATASETBLOB,
  '__module__' : 'protos.public.modeldb.versioning.Dataset_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.versioning.DatasetBlob)
  })
_sym_db.RegisterMessage(DatasetBlob)

PathDatasetComponentBlob = _reflection.GeneratedProtocolMessageType('PathDatasetComponentBlob', (_message.Message,), {
  'DESCRIPTOR' : _PATHDATASETCOMPONENTBLOB,
  '__module__' : 'protos.public.modeldb.versioning.Dataset_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.versioning.PathDatasetComponentBlob)
  })
_sym_db.RegisterMessage(PathDatasetComponentBlob)

PathDatasetBlob = _reflection.GeneratedProtocolMessageType('PathDatasetBlob', (_message.Message,), {
  'DESCRIPTOR' : _PATHDATASETBLOB,
  '__module__' : 'protos.public.modeldb.versioning.Dataset_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.versioning.PathDatasetBlob)
  })
_sym_db.RegisterMessage(PathDatasetBlob)

S3DatasetComponentBlob = _reflection.GeneratedProtocolMessageType('S3DatasetComponentBlob', (_message.Message,), {
  'DESCRIPTOR' : _S3DATASETCOMPONENTBLOB,
  '__module__' : 'protos.public.modeldb.versioning.Dataset_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.versioning.S3DatasetComponentBlob)
  })
_sym_db.RegisterMessage(S3DatasetComponentBlob)

S3DatasetBlob = _reflection.GeneratedProtocolMessageType('S3DatasetBlob', (_message.Message,), {
  'DESCRIPTOR' : _S3DATASETBLOB,
  '__module__' : 'protos.public.modeldb.versioning.Dataset_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.versioning.S3DatasetBlob)
  })
_sym_db.RegisterMessage(S3DatasetBlob)

DatasetDiff = _reflection.GeneratedProtocolMessageType('DatasetDiff', (_message.Message,), {
  'DESCRIPTOR' : _DATASETDIFF,
  '__module__' : 'protos.public.modeldb.versioning.Dataset_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.versioning.DatasetDiff)
  })
_sym_db.RegisterMessage(DatasetDiff)

PathDatasetComponentDiff = _reflection.GeneratedProtocolMessageType('PathDatasetComponentDiff', (_message.Message,), {
  'DESCRIPTOR' : _PATHDATASETCOMPONENTDIFF,
  '__module__' : 'protos.public.modeldb.versioning.Dataset_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.versioning.PathDatasetComponentDiff)
  })
_sym_db.RegisterMessage(PathDatasetComponentDiff)

PathDatasetDiff = _reflection.GeneratedProtocolMessageType('PathDatasetDiff', (_message.Message,), {
  'DESCRIPTOR' : _PATHDATASETDIFF,
  '__module__' : 'protos.public.modeldb.versioning.Dataset_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.versioning.PathDatasetDiff)
  })
_sym_db.RegisterMessage(PathDatasetDiff)

S3DatasetComponentDiff = _reflection.GeneratedProtocolMessageType('S3DatasetComponentDiff', (_message.Message,), {
  'DESCRIPTOR' : _S3DATASETCOMPONENTDIFF,
  '__module__' : 'protos.public.modeldb.versioning.Dataset_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.versioning.S3DatasetComponentDiff)
  })
_sym_db.RegisterMessage(S3DatasetComponentDiff)

S3DatasetDiff = _reflection.GeneratedProtocolMessageType('S3DatasetDiff', (_message.Message,), {
  'DESCRIPTOR' : _S3DATASETDIFF,
  '__module__' : 'protos.public.modeldb.versioning.Dataset_pb2'
  # @@protoc_insertion_point(class_scope:ai.verta.modeldb.versioning.S3DatasetDiff)
  })
_sym_db.RegisterMessage(S3DatasetDiff)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)