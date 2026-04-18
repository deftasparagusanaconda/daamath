# a domain is a function with special UPPERCASE naming, because it is treated as both an object and also as a function

from typing import Any

# 1st order domains (indicator functions):
def THING(fish: Any) -> bool:
    'the base domain of anything. everything is a thing. even nothing is a thing. the indicator function simply returns `true`'
    return True

def TRUTH(fish: Any) -> bool:
    'idk'
    return True

def BOOLEAN(fish: Any) -> bool:
    'idk'
    return True

def NUMBER(fish: Any) -> bool:
    return isinstance(fish, numbers.Number)
                              
def HYPERCOMPLEX(fish: Any) -> bool:
    'idk'
    return NUMBER(fish)

def OCTONION(fish: Any) -> bool:        
    'fish is HYPERCOMPLEX and fish has non-zero octonion vector part'
    return HYPERCOMPLEX(fish)

def QUATERNION(fish: Any) -> bool:      
    'fish is OCTONION and fish has non-zero quaternion vector part'
    return OCTONION(fish)

def COMPLEX(fish: Any) -> bool:         
    'fish is QUATERNION and fish has non-zero imaginary part'
    return OCTONION(fish) and fish.imag == 0

def IMAGINARY(fish: Any) -> bool:
    'fish is COMPLEX and real part is zero'
    return COMPLEX(fish) and fish.real == 0

def REAL(fish: Any) -> bool:            
    'fish is COMPLEX and imaginary part is zero'
    return COMPLEX(fish) and fish.imag == 0

def RATIONAL(fish: Any) -> bool:        
    'fish is REAL and fish can be represented as p / q where q ≠ 0'
    return REAL(fish) and isinstance()

def INTEGER(fish: Any) -> bool:         
    'fish is RATIONAL and fish is divisible by 1'
    return RATIONAL(fish) and fish % 1 == 0

def IRRATIONAL(fish: Any) -> bool:      
    'fish is REAL and fish is not RATIONAL'
    return REAL(fish) and not RATIONAL(fish)

def PRIME(fish: Any) -> bool:           
    'fish is NATURALSTART_2 and fish has two prime divisors'
    raise NotImplementedError('developer hasnt defined this yet')
    return NATURALSTART

def COMPOSITE(fish: Any) -> bool:       
    'fish is NATURAL_1 and fish has more than two prime divisors'
    raise NotImplementedError('developer hasnt defined this yet')
    return NATURALSTART_1(fish)

# 2nd order domains (domain constructors):

def NATURALFROM(start: int) -> Callable[[Any], bool]:
    'natural numbers starting from N'
    if not INTEGER(start) or start < 0:
        raise ValueError('start must be non-negative integer')
    
    def NATURALFROM(fish: Any) -> bool:
        return INTEGER(fish) and fish >= start
    return NATURALFROM

NATURALFROM_0: Callable[[Any], bool] = NATURAL_START_N(0)
NATURALFROM_1: Callable[[Any], bool] = NATURAL_START_N(1)
NATURALFROM_2: Callable[[Any], bool] = NATURAL_START_N(2)

def INTEGERMODULO(mod: int) -> Callable[[Any], bool]:
    'integers modulo N, like in modular arithmetic'
    if mod == 0:
        return INTEGER
    if not INTEGER(mod, int) or mod < 0:
        raise ValueError(f'sorry, but i want mod to be a non-negative integer. i dont know what integers modulo {mod} would mean')
    def INTEGERMODULO_N(fish: Any) -> bool:
        return INTEGER(fish) and fish // mod == 0
    return INTEGERMODULO

INTEGERMODULO_2: Callable[[Any], bool] = INTEGERMODULO(2)
