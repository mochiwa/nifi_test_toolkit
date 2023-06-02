import uuid

from src.app.domain.testcase.testcase import TestCase


def testcase_mother_create(testcase_id: str = str(uuid.uuid4())):
    return TestCase(
        testcase_id=testcase_id,
        name="a testcase",
        start={},
        end={},
        steps={})
