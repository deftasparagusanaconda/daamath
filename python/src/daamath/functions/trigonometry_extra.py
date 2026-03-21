import math, cmath

def csoh2(opposite, hypotenuse):
    raise NotImplementedError

def csah2(adjacent, hypotenuse):
    raise NotImplementedError

from math import atan2 as csoa2

def csao2(adjacent, opposite):
    raise NotImplementedError

def csha2(hypotenuse, adjacent):
    raise NotImplementedError

def csho2(hypotenuse, opposite):
    raise NotImplementedError

def h2b_croh_S_S(semiarea):
    try:    return math.sin(semiarea) / semiarea
    except: return cmath.sin(semiarea) / semiarea
