# if you want to go deeper, i created the pyquantize python package exactly for this

from numbers import Real, Integral
import math, builtins, functools
from typing import Callable, Literal

def round(x: Real, *, directed: bool = False, mode: Literal['floor', 'ceil', 'trunc', 'away', 'even', 'odd'] = 'even') -> Integral:
	"""round to an integer. mode can be one of {'floor', 'ceil', 'trunc', 'away', 'even', 'odd'}

	parameters
	----------
	x: Real
		the number to round to an integer

	directed: bool, default = False
		if False, the number is rounded to the closest integer
		if True, the number is projected according to mode
	
	mode: Literal['floor', 'ceil', 'trunc', 'away', 'even', 'odd'], default = 'even'
		'floor': towards −∞
		'ceil' : towards +∞
		'trunc': towards ±0
		'away' : away from ±0
		'even' : towards nearest even number
		'odd'  : towards nearest odd number
	
	returns
	-------
	Integral
		x quantized to an integer
	
	notes
	-----
	if you want to define an arbitrary lattice other than the integers, go use the pyquantize module for python
	"""

	if not directed and x % 1 != 0.5:
		return builtins.round(x)
	
	# either we perform directed rounding, or we perform tie breaking. tie breaking is also a form of directed rounding so they share the same logic
	
	match mode:
		case 'floor': return math.floor(x)
		case 'ceil' : return math.ceil(x)
		case 'trunc': return math.trunc(x)	# same as int(x)
		case 'away' : return math.floor(x) if x < 0 else math.ceil(x)
		case 'even' : return math.floor(x * 0.5 + 0.5) * 2	# fma(x, 0.5, 0.5) * 2
		case 'odd'  : return math.floor(x * 0.5) * 2 + 1	# fma(x * 0.5, 2, 1)
		#case 'random_uniform'   
		#case 'random_stochastic'
		case _: raise ValueError("invalid mode. must be one of {'floor', 'ceil', 'trunc', 'away', 'even', 'odd'}")

floor       = functools.partial(round, directed = True , mode = 'floor')
ceil        = functools.partial(round, directed = True , mode = 'ceil' )
trunc       = functools.partial(round, directed = True , mode = 'trunc')
away        = functools.partial(round, directed = True , mode = 'away' )
#even        = functools.partial(round, directed = True , mode = 'even' )
#odd         = functools.partial(round, directed = True , mode = 'odd'  )

# NOTE: 
# you: daa.. why not add even() and odd()?
# me: because we need tie-breaking for them. even(3) has to choose between 2 and 4. thats a tie break. cases like these are handled by pyquantize, if you need more advanced rounding

round_floor = functools.partial(round, directed = False, mode = 'floor')
round_ceil  = functools.partial(round, directed = False, mode = 'ceil' )
round_trunc = functools.partial(round, directed = False, mode = 'trunc')
round_away  = functools.partial(round, directed = False, mode = 'away' )
round_even  = functools.partial(round, directed = False, mode = 'even' )
round_odd   = functools.partial(round, directed = False, mode = 'odd'  )

# ------------------------------------------------------------------------------

def quot(a: Real, b: Real, *, projection: Callable[[Real], Integral] = round) -> Integral:
	'quotient of division'
	return projection(a / b)

def rem(a: Real, b: Real, *, projection: Callable[[Real], Integral] = round) -> Real:
	'remainder of division'
	# fma(projection(a / b), -b, a)
	return a - b * projection(a / b)

def quotrem(a: Real, b: Real, *, projection: Callable[[Real], Integral] = round) -> tuple[Integral, Real]:
	'quotient and remainder of division'
	quotient = projection(a / b)
	return quotient, a - b * quotient

quot_1 = functools.partial(quot, b = 1)
rem_1 = functools.partial(rem, b = 1)
quotrem_1 = functools.partial(quotrem, b = 1)

'''
quot_1_floor = functools.partial(quot, b = 1, projection = floor)
rem_1_floor = functools.partial(rem, b = 1, projection = floor)
quotrem_1_floor = functools.partial(quotrem, b = 1, projection = floor)

quot_1_floor = functools.partial(quot, b = 1, projection = floor)
rem_1_floor = functools.partial(rem, b = 1, projection = floor)
quotrem_1_floor = functools.partial(quotrem, b = 1, projection = floor)
'''
