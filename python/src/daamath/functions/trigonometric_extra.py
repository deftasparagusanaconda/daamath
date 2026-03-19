import math, cmath

from math import atan2

def sinc(angle):
    try:    return math.sin(angle) / angle
    except: return cmath.sin(angle) / angle
