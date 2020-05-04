package ai.verta.modeldb.versioning.blob.diff;

import ai.verta.modeldb.ModelDBException;
import ai.verta.modeldb.versioning.Blob;
import ai.verta.modeldb.versioning.BlobDiff;
import ai.verta.modeldb.versioning.DiffStatusEnum.DiffStatus;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenBlobDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenCodeBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenCodeDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenCommandLineEnvironmentDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenConfigBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenConfigDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenDatasetBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenDatasetDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenDiffStatusEnumDiffStatus;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenDockerEnvironmentBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenDockerEnvironmentDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenEnvironmentBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenEnvironmentDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenEnvironmentVariablesBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenEnvironmentVariablesDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenGitCodeBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenGitCodeDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenHyperparameterConfigBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenHyperparameterConfigDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenHyperparameterSetConfigBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenHyperparameterSetConfigDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenNotebookCodeBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenNotebookCodeDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenPathDatasetBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenPathDatasetComponentBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenPathDatasetComponentDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenPathDatasetDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenPythonEnvironmentBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenPythonEnvironmentDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenPythonRequirementEnvironmentBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenPythonRequirementEnvironmentDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenS3DatasetBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenS3DatasetComponentBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenS3DatasetComponentDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenS3DatasetDiff;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenVersionEnvironmentBlob;
import ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model.AutogenVersionEnvironmentDiff;
import io.grpc.Status.Code;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class ConflictGenerator {
  private static final Logger LOGGER = LogManager.getLogger(ConflictGenerator.class);

  public static BlobDiff setConflictBlobsInDiff(
      BlobDiff blobDiff,
      List<BlobDiff> locSpecificBlobDiffA,
      List<BlobDiff> locSpecificBlobDiffB,
      Blob parentBlob)
      throws ModelDBException {
    if (locSpecificBlobDiffA.size() != locSpecificBlobDiffB.size()) {
      LOGGER.warn("expecting diffs of same size");
      throw new ModelDBException("different size of diff not expected", Code.INTERNAL);
    }
    if (locSpecificBlobDiffA.size() != locSpecificBlobDiffB.size()) {
      LOGGER.warn("currently supporting diff of size 1");
      throw new ModelDBException("different size of diff not expected", Code.INTERNAL);
    }
    AutogenBlobDiff diff = AutogenBlobDiff.fromProto(blobDiff);
    AutogenBlobDiff a = AutogenBlobDiff.fromProto(locSpecificBlobDiffA.get(0));
    AutogenBlobDiff b = AutogenBlobDiff.fromProto(locSpecificBlobDiffB.get(0));
    AutogenBlob c = AutogenBlob.fromProto(parentBlob);
    diff.setDataset(getDatasetConflictBlob(a.getDataset(), b.getDataset(), c.getDataset()))
        .setCode(getCodeConflictBlob(a.getCode(), b.getCode(), c.getCode()))
        .setConfig(getConfigConflictBlob(a.getConfig(), b.getConfig(), c.getConfig()))
        .setEnvironment(
            getEnvironmentonflictBlob(a.getEnvironment(), b.getEnvironment(), c.getEnvironment()));

    return diff.toProto().build();
  }

  private static AutogenEnvironmentDiff getEnvironmentonflictBlob(
      AutogenEnvironmentDiff a, AutogenEnvironmentDiff b, AutogenEnvironmentBlob c) {
    return Utils.removeEmpty(
        new AutogenEnvironmentDiff()
            .setCommandLine(
                getCommandLineDiff(
                    a == null ? null : a.getCommandLine(),
                    b == null ? null : b.getCommandLine(),
                    c == null ? Collections.emptyList() : c.getCommandLine()))
            .setDocker(
                getDockerDiff(
                    a == null ? null : a.getDocker(),
                    b == null ? null : b.getDocker(),
                    c == null ? null : c.getDocker()))
            .setEnvironmentVariables(
                getEnvVarDiff(
                    a == null ? null : a.getEnvironmentVariables(),
                    b == null ? null : b.getEnvironmentVariables(),
                    c == null ? null : c.getEnvironmentVariables()))
            .setPython(
                getPythonDiff(
                    a == null ? null : a.getPython(),
                    b == null ? null : b.getPython(),
                    c == null ? null : c.getPython())));
  }

  private static AutogenPythonEnvironmentDiff getPythonDiff(
      AutogenPythonEnvironmentDiff a,
      AutogenPythonEnvironmentDiff b,
      AutogenPythonEnvironmentBlob c) {
    return Utils.removeEmpty(
        new AutogenPythonEnvironmentDiff()
            .setConstraints(
                getRequirementDiff(
                    a == null ? null : a.getConstraints(),
                    b == null ? null : b.getConstraints(),
                    c == null ? null : c.getConstraints()))
            .setRequirements(
                getRequirementDiff(
                    a == null ? null : a.getRequirements(),
                    b == null ? null : b.getRequirements(),
                    c == null ? null : c.getRequirements()))
            .setVersion(
                getVersionDiff(
                    a == null ? null : a.getVersion(),
                    b == null ? null : b.getVersion(),
                    c == null ? null : c.getVersion())));
  }

  private static AutogenVersionEnvironmentDiff getVersionDiff(
      AutogenVersionEnvironmentDiff a,
      AutogenVersionEnvironmentDiff b,
      AutogenVersionEnvironmentBlob c) {
    return Utils.removeEmpty(
        new AutogenVersionEnvironmentDiff()
            .setA(a == null ? null : a.getB())
            .setB(b == null ? null : b.getB())
            .setC(c));
  }

  private static List<AutogenPythonRequirementEnvironmentDiff> getRequirementDiff(
      List<AutogenPythonRequirementEnvironmentDiff> a,
      List<AutogenPythonRequirementEnvironmentDiff> b,
      List<AutogenPythonRequirementEnvironmentBlob> c) {
    Map<String, AutogenPythonRequirementEnvironmentBlob> mapA = getRequirementDiffMap(a);
    Map<String, AutogenPythonRequirementEnvironmentBlob> mapB = getRequirementDiffMap(b);
    Map<String, AutogenPythonRequirementEnvironmentBlob> mapC = getRequirementMap(c);
    HashSet<String> keys = new HashSet<>();
    keys.addAll(mapA.keySet());
    keys.retainAll(mapB.keySet());
    List<AutogenPythonRequirementEnvironmentDiff> retList =
        new LinkedList<AutogenPythonRequirementEnvironmentDiff>();
    for (String key : keys) {
      if (!mapA.get(key).equals(mapB.get(key))) {
        retList.add(
            Utils.removeEmpty(
                new AutogenPythonRequirementEnvironmentDiff()
                    .setStatus(AutogenDiffStatusEnumDiffStatus.fromProto(DiffStatus.CONFLICTED))
                    .setA(mapA.get(key))
                    .setB(mapB.get(key))
                    .setC(mapC.get(key))));
      }
    }
    return retList;
  }

  private static Map<String, AutogenPythonRequirementEnvironmentBlob> getRequirementMap(
      List<AutogenPythonRequirementEnvironmentBlob> list) {
    if (list == null) return Collections.emptyMap();
    Map<String, AutogenPythonRequirementEnvironmentBlob> retMap =
        new HashMap<String, AutogenPythonRequirementEnvironmentBlob>();
    for (AutogenPythonRequirementEnvironmentBlob blob : list) {
      String name = blob.getLibrary();
      retMap.put(name, blob);
    }
    return retMap;
  }

  private static Map<String, AutogenPythonRequirementEnvironmentBlob> getRequirementDiffMap(
      List<AutogenPythonRequirementEnvironmentDiff> list) {

    if (list == null) return Collections.emptyMap();
    Map<String, AutogenPythonRequirementEnvironmentBlob> retMap =
        new HashMap<String, AutogenPythonRequirementEnvironmentBlob>();
    for (AutogenPythonRequirementEnvironmentDiff diff : list) {
      String name = diff.getB().getLibrary();
      retMap.put(name, diff.getB());
    }
    return retMap;
  }

  private static List<AutogenEnvironmentVariablesDiff> getEnvVarDiff(
      List<AutogenEnvironmentVariablesDiff> a,
      List<AutogenEnvironmentVariablesDiff> b,
      List<AutogenEnvironmentVariablesBlob> c) {
    Map<String, AutogenEnvironmentVariablesBlob> mapA = getEnvVarDiffMap(a);
    Map<String, AutogenEnvironmentVariablesBlob> mapB = getEnvVarDiffMap(b);
    Map<String, AutogenEnvironmentVariablesBlob> mapC = getEnvVarMap(c);
    HashSet<String> keys = new HashSet<>();
    keys.addAll(mapA.keySet());
    keys.retainAll(mapB.keySet());
    List<AutogenEnvironmentVariablesDiff> retList =
        new LinkedList<AutogenEnvironmentVariablesDiff>();
    for (String key : keys) {
      if (!mapA.get(key).equals(mapB.get(key))) {
        retList.add(
            Utils.removeEmpty(
                new AutogenEnvironmentVariablesDiff()
                    .setStatus(AutogenDiffStatusEnumDiffStatus.fromProto(DiffStatus.CONFLICTED))
                    .setA(mapA.get(key))
                    .setB(mapB.get(key))
                    .setC(mapC.get(key))));
      }
    }
    return retList;
  }

  private static Map<String, AutogenEnvironmentVariablesBlob> getEnvVarMap(
      List<AutogenEnvironmentVariablesBlob> list) {
    if (list == null) return Collections.emptyMap();
    Map<String, AutogenEnvironmentVariablesBlob> retMap =
        new HashMap<String, AutogenEnvironmentVariablesBlob>();
    for (AutogenEnvironmentVariablesBlob blob : list) {
      String name = blob.getName();
      retMap.put(name, blob);
    }
    return retMap;
  }

  private static Map<String, AutogenEnvironmentVariablesBlob> getEnvVarDiffMap(
      List<AutogenEnvironmentVariablesDiff> list) {
    if (list == null) return Collections.emptyMap();
    Map<String, AutogenEnvironmentVariablesBlob> retMap =
        new HashMap<String, AutogenEnvironmentVariablesBlob>();
    for (AutogenEnvironmentVariablesDiff diff : list) {
      String name = diff.getB().getName();
      retMap.put(name, diff.getB());
    }
    return retMap;
  }

  private static AutogenDockerEnvironmentDiff getDockerDiff(
      AutogenDockerEnvironmentDiff a,
      AutogenDockerEnvironmentDiff b,
      AutogenDockerEnvironmentBlob c) {
    return Utils.removeEmpty(
        new AutogenDockerEnvironmentDiff()
            .setA(a == null ? null : a.getB())
            .setB(b == null ? null : b.getB())
            .setC(c));
  }

  private static AutogenCommandLineEnvironmentDiff getCommandLineDiff(
      AutogenCommandLineEnvironmentDiff a, AutogenCommandLineEnvironmentDiff b, List<String> c) {
    return Utils.removeEmpty(
        new AutogenCommandLineEnvironmentDiff()
            .setA(a == null ? null : a.getB())
            .setB(b == null ? null : b.getB())
            .setC(c));
  }

  private static AutogenConfigDiff getConfigConflictBlob(
      AutogenConfigDiff a, AutogenConfigDiff b, AutogenConfigBlob c) {
    return Utils.removeEmpty(
        new AutogenConfigDiff()
            .setHyperparameters(
                getHyperparametersDiff(
                    a == null ? Collections.emptyList() : a.getHyperparameters(),
                    b == null ? Collections.emptyList() : b.getHyperparameters(),
                    c == null ? Collections.emptyList() : c.getHyperparameters()))
            .setHyperparameterSet(
                getHyperparametersSetDiff(
                    a == null ? Collections.emptyList() : a.getHyperparameterSet(),
                    b == null ? Collections.emptyList() : b.getHyperparameterSet(),
                    c == null ? Collections.emptyList() : c.getHyperparameterSet())));
  }

  private static List<AutogenHyperparameterSetConfigDiff> getHyperparametersSetDiff(
      List<AutogenHyperparameterSetConfigDiff> a,
      List<AutogenHyperparameterSetConfigDiff> b,
      List<AutogenHyperparameterSetConfigBlob> c) {
    Map<String, AutogenHyperparameterSetConfigBlob> mapA = getHyperparameterSetDiffMap(a);
    Map<String, AutogenHyperparameterSetConfigBlob> mapB = getHyperparameterSetDiffMap(b);
    Map<String, AutogenHyperparameterSetConfigBlob> mapC = getHyperparameterSetMap(c);
    HashSet<String> keys = new HashSet<>();
    keys.addAll(mapA.keySet());
    keys.retainAll(mapB.keySet());
    List<AutogenHyperparameterSetConfigDiff> retList =
        new LinkedList<AutogenHyperparameterSetConfigDiff>();
    for (String key : keys) {
      if (!mapA.get(key).equals(mapB.get(key))) {
        retList.add(
            Utils.removeEmpty(
                new AutogenHyperparameterSetConfigDiff()
                    .setStatus(AutogenDiffStatusEnumDiffStatus.fromProto(DiffStatus.CONFLICTED))
                    .setA(mapA.get(key))
                    .setB(mapB.get(key))
                    .setC(mapC.get(key))));
      }
    }
    return retList;
  }

  private static Map<String, AutogenHyperparameterSetConfigBlob> getHyperparameterSetMap(
      List<AutogenHyperparameterSetConfigBlob> list) {
    if (list == null) return Collections.emptyMap();
    Map<String, AutogenHyperparameterSetConfigBlob> retMap =
        new HashMap<String, AutogenHyperparameterSetConfigBlob>();
    for (AutogenHyperparameterSetConfigBlob blob : list) {
      String name = blob.getName();
      retMap.put(name, blob);
    }
    return retMap;
  }

  private static Map<String, AutogenHyperparameterSetConfigBlob> getHyperparameterSetDiffMap(
      List<AutogenHyperparameterSetConfigDiff> list) {
    if (list == null) return Collections.emptyMap();
    Map<String, AutogenHyperparameterSetConfigBlob> retMap =
        new HashMap<String, AutogenHyperparameterSetConfigBlob>();
    for (AutogenHyperparameterSetConfigDiff diff : list) {
      String name = diff.getB().getName();
      retMap.put(name, diff.getB());
    }
    return retMap;
  }

  private static List<AutogenHyperparameterConfigDiff> getHyperparametersDiff(
      List<AutogenHyperparameterConfigDiff> a,
      List<AutogenHyperparameterConfigDiff> b,
      List<AutogenHyperparameterConfigBlob> c) {
    Map<String, AutogenHyperparameterConfigBlob> mapA = getHyperparameterDiffMap(a);
    Map<String, AutogenHyperparameterConfigBlob> mapB = getHyperparameterDiffMap(b);
    Map<String, AutogenHyperparameterConfigBlob> mapC = getHyperparameterMap(c);
    HashSet<String> keys = new HashSet<>();
    keys.addAll(mapA.keySet());
    keys.retainAll(mapB.keySet());
    List<AutogenHyperparameterConfigDiff> retList =
        new LinkedList<AutogenHyperparameterConfigDiff>();
    for (String key : keys) {
      if (!mapA.get(key).equals(mapB.get(key))) {
        retList.add(
            Utils.removeEmpty(
                new AutogenHyperparameterConfigDiff()
                    .setStatus(AutogenDiffStatusEnumDiffStatus.fromProto(DiffStatus.CONFLICTED))
                    .setA(mapA.get(key))
                    .setB(mapB.get(key))
                    .setC(mapC.get(key))));
      }
    }
    return retList;
  }

  private static Map<String, AutogenHyperparameterConfigBlob> getHyperparameterMap(
      List<AutogenHyperparameterConfigBlob> list) {
    if (list == null) return Collections.emptyMap();
    Map<String, AutogenHyperparameterConfigBlob> retMap =
        new HashMap<String, AutogenHyperparameterConfigBlob>();
    for (AutogenHyperparameterConfigBlob pathBlob : list) {
      String name = pathBlob.getName();
      retMap.put(name, pathBlob);
    }
    return retMap;
  }

  private static Map<String, AutogenHyperparameterConfigBlob> getHyperparameterDiffMap(
      List<AutogenHyperparameterConfigDiff> list) {
    if (list == null) return Collections.emptyMap();
    Map<String, AutogenHyperparameterConfigBlob> retMap =
        new HashMap<String, AutogenHyperparameterConfigBlob>();
    for (AutogenHyperparameterConfigDiff diff : list) {
      String name = diff.getB().getName();
      retMap.put(name, diff.getB());
    }
    return retMap;
  }

  private static AutogenCodeDiff getCodeConflictBlob(
      AutogenCodeDiff a, AutogenCodeDiff b, AutogenCodeBlob c) {
    return Utils.removeEmpty(
        new AutogenCodeDiff()
            .setGit(
                getGitDiff(
                    a == null ? null : a.getGit(),
                    b == null ? null : b.getGit(),
                    c == null ? null : c.getGit()))
            .setNotebook(
                getNoteBookDiff(
                    a == null ? null : a.getNotebook(),
                    b == null ? null : b.getNotebook(),
                    c == null ? null : c.getNotebook())));
  }

  private static AutogenNotebookCodeDiff getNoteBookDiff(
      AutogenNotebookCodeDiff a, AutogenNotebookCodeDiff b, AutogenNotebookCodeBlob c) {
    return Utils.removeEmpty(
        new AutogenNotebookCodeDiff()
            .setGitRepo(
                getGitDiff(
                    a == null ? null : a.getGitRepo(),
                    b == null ? null : b.getGitRepo(),
                    c == null ? null : c.getGitRepo()))
            .setPath(
                new AutogenPathDatasetComponentDiff()
                    .setA(a == null || a.getPath() == null ? null : a.getPath().getB())
                    .setB(b == null || b.getPath() == null ? null : b.getPath().getB())
                    .setC(c == null ? null : c.getPath())
                    .setStatus(AutogenDiffStatusEnumDiffStatus.fromProto(DiffStatus.CONFLICTED))));
  }

  private static AutogenGitCodeDiff getGitDiff(
      AutogenGitCodeDiff a, AutogenGitCodeDiff b, AutogenGitCodeBlob c) {
    AutogenGitCodeDiff ret = new AutogenGitCodeDiff();
    return ret.setA(a == null ? null : a.getB())
        .setB(b == null ? null : b.getB())
        .setC(c)
        .setStatus(AutogenDiffStatusEnumDiffStatus.fromProto(DiffStatus.CONFLICTED));
  }

  private static AutogenDatasetDiff getDatasetConflictBlob(
      AutogenDatasetDiff a, AutogenDatasetDiff b, AutogenDatasetBlob c) {
    return Utils.removeEmpty(
        new AutogenDatasetDiff()
            .setPath(
                getPathDatasetConflictBlob(
                    a == null ? null : a.getPath(),
                    b == null ? null : b.getPath(),
                    c == null ? null : c.getPath()))
            .setS3(
                getS3DatasetConflictBlob(
                    a == null ? null : a.getS3(),
                    b == null ? null : b.getS3(),
                    c == null ? null : c.getS3())));
  }

  private static AutogenS3DatasetDiff getS3DatasetConflictBlob(
      AutogenS3DatasetDiff a, AutogenS3DatasetDiff b, AutogenS3DatasetBlob c) {
    return Utils.removeEmpty(
        new AutogenS3DatasetDiff()
            .setComponents(
                getS3DatasetConflictBlob(
                    a == null ? null : a.getComponents(),
                    b == null ? null : b.getComponents(),
                    c == null ? null : c.getComponents())));
  }

  private static List<AutogenS3DatasetComponentDiff> getS3DatasetConflictBlob(
      List<AutogenS3DatasetComponentDiff> a,
      List<AutogenS3DatasetComponentDiff> b,
      List<AutogenS3DatasetComponentBlob> c) {
    Map<String, AutogenS3DatasetComponentBlob> mapA = getS3DiffMap(a);
    Map<String, AutogenS3DatasetComponentBlob> mapB = getS3DiffMap(b);
    Map<String, AutogenS3DatasetComponentBlob> mapC = getS3Map(c);
    HashSet<String> keys = new HashSet<>();
    keys.addAll(mapA.keySet());
    keys.retainAll(mapB.keySet());
    List<AutogenS3DatasetComponentDiff> retList = new LinkedList<AutogenS3DatasetComponentDiff>();
    for (String key : keys) {
      if (!mapA.get(key).equals(mapB.get(key))) {
        retList.add(
            Utils.removeEmpty(
                new AutogenS3DatasetComponentDiff()
                    .setA(mapA.get(key))
                    .setB(mapB.get(key))
                    .setC(mapC.get(key))
                    .setStatus(AutogenDiffStatusEnumDiffStatus.fromProto(DiffStatus.CONFLICTED))));
      }
    }
    return retList;
  }

  private static Map<String, AutogenS3DatasetComponentBlob> getS3Map(
      List<AutogenS3DatasetComponentBlob> list) {
    if (list == null) return Collections.emptyMap();
    Map<String, AutogenS3DatasetComponentBlob> retMap =
        new HashMap<String, AutogenS3DatasetComponentBlob>();
    for (AutogenS3DatasetComponentBlob s3Blob : list) {
      String path = s3Blob.getPath().getPath();
      retMap.put(path, s3Blob);
    }
    return retMap;
  }

  private static Map<String, AutogenS3DatasetComponentBlob> getS3DiffMap(
      List<AutogenS3DatasetComponentDiff> list) {
    if (list == null) return Collections.emptyMap();
    Map<String, AutogenS3DatasetComponentBlob> retMap =
        new HashMap<String, AutogenS3DatasetComponentBlob>();
    for (AutogenS3DatasetComponentDiff diff : list) {
      String path = diff.getB().getPath().getPath();
      retMap.put(
          path,
          new AutogenS3DatasetComponentBlob()
              .setPath(diff.getB().getPath())
              .setS3VersionId(diff.getB().getS3VersionId()));
    }
    return retMap;
  }

  private static AutogenPathDatasetDiff getPathDatasetConflictBlob(
      AutogenPathDatasetDiff a, AutogenPathDatasetDiff b, AutogenPathDatasetBlob c) {
    return Utils.removeEmpty(
        new AutogenPathDatasetDiff()
            .setComponents(
                getPathDatasetConflictBlob(
                    a == null ? Collections.emptyList() : a.getComponents(),
                    b == null ? Collections.emptyList() : b.getComponents(),
                    c == null ? Collections.emptyList() : c.getComponents())));
  }

  private static List<AutogenPathDatasetComponentDiff> getPathDatasetConflictBlob(
      List<AutogenPathDatasetComponentDiff> a,
      List<AutogenPathDatasetComponentDiff> b,
      List<AutogenPathDatasetComponentBlob> c) {
    Map<String, AutogenPathDatasetComponentBlob> mapA = getPathDiffMap(a);
    Map<String, AutogenPathDatasetComponentBlob> mapB = getPathDiffMap(b);
    Map<String, AutogenPathDatasetComponentBlob> mapC = getPathMap(c);
    HashSet<String> keys = new HashSet<>();
    keys.addAll(mapA.keySet());
    keys.retainAll(mapB.keySet());
    List<AutogenPathDatasetComponentDiff> retList =
        new LinkedList<AutogenPathDatasetComponentDiff>();
    for (String key : keys) {
      if (!mapA.get(key).equals(mapB.get(key))) {
        retList.add(
            Utils.removeEmpty(
                new AutogenPathDatasetComponentDiff()
                    .setStatus(AutogenDiffStatusEnumDiffStatus.fromProto(DiffStatus.CONFLICTED))
                    .setA(mapA.get(key))
                    .setB(mapB.get(key))
                    .setC(mapC.get(key))));
      }
    }
    return retList;
  }

  private static Map<String, AutogenPathDatasetComponentBlob> getPathMap(
      List<AutogenPathDatasetComponentBlob> list) {
    if (list == null) return Collections.emptyMap();
    Map<String, AutogenPathDatasetComponentBlob> retMap =
        new HashMap<String, AutogenPathDatasetComponentBlob>();
    for (AutogenPathDatasetComponentBlob pathBlob : list) {
      String path = pathBlob.getPath();
      retMap.put(path, pathBlob);
    }
    return retMap;
  }

  private static Map<String, AutogenPathDatasetComponentBlob> getPathDiffMap(
      List<AutogenPathDatasetComponentDiff> list) {
    if (list == null) return Collections.emptyMap();
    Map<String, AutogenPathDatasetComponentBlob> retMap =
        new HashMap<String, AutogenPathDatasetComponentBlob>();
    for (AutogenPathDatasetComponentDiff diff : list) {
      String path = diff.getB().getPath();
      retMap.put(path, diff.getB());
    }
    return retMap;
  }
}
