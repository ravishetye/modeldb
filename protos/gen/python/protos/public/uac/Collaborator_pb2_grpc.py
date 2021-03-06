# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from ..uac import Collaborator_pb2 as uac_dot_Collaborator__pb2


class CollaboratorServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.addOrUpdateProjectCollaborator = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/addOrUpdateProjectCollaborator',
        request_serializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.Response.FromString,
        )
    self.removeProjectCollaborator = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/removeProjectCollaborator',
        request_serializer=uac_dot_Collaborator__pb2.RemoveCollaborator.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.RemoveCollaborator.Response.FromString,
        )
    self.getProjectCollaborators = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/getProjectCollaborators',
        request_serializer=uac_dot_Collaborator__pb2.GetCollaborator.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.GetCollaborator.Response.FromString,
        )
    self.addOrUpdateDatasetCollaborator = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/addOrUpdateDatasetCollaborator',
        request_serializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.Response.FromString,
        )
    self.removeDatasetCollaborator = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/removeDatasetCollaborator',
        request_serializer=uac_dot_Collaborator__pb2.RemoveCollaborator.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.RemoveCollaborator.Response.FromString,
        )
    self.getDatasetCollaborators = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/getDatasetCollaborators',
        request_serializer=uac_dot_Collaborator__pb2.GetCollaborator.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.GetCollaborator.Response.FromString,
        )
    self.addOrUpdateRepositoryCollaborator = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/addOrUpdateRepositoryCollaborator',
        request_serializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.Response.FromString,
        )
    self.removeRepositoryCollaborator = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/removeRepositoryCollaborator',
        request_serializer=uac_dot_Collaborator__pb2.RemoveCollaborator.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.RemoveCollaborator.Response.FromString,
        )
    self.getRepositoryCollaborators = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/getRepositoryCollaborators',
        request_serializer=uac_dot_Collaborator__pb2.GetCollaborator.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.GetCollaborator.Response.FromString,
        )
    self.addOrUpdateEndpointCollaborator = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/addOrUpdateEndpointCollaborator',
        request_serializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.Response.FromString,
        )
    self.removeEndpointCollaborator = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/removeEndpointCollaborator',
        request_serializer=uac_dot_Collaborator__pb2.RemoveCollaborator.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.RemoveCollaborator.Response.FromString,
        )
    self.getEndpointCollaborators = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/getEndpointCollaborators',
        request_serializer=uac_dot_Collaborator__pb2.GetCollaborator.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.GetCollaborator.Response.FromString,
        )
    self.addOrUpdateRegisteredModelCollaborator = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/addOrUpdateRegisteredModelCollaborator',
        request_serializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.Response.FromString,
        )
    self.removeRegisteredModelCollaborator = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/removeRegisteredModelCollaborator',
        request_serializer=uac_dot_Collaborator__pb2.RemoveCollaborator.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.RemoveCollaborator.Response.FromString,
        )
    self.getRegisteredModelCollaborators = channel.unary_unary(
        '/ai.verta.uac.CollaboratorService/getRegisteredModelCollaborators',
        request_serializer=uac_dot_Collaborator__pb2.GetCollaborator.SerializeToString,
        response_deserializer=uac_dot_Collaborator__pb2.GetCollaborator.Response.FromString,
        )


class CollaboratorServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def addOrUpdateProjectCollaborator(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def removeProjectCollaborator(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getProjectCollaborators(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addOrUpdateDatasetCollaborator(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def removeDatasetCollaborator(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getDatasetCollaborators(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addOrUpdateRepositoryCollaborator(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def removeRepositoryCollaborator(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getRepositoryCollaborators(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addOrUpdateEndpointCollaborator(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def removeEndpointCollaborator(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getEndpointCollaborators(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def addOrUpdateRegisteredModelCollaborator(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def removeRegisteredModelCollaborator(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getRegisteredModelCollaborators(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CollaboratorServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'addOrUpdateProjectCollaborator': grpc.unary_unary_rpc_method_handler(
          servicer.addOrUpdateProjectCollaborator,
          request_deserializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.FromString,
          response_serializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.Response.SerializeToString,
      ),
      'removeProjectCollaborator': grpc.unary_unary_rpc_method_handler(
          servicer.removeProjectCollaborator,
          request_deserializer=uac_dot_Collaborator__pb2.RemoveCollaborator.FromString,
          response_serializer=uac_dot_Collaborator__pb2.RemoveCollaborator.Response.SerializeToString,
      ),
      'getProjectCollaborators': grpc.unary_unary_rpc_method_handler(
          servicer.getProjectCollaborators,
          request_deserializer=uac_dot_Collaborator__pb2.GetCollaborator.FromString,
          response_serializer=uac_dot_Collaborator__pb2.GetCollaborator.Response.SerializeToString,
      ),
      'addOrUpdateDatasetCollaborator': grpc.unary_unary_rpc_method_handler(
          servicer.addOrUpdateDatasetCollaborator,
          request_deserializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.FromString,
          response_serializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.Response.SerializeToString,
      ),
      'removeDatasetCollaborator': grpc.unary_unary_rpc_method_handler(
          servicer.removeDatasetCollaborator,
          request_deserializer=uac_dot_Collaborator__pb2.RemoveCollaborator.FromString,
          response_serializer=uac_dot_Collaborator__pb2.RemoveCollaborator.Response.SerializeToString,
      ),
      'getDatasetCollaborators': grpc.unary_unary_rpc_method_handler(
          servicer.getDatasetCollaborators,
          request_deserializer=uac_dot_Collaborator__pb2.GetCollaborator.FromString,
          response_serializer=uac_dot_Collaborator__pb2.GetCollaborator.Response.SerializeToString,
      ),
      'addOrUpdateRepositoryCollaborator': grpc.unary_unary_rpc_method_handler(
          servicer.addOrUpdateRepositoryCollaborator,
          request_deserializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.FromString,
          response_serializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.Response.SerializeToString,
      ),
      'removeRepositoryCollaborator': grpc.unary_unary_rpc_method_handler(
          servicer.removeRepositoryCollaborator,
          request_deserializer=uac_dot_Collaborator__pb2.RemoveCollaborator.FromString,
          response_serializer=uac_dot_Collaborator__pb2.RemoveCollaborator.Response.SerializeToString,
      ),
      'getRepositoryCollaborators': grpc.unary_unary_rpc_method_handler(
          servicer.getRepositoryCollaborators,
          request_deserializer=uac_dot_Collaborator__pb2.GetCollaborator.FromString,
          response_serializer=uac_dot_Collaborator__pb2.GetCollaborator.Response.SerializeToString,
      ),
      'addOrUpdateEndpointCollaborator': grpc.unary_unary_rpc_method_handler(
          servicer.addOrUpdateEndpointCollaborator,
          request_deserializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.FromString,
          response_serializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.Response.SerializeToString,
      ),
      'removeEndpointCollaborator': grpc.unary_unary_rpc_method_handler(
          servicer.removeEndpointCollaborator,
          request_deserializer=uac_dot_Collaborator__pb2.RemoveCollaborator.FromString,
          response_serializer=uac_dot_Collaborator__pb2.RemoveCollaborator.Response.SerializeToString,
      ),
      'getEndpointCollaborators': grpc.unary_unary_rpc_method_handler(
          servicer.getEndpointCollaborators,
          request_deserializer=uac_dot_Collaborator__pb2.GetCollaborator.FromString,
          response_serializer=uac_dot_Collaborator__pb2.GetCollaborator.Response.SerializeToString,
      ),
      'addOrUpdateRegisteredModelCollaborator': grpc.unary_unary_rpc_method_handler(
          servicer.addOrUpdateRegisteredModelCollaborator,
          request_deserializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.FromString,
          response_serializer=uac_dot_Collaborator__pb2.AddCollaboratorRequest.Response.SerializeToString,
      ),
      'removeRegisteredModelCollaborator': grpc.unary_unary_rpc_method_handler(
          servicer.removeRegisteredModelCollaborator,
          request_deserializer=uac_dot_Collaborator__pb2.RemoveCollaborator.FromString,
          response_serializer=uac_dot_Collaborator__pb2.RemoveCollaborator.Response.SerializeToString,
      ),
      'getRegisteredModelCollaborators': grpc.unary_unary_rpc_method_handler(
          servicer.getRegisteredModelCollaborators,
          request_deserializer=uac_dot_Collaborator__pb2.GetCollaborator.FromString,
          response_serializer=uac_dot_Collaborator__pb2.GetCollaborator.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ai.verta.uac.CollaboratorService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
