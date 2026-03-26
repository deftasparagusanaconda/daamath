import math, cmath
from numbers import Number, Real
from ..exceptions import DomainError

def h1b_0(a: Number) -> Number:
    'sub(0, a), additive inverse'
    
    b = -a
    
    if type(a) != type(b):
        raise DomainError(ainv, (a, ), b)
    
    return b

def h2b_1(a: Number) -> Number:
    'div(1, a), multiplicative inverse'
    b = 1 / a

    if type(a) != type(b):
        raise DomainError(minv, (a, ), b)

    return b

'''
def abs_sq(a: Number) -> Real:
    if isinstance(x, Complex):
        return x.real * x.real + x.imag * x.imag 
    else:
        return abs(a) ** 2
'''

def h3c__2(a: Number) -> Number:
    'pow(a, 2), inverse of sqrt'
    return a * a

def h3c__3(a: Number) -> Number:
    'pow(a, 3), inverse of cbrt'
    return a * a * a

def h3a__2(c: Number) -> Number:
    'root(2, a). inverse of square'
    try:    return math.sqrt(c)
    except:    return cmath.sqrt(c)

def h3a__3(c: Number) -> Number:
    'root(3, a). inverse of cube'
    try:    return math.cbrt(c)
    except: return c ** (1 / 3)

def h2b_1_h3c__2(a: Number) -> Number:
    'reciprocal square. inverse of rsqrt'
    return a ** -2

def h2b_1_h3c__3(a: Number) -> Number:
    'reciprocal cube. inverse of rcbrt'
    return a ** -2

def h2b_1_h3a__2(c: Number) -> Number:
    'reciprocal square root. inverse of rsquare'
    return c ** -0.5

def h2b_1_h3a__3(c: Number) -> Number:
    'reciprocal cube root. inverse of rcube'
    return a ** -3

def h3c_e(b: Number) -> Number:
    'e ^ b'
    try:    return math.exp(b)
    except: return cmath.exp(b)

def h3c_2(b: Number) -> Number:
    'pow(2, b), inverse of log_2'
    try:    return math.exp2(b)
    except:    return 2 ** b

def h3c_10(b: Number) -> Number:
    'pow(10, b), inverse of log_10'
    return 10 ** b

def h3b__e(c: Number) -> Number:
    'log_e(c)'
    try:    return math.log(c)
    except: return cmath.log(c)

def h3b__2(a: Number) -> Number:
    'log(2, a), inverse of pow_2'
    try:    return math.log2(a)
    except:    return cmath.log(a, 2)

def h3b__10(a: Number) -> Number:
    'log(10, a), inverse of pow_10'
    try:    return math.log10(a)
    except: return cmath.log10(a)

#def pow_m1(a: Number, b: Number) -> Number:
#    return math.expm1(math.log(a) * b)

#def root_1p(a: Number, b: Number) -> Number:
#    return math.exp(math.log1p(a) / b)

def h1b_h3c_e__1(b: Number) -> Number:
    'exp(b) - 1'
    return e ** b - 1

def h3b_h1c_1__e(c: Number) -> Number:
    'ln(1 + c)'
    try:
        try:
            return math.log1p(c)
        except:
            return math.log(1 + c)
    except:    
        return cmath.log(1 + c)

try:
    from math import fma as h1c_h2c
except ImportError:
    def h1c_h2c(a: float, b: float, c: float) -> float:
        'a * b + c, fused multiply add'
        return a * b + c
