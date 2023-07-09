from mockito import mock, when, ANY, verify
from starlette.testclient import TestClient

from app.infrastructure.rest import projects_router
from domain.project_mother import ProjectMother
from src.main import create_di, create_app

di = create_di()
app = create_app(di)
client = TestClient(app)
projectService = mock()


def test_post_projects_should_call_project_service():
    response = ProjectMother.create()

    with app.di.project_service.override(projectService):
        when(projectService).create(ANY()).thenReturn(response)
        output = client.post(projects_router.prefix, json={
            "project_name": "name"
        })

    assert output.status_code == 201
    assert output.headers['Location'] == f"/projects/{response.project_id}"
    assert output.json() is None

    verify(projectService).create(ANY())


def test_get_projects_should_call_project_service():
    with app.di.project_service.override(projectService):
        when(projectService).get_all().thenReturn([])
        output = client.get(projects_router.prefix)

    verify(projectService).get_all()
