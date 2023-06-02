from src.app.domain.testcase.project import Project
from src.app.domain.testcase.project_repository import ProjectRepository
from src.app.domain.testcase.testcase import TestCase


class MemoryProjectRepository(ProjectRepository):
    projects: [Project] = []
    testcases: [TestCase] = []

    def get_project(self, project_id: str):
        return next(filter(lambda x: x.project_id == project_id, self.projects), None)

    def save(self, project: Project):
        if self.get_project(project.project_id) is None:
            self.projects.append(project)
