from src.test.domain.testcase.project_mother import project_mother_create
from src.test.domain.testcase.testcase_mother import testcase_mother_create


def test_add_testcase_should_add_testcase():
    project = project_mother_create()
    testCase = testcase_mother_create()

    project.add_testcase(testCase)

    assert testCase in project.testcases
