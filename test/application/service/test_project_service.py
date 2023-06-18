import re

from app.application.service.project_service import ProjectService


def test_create_project_should_return_project_with_id():
    regex_uuid = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    service = ProjectService()

    project = service.create({})

    assert re.match(regex_uuid, project.id)
