from domains.conversation.agent_interface import AgentInterface
from domains.conversation.conversation import Conversation


class AgentClient(AgentInterface):
    """ADKを利用したLLMクライアントの実装(インフラ層)."""

    def __init__(self, api_key: str) -> None:
        """初期化."""
        self.api_key = api_key
        # TODO(teddy): ADKの初期化

    def ask(self, conversation: Conversation) -> str:
        """LLMに問い合わせて応答を返す(現状はダミー)."""
        # TODO(teddy): ADKを使ってLLMに問い合わせる処理を実装
        # ここではダミー応答
        return conversation.latest_user_message()
