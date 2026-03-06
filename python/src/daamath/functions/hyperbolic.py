import math, cmath
from numbers import Number

def sinh(a: Number) -> Number:
	try:	return math.sinh(a)
	except: return cmath.sinh(a)

def cosh(a: Number) -> Number:
	try:	return math.cosh(a)
	except: return cmath.cosh(a)

def tanh(a: Number) -> Number:
	try:	return math.tanh(a)
	except: return cmath.tanh(a)

def coth(a: Number) -> Number:
	try:	return 1 / math.tanh(a)
	except: return 1 / cmath.tanh(a)

def sech(a: Number) -> Number:
	try:	return 1 / math.cosh(a)
	except: return 1 / cmath.cosh(a)

def csch(a: Number) -> Number:
	try:	return 1 / math.sinh(a)
	except: return 1 / cmath.sinh(a)

# inverse

def asinh(a: Number) -> Number:
	try:	return math.asinh(a)
	except: return cmath.asinh(a)

def acosh(a: Number) -> Number:
	try:	return math.acosh(a)
	except: return cmath.acosh(a)

def atanh(a: Number) -> Number:
	try:	return math.atanh(a)
	except: return cmath.atanh(a)

def acoth(a: Number) -> Number:
	try:	return math.atanh(1 / a)
	except: return cmath.atanh(1 / a)

def asech(a: Number) -> Number:
	try:	return math.acosh(1 / a)
	except: return cmath.acosh(1 / a)

def acsch(a: Number) -> Number:
	try:	return math.asinh(1 / a)
	except: return cmath.asinh(1 / a)

