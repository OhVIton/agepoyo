# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc

import agepoyo_pb2 as agepoyo__pb2


class AgepoyoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.converseWithAgent = channel.unary_unary(
            "/agepoyo.AgepoyoService/converseWithAgent",
            request_serializer=agepoyo__pb2.ConversationRequest.SerializeToString,
            response_deserializer=agepoyo__pb2.ConversationResponse.FromString,
            _registered_method=True,
        )
        self.converseWithAgentStream = channel.unary_stream(
            "/agepoyo.AgepoyoService/converseWithAgentStream",
            request_serializer=agepoyo__pb2.ConversationRequest.SerializeToString,
            response_deserializer=agepoyo__pb2.ConversationResponse.FromString,
            _registered_method=True,
        )


class AgepoyoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def converseWithAgent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def converseWithAgentStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AgepoyoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "converseWithAgent": grpc.unary_unary_rpc_method_handler(
            servicer.converseWithAgent,
            request_deserializer=agepoyo__pb2.ConversationRequest.FromString,
            response_serializer=agepoyo__pb2.ConversationResponse.SerializeToString,
        ),
        "converseWithAgentStream": grpc.unary_stream_rpc_method_handler(
            servicer.converseWithAgentStream,
            request_deserializer=agepoyo__pb2.ConversationRequest.FromString,
            response_serializer=agepoyo__pb2.ConversationResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "agepoyo.AgepoyoService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers("agepoyo.AgepoyoService", rpc_method_handlers)


# This class is part of an EXPERIMENTAL API.
class AgepoyoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def converseWithAgent(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/agepoyo.AgepoyoService/converseWithAgent",
            agepoyo__pb2.ConversationRequest.SerializeToString,
            agepoyo__pb2.ConversationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )

    @staticmethod
    def converseWithAgentStream(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/agepoyo.AgepoyoService/converseWithAgentStream",
            agepoyo__pb2.ConversationRequest.SerializeToString,
            agepoyo__pb2.ConversationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
