from dependency_injector import containers, providers

from app.application.service.project_service import ProjectService
from app.infrastructure.persistence.json_project_repository import JsonProjectRepository


class DI(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=["app.infrastructure.rest.projects_router"])
    project_repository = providers.Factory(JsonProjectRepository)

    project_service = providers.Factory(
        ProjectService,
        project_repository
    )
