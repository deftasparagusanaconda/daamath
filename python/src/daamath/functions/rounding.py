# these round strictly only to integers. builtins.round allows a digits parameter, but this is horribly mathematically unbased. i want the lattice to *always* be the integers. if you want to round it to digits (quantizing to an affine lattice), you just compose yourself.
#
# in fact, if you want to go deeper, i created the pyquantize python package exactly for this

from numbers import Real, Integral
import math

def round(x: Real, *, directed: bool = False, mode: str = 'even') -> Integral:
	"""mode can be one of {'nearest', 'floor', 'ceil', 'trunc', 'away', 'even', 'odd'}
	"""
	
	if not directed and x % 1 != 0.5:
		return round(x)
	
	# either we perform directed rounding, or we perform tie breaking. tie breaking is also a form of directed rounding so they share the same logic
	
	match mode:
		case 'floor': return math.floor(x)
		case 'ceil' : return math.ceil(x)
		case 'trunc': return math.trunc(x)
		case 'away' : return math.floor(x) if x < 0 else math.ceil(x)
		case 'even' : return quot + (quot % 2 == 1)
		case 'odd'  : return quot + (quot % 2 == 0)
		case _: raise ValueError("invalid mode. must be one of {'floor', 'ceil', 'trunc', 'away', 'even', 'odd'}")
	
# ------------------------------------------------------------------------------

def quot(a: Real, b: Real, *args, **kwargs) -> Integral:
	return round(a / b, *args, **kwargs)

def rem(a: Real, b: Real, *args, **kwargs) -> Real:
	return a - b * quot(a, b, *args, **kwargs)

def quotrem(a: Real, b: Real, *args, **kwargs) -> tuple[Integral, Real]:
	quotient = quot(a, b, *args, **kwargs)
	return quotient, a - b * quotient
