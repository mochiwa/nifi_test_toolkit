import pytest
from mockito import when, ANY, verify, mockito, unstub
from mockito.mocking import mock

from src.app.application.request.create_testcase_request import CreateTestCaseRequest
from src.app.application.service.create_testcase_service import CreateTestCaseService
from src.app.domain.shared.exception.project_not_found_exception import ProjectNotFoundException
from src.test.domain.testcase.project_mother import project_mother_create
from src.test.helper.arg_captor import ArgCaptor
from src.test.infrastructure.rest.payload import create_testcase_payload


project_repository = mock()
service = CreateTestCaseService(project_repository=project_repository)


@pytest.fixture(autouse=True)
def setup():
    yield
    mockito.verifyNoMoreInteractions(project_repository)
    unstub()


def test_should_return_the_testcase_created():
    project = project_mother_create()
    projectCaptor = ArgCaptor()
    request = CreateTestCaseRequest.from_json(create_testcase_payload())

    when(project_repository).get_project(request.project_id).thenReturn(project)
    when(project_repository).save(ANY).thenAnswer(lambda x: x)

    response = service.execute(request)

    assert response.testcase_id is not None
    assert response.name == request.name
    assert response.start == request.start
    assert response.end == request.end
    assert response.steps == request.steps

    verify(project_repository).get_project(request.project_id)
    verify(project_repository).save(projectCaptor)

    project_save = projectCaptor.getValue()
    assert project_save is not None
    assert project_save.testcases[0].testcase_id == response.testcase_id


def test_should_raise_project_not_found_when_project_repository_not_found_project():
    request = CreateTestCaseRequest.from_json(create_testcase_payload())

    when(project_repository).get_project(request.project_id).thenReturn(None)

    with pytest.raises(ProjectNotFoundException):
        service.execute(request)

    verify(project_repository).get_project(request.project_id)
    verify(project_repository, times=0).save(ANY)


def test_should_add_testcase_to_project_repository():
    ff = project_repository
    project = project_mother_create()
    projectCaptor = ArgCaptor()
    request = CreateTestCaseRequest.from_json(create_testcase_payload())

    when(project_repository).get_project(request.project_id).thenReturn(project)
    when(project_repository).save(ANY).thenAnswer(lambda x: x)

    response = service.execute(request)

    verify(project_repository).get_project(request.project_id)
    verify(project_repository).save(projectCaptor)

    project_saved = projectCaptor.getValue()
    assert project_saved is not None
    assert project_saved.testcases[0].testcase_id == response.testcase_id
