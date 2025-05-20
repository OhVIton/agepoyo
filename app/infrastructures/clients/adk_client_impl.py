import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import BaseSessionService,InMemorySessionService
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from google.genai.types import Content, Part
from google.adk.tools.mcp_tool import MCPTool

from app.domains.conversation.agent_client import AgentClient
from app.domains.conversation.llm_model import LlmModel
from app.domains.conversation.request import ConversationRequest
from app.domains.conversation.role import ConversationRole

class AdkClientImpl(AgentClient):
    """Agent Client Using ADK."""
    APP_NAME = "adk_client_app"
    USER_ID = "user_0"

    async def ask(self, conversation_request: ConversationRequest) -> str:
        """Ask a question to the agent."""

        session_service = InMemorySessionService()

        runner = await self.__generate_agent_runner(
            session_service=session_service,
            conversation_request=conversation_request,
        )

        session = session_service.create_session(
            app_name=self.APP_NAME,
            user_id=self.USER_ID,
        )

        events = runner.run_async(
            user_id=self.USER_ID,
            session_id=session.id,
            new_message=Content(
                parts=self.__conversation_to_agent_parts(conversation_request),
                role=self.__role_to_agent_role(
                    conversation_request.latest_user_message().role
                ),
            ),
        )

        text = ""
        async for event in events:
            print(event)
            if event.content:
                text += "".join(
                    [part.text for part in event.content.parts if part.text]
                )
                print(text)

        return text
    
    async def __generate_agent_runner(
        self,
        session_service: BaseSessionService,
        conversation_request: ConversationRequest,
    ) -> Runner:
        """Run the agent runner."""

        agent = Agent(
            name="adk_client",
            description="ADK Client",
            model=self.__llm_model_to_agent_model(conversation_request.model),
            tools=[*await self.__fetch_tools()],
        )

        return Runner(
            app_name=self.APP_NAME,
            agent=agent,
            session_service=session_service,
        )
    
    async def __fetch_tools(self) -> list[MCPTool]:
        """Fetch tools from the server.
        
        将来的には、ask, askStreamのメソッドで指定できるようにする
        """

        fetch_tools, _ = await MCPToolset.from_server(
            connection_params=StdioServerParameters(
                command='uvx',
                args=[
                    "mcp-server-fetch"
                ],
            ),
        )

        google_maps_tools, _ = await MCPToolset.from_server(
            connection_params=StdioServerParameters(
                command='npx',
                args=[
                    '-y',
                    '@modelcontextprotocol/server-google-maps'
                ],
                env={
                    "GOOGLE_MAPS_API_KEY": os.getenv("GOOGLE_MAPS_API_KEY"),
                }
            )
        )

        return [
            *fetch_tools,
            *google_maps_tools,
        ]

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
