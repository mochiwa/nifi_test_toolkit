import uvicorn as uvicorn
from fastapi import FastAPI

from src.app.infrastructure.rest import testcase_router
from src.app.infrastructure.rest.exception_handler import add_exception_handler
from src.di import DI


def create_di():
    return DI()


def create_app(di: DI):
    app = FastAPI()
    app.di = di
    app.include_router(testcase_router)
    add_exception_handler(app)
    return app


if __name__ == '__main__':
    di = create_di()
    app = create_app(di)
    uvicorn.run(app, host="0.0.0.0", port=8010)
