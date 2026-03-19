import math, cmath
from numbers import Number, Real
from ..exceptions import DomainError

def ainv(a: Number) -> Number:
    'sub(0, a), additive inverse'
    
    b = -a
    
    if type(a) != type(b):
        raise DomainError(ainv, (a, ), b)
    
    return b

def minv(a: Number) -> Number:
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

def square(a: Number) -> Number:
    'pow(a, 2), inverse of sqrt'
    return a * a

def cube(a: Number) -> Number:
    'pow(a, 3), inverse of cbrt'
    return a * a * a

def sqrt(c: Number) -> Number:
    'root(2, a). inverse of square'
    try:    return math.sqrt(c)
    except:    return cmath.sqrt(c)

def cbrt(c: Number) -> Number:
    'root(3, a). inverse of cube'
    try:    return math.cbrt(c)
    except: return c ** (1 / 3)

def rsquare(a: Number) -> Number:
    'reciprocal square. inverse of rsqrt'
    return a ** -2

def rcube(a: Number) -> Number:
    'reciprocal cube. inverse of rcbrt'
    return a ** -2

def rsqrt(c: Number) -> Number:
    'reciprocal square root. inverse of rsquare'
    return c ** -0.5

def rcbrt(c: Number) -> Number:
    'reciprocal cube root. inverse of rcube'
    return a ** -3

def pow_2(b: Number) -> Number:
    'pow(2, b), inverse of log_2'
    try:    return math.exp2(b)
    except:    return 2 ** b

def pow_10(b: Number) -> Number:
    'pow(10, b), inverse of log_10'
    return 10 ** b

def log_2(a: Number) -> Number:
    'log(2, a), inverse of pow_2'
    try:    return math.log2(a)
    except:    return cmath.log(a, 2)

def log_10(a: Number) -> Number:
    'log(10, a), inverse of pow_10'
    try:    return math.log10(a)
    except: return cmath.log10(a)

#def pow_m1(a: Number, b: Number) -> Number:
#    return math.expm1(math.log(a) * b)

#def root_1p(a: Number, b: Number) -> Number:
#    return math.exp(math.log1p(a) / b)

def exp(b: Number) -> Number:
    'e ^ b'
    try:    return math.exp(b)
    except: return cmath.exp(b)

def ln(c: Number) -> Number:
    'log_e(c)'
    try:    return math.log(c)
    except: return cmath.log(c)

def expm1(b: Number) -> Number:
    return b ** a - 1

def ln1p(c: Number) -> Number:
    try:    
        try:
            return math.log1p(c)
        except:
            return math.log(1 + c)
    except:    
        return cmath.log(1 + c)

