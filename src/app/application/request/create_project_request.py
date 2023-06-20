from dataclasses import dataclass

from app.domain.shared.exception.bad_request_exception import BadRequestException


@dataclass
class CreateProjectRequest:
    project_name: str
    project_uri: str
    authentication: bool
    username: str | None
    password: str | None

    @classmethod
    def create(cls, data: dict):
        project_name = data.get('project_name') or ''
        if project_name.strip() == "":
            raise BadRequestException("the 'name' field is mandatory.")

        return CreateProjectRequest(
            project_name=project_name,
            project_uri=data.get('project_uri') or '',
            authentication=data.get('authentication') or False,
            username=data.get('username') or None,
            password=data.get('password') or None
        )
