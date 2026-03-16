# we need to generalize this to support up to tensors, not just vectors

from numbers import Number, Real
from collections.abc import Sequence
import math, functools, builtins

def norm(value: Number | Sequence[Number], *, power: Real) -> Real:
    'Lp frobenius norm, with power = 2 by default. supports real and complex values, and generalizes abs()'

    # yes i know it calculates 1 / power an unnecessary amount of times. i dont care.
    
    if isinstance(value, Number):
        return builtins.abs(value) if power != 0 else bool(value)
    
    assert isinstance(value, Sequence)
    
    if len(value) == 0:
        return 0
    
    # in case a value is [0, 0, 0, …]
    if all(element == 0 for element in value):
        return 0
    
    match power:
        case 0: 
            return sum(norm(element, power = power) for element in value)
        
        case 1: 
            return math.fsum(norm(element, power = power) for element in value)
        
        case 2: 
            norms = tuple(norm(element, power = power) for element in value)
            scale = max(norms)
            return scale * math.sqrt(math.fsum((norm / scale) ** 2 for norm in norms))
        
        case math.inf:
            return max(norm(element, power = power) for element in value)
        
        case _: 
            norms = tuple(norm(element, power = power) for element in value)
            scale = max(norms)
            return scale * math.fsum((norm / scale) ** power for norm in norms) ** (1 / power)

    # NOTE: 'why not use math.hypot in the power == 2 case?'
    # because:
    # 1) math.hypot will take only floats
    # 2) math.hypot requires elements to be passed flatly. we have to unpack our value to use math.hypot, which is slower than the actual function call itself, probably. 
    # in fact, i would like the numeric accuracy of math.hypot, but this is the tradeoff ive made for now

def normalize(value: Number | Sequence[Number], power: Real) -> Number | Sequence[Number]:
    magnitude = norm(value, power = power)

    if magnitude == 0:
        return 0

    return value / magnitude

def clamp(value: Number | Sequence[Number], power: Real) -> Number | Sequence[Number]:
    magnitude = norm(value, power = power)

    if magnitude == 0:
        print('da hek')
        return 0

    return value / magnitude if magnitude > 1 else value

# euclidean norm
abs = functools.partial(norm, power = 2)
sgn = functools.partial(normalize, power = 2)
#clamp_2 = functools.partial(clamp, power = 2)
