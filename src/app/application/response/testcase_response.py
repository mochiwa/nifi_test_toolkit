from dataclasses import dataclass

from src.app.domain.testcase.testcase import TestCase


@dataclass
class TestCaseResponse:
    project_id: str
    testcase_id: str
    name: str
    start: dict
    end: dict
    steps: dict

    @classmethod
    def from_testcase(cls, testcase: TestCase, project_id: str):
        return TestCaseResponse(
            project_id=project_id,
            testcase_id=testcase.testcase_id,
            name=testcase.name,
            start=testcase.start,
            end=testcase.end,
            steps=testcase.steps)
