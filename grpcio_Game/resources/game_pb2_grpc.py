# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import resources.game_pb2 as game__pb2


class AnalizerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendHand = channel.unary_unary(
                '/Analizer/SendHand',
                request_serializer=game__pb2.Hand.SerializeToString,
                response_deserializer=game__pb2.void.FromString,
                )
        self.getWinner = channel.unary_unary(
                '/Analizer/getWinner',
                request_serializer=game__pb2.void.SerializeToString,
                response_deserializer=game__pb2.Hand.FromString,
                )


class AnalizerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendHand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getWinner(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AnalizerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendHand': grpc.unary_unary_rpc_method_handler(
                    servicer.SendHand,
                    request_deserializer=game__pb2.Hand.FromString,
                    response_serializer=game__pb2.void.SerializeToString,
            ),
            'getWinner': grpc.unary_unary_rpc_method_handler(
                    servicer.getWinner,
                    request_deserializer=game__pb2.void.FromString,
                    response_serializer=game__pb2.Hand.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Analizer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Analizer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendHand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Analizer/SendHand',
            game__pb2.Hand.SerializeToString,
            game__pb2.void.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getWinner(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Analizer/getWinner',
            game__pb2.void.SerializeToString,
            game__pb2.Hand.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
