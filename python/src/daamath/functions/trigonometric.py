import math, cmath
from numbers import Number

# circular geometry

def sin(angle: Number) -> Number:
    """circular sine. angle is in radians, the natural unit of angles in circular geometry
    
    csin(angle) = Im(e ^ (angle * i)) where i² = -1
    """
    try:    return math.sin(angle)
    except: return cmath.sin(angle)

def cos(angle: Number) -> Number:
    """circular cosine. angle is in radians, the natural unit of angles in circular geometry
    csin(angle) = Re(e ^ (angle * i)) where i² = -1
    """
    try:    return math.cos(angle)
    except: return cmath.cos(angle)

def tan(angle: Number) -> Number:
    'circular tangent'
    try:    return math.tan(angle)
    except: return cmath.tan(angle)

def cot(angle: Number) -> Number:
    'circular cotangent'
    try:    return 1 / math.tan(angle)
    except: return 1 / cmath.tan(angle)

def sec(angle: Number) -> Number:
    'circular secant'
    try:    return 1 / math.cos(angle)
    except: return 1 / cmath.cos(angle)

def csc(angle: Number) -> Number:
    'circular cosecant'
    try:    return 1 / math.sin(angle)
    except: return 1 / cmath.sin(angle)

# inverse

def asin(angle: Number) -> Number:
    'inverse circular sine'
    try:    return math.asin(angle)
    except: return cmath.asin(angle)

def acos(angle: Number) -> Number:
    'inverse circular cosine'
    try:    return math.acos(angle)
    except: return cmath.acos(angle)

def atan(angle: Number) -> Number:
    'inverse circular tangent'
    try:    return math.atan(angle)
    except: return cmath.atan(angle)

def acot(angle: Number) -> Number:
    'inverse circular cotangent'
    try:    return math.atan(1 / angle)
    except: return cmath.atan(1 / angle)

def asec(angle: Number) -> Number:
    'inverse circular secant'
    try:    return math.acos(1 / angle)
    except: return cmath.acos(1 / angle)

def acsc(angle: Number) -> Number:
    'inverse circular cosecant'
    try:    return math.asin(1 / angle)
    except: return cmath.asin(1 / angle)

# hyperbolic geometry

def sinh(angle: Number) -> Number:
    'hyperbolic sine'
    try:    return math.sinh(angle)
    except: return cmath.sinh(angle)

def cosh(angle: Number) -> Number:
    'hyperbolic cosine'
    try:    return math.cosh(angle)
    except: return cmath.cosh(angle)

def tanh(angle: Number) -> Number:
    'hyperbolic tangent'
    try:    return math.tanh(angle)
    except: return cmath.tanh(angle)

def coth(angle: Number) -> Number:
    'hyperbolic cotangent'
    try:    return 1 / math.tanh(angle)
    except: return 1 / cmath.tanh(angle)

def sech(angle: Number) -> Number:
    'hyperbolic secant'
    try:    return 1 / math.cosh(angle)
    except: return 1 / cmath.cosh(angle)

def csch(angle: Number) -> Number:
    'hyperbolic cosecant'
    try:    return 1 / math.sinh(angle)
    except: return 1 / cmath.sinh(angle)

# inverse

def asinh(angle: Number) -> Number:
    'inverse hyperbolic sine'
    try:    return math.asinh(angle)
    except: return cmath.asinh(angle)

def acosh(angle: Number) -> Number:
    'inverse hyperbolic cosine'
    try:    return math.acosh(angle)
    except: return cmath.acosh(angle)

def atanh(angle: Number) -> Number:
    'inverse hyperbolic tangent'
    try:    return math.atanh(angle)
    except: return cmath.atanh(angle)

def acoth(angle: Number) -> Number:
    'inverse hyperbolic cotangent'
    try:    return math.atanh(1 / angle)
    except: return cmath.atanh(1 / angle)

def asech(angle: Number) -> Number:
    'inverse hyperbolic secant'
    try:    return math.acosh(1 / angle)
    except: return cmath.acosh(1 / angle)

def acsch(angle: Number) -> Number:
    'inverse hyperbolic cosecant'
    try:    return math.asinh(1 / angle)
    except: return cmath.asinh(1 / angle)

# trivia: we have circular and hyperbolic geometries, much like the geometries of the complex and split-complex numbers. 
# "whats the trig associated with the dual numbers then?"
# well my friend, those would be the galilean trig functions which are trivial:
# sing(x) = 1, cosg(x) = x (i think)
# why is this? because the dual numbers are "degenerate" and so are their trig functions too
