# NOTE: these functions shall not support modular arithmetic. there are a few reasons:
#
# 1) adding a (mod=None) parameter to them changes them to a completely different algebra
# 2) it is a very hacky change
# 3) operands will have to be integers, causing a parameter to restrict type dynamically. this is inelegant
# 4) the very meaning of an operation changes when the mod parameter is given

# NOTE: except inc and dec (which are defined only on integers), all these shall support tensorial operands, because tensors support element-wise operators on their scalars.
# as such, all the operators shall be element-wise. that means mul(matrix1, matrix2) shall be the hadamard product, for example

import math, cmath
from typing import Literal, Callable, Generator
from collections.abc import Iterable, Sequence
from numbers import Number
from typing import Any	# for pos

def pos(a: Any) -> Any:
	'+x'
	return a

def neg(a: Number | Sequence) -> Number | Sequence:
	'−x, unary subtraction, additive inverse'
	if isinstance(a, Sequence):
		return type(a)(neg(p) for p in a)
	else:
		return -a

def inc(a: int, *, step: int = 1) -> int:
	'incrementation'
	return a + step

def dec(a: int, *, step: int = 1) -> int:
	'decrementation'
	return a - step

def add(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'a + b, addition'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(add(p, q) for p, q in zip(a, b, strict = True))
	else:
		return a + b

def sub(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'a − b, subtraction, difference, inverse of add'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(sub(p, q) for p, q in zip(a, b, strict = True))
	else:
		return a - b

def mul(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'a × b, a * b, multiplication, product, times'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(mul(p, q) for p, q in zip(a, b, strict = True))
	else:
		return a * b

def div(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'a ∕ b, a / b, division, inverse of mul'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(div(p, q) for p, q in zip(a, b, strict = True))
	else:
		return a / b

def pow(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'aᵇ, a ^ b, a ** b, power, exponentiation to a base, inverse of root'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(pow(p, q) for p, q in zip(a, b, strict = True))
	else:
		return a ** b

def root(a: Number | Sequence, b: Number | Sequence) -> Number | Sequence:
	'nᵗʰ root, n-th root, ᵇ√a, a ^ (1 / b), inverse of pow'
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

def log(a: int | float | complex, b: int | float | complex) -> int | float | complex:
	'logarithm, inverse of exp'
	if isinstance(a, Sequence) and isinstance(b, Sequence):
		return type(a)(log(p, q) for p, q in zip(a, b, strict = True))
	else:
		try   :	return math.log(a, b)
		except:	return cmath.log(a, b)

