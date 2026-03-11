import math

from math import atan2

def sinpi(x):
	return math.sin(x * math.pi) 

def cospi(x):
	return math.cos(x * math.pi) 

def tanpi(x):
	return math.tan(x * math.pi) 

def cotpi(x):
	return 1 / math.tan(x * math.pi) 

def secpi(x):
	return 1 / math.cos(x * math.pi) 

def cscpi(x):
	return 1 / math.sin(x * math.pi) 

def asinpi(x):
	return math.asin(x) / math.pi

def acospi(x):
	return math.acos(x) / math.pi 

def atanpi(x):
	return math.atan(x) / math.pi 

def acotpi(x):
	return math.atan(1 / x) / math.pi 

def asecpi(x):
	return math.acos(1 / x) / math.pi 

def acscpi(x):
	return math.asin(1 / x) / math.pi 

# so asinpi(sinpi(x)) = x
# asin(sin(x * π)) / π
# does this work???
