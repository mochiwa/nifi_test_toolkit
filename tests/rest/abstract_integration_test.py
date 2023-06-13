import pytest
from sqlalchemy import text
from starlette.testclient import TestClient

from src.app.domain.testcase.project import Project
from src.main import create_app, create_di
from src.test.domain.testcase.project_mother import project_mother_create


class AbstractIntegration:
    di = create_di()
    app = create_app(di)
    database = di.db.provided()
    project_repository = di.project_repository.provided()
    client = TestClient(app)

    project: Project

    @pytest.fixture(autouse=True)
    def before_each(self):
        self._init_repository()
        yield
        self._clean_db()

    def _init_repository(self):
        self.project = project_mother_create()
        self.project_repository.save(self.project)

    def _clean_db(self):
        with self.database.session() as session:
            session.execute(text("DELETE FROM testcase"))
            session.execute(text("DELETE FROM project"))
            session.commit()
