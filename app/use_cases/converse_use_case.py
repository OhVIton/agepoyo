from datetime import UTC, datetime
import asyncio

from app.domains.conversation.agent_client import AgentClient
from app.domains.conversation.request import ConversationRequest
from app.domains.conversation.response import ContentType, ConversationResponse


class ConverseUseCase:
    """会話ユースケース."""

    def __init__(self, agent: AgentClient) -> None:
        """ユースケース初期化."""
        self.agent = agent

    def execute(self, request: ConversationRequest) -> ConversationResponse:
        """会話を実行し応答を返す."""
        llm_response = asyncio.run(self.agent.ask(request))
        return ConversationResponse(
            content_type=ContentType.TEXT,
            content=llm_response,
            generated_at=datetime.now(UTC),
        )
