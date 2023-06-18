from mockito.matchers import Matcher


class ArgCaptor(Matcher):
    def __init__(self):
        self._value = None

    def matches(self, arg: any):
        self._value = arg
        return True

    @property
    def value(self):
        return self._value
