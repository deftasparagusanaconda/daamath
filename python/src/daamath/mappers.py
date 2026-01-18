# these functions are [0, 1] → [0, 1] that intersect (0, 0) and (1, 1) and have a parameter p that controls their definite integral in x ∈ [0, 1]
# mathematically, they represent a family of functions, and p is which function of the family you choose, and x is the value for which you evaluate the function. each mapper is a function f(x, y) = z where x, y, z ∈ R, x, y ∈ [0, 1]

import math as _math

def mapper1(x, p):
	"""map [0, 1] → [0, 1] using shifted and scaled versions of 1/x where p controls total area under curve

	formula
	-------
	f(x, q) = fma(x, q, x) / fma(x, q, 1) = (x * q + x) / (x * q + 1)
	
	                      1
	where q = q such that ∫ f(x, q) * dx == p
	                      0

	unfortunately, q must be obtained from a transcendental equation. the function performs numerical iteration with (p / (1 - p)) ^ 1.5 - 1 as its first guess

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

	notes
	-----
	iterative optimization isnt made yet. the first guess is used directly for now…
	"""
	if p == 0:
		return int(x >= 1)
	elif p == 1:
		return int(x > 0)
	
	fma = lambda a, b, c: _math.fma(a, b, c) if hasattr(_math, 'fma') else a * b + c
	f = lambda x, r: fma(x, r, x) / fma(x, r, 1)

	s = (p / (1 - p)) ** 1.5 - 1
	
	return f(x, s)

def mapper2(x, p):
	"""map [0, 1] → [0, 1] using scaled versions of b^x where p controls total area under curve

	count = 100
	p_count = 10
	for p in range(1 + p_count):
		print(p / p_count, sum(mapper2(x / count, p/p_count) for x in range(1, 1 + count)) / count)

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
		return int(x > 0)

	#f = lambda x, b: _math.expm1(x * b) / _math.expm1(b)
	#s = 3.6 * _math.tan(_math.pi / 2 - _math.pi * p)


	#f = lambda x, b: (b ** x - 1) / (b - 1)
	f = lambda x, b: _math.expm1(_math.log(b) * x) / (b - 1)
	s = _math.tan(_math.pi / 2 * (1 - p)) ** 4
	return f(x, s)

def mapper3(x, p):
	"""map [0, 1] → [0, 1] using scaled versions of x^a where p controls total area under curve
	"""
	if p == 0:
		return int(x >= 1)

	f = lambda x, a: x ** a
	s = 1 / p - 1
	return f(x, s)

