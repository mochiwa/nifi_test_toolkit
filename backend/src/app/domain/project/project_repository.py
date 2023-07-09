from app.domain.project.project import Project


class ProjectRepository:
    def save(self, project: Project) -> Project:
        raise NotImplemented()

    def get(self, project_id: str) -> Project:
        raise NotImplemented()

    def get_all(self) -> [Project]:
        raise NotImplemented()

    def delete_project(self, project_id: str):
        raise NotImplemented()
