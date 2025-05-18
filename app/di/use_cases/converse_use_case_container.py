from dependency_injector import containers, providers

from app.infrastructures.clients.adk_client_impl import AdkClientImpl
from app.use_cases.converse_with_agent_use_case import ConverseWithAgentUseCase


class ConverseUseCaseContainer(containers.DeclarativeContainer):
    """ConverseUseCase用のDIコンテナ."""

    agent_client = providers.Singleton(
        AdkClientImpl,
    )
    converse_use_case = providers.Factory(ConverseWithAgentUseCase, agent=agent_client)
