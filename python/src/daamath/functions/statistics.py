from numbers import Number, Real
from collections.abc import Iterable
import math, builtins, statistics

from statistics import harmonic_mean as hmean, geometric_mean as gmean
from builtins import min, max

def mean(data: Iterable[Number], *, power: Real = 1) -> Number:
	'power mean AKA generalized mean (p=1: arithmetic, 0: geometric, -1: harmonic)'
	if power == -1:
		return mean_n1(data)
	elif power == 0:
		return mean_0(data)
	elif power == 1:
		return statistics.mean(data)
	elif power == -math.inf:
		return min(data)
	elif power == math.inf:
		return max(data)
	else:
		return (sum(x ** power for x in data) / len(data)) ** (1 / power)


from statistics import median, mode, variance as var, stdev
