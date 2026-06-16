from types import SimpleNamespace

class Namespace(SimpleNamespace):
    def __dir__(self):
        return self.__dict__.keys()
