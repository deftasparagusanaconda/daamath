from . import arithmetic, arithmetic_numeric, trigonometric, trigonometric_numeric, logical, comparative, hyperbolic, variadic, rounding, hyperoperation, sigmoids, mappers

from .arithmetic import pos, neg, inc, dec, add, sub, mul, div, pow, root, exp, log
from .arithmetic_numeric import fma, powm1, root1p, expm1, log1p
from .arithmetic_numeric import powe, pow2, pow3, pow10, roote, root2, root3, root10, expe, exp2, exp3, exp10, loge, log2, log3, log10
from .arithmetic_numeric import powem1, pow2m1, pow3m1, pow10m1, roote1p, root21p, root31p, root101p, expem1, exp2m1, exp3m1, exp10m1, loge1p, log21p, log31p, log101p
from .trigonometric import sin, cos, tan, cot, sec, csc, asin, acos, atan, acot, asec, acsc
from .trigonometric_numeric import sinpi, cospi, tanpi, cotpi, secpi, cscpi, asinpi, acospi, atanpi, acotpi, asecpi, acscpi
from .logical import and_, nand, or_, nor, xor, xnor, imp, nimp, con, ncon
from .comparative import lt, le, eq, ne, ge, gt
from .hyperbolic import sinh, cosh, tanh, coth, sech, csch, asinh, acosh, atanh, acoth, asech, acsch
from .variadic import vand, vor, vadd, vmul, vparallel
from .rounding import round, quot, rem, quotrem
from .hyperoperation import spow, sroot, sexp, slog
from .sigmoids import *
from .mappers import *

# sinc (sin(x) / x), cosc, … perhaps?

# ==============================================================================

# none of these functions should depend on each other
# complex arithmetic shall be supported as much as possible

from ..classes import Tern as _Tern, ComplexBool as _ComplexBool, ComplexTern as _ComplexTern	# for cmp and complex comparisons
from .. import numbers as _numbers	# POS_INF, NEG_INF in incf, decf

from typing import Literal as _Literal
from typing import Callable as _Callable
from typing import Generator as _Generator
from collections.abc import Iterable as _Iterable
from collections.abc import Sequence as _Sequence
import math as _math	# .. obvious
import cmath as _cmath	# .. also obvious
import struct as _struct	# for direct bit manipulation
from itertools import combinations as _combinations	# for vparallel

def parallel(a, b):
	'1 / {(1 / a) + (1 / b)}, (a * b) / (a + b), parallel operation, parallel addition'
	return (a * b) / (a + b)

def isqrt(x):
	'1 / √x. hardware sometimes has fast implementations for this'
	return 1 / _math.sqrt(x)

#def divrem(x, round: _Literal['toward', 'away', 'floor', 'ceil', 'round']):
	
# complex ----------------------------------------------------------------------

# these should support the following representations:
#rect: complex, polar: tuple[float, float], mat: tuple

#def conj

#def to_polar

#def to_rect

# combinatorial ---------------

def sumt(x):
	'return sum of all numbers from 1 to x. like factorial but with addition'
	return (x * (x + 1)) // 2 if isinstance(x, int) else (x * (x + 1)) / 2

# interval -------------------

"""
# useless not-worth-it functions
def in_open(x, a, b) -> bool:
	return a < x < b

def in_closed(x, a, b) -> bool:
	return a <= x <= b

def in_left_open(x, a, b) -> bool:
	return a < x <= b

def in_right_open(x, a, b) -> bool:
	return a <= x < b
"""
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
	temp = (value - a) / (b - a)
	return (1 - temp) * c + (temp) * d

def pmap(value, a, b, c, d, power = 1) -> float:
	'value from [a, b] to [c, d]. same as plerp(unplerp(a, b, value), c, d)'
	if power == 0:
		return c * (d / c) ** (_math.log(value / a, b / a))
	else:
		value = (value ** power - a ** power) / (b ** power - a** power)
		return ((1 - value) * c ** power + value * d ** power) ** (1 / power)

# floating point numbers -------------------------------------------------------

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

def bytes_to_float(b: bytes, format: str = '>f'):
	return _struct.unpack(format, b)[0]

# miscellaneous ----------------------------------------------------------------

def mod(a: int, b: int) -> int:
	'modulus'
	if not (isinstance(a, int) and isinstance(b, int)):
		raise TypeError(f'only int allowed. perhaps you want floorrem({a}, {b})?')
	return a % b

def hyper(n, a, b):
	'return n-th hyperoperation of a, b'
	raise NotImplementedError('not made yet')

import re as _re
import decimal as _decimal

def eval_prec(expr: str, prec: int) -> str:
	'eval but to a certain precision. super useful for defining constants'
	# regex to find numbers: integers or decimals
	number_pattern = _re.compile(r'\b\d+(\.\d*)?|\.\d+\b')

	# wrap numbers with _decimal.Decimal('...')
	def replacer(match):
		return f"_decimal.Decimal('{match.group(0)}')"

	expr_decimal = number_pattern.sub(replacer, expr)

	safe_dict = {'_decimal': _decimal, '__builtins__': {}}

	with _decimal.localcontext() as ctx:
		ctx.prec = prec
		result = eval(expr_decimal, safe_dict)
		return str(result)

def fma(a, b, c) -> float:
	'fused multiply-add. this has special hardware implementations, and is significant enough to include.'
	# return math.fma()	# only available in python ≥3.13
	return a * b + c

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

def ifelse(a: bool | _Tern, b: any, c: any, d: any = None) -> any:
	'return b if a is True, c if a is False, d if a is -True'

	match a:
		case  1: return b
		case  0: return c
		case -1: return d
		case  _: raise TypeError('a must be a bool or a Tern')

def binet(n: int | float) -> float:
	return (_numbers.PHI ** n - _numbers.PSI ** n) * _numbers.ISQRT_5
	
# iterables --------------------------

def concat(iterables: _Iterable[_Iterable[any]]) -> _Iterable[any]:
	'variadic concatenation'
	result = iterables[0]
	for iterable in iterables[1:]:
		result += iterable
	return result
"""
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
"""
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
'''
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
'''
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

