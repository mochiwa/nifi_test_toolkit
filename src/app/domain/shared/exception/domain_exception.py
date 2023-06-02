from src.app.domain.shared.exception.error_code import ErrorCode


class DomainException(RuntimeError):
    message: str
    code: ErrorCode

    def __init__(self, code: ErrorCode, message: str):
        super().__init__(message)
        self.message = message
        self.code = code
