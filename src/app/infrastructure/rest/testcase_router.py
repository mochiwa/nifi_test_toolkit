from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from starlette.responses import Response

from src.app.application.request.create_testcase_request import CreateTestCaseRequest
from src.app.application.service.create_testcase_service import CreateTestCaseService
from src.di import DI

router = APIRouter(
    prefix="/testcase",
)


@router.post("/", status_code=201)
@inject
def create_project(
        payload: dict,
        response: Response,
        service: CreateTestCaseService = Depends(Provide[DI.create_testcase_service])) -> dict:
    request = CreateTestCaseRequest.from_json(payload)
    output = service.execute(request)
    response.headers['Location'] = output.testcase_id
    return output
