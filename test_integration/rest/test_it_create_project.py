import re

from abstract_integration_test import AbstractIntegration


class TestCreateProjectIntegrationTest(AbstractIntegration):

    def test_should_return_code_201_with_location_header(self):
        response = self.client.post('/projects', json={})
        regex_uuid = "[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"

        assert response.status_code == 201
        assert re.match(f"/projects/{regex_uuid}",  response.headers.get('Location'))

    def test_should_save_new_project_in_repository(self):
        response = self.client.post('/projects', json={})
        id_created = response.headers.get('Location').split("/projects/")[-1]
        saved = self.project_repository.get(id_created)

        assert saved is not None