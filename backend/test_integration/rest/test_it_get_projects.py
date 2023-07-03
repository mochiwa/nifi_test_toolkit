from abstract_integration_test import AbstractIntegration


class TestCreateProjectIntegrationTest(AbstractIntegration):

    def test_should_return_empty_list_when_no_projects_found(self):
        response = self.client.get('/projects')

        assert response.status_code == 200
        assert response.json() == []
