from pydantic import BaseModel


class ProjectDto(BaseModel):
    name: str
