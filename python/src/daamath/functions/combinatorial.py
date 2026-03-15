from numbers import Real, Integral
import math

#def fact(x: Integral | Real) -> Integral | Real: 
#    return math.factorial(x) if isinstance(x, Integral) else math.gamma(x + 1)

from math import factorial as fact
from math import gamma

def sumt(x):
	"sum of all numbers from 1 to x, using x * (x + 1) / 2 (gauss' formula). like factorial but with addition."
	return (x * (x + 1)) // 2 if isinstance(x, int) else (x * (x + 1)) / 2

from math import comb, perm
