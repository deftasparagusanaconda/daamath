from typing import Any
from types import FunctionType

class DaaMathException(Exception):
    'superclass for any exception in daamath. daddy of exceptions'
    # this cheeky hack allows it to show things like:
    # ClosureError: float INTEGER div(float INTEGER 1.0, float INTEGER 2.0) returned float 0.5 which is not INTEGER
    # instead of:
    # dm.exceptions.ClosureError: float INTEGER div(float INTEGER 1.0, float INTEGER 2.0) returned float 0.5 which is not INTEGER
    __module__ = 'builtins'

class SignatureViolation(Exception):
    "this occurs when a function's signature (domain, codomain, mapping) is violated"
    __module__ = 'builtins'

class DomainViolation(SignatureViolation):
    "this occurs when a function receives something out of its domains"

    def __init__(self, function_name: str, args: tuple[Any, ...], kwargs: dict[str, Any], offender: Any, offender_domain: Callable):
        args: list[str] = [f'{type(arg).__name__} {arg}' for arg in args]
        kwargs: list[str] = [f'{key}={type(val).__name__} {val!r}' for key, val in kwargs.items()]
        
        inputs: str = ', '.join(args + kwargs)

        super().__init__(f'{function_name}({inputs}) received {type(offender).__name__} {offender!r} ∉ {offender_domain.__name__}')
    __module__ = 'builtins'

class CodomainViolation(SignatureViolation):
    "this occurs when a function tries to return something out of its codomain"
    def __init__(self, function_name: str, args: tuple[Any, ...], kwargs: dict[str, Any], offender: Any, offender_domain: Callable):
        args: list[str] = [f'{type(arg).__name__} {arg}' for arg in args]
        kwargs: list[str] = [f'{key}={type(val).__name__} {val!r}' for key, val in kwargs.items()]
        
        inputs: str = ', '.join(args + kwargs)
        
        super().__init__(f'{function_name}({inputs}) returned {type(offender).__name__} {offender!r} ∉ {offender_domain.__name__}')
    __module__ = 'builtins'
