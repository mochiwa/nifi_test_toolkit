from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.responses import Response

from app.application.request.create_project_request import CreateProjectRequest
from app.application.service.project_service import ProjectService
from di import DI

router = APIRouter(
    prefix="/projects",
)


@router.post("/", status_code=201)
@inject
def create_project(
        payload: dict,
        response: Response,
        service: ProjectService = Depends(Provide[DI.project_service])):
    request = CreateProjectRequest.create(payload)
    project = service.create(request)
    response.headers['Location'] = f"{router.prefix}/{project.project_id}"
