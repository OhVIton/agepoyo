from datetime import datetime
from enum import Enum


class ContentType(Enum):
    """応答のコンテンツ種別."""

    TEXT = 1
    IMAGE = 2
    AUDIO = 3
    VIDEO = 4
    FILE = 5

class ConversationResponse:
    """会話応答."""

    def __init__(
        self,
        content_type: ContentType,
        content: str,
        generated_at: datetime,
    ) -> None:
        """応答生成."""
        self.content_type = content_type
        self.content = content
        self.generated_at = generated_at
