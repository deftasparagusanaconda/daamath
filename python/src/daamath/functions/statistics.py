from numbers import Number, Real
from collections.abc import Iterable
import math, builtins, statistics

from statistics import harmonic_mean as mean_n1
from statistics import geometric_mean as mean_0
from statistics import mean as mean_p1
from builtins import min, min as mean_ninf
from builtins import max, max as mean_pinf

def mean(data: Iterable[Number], *, power: Real = 1) -> Number:
	'power mean AKA generalized mean (p=1: arithmetic, 0: geometric, -1: harmonic)'
	if power == -1:
		return mean_n1(data)
	elif power == 0:
		return mean_0(data)
	elif power == 1:
		return mean_p1(data)
	elif power == -math.inf:
		return mean_ninf(data)
	elif power == math.inf:
		return mean_pinf(data)
	else:
		return (sum(x ** power for x in data) / len(data)) ** (1 / power)


from statistics import median, mode, variance as var, stdev
