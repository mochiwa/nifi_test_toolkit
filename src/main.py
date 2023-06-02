from fastapi import FastAPI

from src.app.infrastructure.rest import testcase_router
from src.app.infrastructure.rest.exception_handler import add_exception_handler
from src.di import DI


def create_app():
    app = FastAPI()
    app.di = DI()
    app.include_router(testcase_router)
    add_exception_handler(app)
    return app


if __name__ == '__main__':
    pass
