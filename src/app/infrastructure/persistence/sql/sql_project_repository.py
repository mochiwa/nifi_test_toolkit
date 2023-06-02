from src.app.domain.testcase.project_repository import ProjectRepository


class SQlProjectRepository(ProjectRepository):
    def get_project(self, project_id: str):
        raise NotImplemented
