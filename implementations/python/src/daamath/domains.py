# a domain is a function with special UPPERCASE naming, because it is treated as both an object and also as a function

from collections.abc import Iterable 
from typing import Any, Callable, Literal
import numbers, builtins, cmath

# abstract concepts ------------------------------------------------------------

def anything(fish: Any) -> Literal[True]:
    'the universal set. the set of all things. every thing is in it. returns True. useful when a function wants to receive/return any thing'
    return True

def nothing(fish: Any) -> Literal[False]:
    'the null set. the set of no things. not any thing is in it. returns False. useful when a function wants to receive/return no thing'
    return False

# number sets ------------------------------------------------------------------

# NONE of these indicators are allowed to check by datatype
# only purely by mathematical meaning
#
# {0} ⊂

def zero(fish: Any) -> bool:
    'fish == 0. useful for compositions like ncon(zero(fish), natural(fish)) which represents naturals excluding one'
    return fish == 0

def positive(fish: Any) -> bool:
    'fish > 0. zero excluded'
    return fish > 0

def negative(fish: Any) -> bool:
    'fish < 0. zero excluded'
    return fish < 0

def one(fish: Any) -> bool:
    'fish == 1'
    return fish == 1

def natural(fish: Any) -> bool:
    'fish is a non-negative integer'
    return integer(fish) and fish >= 0

def integer(fish: Any) -> bool: 
    'fish is rational and fish is divisible by 1'
    return rational(fish) and fish % 1 == 0

def complex(fish: Any) -> bool: 
    'fish.imag != 0'
    return fish.imag != 0

def IMAGINARY(fish: Any) -> bool: 
    'fish is COMPLEX and real part is zero'
    return COMPLEX(fish) and fish.real == 0

def EXTENDED_REAL(fish: Any) -> bool: 
    '−∞ ≤ fish ≤ +∞'
    return cmath.isfinite(fish) or cmath.isinf(fish)
    
def real(fish: Any) -> bool: 
    'fish is complex and imaginary part is zero'
    return complex(fish) and fish.imag == 0

def finite(fish: Any) -> bool:
    return cmath.isfinite(fish)

def RATIONAL(fish: Any) -> bool:
    'fish is real and fish can be represented as p / q where q ≠ 0'
    return real(fish) and ...

def IRRATIONAL(fish: Any) -> bool:      
    'fish is REAL and fish is not RATIONAL'
    return REAL(fish) and not RATIONAL(fish)

# non-number sets --------------------------------------------------------------

def boolean(fish: Any) -> bool:
    'fish is False or fish is True'
    return fish is False or fish is True

# datatypes --------------------------------------------------------------------

def f64(fish: Any) -> bool:
    'a datatype representing floating point numbers as an IEEE-754 binary64'
    return float(fish)

float = f64

def int(fish: Any) -> bool:
    "a datatype representing the integers as a 2's complement signed integer"
    return isinstance(fish, builtins.int)

def bool(fish: Any) -> bool:
    'a datatype with two possible values: false & true'
    return isinstance(fish, builtins.bool)

def c64(fish: Any) -> bool:
    'a datatype representing the complex numbers in rectangular coordinates as a (f64, f64) pair'
    return isinstance(fish, builtins.complex)

def str(fish: Any) -> bool:
    'a datatype representing a sequence of characters'
    return isinstance(fish, builtins.str)

def function(fish: Any) -> bool:
    'a function that can be called. returns callable(fish)'
    return callable(fish)

def iterable(fish: Any) -> bool:
    'isinstance(fish, collections.abc.Iterable)'
    return isinstance(fish, Iterable)

# set constructors (indicator function factories) ------------------------------

def NATURALFROM(start: int) -> Callable[[Any], bool]:
    'natural numbers starting from N'
    if not INTEGER(start) or start < 0:
        raise ValueError('start must be non-negative integer')
    
    def NATURALFROM(fish: Any) -> bool:
        return INTEGER(fish) and fish >= start
    return NATURALFROM

#NATURALFROM_0: Callable[[Any], bool] = NATURALFROM(0)
#NATURALFROM_1: Callable[[Any], bool] = NATURALFROM(1)
#NATURALFROM_2: Callable[[Any], bool] = NATURALFROM(2)

def INTEGERMODULO(mod: int) -> Callable[[Any], bool]:
    'integers modulo N, like in modular arithmetic'
    if mod == 0:
        return INTEGER
    if not INTEGER(mod) or mod < 0:
        raise ValueError(f'sorry, but i want mod to be a non-negative integer. i dont know what integers modulo {mod} would mean')
    def INTEGERMODULO_N(fish: Any) -> bool:
        return INTEGER(fish) and fish // mod == 0
    raise Exception

#INTEGERMODULO_2: Callable[[Any], bool] = INTEGERMODULO(2)

# i need something that gives an orderding to the domains
# first, daa, know that an ordering on a domain is a subset of the cartesian product of tthat domain and itself. so fundamentally it has the domain as a dependency. in the namespace, it should occupy a resolution in that domain's namespace. if mydomain.is_countable is true, it should have at least 1 mydomain.ordering() under it. mydomain.ordering is an indicator function of the order, represented as tuples.
#

# idfk -------------------------------------------------------------------------

def FUNCTION(fish: Any) -> bool:
    return callable(fish)

def ITERABLE(fish: Any) -> bool:
    return isinstance(fish, Iterable)

def FLOAT(fish: Any) -> bool:
    return isinstance(fish, float)
