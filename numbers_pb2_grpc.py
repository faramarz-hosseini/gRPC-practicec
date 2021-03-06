# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import numbers_pb2 as numbers__pb2


class OperationsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DoOps = channel.unary_unary(
                '/Operations/DoOps',
                request_serializer=numbers__pb2.Number.SerializeToString,
                response_deserializer=numbers__pb2.Result.FromString,
                )


class OperationsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def DoOps(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OperationsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DoOps': grpc.unary_unary_rpc_method_handler(
                    servicer.DoOps,
                    request_deserializer=numbers__pb2.Number.FromString,
                    response_serializer=numbers__pb2.Result.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Operations', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Operations(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def DoOps(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Operations/DoOps',
            numbers__pb2.Number.SerializeToString,
            numbers__pb2.Result.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
