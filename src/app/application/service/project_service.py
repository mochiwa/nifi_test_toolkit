import uuid

from app.domain.project.project import Project
from app.domain.project.project_repository import ProjectRepository


class ProjectService:

    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def create(self, data) -> Project:
        project = Project(project_id=str(uuid.uuid4()))
        return self.project_repository.save(project)
