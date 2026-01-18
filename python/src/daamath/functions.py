# none of these functions should depend on each other
# complex arithmetic shall be supported as much as possible

from .classes import Tern, ComplexTruth	# for cmp and complex comparisons
from .mappers import *
from .sigmoids import *
from . import numbers as _numbers	# POS_INF, NEG_INF in incf, decf

from .strings import ASCII, ASCII_SUPERSCRIPT, ASCII_SUBSCRIPT
from typing import Literal as _Literal
from typing import Callable as _Callable
from typing import Generator as _Generator
from collections.abc import Iterable as _Iterable
from collections.abc import Sequence as _Sequence
from collections import deque as _deque
import math as _math
import cmath as _cmath
import struct as _struct	# for direct bit manipulation
from itertools import combinations as _combinations	# for vparallel

def add(a, b):
	'a + b also known as addition'
	return a + b

def sub(a, b):
	'a − b also known as subtraction also known as difference'
	return a - b

def mul(a, b):
	'a × b also known as multiplication also known as product also known as times'
	return a * b

def div(a, b):
	'a ∕ b also known as division'
	return a / b

def nexttowards(x: int | float, target: int | float, steps: int = 1) -> int | float:
	if type(x) != type(target):
		raise TypeError('x and target must be same type')
	
	if isinstance(x, int):
		if abs(x - target) <= steps:
			return target
		return x + steps if x < target else x - steps
	elif isinstance(x, float):
		for _ in range(steps):
			x = _math.nextafter(x, target)
		return x
	else:
		raise TypeError('x must be either int or float')

def inc(x: int | float, steps: int = 1) -> int | float:
	'incrementation. like nexttowards but with target = ∞'
	if isinstance(x, int):
		return x + steps
	elif isinstance(x, float):
		for _ in range(steps):
			x = _math.nextafter(x, _numbers.POS_INF)
		return x
	else:
		raise TypeError('x must be int or float')

def dec(x: int | float, steps: int = 1) -> int | float:
	'decrementation. like nexttowards but with target = -∞'
	if isinstance(x, int):
		return x - steps
	elif isinstance(x, float):
		for _ in range(steps):
			x = _math.nextafter(x, _numbers.NEG_INF)
		return x
	else:
		raise TypeError('x must be int or float')

def neg(x, *, add_identity = 0.0):
	'−x, unary subtraction, additive inverse'
	return add_identity - x

def inv(x, *, mul_identity = 1.0):
	'1 / x, reciprocal, unary division, multiplicative inverse, y such that x * y = 1 where 1 is the multiplicative identity'
	return mul_identity / x

def mod(a, b):
	'modulus'
	if not (isinstance(a, int) and isinstance(b, int)):
		raise TypeError("modulus only deals with integers. perhaps you meant floorrem?")
	return a % b

def root(a, b):
	'nᵗʰ root, n-th root, ᵇ√a, a ^ (1 / b), inverse of exponentiation'
	return a ** (1/b)

def pow(a, b):
	'aᵇ also known as exponentiation'
	return a ** b

def exp10(x):
	'exponentiation, base 10'
	return 10 ** x

def log(a, base) -> float | complex:
	'logarithm also known as inverse of exponentiation'
	if base == 2:
		try:	return _math.log2(a, base)
		except (ValueError, TypeError):	return _cmath.log(a, base)
	elif base == 10:
		try:	return _math.log10(a, base)
		except (ValueError, TypeError):	return _cmath.log10(a, base)
	else:
		try:	return _math.log(a, base)
		except (ValueError, TypeError):	return _cmath.log(a, base)

def log2(a) -> float | complex:
	'logarithm, base 2'
	try:
		return _math.log2(a, base)
	except (ValueError, TypeError):	
		return _cmath.log(a, base)

def log10(a) -> float | complex:
	'logarithm, base 10'
	try:
		return _math.log10(a, base)
	except (ValueError, TypeError):	
		return _cmath.log10(a, base)

def loge(x) -> float | complex:
	'logarithm, base e'
	return _math.log(x)

def powm1(a, b):
	'a ** b - 1'
	return a ** b - 1

def exp2m1(x):
	'2 ** x - 1'
	return 2 ** x - 1

def exp10m1(x):
	'10 ** x - 1'
	return 10 ** x - 1

def logp1(a, b):
	'log(a+1, b)'
	return _math.log(a+1, b)

def log2p1(x):
	'log2(x+1)'
	return _math.log(x+1, 2)

def log10p1(x):
	'log10(x+1)'
	return _math.log(x+1, 10)

def sexp(a, b):
	'superexponentiation also known as tetration'
	raise NotImplementedError('i havent made this yet')

def sroot(a, b):
	'superroot also known as inverse of tetration'
	raise NotImplementedError('i havent made this yet')

def slog(a, b):
	'superlogarithm also known as inverse of tetration'
	raise NotImplementedError('i havent made this yet')

def parallel(a, b):
	'1 / {(1 / a) + (1 / b)}, (a * b) / (a + b), parallel operation, parallel addition'
	return (a * b) / (a + b)
#  1
# ---------------
# 1/a + 1/b + 1/c
#
#

from math import sqrt
from math import cbrt

def qdrt(x):
	'x⁴, x ^ 4, x ** 4, zenzizenzic'
	return x ** 4

def isqrt(x):
	'1 / √x. hardware sometimes has fast implementations for this'
	return 1 / _math.sqrt(x)

def icbrt(x):
	'1 / ∛x'
	return 1 / _math.cbrt(x)

def iqdrt(x):
	'1 / ∜x'
	return x ** -0.25

from math import floor
from math import ceil

def floor1p(x):
	'⌊x⌋ + 1. like ⌈x⌉ but x + 1 when x ∈ ℤ'
	return _math.floor(x) + 1

def ceil1m(x):
	'⌈x⌉ - 1. like ⌊x⌋ but x - 1 when x ∈ ℤ'
	return _math.ceil(x) - 1

def hyper(n, a, b):
	'return n-th hyperoperation of a, b'
	raise NotImplementedError('not made yet')

def away(x):
	'directed rounding to integer, away from ±0'
	raise NotImplementedError('not made yet')

def ceildiv(x):
	'division rounded to +∞'
	raise NotImplementedError('not made yet')

def truncdiv(x):
	'division rounded to ±0'
	raise NotImplementedError('not made yet')

def awaydiv(x):
	'division rounded away from ±0'
	raise NotImplementedError('not made yet')

def rounddiv(x):
	'round(div(a,b))'
	raise NotImplementedError('not made yet')

def floorrem(x):
	'remainder of floordiv'
	raise NotImplementedError('not made yet')

def ceilrem(x):
	'remainder of ceildiv'
	raise NotImplementedError('not made yet')

def truncrem(x):
	'remainder of truncdiv'
	raise NotImplementedError('not made yet')

def awayrem(x):
	'remainder of awaydiv'
	raise NotImplementedError('not made yet')

def roundrem(x):
	'remainder of rounddiv'
	raise NotImplementedError('not made yet')

def floordivrem(x):
	'return (floordiv, floorrem)'
	raise NotImplementedError('not made yet')

def ceildivrem(x):
	'return ( ceildiv,  ceilrem)'
	raise NotImplementedError('not made yet')
	
def truncdivrem(x):
	'return (truncdiv, truncrem)'
	raise NotImplementedError('not made yet')

def awaydivrem(x):
	'return ( awaydiv,  awayrem)'
	raise NotImplementedError('not made yet')

def rounddivrem(x):
	'return (rounddiv, roundrem)'
	raise NotImplementedError('not made yet')

# comparative ------------------------------------------------------------------

def lt(a: int | float, b: int | float) -> bool:
	'a < b'
	return a < b

def le(a: int | float, b: int | float) -> bool:
	'a ≤ b'
	return a <= b

def eq(a: int | float, b: int | float) -> bool:
	'a = b'
	return a == b

def ne(a: int | float, b: int | float) -> bool:
	'a ≠ b'
	return a != b

def ge(a: int | float, b: int | float) -> bool:
	'a ≥ b'
	return a >= b

def gt(a: int | float, b: int | float) -> bool:
	'a > b'
	return a > b

def lt(a: int | float | complex | tuple[float, float], b: int | float | complex | tuple[float, float]) -> bool | complex | tuple[bool, bool]:
	'a less than b'
	if isinstance(a, bool) or isinstance(b, bool):
		raise TypeError('bool is a truth, not a number')
	elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
		return a < b
	elif isinstance(a, complex) and isinstance(b, complex):
		return complex(a.real < b.real, a.imag < b.imag)
	elif isinstance(a, tuple) and isintance(b, tuple):
		return (a[0] < b[0], a[1] < b[1])
	else:
		raise ValueError('allowed types are: int|float & int|float, complex & complex, tuple[float, float], tuple[float, float]')

def cle(a: complex, b: complex) -> tuple[bool]:
	'complex less-than-or-equal-to'
	return (a.real <= b.real, a.imag <= b.imag)

def ceq(a: complex, b: complex) -> tuple[bool]:
	'complex equals'
	return (a.real == b.real, a.imag == b.imag)

def cne(a: complex, b: complex) -> tuple[bool]:
	'complex not-equals'
	return (a.real != b.real, a.imag != b.imag)

def cge(a: complex, b: complex) -> tuple[bool]:
	'complex greater-than-or-equals'
	return (a.real >= b.real, a.imag >= b.imag)

def cgt(a: complex, b: complex) -> tuple[bool]:
	'complex greater-than'
	return (a.real > b.real, a.imag > b.imag)

def cmp(a, b) -> Tern | ComplexTruth[Tern, Tern] | tuple[Tern, Tern]:
	'comparison. -1 if a < b, 0 if a == b, 1 if a > b'
	if isinstance(a, bool) or isinstance(b, bool):
		raise TypeError('bool is a truth, not a number')
	elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
		return Tern(a, b)
	elif isinstance(a, complex) and isinstance(b, complex):
		return ComplexTruth(Tern(a.real, b.real), Tern(a.imag, b.imag))
	elif isinstance(a, tuple) and isintance(b, tuple):
		return (Tern(a[0], b[0]), Tern(a[1], b[1]))
	else:
		raise ValueError('unrecognized input')

def sin(a):
	'circular sine'
	if isinstance(a, complex):
		return _cmath.sin(a)
	else:
		return _math.sin(a)

# boolean ----------------------

def nand(a: bool, b: bool) -> bool:
	'not(and(a, b))'
	return not(a and b)

def nor(a: bool, b: bool) -> bool:
	'not(or(a, b))'
	return not(a or b)

def xnor(a: bool, b: bool) -> bool:
	'not(xor(a, b))'
	return not(xor(a, b))

def imp(a: bool, b: bool) -> bool:
	'a → b, ¬a ∨ b, material implication'
	return not a or b

def nimp(a: bool, b: bool) -> bool:
	'¬(a → b), a ∧ ¬b, only a'
	return a and not b

def con(a: bool, b: bool) -> bool:
	'a ← b, a ∨ ¬b, converse implication'
	return a or not b

def ncon(a: bool, b: bool) -> bool:
	'¬(a ← b), ¬a ∧ b, only b'
	return not a and b

# combinatorial ---------------

def sumt(x):
	'return sum of all numbers from 1 to x. like factorial but with addition'
	if isinstance(x, int): 
		return (x*(x+1))//2
	return (x*(x+1))/2

# interval -------------------

def in_open(a, x, b) -> bool:
	return a < x < b

def in_closed(a, x, b) -> bool:
	return a <= x <= b

def in_left_open(a, x, b) -> bool:
	return a < x <= b

def in_right_open(a, x, b) -> bool:
	return a <= x < b

def clamp(value, low = 0, high = 1) -> float:
	'restrict value to [low, high]. returns min(max(low, value), high)'
	return min(max(low, value), high)

def lerp(value, low, high) -> float:
	'linear interpolation. maps value in [0, 1] to [low, high]'
	return (1 - value) * low + value * high

def unlerp(value, low, high) -> float:
	'inverse of linear interpolation. maps value in [low, high] to [0, 1]'
	return (value - low) / (high - low)

def plerp(value, low, high, power = 1) -> float:
	if power == 0:
		return low * (high / low) ** value
	else:
		return ((1 - value) * low ** power + value * high ** power) ** (1 / power)

def unplerp(value, low, high, power = 1) -> float:
	if power == 0:
		return _math.log(value / low, high / low)
	else:
		return (value ** power - low ** power) / (high ** power - low ** power)

def map(value, a, b, c, d) -> float:
	'value from [a, b] to [c, d]. same as lerp(unlerp(a, b, value), c, d)'
	return (1 - (value - a) / (b - a)) * c + ((value - a) / (b - a)) * d

def pmap(value, a, b, c, d, power = 1) -> float:
	'value from [a, b] to [c, d]. same as plerp(unplerp(a, b, value), c, d)'
	if power == 0:
		return c * (d / c) ** (_math.log(value / a, b / a))
	else:
		value = (value ** power - a ** power) / (b ** power - a** power)
		return ((1 - value) * c ** power + value * d ** power) ** (1 / power)

# variadic ---------------------------------------------------------------------

def vor(iterable: _Iterable[bool]) -> bool:
	'variadic OR gate'
	return any(iterable)

def vand(iterable: _Iterable[bool]) -> bool:
	'variadic AND gate'
	return all(iterable)

def vadd(iterable: _Iterable[int | float | complex]) -> int | float | complex:
	'variadic addition'
	return sum(iterable)

def vmul(iterable: _Iterable[int | float | complex]) -> int | float | complex:
	'variadic multiplication'
	return _math.prod(iterable)

def vparallel(iterable: _Iterable[int | float | complex]) -> int | float | complex: 
	'variadic parallel'

	n = len(iterable)

	if n == 0:
		return 0
	if n == 1:
		return iterable[0]

	numerator = _math.prod(iterable)

	# sum of products of n-1 elements
	#denominator = sum(prod(xs[j] for j in range(n) if j != i) for i in range(n))
	denominator = sum(_math.prod(i) for i in _combinations(iterable, n - 1))

	return numerator / denominator

# floating point numbers -------------------------------------------------------

def bytes_to_float(b: bytes, format: str = '>f'):
	return _struct.unpack(format, b)[0]

# miscellaneous ----------------------------------------------------------------

def fixed_log(value: int | float, A_x = 1, A_y = 0, B_x = _math.e, B_y = 1) -> float:
	"""inverse of fixed_exp. its logarithm, but instead of specifying base, you specify two fixed points. 
	
	formula: (1 - temp) * A_y + temp * B_y
		where temp = log(x / A_x, base = B_x / A_x)
	
	the defualts correspond to ln(x)
	"""
	temp = _math.log(value / A_x, B_x / A_x)
	return (1 - temp) * A_y + temp * B_y

def fixed_exp(value: int | float, A_x = 0, A_y = 1, B_x = 1, B_y = _math.e) -> float:
	"""inverse of fixed_log. its exponent, but instead of specifying exponent, you specify two fixed points. 
	
	formula: A_y * (B_y / A_y) ** ((value - A_x) / (B_x - A_x))
	
	the defualts correspond to exp(x)
	"""
	return A_y * (B_y / A_y) ** ((value - A_x) / (B_x - A_x))

def soft_log(value: int | float, softness = 1, low_x = 0, low_y = 0, high_x = _math.expm1(1), high_y = 1) -> float:
	"""inverse of soft_exp. softness values closer to low_x are similar to using y = log(x). softness values closer to ∞ are similar to using y = x

	formula: (1 - temp) * low_y + temp * high_y
		where temp = math.log1p((value - low_x) / softness) / math.log1p((high_x - low_x) / softness) 

	the defaults correspond to math.log1p(x) so that changing softness will still allow a one-one mapping for all +ve x
	if you want it to mirror math.log(x), use low_x = 1, high_x = math.e but know that soft_log(x) is undefined for x ≤ low_x - softness)
	"""
	temp = _math.log1p((value - low_x) / softness) / _math.log1p((high_x - low_x) / softness) 
	return (1 - temp) * low_y + temp * high_y

def soft_exp(value: int | float, softness = 1, low_x = 0, low_y = 0, high_x = 1, high_y = _math.expm1(1)) -> float:
	"""inverse of soft_log. softness values closer to low_x are similar to using y = exp(x). softness values closer to ∞ are similar to using y = x

	formula: low_x + softness * math.expm1(temp * math.log1p((high_x - low_x) / softness))
		where temp = (value - low_y) / (high_y - low_y)

	the defaults correspond to math.expm1(x) so that changing softness will still allow a one-one mapping for all +ve x
	if you want it to mirror math.exp(x), use low_x = 1, high_x = math.e
	"""
	return low_y + softness * _math.expm1(((value - low_x) / (high_x - low_x)) * _math.log1p((high_y - low_y) / softness))
	# here is an algebraically equivalent but numerically unstable form:
	# temp = low_y + softness * ((1 + (high_y - low_y) / softness) ** value - 1)
	# return (temp - low_x) / (high_x - low_x)

def logit(x):
	return _math.log(x/(1-x))

def boolmap(a: bool, b: any, c: any):
	'if a then b else c'
	return b if a else c

def ternmap(a: Tern | int | float, p: any, q: any, r: any):
	'p if a = -1, q if a = 0, r if a = 1'

	match Tern(a) if not isinstance(a, Tern) else a:
		case -1: return p
		case  0: return q
		case  1: return r

def cmpmap(a: int | float, b: int | float, p: any, q: any, r: any):
	'p if a < b, q if a == b, r if a > b. like ifelse but with ternary'
	match (a > b) - (a < b):
		case -1: return p
		case  0: return q
		case  1: return r
		case  _: raise ValueError('Tern(a, b) is out of bounds {-1, 0, 1}')

def binet(n: int | float) -> float:
	return (_numbers.PHI ** n - _numbers.PSI ** n) * _numbers.ISQRT_5
	
# iterables --------------------------

def concat(iterables: _Iterable[_Iterable[any]]) -> _Iterable[any]:
	'variadic concatenation'
	result = iterables[0]
	for iterable in iterables[1:]:
		result += iterable
	return result

# sequences --------------------------

def nth(stuff) -> any:
	return stuff[n]

def head(stuff) -> _Sequence:
	return stuff[0]

def last(stuff) -> _Sequence:
	return stuff[-1]

def tail(stuff) -> _Sequence:
	return stuff[1:]

def init(stuff) -> _Sequence:
	return stuff[:-1]

def slice(stuff, a, b) -> _Sequence:
	raise NotImplementedError("not sure if to include or exclude a-th and b-th elements")
	return stuff[a, b]

# angle conversions -------------------------

def deg_to_rad(deg):
	'deg * τ / 360'
	return deg * 0.017453292519943295769236907684886127134388888888888888888888888888888888888888889

def deg_to_turn(deg):
	'degree / 360'
	return deg * 0.002777777777777777777777777777777777777777777777777777777777777777777777777777777

def rad_to_deg(rad):
	'radian * 360 / τ'
	return rad * 57.295779513082320876798154814105170332536226632088586087901802477036600940354404

def rad_to_turn(rad):
	'radian * 4 / τ'
	return rad * 0.15915494309189533576888376337251436203482285175580162802194945132510166927876223

def turn_to_deg(turn):
	'turn * 360'
	return turn * 360

def turn_to_rad(turn):
	'turn * τ'
	return turn * 6.28318530717958647692528676655900576838

# string helpers ---------------------------------------------------------------

# factories --------------------------------------------------------------------
"""
def multilerp(value: float, x_values: _Iterable[float], y_values: _Iterable[float], is_sorted: bool = False) -> float:
	'a slow inefficient ass function that linearly interpolates a bunch of points and lets you sample on them'
	
	if x_value
	
	#x_values, y_values = (x_values, y_values) if is_sorted else zip(*sorted(zip(x_values, y_values)))

	index_low: int = 0
	index_high: int = 0

	if is_sorted:
		for index, x_value in enumerate(x_values):
			if x_value > value:
				break
			index_low = 
	else:
		for index, x_value in enumerate(x_values):
			if x_value == value:
				return y_values[index]
			index_low = index if x_value < value and index_low < index else index_low
			index_high = index if x_value > value and index_high > index else index_high
	
	value_intermediate = (value - x_values[index_low]) / (x_values[index_high] - x_values[index_low])
	return y_values[index_low] * (1 - value_intermediate) + y_values[index_high] * value_intermediate
"""	
def factory_ascii_converter(from_str: str, to_str: str) -> _Callable[[str], str]:
	# create a dictionary mapping for all non-space characters
    mapping = {a: b for a, b in zip(from_str, to_str) if b.strip()}
    def converter(s: str) -> str:
        return ''.join(mapping.get(ch, ch) for ch in s)
    return converter

def factory_interpolation(x_values: _Sequence[int|float], y_values: _Sequence[int|float]) -> _Callable[[int|float], int|float]:
	'a factory that turns a bunch of points into a sample-able ℝ ⟼ ℝ function by a polynomial interpolation'
	raise NotImplementedError



# specific converters
to_superscript = factory_ascii_converter(ASCII, ASCII_SUPERSCRIPT)
to_subscript = factory_ascii_converter(ASCII, ASCII_SUBSCRIPT)

# add slerp and unslerp

def coeffs_from_roots(roots: _Sequence[float]) -> _Sequence[float]:
    """
    given an iterable of roots r1, r2, ..., rn
    returns coefficients [c0, c1, ..., cn] such that
	
    (x - r1)(x - r2)...(x - rn)
    = c0*x^n + c1*x^(n-1) + ... + cn
    """
    coeffs = [1]
	
    for r in roots:
        new = [0] * (len(coeffs) + 1)
        for i, c in enumerate(coeffs):
            new[i]     += c        # multiply by x
            new[i + 1] -= r * c    # multiply by -r
        coeffs = new
	
    return coeffs

