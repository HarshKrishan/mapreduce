# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protos_pb2 as protos__pb2


class WordCountStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.clientStartup = channel.unary_unary(
                '/wordcount.WordCount/clientStartup',
                request_serializer=protos__pb2.node.SerializeToString,
                response_deserializer=protos__pb2.reply.FromString,
                )
        self.register_mapper = channel.unary_unary(
                '/wordcount.WordCount/register_mapper',
                request_serializer=protos__pb2.node.SerializeToString,
                response_deserializer=protos__pb2.reply.FromString,
                )
        self.register_reducer = channel.unary_unary(
                '/wordcount.WordCount/register_reducer',
                request_serializer=protos__pb2.node.SerializeToString,
                response_deserializer=protos__pb2.reply.FromString,
                )
        self.SubmitJob = channel.unary_unary(
                '/wordcount.WordCount/SubmitJob',
                request_serializer=protos__pb2.JobRequest.SerializeToString,
                response_deserializer=protos__pb2.reply.FromString,
                )
        self.callMapper = channel.unary_unary(
                '/wordcount.WordCount/callMapper',
                request_serializer=protos__pb2.files.SerializeToString,
                response_deserializer=protos__pb2.reply.FromString,
                )
        self.Map = channel.unary_unary(
                '/wordcount.WordCount/Map',
                request_serializer=protos__pb2.MapInput.SerializeToString,
                response_deserializer=protos__pb2.MapOutput.FromString,
                )
        self.callReducer = channel.unary_unary(
                '/wordcount.WordCount/callReducer',
                request_serializer=protos__pb2.files.SerializeToString,
                response_deserializer=protos__pb2.reply.FromString,
                )
        self.Reduce = channel.unary_unary(
                '/wordcount.WordCount/Reduce',
                request_serializer=protos__pb2.ReduceInput.SerializeToString,
                response_deserializer=protos__pb2.reduceOutputList.FromString,
                )


class WordCountServicer(object):
    """Missing associated documentation comment in .proto file."""

    def clientStartup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def register_mapper(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def register_reducer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def callMapper(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Map(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def callReducer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reduce(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WordCountServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'clientStartup': grpc.unary_unary_rpc_method_handler(
                    servicer.clientStartup,
                    request_deserializer=protos__pb2.node.FromString,
                    response_serializer=protos__pb2.reply.SerializeToString,
            ),
            'register_mapper': grpc.unary_unary_rpc_method_handler(
                    servicer.register_mapper,
                    request_deserializer=protos__pb2.node.FromString,
                    response_serializer=protos__pb2.reply.SerializeToString,
            ),
            'register_reducer': grpc.unary_unary_rpc_method_handler(
                    servicer.register_reducer,
                    request_deserializer=protos__pb2.node.FromString,
                    response_serializer=protos__pb2.reply.SerializeToString,
            ),
            'SubmitJob': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitJob,
                    request_deserializer=protos__pb2.JobRequest.FromString,
                    response_serializer=protos__pb2.reply.SerializeToString,
            ),
            'callMapper': grpc.unary_unary_rpc_method_handler(
                    servicer.callMapper,
                    request_deserializer=protos__pb2.files.FromString,
                    response_serializer=protos__pb2.reply.SerializeToString,
            ),
            'Map': grpc.unary_unary_rpc_method_handler(
                    servicer.Map,
                    request_deserializer=protos__pb2.MapInput.FromString,
                    response_serializer=protos__pb2.MapOutput.SerializeToString,
            ),
            'callReducer': grpc.unary_unary_rpc_method_handler(
                    servicer.callReducer,
                    request_deserializer=protos__pb2.files.FromString,
                    response_serializer=protos__pb2.reply.SerializeToString,
            ),
            'Reduce': grpc.unary_unary_rpc_method_handler(
                    servicer.Reduce,
                    request_deserializer=protos__pb2.ReduceInput.FromString,
                    response_serializer=protos__pb2.reduceOutputList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'wordcount.WordCount', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WordCount(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def clientStartup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wordcount.WordCount/clientStartup',
            protos__pb2.node.SerializeToString,
            protos__pb2.reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def register_mapper(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wordcount.WordCount/register_mapper',
            protos__pb2.node.SerializeToString,
            protos__pb2.reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def register_reducer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wordcount.WordCount/register_reducer',
            protos__pb2.node.SerializeToString,
            protos__pb2.reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wordcount.WordCount/SubmitJob',
            protos__pb2.JobRequest.SerializeToString,
            protos__pb2.reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def callMapper(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wordcount.WordCount/callMapper',
            protos__pb2.files.SerializeToString,
            protos__pb2.reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Map(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wordcount.WordCount/Map',
            protos__pb2.MapInput.SerializeToString,
            protos__pb2.MapOutput.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def callReducer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wordcount.WordCount/callReducer',
            protos__pb2.files.SerializeToString,
            protos__pb2.reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reduce(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wordcount.WordCount/Reduce',
            protos__pb2.ReduceInput.SerializeToString,
            protos__pb2.reduceOutputList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)