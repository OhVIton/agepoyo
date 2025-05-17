from .role import ConversationRole


class ConversationMessage:
    """会話メッセージ."""

    def __init__(self, role: ConversationRole, content: str) -> None:
        """メッセージ生成."""
        self.role = role
        self.content = content
