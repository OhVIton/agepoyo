from datetime import UTC, datetime

from domains.conversation.agent_interface import AgentInterface
from domains.conversation.conversation import Conversation
from domains.conversation.response import ContentType, ConversationResponse


class ConverseUseCase:
    """会話ユースケース."""

    def __init__(self, agent: AgentInterface) -> None:
        """ユースケース初期化."""
        self.agent = agent

    def execute(self, conversation: Conversation) -> ConversationResponse:
        """会話を実行し応答を返す."""
        llm_response = self.agent.ask(conversation)
        return ConversationResponse(
            content_type=ContentType.TEXT,
            content=llm_response,
            generated_at=datetime.now(UTC)
        )
