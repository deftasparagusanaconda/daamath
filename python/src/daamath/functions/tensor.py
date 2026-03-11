# we need to generalize this to support up to tensors, not just vectors

from numbers import Number, Real
from collections.abc import Sequence
import math, functools

def norm(value: Number | Sequence[Number], *, power: Real) -> Real:
	'Lp norm, with power = 2 by default. supports real and complex values, and generalizes abs()'
	if isinstance(value, Number):
		return abs(value)

	if len(value) == 0:
		return 0

	# in case a value is [0, 0, 0, …]
	if all(element == 0 for element in value):
		return 0
	
	match p:
		case 0: 
			return sum(bool(element) for element in value)

		case 1: 
			return math.fsum(abs(element) for element in value)

		case 2: 
			scale = max(abs(element) for element in value)
			return scale * math.sqrt(math.fsum((abs(element) / scale) ** 2 for element in value))

		case math.inf:
			return max(abs(element) for element in value)

		case _: 
			scale = max(abs(element) for element in value)
			return scale * math.fsum((abs(element) / scale) ** power for element in value) ** (1 / power)

	# NOTE: 'why not use math.hypot in the power == 2 case?'
	# because:
	# 1) math.hypot will take only floats
	# 2) math.hypot requires elements to be passed flatly. we have to unpack our value to use math.hypot, which is slower than the actual function call itself, probably. 
	# in fact, i would like the numeric accuracy of math.hypot, but this is the tradeoff ive made for now

def norm(value: Number | Sequence[Number], *, power) -> Real:
	'frobenius norm'
	# yes i know it calculates 1 / power an unnecessary amount of times. i dont care.
	if isinstance(value, Sequence):
		return math.fsum(norm(element, power = power) ** power for element in value) ** (1 / power)
	else:
		return abs(value)

def normalize(value: Number | Sequence[Number], *args, **kwargs) -> Number | Sequence[Number]:
	return value / norm(value)

# euclidean norm
abs = norm_2 = functools.partial(norm, power = 2)
signum = normalize_2 = functools.partial(normalize, power = 2)
