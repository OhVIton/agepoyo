from typing import TYPE_CHECKING, Any

from dependency_injector.wiring import Provide, inject
from google.protobuf.timestamp_pb2 import Timestamp
from grpc import StatusCode

from app.di.application import ApplicationContainer
from app.domains.conversation.llm_model import LlmModel
from app.domains.conversation.message import ConversationMessage
from app.domains.conversation.request import ConversationRequest
from app.domains.conversation.response import ContentType
from app.domains.conversation.role import ConversationRole
from app.gen import agepoyo_pb2, agepoyo_pb2_grpc
from app.use_cases.converse_with_agent_use_case import ConverseWithAgentUseCase

if TYPE_CHECKING:
    from app.domains.conversation.response import ConversationResponse


class AgepoyoServiceImpl(agepoyo_pb2_grpc.AgepoyoServiceServicer):
    """gRPC Agepoyoサービスの実装."""

    @inject
    def __init__(
        self,
        converse_use_case: ConverseWithAgentUseCase = Provide[
            ApplicationContainer.converse_use_case
        ],
    ) -> None:
        """DIでConverseUseCaseを注入."""
        self.converse_use_case = converse_use_case

    def converseWithAgent(
        self, request: Any, context: Any
    ) -> agepoyo_pb2.ConversationResponse:
        """会話リクエストを処理し、レスポンスを返す."""
        messages = [
            ConversationMessage(role=ConversationRole(msg.role), content=msg.content)
            for msg in request.messages
        ]
        match request.model:
            case agepoyo_pb2.GPT_41:
                model = LlmModel.GPT_41
            case agepoyo_pb2.GPT_4O:
                model = LlmModel.GPT_4O
            case agepoyo_pb2.GEMINI_20_FLASH:
                model = LlmModel.GEMINI_20_FLASH
            case agepoyo_pb2.CLAUDE_37_SONNET:
                model = LlmModel.CLAUDE_37_SONNET
            case _:
                context.set_code(StatusCode.UNIMPLEMENTED)
                context.set_details("Unsupported model")
                raise NotImplementedError(f"Unsupported model: {request.model}")
        model = LlmModel(request.model)
        domain_request = ConversationRequest(messages=messages, model=model)

        # ユースケース呼び出し
        try:
            domain_response: ConversationResponse = self.converse_use_case.call(
                domain_request
            )
        except Exception as e:
            context.set_code(StatusCode.INTERNAL)
            context.set_details("Internal server error")
            raise e

        # ドメインレスポンス→protobufレスポンス変換
        ts = Timestamp()
        ts.FromDatetime(domain_response.generated_at)

        match domain_response.content_type:
            case ContentType.TEXT:
                content_type = agepoyo_pb2.ContentType.TEXT
            case ContentType.IMAGE:
                content_type = agepoyo_pb2.ContentType.IMAGE
            case ContentType.VIDEO:
                content_type = agepoyo_pb2.ContentType.VIDEO
            case ContentType.FILE:
                content_type = agepoyo_pb2.ContentType.FILE
            case ContentType.AUDIO:
                content_type = agepoyo_pb2.ContentType.AUDIO

        return agepoyo_pb2.ConversationResponse(
            content_type=content_type,
            content=domain_response.content,
            generated_at=ts,
        )

    def converseWithAgentStream(self, _request: Any, context: Any) -> None:
        """未実装: ストリーム会話API."""
        context.set_code(12)
        context.set_details("Method not implemented!")
        raise NotImplementedError
