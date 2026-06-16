from types import SimpleNamespace

class Namespace(SimpleNamespace):
    'turn a dict into a namespace with tab autocomplete. just a types.SimpleNamespace with __dir__ = __dict__.keys'
    def __dir__(self):
        return self.__dict__.keys()
