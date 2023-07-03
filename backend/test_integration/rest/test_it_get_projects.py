from abstract_integration_test import AbstractIntegration
from domain.project_mother import ProjectMother


class TestCreateProjectIntegrationTest(AbstractIntegration):

    def test_should_return_empty_list_when_no_projects_found(self):
        response = self.client.get('/projects')

        assert response.status_code == 200
        assert response.json() == []

    def test_should_return_all_project_saved_in_repository(self):
        project = ProjectMother.create()
        self.project_repository.save(project)

        response = self.client.get("/projects")

        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]['project_id'] == project.project_id
