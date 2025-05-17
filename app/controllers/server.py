import grpc
from concurrent import futures
from gen.schema import schema_pb2_grpc

class AgepoyoServiceImpl(schema_pb2_grpc.AgepoyoServiceServicer):
    pass  # 実装は後で

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    schema_pb2_grpc.add_AgepoyoServiceServicer_to_server(AgepoyoServiceImpl(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('gRPC server started on port 50051')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
