from collections.abc import Generator

from google.adk.agents import Agent
from google.adk.events import Event
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.genai.types import Content, Part

from app.domains.conversation.agent_client import AgentClient
from app.domains.conversation.llm_model import LlmModel
from app.domains.conversation.request import ConversationRequest
from app.domains.conversation.role import ConversationRole


class AdkClientImpl(AgentClient):
    """Agent Client Using ADK."""

    def ask(self, conversation_request: ConversationRequest) -> str:
        agent = Agent(
            name="adk_client",
            description="ADK Client",
            model=self.__llm_model_to_agent_model(conversation_request.model),
        )
        session_service = InMemorySessionService()

        APP_NAME = "adk_client_app"
        USER_ID = "user_0"
        SESSION_ID = "session_0"

        session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=SESSION_ID,
        )

        runner = Runner(
            app_name=APP_NAME,
            agent=agent,
            session_service=session_service,
        )

        generator: Generator[Event, None, None] = runner.run(
            new_message=Content(
                parts=self.__conversation_to_agent_parts(conversation_request),
                role=self.__role_to_agent_role(conversation_request.latest_user_message().role),
            ),
            user_id=USER_ID,
            session_id=SESSION_ID,
        )

        return "".join(
            [event.content.parts[0].text for event in generator]
        )

    def __llm_model_to_agent_model(self, llm_model: LlmModel) -> str:
        match (llm_model):
            case LlmModel.GPT_41:
                return LiteLlm(model="gpt-4.1")
            case _:
                return "gemini-2.0-flash"

    def __role_to_agent_role(self, role: ConversationRole) -> str:
        match (role):
            case ConversationRole.USER:
                return "user"
            case ConversationRole.ASSISTANT:
                return "model"
            case _:
                return "user"

    def __conversation_to_agent_parts(self, conversation_request: ConversationRequest) -> list[Part]:
        return [
            Part(
                text=conversation_request
                    .latest_user_message()
                    .content
            )
        ]
