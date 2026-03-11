# hey! you! yeah, you! daa!
#
# implement a generalization of signum and normalize, because these are just the same radial projection operation. also allow adjusting the radius, and the norm of this.
# also implement a generalized clamp function that supports clamping a vector. the clamp function takes [a, b] as of now, but we have to somehow 
#
#
# also, theres stuff to be learned from putting abs and norm under the same umbrella. abs takes the distance from the centre, does it not? norm does the same thing
#
# also, implement vector products like dot product, cross product (just a compositon of wedge product and hodge star. also, in 3D and 7D only! because they tie with quaternions and octonions, but none higher. no more normed algebrae after that), wedge product, 

from . import arithmetic, arithmetic_numeric, complex, complex_numeric, trigonometric, trigonometric_numeric, hyperbolic, logical, bitwise, set, interval, combinatorial, variadic, rounding, sigmoids, mappers, tensor, floating

from .arithmetic import inc, dec, add, sub, mul, div, pow, root, log, spow, sroot, slog, ainv, minv
from .arithmetic import h0c, h0b, h1c, h1b, h1a, h2c, h2b, h2a, h3c, h3b, h3a, h4c, h4b, h4a, hyper, h1b_c0, h1a_c0, h2b_c1, h2a_c1
from .arithmetic_numeric import fma, pow_m1, root_1p, exp_m1, log_1p
from .arithmetic_numeric import pow_e, pow_2, pow_3, pow_10, root_e, root_2, root_3, root_10, exp_e, exp_2, exp_3, exp_10, log_e, log_2, log_3, log_10
from .arithmetic_numeric import pow_e_m1, pow_2_m1, pow_3_m1, pow_10_m1, root_e_1p, root_2_1p, root_3_1p, root_10_1p, exp_e_m1, exp_2_m1, exp_3_m1, exp_10_m1, log_e_1p, log_2_1p, log_3_1p, log_10_1p

from .complex import real, imag, arg, rect, polar, conj
from .complex_numeric import cis

from .trigonometric import sin, cos, tan, cot, sec, csc, asin, acos, atan, acot, asec, acsc
from .trigonometric_numeric import atan2, sinpi, cospi, tanpi, cotpi, secpi, cscpi, asinpi, acospi, atanpi, acotpi, asecpi, acscpi
from .hyperbolic import sinh, cosh, tanh, coth, sech, csch, asinh, acosh, atanh, acoth, asech, acsch

from .logical import bool_not, bool_and, bool_nand, bool_or, bool_nor, bool_xor, bool_nxor, bool_imp, bool_nimp, bool_con, bool_ncon
from .bitwise import bit_not, bit_and, bit_nand, bit_or, bit_nor, bit_xor, bit_nxor, bit_imp, bit_nimp, bit_con, bit_ncon
from .set import set_not, set_and, set_nand, set_or, set_nor, set_xor, set_nxor, set_imp, set_nimp, set_con, set_ncon

from .interval import lt, le, eq, ne, ge, gt, oo, oc, co, cc

from .statistics import min, max, mean, median, mode, var, stdev
from .statistics import mean_ninf, mean_n1, mean_0, mean_p1, mean_pinf
from .combinatorial import fact, sumt
from .variadic import vand, vor, vadd, vmul, vparallel
from .rounding import round, floor, ceil, trunc, away, round_floor, round_ceil, round_trunc, round_away, round_even, round_odd, quot, rem, quotrem, quot_1, rem_1, quotrem_1
#from .hyperoperation import
from .sigmoids import *
from .mappers import *
from .tensor import norm, normalize, norm_2, normalize_2
from .floating import copysign

# sinc (sin(x) / x), cosc, … perhaps?

# ==============================================================================

# none of these functions should depend on each other
# complex arithmetic shall be supported as much as possible

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

def signum(a, b = 0):
	return (a > b) - (a < b)

def clamp(value: Complex | Sequence[Complex], centre: Complex | Sequence[Complex], radius: Real, *, p: Real = 2) -> Complex | Sequence[Complex]:
	'project to a hyperball. generalizes scalar signum() and vectorial normalize()'
	if isinstance(value, Sequence):
		return value / norm(value)
	else:
		return radius * ((a > b) - (a < b))

def clamp(value: Complex | Sequence[Complex], centre: Complex | Sequence[Complex], radius: Real) -> Complex | Sequence[Complex]:
	'project to a hypersphere. generalizes scalar clamp() and vectorial clamp (graphics libraries implement component-wise clamping, which clamps the vector to a cube (a hypersphere in p = ∞))'

def clamp(value, low = 0, high = 1) -> float:
	'restrict value to [low, high]. returns min(max(low, value), high)'
	return min(max(low, value), high)

def lerp(parameter, low, high, *, power = 1) -> float:
	'linear interpolation. maps parameter in [0, 1] to [low, high]. formula is low * (1 - parameter) + high * parameter instead of low + parameter * (high - low) because the former is symmetric and stable at parameter = 0 and parameter = 1, and the latter is asymmetric'
	if power == 0:
		return low * (high / low) ** parameter
	elif power == 1:
		return low * (1 - parameter) + high * parameter
	else:
		return ((1 - parameter) * low ** power + parameter * high ** power) ** (1 / power)

def unlerp(parameter, low, high, *, power = 1) -> float:
	'inverse of linear interpolation. maps parameter in [low, high] to [0, 1]. returns (parameter - low) / (high - low)'
	if power == 0:
		return _math.log(parameter / low, high / low)
	elif power == 1:
		return (parameter - low) / (high - low)
	else:
		return (parameter ** power - low ** power) / (high ** power - low ** power)

def map(value, a, b, c, d, *, power = 1) -> float:
	'value from [a, b] to [c, d]. same as lerp(unlerp(value, a, b), c, d)'
	if power == 0:
		return c * (d / c) ** (_math.log(value / a, b / a))
	elif power == 1:
		temp = (value - a) / (b - a)
		return (1 - temp) * c + (temp) * d
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

def fixed_log(value: int | float, A_x = 1, A_y = 0, B_x = _math.e, B_y = 1) -> float:
	"""inverse of fixed_exp. its logarithm, but instead of specifying base, you specify two fixed points. 
	
	formula: (1 - temp) * A_y + temp * B_y
		where temp = log(x / A_x, base = B_x / A_x)
	
	the defualts correspond to ln(x)
	"""
	temp = _math.log(value / A_x, B_x / A_x)
	return (1 - temp) * A_y + temp * B_y

def logit(x):
	return _math.log(x/(1-x))

def ifelse(a: bool, b: any, c: any) -> any:
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

def torsor(a, b, c):
	'a + (c - b). think of c - b as vector. we displace a by the vector c - b'
	return a - b + c

