import uuid

from src.app.domain.testcase.project import Project


def project_mother_create(project_id: str = str(uuid.uuid4())):
    return Project(project_id)
