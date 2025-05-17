from app.domains.conversation.agent_client import AgentClient
from app.domains.conversation.request import ConversationRequest


class TestClientImpl(AgentClient):
    """テスト用のダミーLLMクライアント実装."""

    def ask(self, conversation: ConversationRequest) -> str:
        """ダミー応答を返す."""
        return 'テスト応答: ' + (conversation.latest_user_message().content or '(empty)')
