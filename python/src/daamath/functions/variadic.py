from numbers import Number, Real
from collections.abc import Iterable
import math, builtins, statistics

# variadic and. unicode : ⋀
from builtins import all

# variadic or. unicode: ⋁
from builtins import any

# variadic add. unicode: ∑
from builtins import sum

# variadic mul. unicode: ∏
from math import prod

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

from statistics import mean as amean, harmonic_mean as hmean, geometric_mean as gmean

# pmean with power = −∞
from builtins import min

# pmean with power = +∞
from builtins import max

def pmean(data: Iterable[Number], *, power: Real = 1) -> Number:
	'power mean AKA generalized mean (p=1: arithmetic, 0: geometric, -1: harmonic)'
	if power == -math.inf:
		return min(data)
	elif power == math.inf:
		return max(data)
	else:
		return (sum(x ** power for x in data) / len(data)) ** (1 / power)


from statistics import median, mode, variance as var, stdev
