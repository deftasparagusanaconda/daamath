from collections.abc import Callable
from typing import Any

class DomainError(ArithmeticError):
    def __init__(self, function: Callable, inputs: tuple[Any], output: Any):

        function: str = function.__name__
        inputs: str = ', '.join(f'{type(input).__name__} {input}' for input in inputs)
        output: str = f'{type(output).__name__} {output}'
        
        super().__init__(f'{function}({inputs}) returned {output}')

    # this cheeky hack allows it to show things like:
    # DomainError: inc(bool True) returned int 2
    # instead of :
    # daamath.exceptions.DomainError: inc(bool True) returned int 2
    __module__ = 'builtins'
