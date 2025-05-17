from typing import Protocol

from .request import ConversationRequest


class AgentInterface(Protocol):
    """LLMエージェントの抽象インターフェース."""

    def ask(self, conversation: ConversationRequest) -> str:
        """会話リクエストを受けて応答を返す."""
        ...
