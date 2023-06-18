import os

from starlette.testclient import TestClient

from src.main import create_di, create_app


class AbstractIntegration:
    di = create_di()
    di.config.from_ini(os.path.abspath(os.curdir) + "/config.ini")

    app = create_app(di)
    client = TestClient(app)
