import os
import shutil

import pytest
from starlette.testclient import TestClient

from app.infrastructure.persistence.json_project_repository import ROOT_DIR_NAME
from src.main import create_di, create_app


class AbstractIntegration:
    di = create_di()
    di.config.from_ini(os.path.abspath(os.curdir) + "/config.ini")
    app = create_app(di)
    client = TestClient(app)

    project_repository = di.project_repository.provided()

    @pytest.fixture(autouse=True)
    def setup(self):
        yield
        shutil.rmtree(f"./{ROOT_DIR_NAME}")
