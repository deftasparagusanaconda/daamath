# this file is meant purely to be imported. the __all__ dunder is the centerpiece here

import sys, yaml
from collections.abc import Mapping
from importlib.resources import files

class Namespace:
    're-present a dict as a namespace'
    def __init__(self, mapping: Mapping):
        self.__dict__.update((k, Namespace(v) if isinstance(v, dict) else v) for k, v in mapping.items())

this = sys.modules[__name__]
__all__ = []

for path in (files(__package__) / 'strings').iterdir():
    if path.suffix != '.yaml':
        continue

    with path.open("r") as file:
        name = path.stem
        setattr(this, name, Namespace(yaml.safe_load(file)))
        __all__.append(name)
