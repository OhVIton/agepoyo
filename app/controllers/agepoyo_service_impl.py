from app.gen.schema import schema_pb2_grpc, schema_pb2
from dependency_injector.wiring import inject, Provide
from app.di.application import ApplicationContainer
from app.use_cases.converse_use_case import ConverseUseCase
from app.domains.conversation.message import ConversationMessage
from app.domains.conversation.role import ConversationRole
from app.domains.conversation.request import ConversationRequest
from app.domains.conversation.llm_model import LlmModel
from app.domains.conversation.response import ContentType, ConversationResponse
from google.protobuf.timestamp_pb2 import Timestamp

class AgepoyoServiceImpl(schema_pb2_grpc.AgepoyoServiceServicer):
    @inject
    def __init__(self, converse_use_case: ConverseUseCase = Provide[ApplicationContainer.converse_use_case]):
        self.converse_use_case = converse_use_case

    def converse(self, request, context):
        # protobufリクエスト→ドメインリクエスト変換
        messages = [
            ConversationMessage(
                role=ConversationRole(msg.role),
                content=msg.content
            ) for msg in request.messages
        ]
        model = LlmModel(request.model)
        domain_request = ConversationRequest(messages=messages, model=model)

        # ユースケース呼び出し
        domain_response: ConversationResponse = self.converse_use_case.execute(domain_request)

        # ドメインレスポンス→protobufレスポンス変換
        ts = Timestamp()
        ts.FromDatetime(domain_response.generated_at)
        proto_response = schema_pb2.ConversationResponse(
            content_type=domain_response.content_type.value,
            content=domain_response.content,
            generated_at=ts
        )
        return proto_response

    def converseStream(self, request, context):
        context.set_code(12)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')
