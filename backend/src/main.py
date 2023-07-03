import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.infrastructure.rest.exception_handler import add_exception_handler
from app.infrastructure.rest.projects_router import router
from di import DI


def create_di():
    return DI()


def create_app(di: DI):
    app = FastAPI()
    app.di = di
    app.include_router(router)
    add_exception_handler(app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["Location"]
    )
    return app


if __name__ == '__main__':
    app = create_app(create_di())
    uvicorn.run(app)
