from abc import ABC, abstractmethod

from .request import ConversationRequest


class AgentClient(ABC):
    """LLMエージェントの抽象インターフェース."""

    @abstractmethod
    def ask(self, conversation: ConversationRequest) -> str:
        """会話リクエストを受けて応答を返す."""
