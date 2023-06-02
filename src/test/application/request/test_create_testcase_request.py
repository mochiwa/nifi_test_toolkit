import pytest

from src.app.application.request.create_testcase_request import CreateTestCaseRequest
from src.app.domain.shared.exception.bad_request_exception import BadRequestException


def test_should_raise_bad_request_when_project_id_is_none():
    with pytest.raises(BadRequestException):
        CreateTestCaseRequest(None, "", {}, {}, {})
