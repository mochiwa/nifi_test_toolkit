from app.domain.shared.exception.domain_exception import DomainException


class BadRequestException(DomainException):

    def __init__(self, details: str, code: str = "BAD_REQUEST"):
        super().__init__(code, details)
