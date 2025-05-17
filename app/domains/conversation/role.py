from enum import Enum


class ConversationRole(Enum):
    """会話の役割(ユーザー/アシスタント)."""

    USER = 1
    ASSISTANT = 2
