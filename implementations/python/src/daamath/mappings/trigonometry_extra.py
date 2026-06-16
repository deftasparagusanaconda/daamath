import math as _math, cmath as _cmath

def sinc(semiarea):
    try:    return _math.sin(semiarea) / semiarea
    except: return _cmath.sin(semiarea) / semiarea

# 2 argument versions
# these ones take a triangle's sides and try to recover the correct quadrant

def asin2(opposite, hypotenuse):
    'asin(opposite / hypotenuse). absorbs  the division, and gives you full τ periodic range from signage of the two arguments'
    return _math.asin(opposite / hypotenuse) + (hypotenuse < 0) * _math.copysign(_math.pi, opposite)

def acos2(adjacent, hypotenuse):
    'acos(adjacent / hypotenuse). absorbs the division, and gives you full τ periodic range from the signage of the two arguments'
    return _math.acos(adjacent / hypotenuse) + (hypotenuse < 0) * _math.copysign(_math.pi, opposite)

def atan2(opposite, adjacent):
    'atan(opposite / adjacent). absorbs the division, and gives you full τ periodic range from the signage of the two arguments'
    # return _math.atan(opposite / adjacent) - (adjacent > 0) * _math.copysign(_math.pi, opposite * adjacent)
    return _math.atan2(opposite, adjacent)

def acot2(adjacent, opposite):
    # return _math.atan(opposite / adjacent) + _math.pi * ((o < 0) + (a * o < 0))
    return _math.atan2(opposite, adjacent)

def asec2(hypotenuse, adjacent):
    try: _math.acos(adjacent / hypotenuse)
    except: _cmath.acos(adjacent / hypotenuse)

def acsc2(hypotenuse, opposite):
    try: _math.asin(opposite / hypotenuse)
    except: _cmath.asin(opposite / hypotenuse)

