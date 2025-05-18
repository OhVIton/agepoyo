from contextlib import AsyncExitStack
from typing import TYPE_CHECKING

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from google.genai.types import Content, Part

from app.domains.conversation.agent_client import AgentClient
from app.domains.conversation.llm_model import LlmModel
from app.domains.conversation.request import ConversationRequest
from app.domains.conversation.role import ConversationRole

if TYPE_CHECKING:
    from collections.abc import Generator

    from google.adk.events import Event


class AdkClientImpl(AgentClient):
    """Agent Client Using ADK."""

    async def ask(self, conversation_request: ConversationRequest) -> str:
        """Ask a question to the agent."""

        common_exit_stack = AsyncExitStack()

        fetch_tools, _ = await MCPToolset.from_server(
            connection_params=StdioServerParameters(
                command='uvx',
                args=[
                    "mcp-server-fetch"
                ],
                common_exit_stack=common_exit_stack,
            ),
        )

        agent = Agent(
            name="adk_client",
            description="ADK Client",
            model=self.__llm_model_to_agent_model(conversation_request.model),
            tools=[*fetch_tools],
        )
        session_service = InMemorySessionService()

        app_name = "adk_client_app"
        user_id = "user_0"
        session_id = "session_0"

        session_service.create_session(
            app_name=app_name,
            user_id=user_id,
            session_id=session_id,
        )

        runner = Runner(
            app_name=app_name,
            agent=agent,
            session_service=session_service,
        )

        generator: Generator[Event, None, None] = runner.run(
            new_message=Content(
                parts=self.__conversation_to_agent_parts(conversation_request),
                role=self.__role_to_agent_role(
                    conversation_request.latest_user_message().role
                ),
            ),
            user_id=user_id,
            session_id=session_id,
        )

        return "".join([event.content.parts[0].text for event in generator])

    def __llm_model_to_agent_model(self, llm_model: LlmModel) -> LiteLlm | str:
        match llm_model:
            case LlmModel.GPT_41:
                return LiteLlm(model="gpt-4.1")
            case LlmModel.GPT_4O:
                return LiteLlm(model="gpt-4o")
            case LlmModel.CLAUDE_37_SONNET:
                return LiteLlm(model="claude-3-7-sonnet-20250219")
            case _:
                return "gemini-2.0-flash"

    def __role_to_agent_role(self, role: ConversationRole) -> str:
        match role:
            case ConversationRole.USER:
                return "user"
            case ConversationRole.ASSISTANT:
                return "model"

    def __conversation_to_agent_parts(
        self, conversation_request: ConversationRequest
    ) -> list[Part]:
        return [Part(text=conversation_request.latest_user_message().content)]
