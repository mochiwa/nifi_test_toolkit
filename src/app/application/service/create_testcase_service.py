import uuid

from src.app.application.request.create_testcase_request import CreateTestCaseRequest
from src.app.application.response.testcase_response import TestCaseResponse
from src.app.domain.shared.exception.project_not_found_exception import ProjectNotFoundException
from src.app.domain.testcase.project_repository import ProjectRepository
from src.app.domain.testcase.testcase import TestCase


class CreateTestCaseService:

    def __init__(self, project_repository: ProjectRepository):
        self.project_repository = project_repository

    def execute(self, request: CreateTestCaseRequest) -> TestCaseResponse:
        project = self._get_project(request.project_id)
        testcase = self._build_testcase(request)
        project.add_testcase(testcase)
        self.project_repository.save(project)
        return TestCaseResponse.from_testcase(testcase, project.project_id)

    def _get_project(self, project_id: str):
        project = self.project_repository.get_project(project_id)
        if project is None:
            raise ProjectNotFoundException()
        return project

    def _build_testcase(self, request: CreateTestCaseRequest):
        return TestCase(
            testcase_id=str(uuid.uuid4()),
            name=request.name,
            start=request.start,
            end=request.end,
            steps=request.steps)
