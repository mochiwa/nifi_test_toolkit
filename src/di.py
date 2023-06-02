from dependency_injector import containers, providers

from src.app.application.service.create_testcase_service import CreateTestCaseService
from src.app.infrastructure.persistence.sql.sql_project_repository import SQlProjectRepository


class DI(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=['config.ini'])
    wiring_config = containers.WiringConfiguration(modules=[".app.infrastructure.rest.testcase_router"])
    project_repository = providers.Factory(
        SQlProjectRepository
    )
    create_testcase_service = providers.Factory(
        CreateTestCaseService,
        project_repository=project_repository
    )
