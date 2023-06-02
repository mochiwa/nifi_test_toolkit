from dataclasses import dataclass

from src.app.domain.shared.exception.bad_request_exception import BadRequestException
from src.app.domain.shared.exception.error_code import ErrorCode


@dataclass
class CreateTestCaseRequest:
    project_id: str
    name: str
    start: dict
    end: dict
    steps: dict

    def __init__(self, project_id: str, name: str, start: {}, end: {}, steps: {}):
        if project_id is None:
            raise BadRequestException(ErrorCode.BAD_REQUEST, 'project_id is mandatory')

        self.project_id = project_id
        self.name = name
        self.start = start
        self.end = end
        self.steps = steps

    @classmethod
    def from_json(cls, payload: dict):
        return CreateTestCaseRequest(
            project_id=payload['project_id'],
            name=payload['name'],
            start=payload['start'],
            end=payload['end'],
            steps=payload['steps'])
