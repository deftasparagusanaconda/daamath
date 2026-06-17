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

    def __str__(self) -> str:
        INDENT = '    '

        lines = ['domains:']

        for k, v in self.domains.__dict__.items():
            lines.append(f'{INDENT}{k} = {v}')
        
        lines.append(f'codomain = {self.codomain}')
        lines.append(f'mapping = {self.mapping}')

        return '\n'.join(lines)
