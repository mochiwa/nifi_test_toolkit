import pytest
from starlette.testclient import TestClient

from src.app.domain.testcase.project import Project
from src.app.infrastructure.persistence.memory.memory_project_repository import MemoryProjectRepository
from src.main import create_app
from src.test.domain.testcase.project_mother import project_mother_create


class AbstractIntegration:
    project_repository = MemoryProjectRepository()
    app = create_app()
    app.di.project_repository.override(project_repository)
    client = TestClient(app)

    project: Project

    @pytest.fixture(autouse=True)
    def before_each(self):
        self._init_repository()

    def _init_repository(self):
        self.project = project_mother_create()
        self.project_repository.projects = [self.project]
