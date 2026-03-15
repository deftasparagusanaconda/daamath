from collections.abc import Iterable, Sequence
from typing import Any

def parallel(a, b):
	'1 / {(1 / a) + (1 / b)}, (a * b) / (a + b), parallel operation, parallel addition'
	return (a * b) / (a + b)

def rsqrt(x):
	'1 / √x. hardware sometimes has fast implementations for this'
	return 1 / _math.sqrt(x)

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

def logit(x):
	return _math.log(x / (1 - x))

from typing import Any
def ifelse(a: bool, b: Any, c: Any) -> Any:
    'return b if a is True, c if a is False'
    return b if a else c

def binet(n: int | float) -> float:
	return (_numbers.PHI ** n - _numbers.PSI ** n) * _numbers.ISQRT_5
	
# iterables --------------------------

def concat(iterables: Iterable[Iterable[Any]]) -> Iterable[Any]:
	'variadic concatenation'
	result = iterables[0]
	for iterable in iterables[1:]:
		result += iterable
	return result
"""
# sequences --------------------------

def nth(stuff) -> any:
	return stuff[n]

def head(stuff) -> Sequence:
	return stuff[0]

def last(stuff) -> Sequence:
	return stuff[-1]

def tail(stuff) -> Sequence:
	return stuff[1:]

def init(stuff) -> Sequence:
	return stuff[:-1]

def slice(stuff, a, b) -> Sequence:
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

def factory_interpolation(x_values: Sequence[int|float], y_values: Sequence[int|float]) -> _Callable[[int|float], int|float]:
	'a factory that turns a bunch of points into a sample-able ℝ ⟼ ℝ function by a polynomial interpolation'
	raise NotImplementedError



# specific converters
to_superscript = factory_ascii_converter(ASCII, ASCII_SUPERSCRIPT)
to_subscript = factory_ascii_converter(ASCII, ASCII_SUBSCRIPT)
'''
# add slerp and unslerp

def coeffs_from_roots(roots: Sequence[float]) -> Sequence[float]:
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

