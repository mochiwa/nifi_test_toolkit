from dependency_injector import containers, providers

from app.application.service.project_service import ProjectService


class DI(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["app.infrastructure.rest.projects_router"])
    project_service = providers.Factory(
        ProjectService
    )

    # db = providers.Singleton(Database, url=config.db.url)
    #
    # project_repository = providers.Factory(
    #     SQlProjectRepository,
    #     session_factory=db.provided.session
    # )


