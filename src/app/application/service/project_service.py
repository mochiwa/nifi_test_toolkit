import uuid

from app.domain.project.project import Project


class ProjectService:

    def create(self, data):
        project = Project(project_id=str(uuid.uuid4()))
        return project
