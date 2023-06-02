class TestCase:
    _testcase_id: str
    _name: str
    _start: dict
    _end: dict
    _steps: dict

    def __init__(self,
                 testcase_id: str,
                 name: str,
                 start: dict,
                 end: dict,
                 steps: dict):
        self._testcase_id = testcase_id
        self._name = name
        self._start = start
        self._end = end
        self._steps = steps

    @property
    def testcase_id(self):
        return self._testcase_id

    @property
    def name(self):
        return self._name

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def steps(self):
        return self._steps
