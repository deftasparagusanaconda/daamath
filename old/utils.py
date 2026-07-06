from types import SimpleNamespace
from dataclasses import dataclass
from typing import Callable, Any

@dataclass
class Signature:
    domains: SimpleNamespace[Callable[[Any], bool]]
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
