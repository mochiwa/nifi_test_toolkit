from mockito.matchers import Matcher


class ArgCaptor(Matcher):
    def matches(self, arg):
        self.value = arg
        return True

    def getValue(self):
        return self.value
