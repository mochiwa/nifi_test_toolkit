import uuid

from app.domain.project.project import Project


class ProjectMother:

    @classmethod
    def create(cls,
               project_name="project_name",
               project_uri="http://localhost:8080",
               authentication=True,
               username="username",
               password="password"):
        return Project(
            project_id=str(uuid.uuid4()),
            project_name=project_name,
            project_uri=project_uri,
            authentication=authentication,
            username=username,
            password=password
        )
