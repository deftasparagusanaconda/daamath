# mapper_* functions satisfy:
# active domain of f is x ∈ [0, 1], a ∈ [0, 1]
# active codomain of f is [0, 1]
# ∀a, f(0, a) = 0
# ∀a, f(1, a) = 1
# f is bijective
# ∫f(x, a) dx in x ∈ [0, 1] = a

from numbers import Number, Complex, Real
from collections.abc import Sequence
import math

fma = math.fma if hasattr(math, 'fma') else lambda a, b, c: a * b + c

def mapper1(a):
	"""map [0, 1] → [0, 1] using shifted and scaled versions of 1/x where a controls total area under curve

	formula
	-------
	f(x, A) = fma(x, A, x) / fma(x, A, 1) = (x * A + x) / (x * A + 1)
	
	                      1
	where A = A such that ∫ f(x, a) * dx == a
	                      0
	
	unfortunately, A must be obtained from the transcendental equation:
	a = (A + 1) * (A - ln(1 + A)) / A²
	
	so the function performs newton-raphson iteration with A = (1 / a - 1) ** -1.5 - 1 as its first guess

	visualization
	-------------
	0 100 100 100 100 100 100 100 100 100 100
	0  75  87  92  95  96  98  98  99 100 100
	0  47  67  77  84  89  92  95  97  99 100
	0  28  47  60  70  78  84  89  93  97 100
	0  17  31  44  55  65  73  81  88  94 100
	0  10  20  30  40  50  60  70  80  90 100
	0   6  12  19  27  35  45  56  69  83 100
	0   3   7  11  16  22  30  40  53  72 100
	0   1   3   5   8  11  16  23  33  53 100
	0   0   1   2   2   4   5   8  13  25 100
	0   0   0   0   0   0   0   0   0   0 100

	# (obtained from this)
for i in range(11):
	for j in range(11):
		print(str(round(mapper1(j/10, (10-i)/10)*100)).rjust(3, ' '), end = ' ')
	print()
	"""
	if a == 0:
		return lambda x: int(x >= 1)
	elif a == 1:
		return lambda x: int(x > 0)
	
	# newton-raphson iteration
	A = (1 / a - 1) ** -1.5 - 1	# first guess
	for i in range(1):
		# A = A - f(A) / f'(A) where f(A) = g(A) - a where g(A) = 
		# A = A - f(A) / f'(A)
		# 
		# 
		L = math.log1p(A)
		A = sum((math.prod((a, A, A)), A ** 2, math.prod((2, L, A)), -3 * A, 3 * L)) / sum((L, -2, 2 * L / A))
	
	return lambda x: fma(x, A, x) / fma(x, A, 1)

def mapper2(a):
	"""map [0, 1] → [0, 1] using scaled versions of b^x where a controls total area under curve

	count = 100
	a_count = 10
	for a in range(1 + a_count):
		print(a / a_count, sum(mapper2(x / count, a / a_count) for x in range(1, 1 + count)) / count)

	0.0 0.0128971672396949
	0.1 0.14010000587296564
	0.2 0.21615109481095915
	0.3 0.30351909900627655
	0.4 0.4013142571933184
	0.5 0.505
	0.6 0.6086857428066815
	0.7 0.7064809009937234
	0.8 0.7938489051890407
	0.9 0.8698999941270341
	1.0 1.0
	"""
	if p == 1:
		return lambda x: int(x > 0)
	
	A = math.tan(math.pi / 2 * (1 - a)) ** 4
	
	return lambda x: math.expm1(math.log(A) * x) / (A - 1)

def mapper3(a):
	"""map [0, 1] → [0, 1] using scaled versions of x^p where a controls total area under curve
	"""
	if a == 0:
		return int(x >= 1)

	A = (1 / a - 1)

	return lambda x: x ** A

# ------------------------------------------------------------------------------

def clamp(value: Real, low: Real = 0, high: Real = 1) -> Real:
	'restrict value to [low, high]. returns min(max(value, low), high)'
	return min(max(value, low), high)

def lerp(value: Real, low: Complex | Sequence[Complex], high: Complex | Sequence[Complex]) -> Complex | Sequence[Complex]:
	"""linear interpolation. maps value in [0, 1] to [low, high]. complex numbers are interpolated as a line in the rectangular (cartesian) argand plane. vectors are interpolated as a straight line in their respective space.

	values
	----------
	low

	returns
	-------
	low * (1 - value) + high * value

	formula
	-------
	notes
	-----
	a * (1 - t) + b * t is better than a + t * (b - a) because the former is symmetric and stable at t = 0 and t = 1, while the latter is asymmetric

	"""
	if isinstance(low, Sequence) and isinstance(high, Sequence):
		return type(low)(lerp(value, l, h) for l, h in zip(low, high, strict = True))
	else:
		return low * (1 - value) + high * value

def unlerp(value: Real, low: Complex, high: Complex) -> Complex:
	'inverse of linear interpolation. maps value in [low, high] to [0, 1]. returns (value - low) / (high - low)'
	if isinstance(low, Sequence) and isinstance(high, Sequence):
		return type(low)(unlerp(value, l, h) for l, h in zip(low, high, strict = True))
	else:
		return (value - low) / (high - low)

def plerp(value: Real, low: Complex, high: Complex, power: Real = 1) -> Complex:
	if power == 0:
		return low * (high / low) ** value
	else:
		return ((1 - value) * low ** power + value * high ** power) ** (1 / power)

def unplerp(value: Real, low: Complex, high: Complex, power: Real = 1) -> Complex:
	if power == 0:
		return math.log(value / low, high / low)
	else:
		return (value ** power - low ** power) / (high ** power - low ** power)

def map(value: Real, a: Complex, b: Complex, c: Complex, d: Complex) -> Complex:
	'value from [a, b] to [c, d]. same as lerp(unlerp(a, b, value), c, d)'
	temp = (value - a) / (b - a)
	return (1 - temp) * c + (temp) * d

def pmap(value: Real, a: Complex, b: Complex, c: Complex, d: Complex, power: Real = 1) -> Complex:
	'value from [a, b] to [c, d]. same as plerp(unplerp(a, b, value), c, d)'
	if power == 0:
		return c * (d / c) ** (math.log(value / a, b / a))
	else:
		value = (value ** power - a ** power) / (b ** power - a** power)
		return ((1 - value) * c ** power + value * d ** power) ** (1 / power)

def fixed_log(value: Real, A_x = 1, A_y = 0, B_x = math.e, B_y = 1) -> Real:
	"""inverse of fixed_exp. its logarithm, but instead of specifying base, you specify two fixed points. 
	
	formula: (1 - temp) * A_y + temp * B_y
		where temp = log(x / A_x, base = B_x / A_x)
	
	the defualts correspond to ln(x)
	"""
	temp = math.log(value / A_x, B_x / A_x)
	return (1 - temp) * A_y + temp * B_y

def fixed_exp(value: Real, A_x = 0, A_y = 1, B_x = 1, B_y = math.e) -> Real:
	"""inverse of fixed_log. its exponent, but instead of specifying exponent, you specify two fixed points. 
	
	formula: A_y * (B_y / A_y) ** ((value - A_x) / (B_x - A_x))
	
	the defualts correspond to exp(x)
	"""
	return A_y * (B_y / A_y) ** ((value - A_x) / (B_x - A_x))

def soft_log(value: Real, softness = 1, low_x = 0, low_y = 0, high_x = math.expm1(1), high_y = 1) -> Real:
	"""inverse of soft_exp. softness values closer to low_x are similar to using y = log(x). softness values closer to ∞ are similar to using y = x

	formula
	-------
	(1 - temp) * low_y + temp * high_y
	where temp = math.log1p((value - low_x) / softness) / math.log1p((high_x - low_x) / softness) 

	notes
	-----
	the defaults correspond to math.log1p(x) so that changing softness will still allow a one-one mapping for all +ve x
	if you want it to mirror math.log(x), use low_x = 1, high_x = math.e but know that soft_log(x) is undefined for x ≤ low_x - softness)
	"""
	temp = math.log1p((value - low_x) / softness) / math.log1p((high_x - low_x) / softness) 
	return (1 - temp) * low_y + temp * high_y

def soft_exp(value: Real, softness = 1, low_x = 0, low_y = 0, high_x = 1, high_y = math.expm1(1)) -> Real:
	"""inverse of soft_log. softness values closer to low_x are similar to using y = exp(x). softness values closer to ∞ are similar to using y = x

	formula: low_x + softness * math.expm1(temp * math.log1p((high_x - low_x) / softness))
		where temp = (value - low_y) / (high_y - low_y)

	the defaults correspond to math.expm1(x) so that changing softness will still allow a one-one mapping for all +ve x
	if you want it to mirror math.exp(x), use low_x = 1, high_x = math.e
	"""
	return low_y + softness * math.expm1(((value - low_x) / (high_x - low_x)) * math.log1p((high_y - low_y) / softness))
	# here is an algebraically equivalent but numerically unstable form:
	# temp = low_y + softness * ((1 + (high_y - low_y) / softness) ** value - 1)
	# return (temp - low_x) / (high_x - low_x)
