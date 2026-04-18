from .context import Context
from collections.abc import Callable
from typing import Any

class ClosureError(ArithmeticError):
    'this occurs when the result of a function is outside of its codomain'
    def __init__(self, function_or_str: Callable | str, inputs: tuple[Any] = None, output: Any = None):
        'the arguments to ClosureError are entirely optional'
        
        if inputs is None and output is None:
            super().__init__(function_or_str)
            return
        
        function: str = function_or_str.__name__
        inputs: str = ', '.join(f'{type(input).__name__} {input}' for input in inputs)
        output: str = f'{type(output).__name__} {output}'
        
        super().__init__(f'{function}({inputs}) returned {output}')

    def __init__(self, function_or_str: Callable | str, args: tuple[...] = None, kwargs: dict[str, Any] = None, output: Any = None, context: Context = None):
        'the arguments to ClosureError are entirely optional. these are just here to help you format the error message neater'
        if args is None and kwargs is None and output is None:
            super().__init__(function_or_str)
            return
        
        if args is None or kwargs is None or output is None:
            raise ValueError('developer! lazy developer! give args, kwargs, output for this function')
        
        function: str = function_or_str.__name__
        args: str = ', '.join(f'{type(input).__name__} {input}' for input in inputs)
        kwargs: str = 
        inputs: str = ', '.join(f'{type(input).__name__} {input}' for input in inputs)
        output: str = f'{type(output).__name__} {output}'
            

    # this cheeky hack allows it to show things like:
    # ClosureError: float INTEGER div(float INTEGER 1.0, float INTEGER 2.0) returned float 0.5 which is not INTEGER
    # instead of:
    # dm.exceptions.ClosureError: float INTEGER div(float INTEGER 1.0, float INTEGER 2.0) returned float 0.5 which is not INTEGER
    __module__ = 'builtins'

class RepresentationError(TypeError):
    'this occurs when a representation (like a datatype) of something cannot represent that thing accurately'
    
    # this cheeky hack allows it to show things like:
    # RepresentationError: int REAL div(int REAL 1.0, int REAL 2.0) returned REAL 0.5 which cannot be accurately represented by int
    # instead of:
    # dm.exceptions.RepresentationError: int REAL div(int REAL 1.0, int REAL 2.0) returned REAL 0.5 which cannot be accurately represented by int
    __module__ = 'builtins'
