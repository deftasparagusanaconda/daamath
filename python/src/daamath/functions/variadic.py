from numbers import Number, Real
from collections.abc import Iterable
import math, builtins, statistics, functools

# variadic and. unicode : ⋀
from builtins import all as vffft

# variadic or. unicode: ⋁
from builtins import any as vfttt

# variadic add. unicode: ∑
from builtins import sum as vh1c

# variadic mul. unicode: ∏
from math import prod as vh2c

def vparallel(iterable: Iterable[int | float | complex]) -> int | float | complex: 
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

from statistics import mean as mean__p1, harmonic_mean as mean__n1, geometric_mean as mean__0

# pmean with power = −∞
from builtins import min as mean__ninf

# pmean with power = +∞
from builtins import max as mean__pinf

def mean(data: Iterable[Number], *, power: Real = 1) -> Number:
	'power mean AKA generalized mean (p=1: arithmetic, 0: geometric, -1: harmonic)'
	if power == -math.inf:
		return min(data)
	elif power == math.inf:
		return max(data)
	else:
		return (sum(x ** power for x in data) / len(data)) ** (1 / power)

mean__p2 = functools.partial(mean, power = 2)
mean__p3 = functools.partial(mean, power = 3)

#from statistics import median, mode, variance as var, stdev
