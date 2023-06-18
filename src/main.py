from fastapi import FastAPI

from app.infrastructure.rest.projects_router import router
from di import DI


def create_di():
    return DI()


def create_app(di: DI):
    app = FastAPI()
    app.di = di
    app.include_router(router)
    return app


if __name__ == '__main__':
    create_app(create_di())
