from src.app.domain.shared.exception.error_code import ErrorCode
from src.app.domain.shared.exception.not_found_exception import NotFoundException


class ProjectNotFoundException(NotFoundException):
    def __init__(self):
        super().__init__(ErrorCode.PROJECT_NOT_FOUND, "the project with given id not found.")
