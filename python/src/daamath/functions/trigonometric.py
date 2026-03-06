import math, cmath
from numbers import Number

def sin(a: Number) -> Number:
	try:	return math.sin(a)
	except: return cmath.sin(a)

def cos(a: Number) -> Number:
	try:	return math.cos(a)
	except: return cmath.cos(a)

def tan(a: Number) -> Number:
	try:	return math.tan(a)
	except: return cmath.tan(a)

def cot(a: Number) -> Number:
	try:	return 1 / math.tan(a)
	except: return 1 / cmath.tan(a)

def sec(a: Number) -> Number:
	try:	return 1 / math.cos(a)
	except: return 1 / cmath.cos(a)

def csc(a: Number) -> Number:
	try:	return 1 / math.sin(a)
	except: return 1 / cmath.sin(a)

# inverse

def asin(a: Number) -> Number:
	try:	return math.asin(a)
	except: return cmath.asin(a)

def acos(a: Number) -> Number:
	try:	return math.acos(a)
	except: return cmath.acos(a)

def atan(a: Number) -> Number:
	try:	return math.atan(a)
	except: return cmath.atan(a)

def acot(a: Number) -> Number:
	try:	return math.atan(1 / a)
	except: return cmath.atan(1 / a)

def asec(a: Number) -> Number:
	try:	return math.acos(1 / a)
	except: return cmath.acos(1 / a)

def acsc(a: Number) -> Number:
	try:	return math.asin(1 / a)
	except: return cmath.asin(1 / a)

