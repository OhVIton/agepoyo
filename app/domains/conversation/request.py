
from .llm_model import LlmModel
from .message import ConversationMessage
from .role import ConversationRole


class ConversationRequest:
    """会話リクエスト(複数メッセージ+モデル指定)."""

    def __init__(self, messages: list[ConversationMessage], model: LlmModel) -> None:
        """リクエスト生成."""
        self.messages = messages
        self.model = model

    def latest_user_message(self) -> str:
        """直近のユーザーメッセージを返す."""
        for msg in reversed(self.messages):
            if msg.role == ConversationRole.USER:
                return msg.content
        return ""
