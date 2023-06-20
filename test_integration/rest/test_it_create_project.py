import re

from abstract_integration_test import AbstractIntegration
from application.request.create_project_request_mother import CreateProjectRequestMother
from helper.const import REGEX_UUID


class TestCreateProjectIntegrationTest(AbstractIntegration):

    def test_should_return_code_201_with_location_header(self):
        request = CreateProjectRequestMother.create()
        response = self.client.post('/projects', json=request.__dict__)

        assert response.status_code == 201
        assert re.match(f"/projects/{REGEX_UUID}", response.headers.get('Location'))

    def test_should_save_new_project_in_repository(self):
        request = CreateProjectRequestMother.create()
        response = self.client.post('/projects', json=request.__dict__)
        id_created = response.headers.get('Location').split("/projects/")[-1]
        saved = self.project_repository.get(id_created)

        assert saved is not None
        assert saved.project_name == request.project_name
        assert saved.project_uri == request.project_uri
        assert saved.authentication is request.authentication
        assert saved.username == request.username
        assert saved.password == request.password

    def test_should_return_bad_request_when_payload_not_contains_name(self):
        response = self.client.post('/projects', json={})
        assert response.json()['details'] == "the 'name' field is mandatory."
