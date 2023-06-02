from src.test.infrastructure.rest.payload import create_testcase_payload
from tests.rest.abstract_integration_test import AbstractIntegration


class TestCreateTestCaseIntegration(AbstractIntegration):

    def test_should_return_payload_of_testcase_created(self):
        response = self.client.post('/testcase', json={
            'project_id': self.project.project_id,
            'name': 'my testcase',
            'start': {
                'componentId': '3c2755da-e15e-4072-a1e0-0046c7588dd0',
                'type': 'start',
                'node': 'primary'
            },
            'end': {
                'componentId': 'd5ab2ffb-ab5d-4048-838e-1296be40d1f8'
            },
            'steps': [
                {
                    'name': 'step 1',
                    'componentId': '3c2755da-e15e-4072-a1e0-0046c7588dd0',
                    'type': 'output'
                },
                {
                    'name': 'step 2',
                    'componentId': 'd5ab2ffb-ab5d-4048-838e-1296be40d1f8',
                    'type': 'output'
                }
            ]
        })

        assert response.status_code == 201

        payload = response.json()

        assert payload['testcase_id'] is not None
        assert payload['project_id'] == self.project.project_id
        assert payload['name'] == "my testcase"
        assert payload['start']['componentId'] == "3c2755da-e15e-4072-a1e0-0046c7588dd0"
        assert payload['start']['type'] == "start"
        assert payload['start']['node'] == "primary"
        assert payload['end']['componentId'] == "d5ab2ffb-ab5d-4048-838e-1296be40d1f8"
        assert payload['steps'] is not None

    def test_should_return_error_when_project_id_is_empty(self):
        payload = create_testcase_payload()
        payload['project_id'] = None
        response = self.client.post('/testcase', json=payload)

        assert response.status_code == 400

        payload = response.json()
        assert "BAD_REQUEST" in payload['title']
        assert "project_id is mandatory" in payload['detail']

    def test_should_return_error_project_not_found_when_project_not_found(self):
        payload = create_testcase_payload()
        response = self.client.post('/testcase', json=payload)

        assert response.status_code == 404

        payload = response.json()
        assert "PROJECT_NOT_FOUND" in payload['title']
        assert "the project with given id not found." in payload['detail']

    def test_should_save_testcase_in_testcase_repository(self):
        payload = create_testcase_payload(self.project.project_id)
        response = self.client.post('/testcase', json=payload)

        assert response.status_code == 201

        payload = response.json()
        project = self.project_repository.get_project(payload['project_id'])
        testcase = project.testcases[0]
        assert testcase is not None
        assert testcase.testcase_id == payload['testcase_id']
        assert testcase.name == payload['name']
        assert testcase.start == payload['start']
        assert testcase.end == payload['end']
        assert testcase.steps == payload['steps']
