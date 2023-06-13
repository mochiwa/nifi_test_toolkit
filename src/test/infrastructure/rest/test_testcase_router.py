from mockito import mock, verify, when, ANY
from starlette.testclient import TestClient

from src.app.application.request.create_testcase_request import CreateTestCaseRequest
from src.app.application.response.testcase_response import TestCaseResponse
from src.app.infrastructure.rest import testcase_router
from src.main import create_app, create_di
from src.test.helper.arg_captor import ArgCaptor
from src.test.infrastructure.rest.payload import create_testcase_payload

di = create_di()
app = create_app(di)
client = TestClient(app)
createTestCaseService = mock()


def test_post_testcase_should_create_testcase_and_return_id_in_location_header():
    payload = create_testcase_payload()
    response = TestCaseResponse('1', '0a69092a-3b48-4e04-83fa-3ea92190c008', '', {}, {}, {})

    with app.di.create_testcase_service.override(createTestCaseService):
        when(createTestCaseService).execute(ANY()).thenReturn(response)
        output = client.post(testcase_router.prefix, json=payload)

    assert output.status_code == 201
    assert output.headers['Location'] == response.testcase_id

    requestCaptor = ArgCaptor()
    verify(createTestCaseService).execute(requestCaptor)
    assert isinstance(requestCaptor.getValue(), CreateTestCaseRequest)
