from enum import Enum
from . import domains
from .functions import rounding

class Context:
    "a collection of variables that define daamath's behaviour"

    def __init__(self, default_argument_constructor = None, **kwargs: dict[str, Any]) -> None:
        if default_argument_constructor is None:
            default_argument_constructor = context
        
        for key, val in vars(default_argument_constructor).items:
            setattr(self, key, val)

        for key, val in kwargs.items():
            setattr(self, key, val)
    
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} at {hex(id(self))}>'

class ErrorBehaviour(Enum):
    NONE = 0    # do nothing
    FLAG = 1    # set flags and return sentinel values
    RAISE = 2   # raise exceptions and halt execution
    FLAG_AND_RAISE = 3  # FLAG, then RAISE

context = Context(
        check_input_domain  = True                         ,
        check_output_domain = True                         ,
        domain              = domains.REAL                 ,
        error_behaviour     = ErrorBehaviour.FLAG_AND_RAISE,
        rounding            = rounding.nearest_even        ,
    )
