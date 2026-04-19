from .context import Context
from collections.abc import Callable
from typing import Any

class Error(Exception):
    'the base class of any exception in daamath'

class DomainError(Error, ArithmeticError):
    'this occurs when something related to the domain goes wrong'

class DataTypeError(Error, TypeError):
    'this occurs when something related to the datatype goes wrong'

class OutOfDomainError(DomainError):
    'this occurs when something is unexpectedly not in a domain'

    def __init__(self, function_or_str: Callable | str, args: tuple[...] = None, kwargs: dict[str, Any] = None, output: Any = None, context: Context = None):
        'the arguments here are entirely optional. these are just here to help you format the error message neater'
        if args is None and kwargs is None and output is None:
            super().__init__(function_or_str)
            return
        
        if args is None or kwargs is None or output is None:
            raise ValueError('developer! lazy developer! give args, kwargs, output for this function')

        raise NotImplementedError
        
        args: str = ', '.join(f'{type(input).__name__} {input}' for arg in args)
        kwargs: str = ', '.join(f'{key}={val!r}' for key, val in kwargs)
        
        function: str = function_or_str.__name__
        inputs: list[Any] = [f'{type(input).__name__} {input}' for arg in args] + []
        input_types: list[Any] = [f'{type(input).__name__} {input}' for arg in args] + []
        input_domains: list[Any] = []
        output_type: str = type(output).__name__
        output_domain: str = str(getattr(context.functions, function.__name__))

        super().__init__(f'{function}{output_type} {output} which is not {output_domain}')
        
    # this cheeky hack allows it to show things like:
    # ClosureError: float INTEGER div(float INTEGER 1.0, float INTEGER 2.0) returned float 0.5 which is not INTEGER
    # instead of:
    # dm.exceptions.ClosureError: float INTEGER div(float INTEGER 1.0, float INTEGER 2.0) returned float 0.5 which is not INTEGER
    __module__ = 'builtins'

class FidelityError(DataTypeError):
    'this occurs when a datatype cannot represent something accurately'
    
    # this cheeky hack allows it to show things like:
    # RepresentationError: int REAL div(int REAL 1.0, int REAL 2.0) returned REAL 0.5 which cannot be accurately represented by int
    # instead of:
    # dm.exceptions.RepresentationError: int REAL div(int REAL 1.0, int REAL 2.0) returned REAL 0.5 which cannot be accurately represented by int
    __module__ = 'builtins'
