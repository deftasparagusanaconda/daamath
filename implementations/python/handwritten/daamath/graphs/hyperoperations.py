import math, cmath

def succ_complex(a):
    'a + 1'
    return a + 1

def pred_complex(b):
    'b - 1'
    return b - 1

from operator import add as add_complex, sub

def bus(c, a):
    '-a + c'
    return -a + c

from operator import mul, truediv as div

def vid(c, a):
    '(1 / a) * c'
    return (1 / a) * c

from operator import pow

def log(c, b):
    'try math.log andif that dont work, try cmath.log'
    try: return math.log(c, b)
    except: return cmath.log(c, b)

def root(c, a): 
    'c ** (1 / a)'
    return c ** (1 / a)


