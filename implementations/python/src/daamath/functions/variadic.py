# these are functions that are either naturally variadic, or come from associative operators
#
# it is not required that they are commutative. an example is concatenation. it is associative but not commutative :) interesting, right??
#
# if the primitive operator has an identity element, its minimum argument count is zero. otherwise, it must receive at least as much elements as the primitive requires.

from numbers import Number, Real
from collections.abc import Iterable
import math, builtins, statistics, functools
from . import logic
from typing import Callable

# this turns any binary operator into a variadic thing
from functools import reduce

# variadic and. unicode : ⋀
#functools.partial(functools.reduce, ffft)
from builtins import all as vffft

# variadic or. unicode: ⋁
#functools.partial(functools.reduce, fttt)
from builtins import any as vfttt

# variadic add. unicode: ∑
#functools.partial(functools.reduce, h1c)
from builtins import sum as vh1c

# variadic mul. unicode: ∏
# functools.partial(functools.reduce, h2c)
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

from statistics import mean as mean__1, harmonic_mean as mean__h1b_0_1, geometric_mean as mean__0

# pmean with power = −∞
from builtins import min as mean__h1b_0_inf

# pmean with power = +∞
from builtins import max as mean__inf

def mean(data: Iterable[Number], *, power: Real = 1) -> Number:
	'power mean AKA generalized mean (p=1: arithmetic, 0: geometric, -1: harmonic)'
	if power == -math.inf:
		return min(data)
	elif power == math.inf:
		return max(data)
	else:
		return (sum(x ** power for x in data) / len(data)) ** (1 / power)

mean__2 = functools.partial(mean, power = 2)
mean__3 = functools.partial(mean, power = 3)

from statistics import median, mode, variance as var, stdev

def fmean(data: Iterable[Number], *, forward: Callable[[Number], Number], inverse: Callable[[Number], Number]) -> Number:
    ...

# variadic xor. oddness check. 1 if odd number of stuff. 0 otherwise 
vfttf = functools.partial(functools.reduce, logic.fttf)

# variadic nxor. evenness check. 1 if even number of stuff. 0 otherwise
vtfft = functools.partial(functools.reduce, logic.tfft)
