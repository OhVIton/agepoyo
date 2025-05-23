import logging
import os
from concurrent import futures

import grpc
from dotenv import load_dotenv

from app.controllers.agepoyo_service_impl import AgepoyoServiceImpl
from app.di.application import ApplicationContainer
from app.gen import agepoyo_pb2_grpc

PORT = 50000


def serve() -> None:
    """gRPCサーバーを起動する."""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("agepoyo")

    container = ApplicationContainer()
    container.wire(modules=["app.controllers.agepoyo_service_impl"])

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agepoyo_pb2_grpc.add_AgepoyoServiceServicer_to_server(AgepoyoServiceImpl(), server)
    server.add_insecure_port(f"[::]:{PORT}")

    logger.info("Starting gRPC Server")
    server.start()
    logger.info("Server started, listening")
    server.wait_for_termination()


if __name__ == "__main__":
    env = os.getenv("ENV")
    load_dotenv(f"app/.env{('.' + env) if env else ''}")

    serve()
