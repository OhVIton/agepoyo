from typing import TYPE_CHECKING, Any

from dependency_injector.wiring import Provide, inject
from google.protobuf.timestamp_pb2 import Timestamp

from app.di.application import ApplicationContainer
from app.domains.conversation.llm_model import LlmModel
from app.domains.conversation.message import ConversationMessage
from app.domains.conversation.request import ConversationRequest
from app.domains.conversation.role import ConversationRole
from app.gen import schema_pb2, schema_pb2_grpc
from app.use_cases.converse_use_case import ConverseUseCase

if TYPE_CHECKING:
    from app.domains.conversation.response import ConversationResponse


class AgepoyoServiceImpl(schema_pb2_grpc.AgepoyoServiceServicer):
    """gRPC Agepoyoサービスの実装."""

    @inject
    def __init__(
        self,
        converse_use_case: ConverseUseCase = Provide[
            ApplicationContainer.converse_use_case
        ],
    ) -> None:
        """DIでConverseUseCaseを注入."""
        self.converse_use_case = converse_use_case

    def converse(self, request: Any, _context: Any) -> schema_pb2.ConversationResponse:
        """会話リクエストを処理し、レスポンスを返す."""
        messages = [
            ConversationMessage(role=ConversationRole(msg.role), content=msg.content)
            for msg in request.messages
        ]
        model = LlmModel(request.model)
        domain_request = ConversationRequest(messages=messages, model=model)

        # ユースケース呼び出し
        domain_response: ConversationResponse = self.converse_use_case.execute(
            domain_request
        )

        # ドメインレスポンス→protobufレスポンス変換
        ts = Timestamp()
        ts.FromDatetime(domain_response.generated_at)
        return schema_pb2.ConversationResponse(
            content_type=domain_response.content_type.value,
            content=domain_response.content,
            generated_at=ts,
        )

    def converse_stream(self, _request: Any, context: Any) -> None:
        """未実装: ストリーム会話API."""
        context.set_code(12)
        context.set_details('Method not implemented!')
        raise NotImplementedError
