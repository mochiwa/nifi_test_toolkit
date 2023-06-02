from fastapi import FastAPI
from httpx import Request
from starlette import status
from starlette.responses import JSONResponse

from src.app.domain.shared.exception.bad_request_exception import BadRequestException
from src.app.domain.shared.exception.domain_exception import DomainException
from src.app.domain.shared.exception.not_found_exception import NotFoundException


def runtime_exception_handler(request: Request, exception: RuntimeError):
    if isinstance(exception, BadRequestException):
        return build_response(status.HTTP_400_BAD_REQUEST, exception)
    if isinstance(exception, NotFoundException):
        return build_response(status.HTTP_404_NOT_FOUND, exception)


def build_response(status_code: int, exception: DomainException):
    return JSONResponse(status_code=status_code, content={
        'title': exception.code.name,
        'detail': exception.message
    })


def add_exception_handler(app: FastAPI):
    app.add_exception_handler(DomainException, runtime_exception_handler)
