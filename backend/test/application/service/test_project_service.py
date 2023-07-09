import re

import mockito
import pytest
from mockito import mock, when, ANY, verify

from app.application.service.project_service import ProjectService
from application.request.create_project_request_mother import CreateProjectRequestMother
from domain.project_mother import ProjectMother
from helper.arg_captor import ArgCaptor
from helper.const import REGEX_UUID

request = CreateProjectRequestMother.create()
project_repository = mock()
service = ProjectService(project_repository)


@pytest.fixture(autouse=True)
def setup():
    yield
    mockito.unstub()


def test_create_project_should_return_project_with_id():
    when(project_repository).save(ANY).thenAnswer(lambda x: x)
    project = service.create(request)

    assert re.match(REGEX_UUID, project.project_id)

    verify(project_repository).save(ANY)


def test_create_project_should_insert_new_project_in_repository():
    project_to_save_captor = ArgCaptor()

    when(project_repository).save(ANY).thenAnswer(lambda x: x)

    project = service.create(request)

    verify(project_repository).save(project_to_save_captor)
    project_saved = project_to_save_captor.value

    assert project_saved.project_id is not None
    assert project_saved.project_id == project.project_id


def test_get_all_should_return_all_projects_from_repository():
    project = ProjectMother.create()

    when(project_repository).get_all().thenReturn([project])

    output = service.get_all()

    assert len(output) == 1
    assert output[0].project_id == project.project_id
