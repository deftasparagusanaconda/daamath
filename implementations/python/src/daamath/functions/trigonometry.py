import math, cmath
from numbers import Number

# circular geometry

def sin(semiarea: Number) -> Number:
    """circular sine. semiarea is in radians
    
    csin(semiarea) = Im(e ^ (semiarea * i)) where i² = -1
    """
    try:    return math.sin(semiarea)
    except: return cmath.sin(semiarea)

def cos(semiarea: Number) -> Number:
    """circular cosine. semiarea is in radians
    csin(semiarea) = Re(e ^ (semiarea * i)) where i² = -1
    """
    try:    return math.cos(semiarea)
    except: return cmath.cos(semiarea)

def tan(semiarea: Number) -> Number:
    'circular tangent'
    try:    return math.tan(semiarea)
    except: return cmath.tan(semiarea)

def cot(semiarea: Number) -> Number:
    'circular cotangent'
    try:    return 1 / math.tan(semiarea)
    except: return 1 / cmath.tan(semiarea)

def sec(semiarea: Number) -> Number:
    'circular secant'
    try:    return 1 / math.cos(semiarea)
    except: return 1 / cmath.cos(semiarea)

def csc(semiarea: Number) -> Number:
    'circular cosecant'
    try:    return 1 / math.sin(semiarea)
    except: return 1 / cmath.sin(semiarea)

# inverse

def asin(semiarea: Number) -> Number:
    'inverse circular sine'
    try:    return math.asin(semiarea)
    except: return cmath.asin(semiarea)

def acos(semiarea: Number) -> Number:
    'inverse circular cosine'
    try:    return math.acos(semiarea)
    except: return cmath.acos(semiarea)

def atan(semiarea: Number) -> Number:
    'inverse circular tangent'
    try:    return math.atan(semiarea)
    except: return cmath.atan(semiarea)

def acot(semiarea: Number) -> Number:
    'inverse circular cotangent'
    try:    return math.atan(1 / semiarea)
    except: return cmath.atan(1 / semiarea)

def asec(semiarea: Number) -> Number:
    'inverse circular secant'
    try:    return math.acos(1 / semiarea)
    except: return cmath.acos(1 / semiarea)

def acsc(semiarea: Number) -> Number:
    'inverse circular cosecant'
    try:    return math.asin(1 / semiarea)
    except: return cmath.asin(1 / semiarea)

# hyperbolic geometry

def sinh(semiarea: Number) -> Number:
    'hyperbolic sine'
    try:    return math.sinh(semiarea)
    except: return cmath.sinh(semiarea)

def cosh(semiarea: Number) -> Number:
    'hyperbolic cosine'
    try:    return math.cosh(semiarea)
    except: return cmath.cosh(semiarea)

def tanh(semiarea: Number) -> Number:
    'hyperbolic tangent'
    try:    return math.tanh(semiarea)
    except: return cmath.tanh(semiarea)

def coth(semiarea: Number) -> Number:
    'hyperbolic cotangent'
    try:    return 1 / math.tanh(semiarea)
    except: return 1 / cmath.tanh(semiarea)

def sech(semiarea: Number) -> Number:
    'hyperbolic secant'
    try:    return 1 / math.cosh(semiarea)
    except: return 1 / cmath.cosh(semiarea)

def csch(semiarea: Number) -> Number:
    'hyperbolic cosecant'
    try:    return 1 / math.sinh(semiarea)
    except: return 1 / cmath.sinh(semiarea)

# inverse

def asinh(semiarea: Number) -> Number:
    'inverse hyperbolic sine'
    try:    return math.asinh(semiarea)
    except: return cmath.asinh(semiarea)

def acosh(semiarea: Number) -> Number:
    'inverse hyperbolic cosine'
    try:    return math.acosh(semiarea)
    except: return cmath.acosh(semiarea)

def atanh(semiarea: Number) -> Number:
    'inverse hyperbolic tangent'
    try:    return math.atanh(semiarea)
    except: return cmath.atanh(semiarea)

def acoth(semiarea: Number) -> Number:
    'inverse hyperbolic cotangent'
    try:    return math.atanh(1 / semiarea)
    except: return cmath.atanh(1 / semiarea)

def asech(semiarea: Number) -> Number:
    'inverse hyperbolic secant'
    try:    return math.acosh(1 / semiarea)
    except: return cmath.acosh(1 / semiarea)

def acsch(semiarea: Number) -> Number:
    'inverse hyperbolic cosecant'
    try:    return math.asinh(1 / semiarea)
    except: return cmath.asinh(1 / semiarea)

# trivia: we have circular and hyperbolic geometries, much like the geometries of the complex and split-complex numbers. 
# "whats the trig associated with the dual numbers then?"
# well my friend, those would be the galilean trig functions which are trivial:
# sing(x) = 1, cosg(x) = x (i think)
# why is this? because the dual numbers are "degenerate" and so are their trig functions too
