
from dependency_injector import containers, providers

from app.di.use_cases.converse_use_case_container import ConverseUseCaseContainer


# アプリケーション全体のDIコンテナ
class ApplicationContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=[
        "app.controllers",
        "app.use_cases",
        "app.services",
        "app.infrastructures",
    ])

    converse_use_case = providers.DelegatedFactory(
        ConverseUseCaseContainer.converse_use_case
    )
