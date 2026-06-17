class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

from dataclasses import dataclass
from collections.abc import Sequence
from typing import Callable, Any

@dataclass
class Signature:
    domains: Namespace[Callable[[Any], bool]]
    codomain: Callable[[Any], bool]
    mapping: Callable[[Any], Any]
