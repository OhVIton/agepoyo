
from google.adk.agents import Agent

from app.domains.conversation.agent_client import AgentClient
from app.domains.conversation.request import ConversationRequest


class ADKClientImpl(AgentClient):
    """ADKを利用したLLMクライアントの実装(インフラ層)."""

    def __init__(self, api_key: str) -> None:
        """初期化."""
        self.api_key = api_key
        # ADK Agentの初期化（OpenAIモデル指定）
        self.agent = Agent(
            name="openai_agent",
            model="openai/gpt-3.5-turbo",
            description="OpenAI GPT-3.5 agent",
            instruction="You are a helpful assistant.",
            api_key=api_key,
        )

    def ask(self, conversation: ConversationRequest) -> str:
        """ADK経由でOpenAI APIに問い合わせて応答を返す."""
        messages = [
            {"role": "user" if m.role.name == "USER" else "assistant", "content": m.content}
            for m in conversation.messages
        ]
        result = self.agent.run(messages)
        return result["output"] if isinstance(result, dict) and "output" in result else str(result)
