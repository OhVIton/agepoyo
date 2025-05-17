from dependency_injector import containers, providers
from app.infrastructures.clients.adk_client_impl import ADKClientImpl
from app.infrastructures.clients.test_client_impl import TestClientImpl
from app.use_cases.converse_use_case import ConverseUseCase
from app.domains.conversation.agent_client import AgentClient
import os

# アプリケーション全体のDIコンテナ
class ApplicationContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=[
        "app.controllers",
        "app.use_cases",
        "app.services",
        "app.infrastructures",
    ])

    # AgentClientの実装をDI
    agent_client = providers.Singleton(
        TestClientImpl,
        api_key=os.environ.get("ADK_API_KEY", "dummy-key")
    )

    # ConverseUseCaseをDI
    converse_use_case = providers.Factory(
        ConverseUseCase,
        agent=agent_client
    )
