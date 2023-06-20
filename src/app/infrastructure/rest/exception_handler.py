from fastapi import FastAPI
from httpx import Request
from starlette.responses import JSONResponse

from app.domain.shared.exception.bad_request_exception import BadRequestException
from app.domain.shared.exception.domain_exception import DomainException


def validation_exception_handler(request: Request, exception: DomainException):
    if isinstance(exception, BadRequestException):
        return build_response(400, exception)


def build_response(status_code: int, exception: DomainException):
    return JSONResponse(status_code=status_code, content={
        'title': exception.code,
        'details': exception.details
    })


def add_exception_handler(app: FastAPI):
    app.add_exception_handler(DomainException, validation_exception_handler)
