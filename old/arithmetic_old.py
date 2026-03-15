# NOTE: these operators shall not support modular arithmetic. there are a few reasons:
#
# 1) adding a (mod=None) parameter to them changes them to a completely different algebra with a different structure
# 2) it is a very hacky change
# 3) operands will have to be integers, causing a parameter to restrict type dynamically. this is inelegant
# 4) the very meaning of an operator changes when the mod parameter is given
# 5) "oh! added a mod parameter on add. well, might as well add a saturation_threshold on it. oh! and also might as well make it variadic too!". do you see where im going with this?

import math, cmath, operator, functools
from typing import Literal, Callable, Generator
from collections.abc import Iterable, Sequence
from numbers import Number
from typing import Any	# for pos

def inc(a: Number | Sequence) -> Number | Sequence:
	'incrementation, a++, ++a, inverse of dec'
	if isinstance(a, Sequence):
		return type(a)(inc(p) for p in a)
	else:
		return a + 1

def dec(a: Number | Sequence) -> Number | Sequence:
	'decrementation, a--, --a, inverse of inc'
	if isinstance(a, Sequence):
		return type(a)(dec(p) for p in a)
	else:
		return a - 1

def add(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'addition, a + b, inverse of sub'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(add(p, q) for p, q in zip(a, b, strict = True))
	else:
		return a + b

def sub(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'subtraction, a − b, difference, inverse of add'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(sub(p, q) for p, q in zip(a, b, strict = True))
	else:
		return a - b

def mul(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'multiplication, a × b, a * b, product, times, inverse of div'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(mul(p, q) for p, q in zip(a, b, strict = True))
	else:
		return a * b

def div(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'division, a ∕ b, a / b, inverse of mul'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(div(p, q) for p, q in zip(a, b, strict = True))
	else:
		return a / b

def pow(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'power, aᵇ, a ^ b, a ** b, exponentiation to a base, inverse of root'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(pow(p, q) for p, q in zip(a, b, strict = True))
	else:
		return a ** b

def root(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'root, ᵇ√a, a ^ (1 ∕ b), nᵗʰ root, inverse of pow'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(root(p, q) for p, q in zip(a, b, strict = True))
	else:
		return a ** (1 / b)

def exp(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'exponentiation, b ^ a, inverse of log'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(exp(p, q) for p, q in zip(a, b, strict = True))
	else:
		return b ** a

def log(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'logarithm, inverse of exp'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(log(p, q) for p, q in zip(a, b, strict = True))
	else:
		try   :	return math.log(a, b)
		except:	return cmath.log(a, b)
'''
def ainv(a: Number | Sequence) -> Number | Sequence:
	'additive inverse, -x, unary subtraction'
	if isinstance(a, Sequence):
		return type(a)(ainv(p) for p in a)
	else:
		return -a
	
def minv(a: Number | Sequence) -> Number | Sequence:
	'multiplicative inverse, 1 ∕ x, unary division'
	if isinstance(a, Sequence):
		return type(a)(minv(p) for p in a)
	else:
		return 1 / a
	
'''
add_1 = functools.partial(add, b = 1)	# increment
sub_1 = functools.partial(sub, b = 1)	# decrement
ainv = functools.partial(sub, a = 0)	# additive inverse. negation
minv = functools.partial(div, a = 1)	# multiplicative inverse. reciprocal
