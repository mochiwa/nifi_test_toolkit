import uuid

from abstract_integration_test import AbstractIntegration
from domain.project_mother import ProjectMother


class TestDeleteProjectIntegrationTest(AbstractIntegration):

    def test_should_return_empty_body_with_201_when_project_deleted(self):
        project = ProjectMother.create()
        self.project_repository.save(project)

        response = self.client.delete(f'/projects/{project.project_id}')

        assert response.status_code == 201
        assert response.json() is None

    def test_should_return_empty_body_with_201_when_project_that_not_exist(self):
        response = self.client.delete(f'/projects/{uuid.uuid4()}')

        assert response.status_code == 201
        assert response.json() is None
