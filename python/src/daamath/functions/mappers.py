# these functions satisfy:
# active domain of f is x ∈ [0, 1], a ∈ [0, 1]
# active codomain of f is [0, 1]
# ∀a, f(0, a) = 0
# ∀a, f(1, a) = 1
# f is bijective
# ∫f(x, a) dx in x ∈ [0, 1] = a

import math as _math

_fma = _math.fma if hasattr(_math, 'fma') else lambda a, b, c: a * b + c

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
		L = _math.log1p(A)
		A = sum((_math.prod((a, A, A)), A ** 2, _math.prod((2, L, A)), -3 * A, 3 * L)) / sum((L, -2, 2 * L / A))
	
	return lambda x: _fma(x, A, x) / _fma(x, A, 1)

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
	
	A = _math.tan(_math.pi / 2 * (1 - a)) ** 4
	
	return lambda x: _math.expm1(_math.log(A) * x) / (A - 1)

def mapper3(a):
	"""map [0, 1] → [0, 1] using scaled versions of x^p where a controls total area under curve
	"""
	if a == 0:
		return int(x >= 1)

	A = (1 / a - 1)

	return lambda x: x ** A
