import time
from multiprocessing import Process

import grpc
import pytest

from app.gen.schema import schema_pb2, schema_pb2_grpc
from app.main import serve


# サーバーを別プロセスで起動
@pytest.fixture(scope="module", autouse=True)
def grpc_server():
    proc = Process(target=serve)
    proc.start()
    time.sleep(1)  # サーバー起動待ち
    yield
    proc.terminate()
    proc.join()

def test_converse(grpc_server):
    channel = grpc.insecure_channel("localhost:50051")
    stub = schema_pb2_grpc.AgepoyoServiceStub(channel)
    req = schema_pb2.ConversationRequest(
        messages=[
            schema_pb2.ConversationMessage(role=1, content="こんにちは")
        ],
        model=1
    )
    res = stub.converse(req)
    assert res.content  # 何か返ってくること
    assert res.content_type == 1  # TEXT
