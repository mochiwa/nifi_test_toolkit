class DomainException(RuntimeError):
    _code: str
    _details: str

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self._details = message
        self._code = code

    @property
    def details(self):
        return self._details

    @property
    def code(self):
        return self._code
