from src.app.domain.testcase.testcase import TestCase


class Project:
    _project_id: str
    _testcases: [TestCase]

    def __init__(self, project_id: str, testcases: [TestCase] = None):
        if testcases is None:
            testcases = []
        self._project_id = project_id
        self._testcases = testcases

    @property
    def project_id(self) -> str:
        return self._project_id

    @property
    def testcases(self) -> [TestCase]:
        return self._testcases

    def add_testcase(self, testcase: TestCase):
        self._testcases.append(testcase)
