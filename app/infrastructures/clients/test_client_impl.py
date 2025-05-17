from app.domains.conversation.agent_client import AgentClient
from app.domains.conversation.request import ConversationRequest

class TestClientImpl(AgentClient):
    """テスト用のダミーLLMクライアント実装."""
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
    def ask(self, conversation: ConversationRequest) -> str:
        return "テスト応答: " + (conversation.latest_user_message() or "(empty)")
