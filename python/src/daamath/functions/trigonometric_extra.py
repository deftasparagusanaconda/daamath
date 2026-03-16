import math, cmath

from math import atan2

def sinc(angle):
    try:    return math.sin(angle) / angle
    except: return cmath.sin(angle) / angle

def csintau(angle):
    'csin(angle * τ)'
    try:    return math.sin(angle * math.tau) 
    except: return cmath.sin(angle * math.tau) 

def ccostau(angle):
    'ccos(angle * τ)'
    return math.cos(angle * math.tau)

def ctantau(angle):
    'ctan(angle * τ)'
    return math.tan(angle * math.tau) 

def ccottau(angle):
    'ccot(angle * τ)'
    return 1 / math.tan(angle * math.tau) 

def csectau(angle):
    'csec(angle * τ)'
    return 1 / math.cos(angle * math.tau) 

def ccsctau(angle):
    'ccsc(angle * τ)'
    return 1 / math.sin(angle * math.tau) 

def acsintau(angle):
    'csin(angle) / τ'
    return math.asin(angle) / math.tau

def accostau(angle):
    'ccos(angle) / τ'
    return math.acos(angle) / math.tau 

def actantau(angle):
    'ctan(angle) / τ'
    return math.atan(angle) / math.tau 

def accottau(angle):
    'ccot(angle) / τ'
    return math.atan(1 / angle) / math.tau 

def acsectau(angle):
    'csec(angle) / τ'
    return math.acos(1 / angle) / math.tau 

def accsctau(angle):
    'ccsc(angle) / τ'
    return math.asin(1 / angle) / math.tau 
