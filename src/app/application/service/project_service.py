import uuid

from app.application.request.create_project_request import CreateProjectRequest
from app.domain.project.project import Project
from app.domain.project.project_repository import ProjectRepository


class ProjectService:

    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def create(self, request: CreateProjectRequest) -> Project:
        project = Project(
            project_id=str(uuid.uuid4()),
            project_name=request.project_name,
            project_uri=request.project_uri,
            authentication=request.authentication,
            username=request.username,
            password=request.password)
        return self.project_repository.save(project)
