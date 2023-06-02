from src.app.domain.shared.exception.domain_exception import DomainException
from src.app.domain.shared.exception.error_code import ErrorCode


class BadRequestException(DomainException):

    def __init__(self, code: ErrorCode, message: str, ):
        super().__init__(code, message)
