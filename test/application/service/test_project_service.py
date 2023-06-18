import re

from mockito import mock, when, ANY, verify

from app.application.service.project_service import ProjectService
from helper.arg_captor import ArgCaptor


def test_create_project_should_return_project_with_id():
    regex_uuid = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
    project_repository = mock()
    service = ProjectService(project_repository)

    when(project_repository).save(ANY).thenAnswer(lambda x: x)
    project = service.create({})

    assert re.match(regex_uuid, project.project_id)

    verify(project_repository).save(ANY)


def test_create_project_should_insert_new_project_in_repository():
    project_to_save_captor = ArgCaptor()
    project_repository = mock()
    service = ProjectService(project_repository=project_repository)
    when(project_repository).save(ANY).thenAnswer(lambda x: x)

    project = service.create({})

    verify(project_repository).save(project_to_save_captor)
    project_to_save = project_to_save_captor.value

    assert project_to_save.project_id is not None
    assert project_to_save.project_id == project.project_id
