# none of these functions should depend on each other

from typing import Literal as _Literal

from operator import add
from operator import sub
from operator import mul
from operator import truediv as div
from operator import pos
from operator import neg
from operator import mod
from operator import floordiv
from operator import mod
from operator import truth, xor, not_, and_, or_, eq as xnor, lt, le, eq, ne, ge, gt, lshift, rshift, call, matmul, concat, is_, is_not
from builtins import pow, round, any, all, len, range, reversed, sorted, divmod, min, max
from math import floor, ceil, trunc as ipart, exp, exp2, log10, log2, log, sqrt, cbrt, comb, perm, factorial as fact, gamma, gcd, lcm
from cmath import phase
from statistics import mean, median, mode, variance as var, stdev

from math import isnan as _isnan
from math import sin, cos, tan, asin, acos, atan, atan2, sinh, cosh, tanh, asinh, acosh, atanh
from math import copysign

def scaler_tan(x:int|float) -> float:
	if x < 0 or x > 1:
		raise ValueError("out of range [0,1]")
	elif x == 0:
		return float('-inf')
	elif x == 0.25:
		return -1.0
	elif x == 0.75:
		return 1.0
	elif x == 1:
		return float('inf')
	else:
		from math import tan, pi
		return tan((x-0.5)*pi)
"""
def ieee_div(a,b):
	if _isnan(a) or _isnan(b):
		return float('nan')

	elif b == 0:
		if copysign(1, b) == 1:
			return float('inf')
		else:
			return float('-inf')
	
	else:
		return a/b
"""

def floordiv(a, b):
	'division rounded to integers towards -∞'
	return a // b

def truncdiv(a, b):
	'division rounded to integers towards ±0'
	raise NotImplementedError('i havent made this yet')

def scaler_sigmoid(x:int|float):
	raise NotImplementedError

def inv(x):
	'y such that x*y = 1, where 1 is the multiplicative identity'
	return 1/x

def square(x):
	'x**2, x*x, x^2, x²'
	return x**2

def cube(x):
	'x**3, x*x*x, x^2, x³'
	return x**3

def fpart(x):
	'the non-integer part of a number'
	return _math.modf(x)[0]

def root(x, base):
	'root of a number in an arbitrary base'
	return x**(1/base)

def ifelse(a,b,c):
	'return b if a else c. in other words, if a then b else c'
	return b if a else c

def abs(*args):
	'return the absolute value of whatever value/abomination you passed'
	return sqrt(sum(arg**2 for arg in args))

# complex -------------------------------

def real(x):
	'get real lmao https://www.youtube.com/watch?v=dQw4w9WgXcQ'
	return x.real

def imag(x):
	'any good complex type should have .real and .imag, right??'
	return x.imag

#import cmath
#phase = cmath.phase

def conj(x):
	'return the conjugate of a complex'
	return x.conjugate()

#def to_polar(x):
#	'a complex number from cartesian to polar form'
#	return 

#def to_cartesian(x):
#	'a complex number from polar to cartesian form'

# ---------------------------------------------

def piecewise(*args):
	'variadic([cond1, val1], [cond2, val2], ....)'
	raise NotImplementedError

def summation(*args):
	'variadic summation'
	return sum(args)

def product(*args):
	'variadic multiplication'
	return math.prod(args)

def sigma_summation(expr, var, lower, upper):
	'quadric Σ(expr, var, lower, upper)'
	return sum(expr(var=val) for value in range(lower, upper))

def pi_product(expr, var, lower, upper):
	'quadric ∏(expr, var, lower, upper)'
	return _math.prod(expr(var=value) for value in range(lower, upper))

# matrix
def det(a):
	'unary |mat|'
	raise NotImplementedError

def transpose(a):
	'unary mat\''
	raise NotImplementedError

def dot_product(a, b):
	'binary vector A • vector B'
	raise NotImplementedError

def cross_product(a, b):
	'binary vector A × vector B'
	raise NotImplementedError

# infinitesimal --------------------------------

def limit():
	'quadric (func var, val, direction)'
	raise NotImplementedError

def definite_integral():
	'quadric integral a to b, f(x)dx(func(var, lower, upper))'
	raise NotImplementedError

def indefinite_integral():
	'binary ∫f(x)dx(func, var)'
	raise NotImplementedError

def derivative():
	'binary (func, var)'
	raise NotImplementedError

def partial_derivative():
	'variadic(func, var1, var2, ..., varN)'
	raise NotImplementedError

def clamp(x, low=0, high=1):
	'return x but constrained within [low, high]'
	return min(max(x,low),high)

def lerp(x, low, high):
	'linear interpolation. maps [0,1] to [low,high]. allows 1<x<0'
	return low + x*(high-low)

def unlerp(x, low, high):
	'inverse of linear interpolation. maps [low,high] to [0,1] allows high<x<low'
	return (x-low)/(high-low)

def map(x, a, b, c, d):
	'maps [a,b] to [c,d]'
	return lerp(unlerp(x,a,b),c,d)

def sumt(x):
	'return sum of all numbers from 1 to x. like factorial but with addition'
	if isinstance(x, int): 
		return (x*(x+1))//2
	return (x*(x+1))/2

def sgn(a):
	'return -1 if negative, 0 if zero, 1 if positive. also known as signum'
	return a if _isnan(a) else (a>0) - (a<0)

# boolean	  ---------------------------

def nand(a,b):
	'return not(a and b) AKA ¬(a∧b) AKA negation(conjunction(a,b))'
	return not(a and b)

def nor(a, b):
	'return not(a or b) AKA ¬(a∨b) AKA negation(disjunction(a,b))'
	return not(a or b)

def imp(a, b):
	'return not a or b AKA a->b AKA ¬a∨b AKA disjunction(negation(a),b)'
	return not a or b

def con(a, b):
	'return a or not b AKA b->a AKA a∨¬b AKA disjunction(a,negation,b)'
	return a or not b

def nimp(a, b):
	'return a and not b AKA ¬(a->b) AKA a∧¬b AKA negation(implication(a,b))'
	return a and not b

def ncon(a, b):
	'return not a and b AKA ¬(a->b) AKA ¬a∧b AKA negation(converse_implication(a,b))'
	return not a and b

# trigonometric -----------------------------------------------

def cot(x):
	'trigonometric cotangent (using cmath)'
	return 1/tan(x)

def sec(x):
	'trigonometric secant (using cmath)'
	return 1/cos(x)

def csc(x):
	'trigonometric cosecant (using cmath)'
	return 1/sin(x)

def acot(x):
	'inverse trigonometric cotangent (using cmath)'
	return atan(1/x)

def asec(x):
	'inverse trigonometric secant (using cmath)'
	return acos(1/x)

def acsc(x):
	'inverse trigonometric cosecant (using cmath)'
	return asin(1/x)

# hyperbolic -----------------------

def coth(x):
	'hyperbolic cotangent (using cmath)'
	return 1/tanh(x)

def sech(x):
	'hyperbolic secant (using cmath)'
	return 1/cosh(x)

def csch(x):
	'hyperbolic cosecant (using cmath)'
	return 1/sinh(x)

def acoth(x):
	'inverse hyperbolic cotangent (using cmath)'
	return atanh(1/x)

def asech(x):
	'inverse hyperbolic secant (using cmath)'
	return acosh(1/x)

def acsch(x):
	'inverse hyperbolic cosecant (using cmath)'
	return asinh(1/x)

# statistical --------------

def pmean(data, p):
	'power mean AKA generalized mean (p=1: arithmetic, 0: geometric, -1: harmonic)'
	if p == 1:
		return mean(data)
	if p == 0:
		return exp(sum(log(x) for x in data)/len(data))
	return (sum(x**p for x in data)/len(data)) ** (1/p)

def rms(data):
	'root mean square'
	return sqrt(sum(datum**2 for datum in data)/len(data))

#def aad(data, centre=_Literal['mean','median','mode'], measure=_):
#	'average absolute deviation. '
#	match centre
#	return sum(abs(datum-mean_value) for datum in data)/len(data)

#def pdev(data, p):
#	'power mean of absolute deviation'
#	mean_value = mean(data)


# bitwise -----------------------
"""
'bittruth': lambda a: a,
'bitnot'  : _operator.invert,	  # 10
'bitand'  : _operator.and_,		# 0001
'bitor'   : _operator.or_,		 # 0111
'bitnand' : _nand,				 # 1110
'bitnor'  : _nor,				  # 1000
'bitxor'  : _operator.xor,		 # 0110
'bitxnor' : _operator.eq,		  # 1001
'bitimp'  : _implication,		  # 1101
'bitcon'  : _converse_implication, # 1011
'bitnimp' : _nimp,				 # 0010
'bitncon' : _ncon,				 # 0100
"""
"""
# "why is there a '_' everywhere?!?"
# because this file is directly exposed in the module's namespace, and we want only the operator_dicts to be visible; not anything else

#from .miscellaneous.dot_dict import DotDict as _DotDict
import math as _math
import cmath as _cmath
import operator as _operator
import numbers as _numbers
import builtins as _builtins
import statistics as _statistics

def _generalized_mean(p, *args):
	'returns the power mean for given p (first argument) (p=1: arithmetic, 0: geometric, -1: harmonic)'
	if p == 0:
		return _math.exp(sum(_math.log(x) for x in args)/len(args))
	return (sum(x**p for x in args)/len(args)) ** (1/p)

def _mean(*args):
	'arithmetic mean'
	return _statistics.mean(args)

def _median(*args):
	return _statistics.median(args)

def _mode(*args):
	return _statistics.mode(args)

def _reciprocal(x):
	'y such that x*y = 1, where 1 is the multiplicative identity'
	return 1/x

def _root(x, base):
	'root of a number in an arbitrary base'
	return x**(1/base)

def _square(x):
	'x**2, x*x, x^2, x²'
	return x**2

def _cube(x):
	'x**3, x*x*x, x^2, x³'
	return x**3

def _fractional_part(x):
	'the non-integer part of a number'
	return _math.modf(x)[0]

def _ifelse(a,b,c):
	'return b if a is true, otherwise return c'
	return b if a else c

def _cot(x):
	'trigonometric cotangent'
	return 1/_math.tan(x)

def _sec(x):
	'trigonometric secant'
	return 1/_math.cos(x)

def _csc(x):
	'trigonometric cosecant'
	return 1/_math.sin(x)

def _acot(x):
	'inverse trigonometric cotangent'
	return _math.atan(1/x)

def _asec(x):
	'inverse trigonometric secant'
	return _math.acos(1/x)

def _acsc(x):
	'inverse trigonometric cosecant'
	return _math.asin(1/x)

def _coth(x):
	'hyperbolic cotangent'
	return 1/_math.tanh(x)

def _sech(x):
	'hyperbolic secant'
	return 1/_math.cosh(x)

def _csch(x):
	'hyperbolic cosecant'
	return 1/_math.sinh(x)

def _acoth(x):
	'inverse hyperbolic cotangent'
	return _math.atanh(1/x)

def _asech(x):
	'inverse hyperbolic secant'
	return _math.acosh(1/x)

def _acsch(x):
	'inverse hyperbolic cosecant'
	return _math.asinh(1/x)

def _get_real(x):
	'get real lmao https://www.youtube.com/watch?v=dQw4w9WgXcQ'
	return x.real

def _get_imag(x):
	'any good complex type should have .real and .imag, right??'
	return x.imag

def _call_conjugate(x):
	'returns x.conjugate()'
	return x.conjugate()

def _piecewise(*args):
	'variadic([cond1, val1], [cond2, val2], ....)'
	raise NotImplementedError

def _summation(*args):
	'variadic summation'
	return sum(args)

def _product(*args):
	'variadic multiplication'
	return math.prod(args)

def _sigma_summation(expr, var, lower, upper):
	'quadric Σ(expr, var, lower, upper)'
	return sum(expr(var=val) for value in range(lower, upper))

def _pi_product(expr, var, lower, upper):
	'quadric ∏(expr, var, lower, upper)'
	return _math.prod(expr(var=value) for value in range(lower, upper))

# matrix
def _determinant(a):
	'unary |mat|'
	raise NotImplementedError

def _transpose(a):
	'unary mat\''
	raise NotImplementedError

def _dot_product(a, b):
	'binary vector A • vector B'
	raise NotImplementedError

def _cross_product(a, b):
	'binary vector A × vector B'
	raise NotImplementedError

# infinitesimal
def _limit():
	'quadric (func var, val, direction)'
	raise NotImplementedError

def _definite_integral():
	'quadric integral a to b, f(x)dx(func(var, lower, upper))'
	raise NotImplementedError

def _indefinite_integral():
	'binary ∫f(x)dx(func, var)'
	raise NotImplementedError

def _derivative():
	'binary (func, var)'
	raise NotImplementedError

def _partial_derivative():
	'variadic(func, var1, var2, ..., varN)'
	raise NotImplementedError

def _clamp(x, low, high):
	'return x but constrained within [low, high]'
	return min(max(x,low),high)

def _lerp(x, low, high):
	'linear interpolation. allows 1<x<0'
	return low + x*(high-low)

def _unlerp(x, low, high):
	'inverse of linear interpolation. allows high<x<low'
	return (x-low)/(high-low)

def _sumtorial(x):
	'return sum of all numbers from 1 to x. like factorial but with addition'
	return sum(range(1, a+1))

def _signum(a):
	'return -1 if negative, 0 if zero, 1 if positive'
	return (a>0) - (a<0)

def _nand(a,b):
	'return not(a and b) AKA ¬(a∧b) AKA negation(conjunction(a,b))'
	return not(a and b)

def _nor(a, b):
	'return not(a or b) AKA ¬(a∨b) AKA negation(disjunction(a,b))'
	return not(a or b)

def _implication(a, b):
	'return not a or b AKA a->b AKA ¬a∨b AKA disjunction(negation(a),b)'
	return not a or b

def _converse_implication(a, b):
	'return a or not b AKA b->a AKA a∨¬b AKA disjunction(a,negation,b)'
	return a or not b

def _nimp(a, b):
	'return a and not b AKA ¬(a->b) AKA a∧¬b AKA negation(implication(a,b))'
	return a and not b

def _ncon(a, b):
	'return not a and b AKA ¬(a->b) AKA ¬a∧b AKA negation(converse_implication(a,b))'
	return not a and b

def _cot_cmath(x):
	'trigonometric cotangent (using cmath)'
	return 1/_cmath.tan(x)

def _sec_cmath(x):
	'trigonometric secant (using cmath)'
	return 1/_cmath.cos(x)

def _csc_cmath(x):
	'trigonometric cosecant (using cmath)'
	return 1/_cmath.sin(x)

def _acot_cmath(x):
	'inverse trigonometric cotangent (using cmath)'
	return _cmath.atan(1/x)

def _asec_cmath(x):
	'inverse trigonometric secant (using cmath)'
	return _cmath.acos(1/x)

def _acsc_cmath(x):
	'inverse trigonometric cosecant (using cmath)'
	return _cmath.asin(1/x)

def _coth_cmath(x):
	'hyperbolic cotangent (using cmath)'
	return 1/_cmath.tanh(x)

def _sech_cmath(x):
	'hyperbolic secant (using cmath)'
	return 1/_cmath.cosh(x)

def _csch_cmath(x):
	'hyperbolic cosecant (using cmath)'
	return 1/_cmath.sinh(x)

def _acoth_cmath(x):
	'inverse hyperbolic cotangent (using cmath)'
	return _cmath.atanh(1/x)

def _asech_cmath(x):
	'inverse hyperbolic secant (using cmath)'
	return _cmath.acosh(1/x)

def _acsch_cmath(x):
	'inverse hyperbolic cosecant (using cmath)'
	return _cmath.asinh(1/x)

def _dist(*args):
	'euclidean distance in n dimensions'
	from math import sqrt
	return sqrt(sum(arg**2 for arg in args))

#default = _DotDict()

default = {
# arithmetic
'add'	 : _operator.add,
'sub'	 : _operator.sub,
'mul'	 : _operator.mul,
'div'	 : _operator.truediv,

# numeric
'pos'	 : _operator.pos,	  # unary plus, positive
'neg'	 : _operator.neg,	# unary minus, negative, additive inverse
'mod'	 : _operator.mod,
'floordiv': _operator.floordiv,
'abs'	 : _operator.abs,
'inv'	 : _reciprocal,	  # multiplicative inverse
'square'  : _square,
'cube'	: _cube,
'pow'	 : _builtins.pow,
'floor'   : _math.floor,
'round'   : _builtins.round,
'ceil'	: _math.ceil,
'ipart'   : _math.trunc,
'fpart'   : _fractional_part,
'exp'	 : _math.exp,
'exp2'	: _math.exp2,
'log10'   : _math.log10,
'log2'	: _math.log2,
'log'	 : _math.log,
'sqrt'	: _math.sqrt,
'cbrt'	: _math.cbrt,
'root'	: _root,

# trigonometric
'sin'	 : _math.sin,
'cos'	 : _math.cos,
'tan'	 : _math.tan,
'cot'	 : _cot,
'sec'	 : _sec,
'csc'	 : _csc,
'asin'	: _math.asin,
'acos'	: _math.acos,
'atan'	: _math.atan,
'acot'	: _acot,
'asec'	: _asec,
'acsc'	: _acsc,

# hyperbolic
'sinh'	: _math.sinh,
'cosh'	: _math.cosh,
'tanh'	: _math.tanh,
'coth'	: _coth,
'sech'	: _sech,
'csch'	: _csch,
'asinh'   : _math.asinh,
'acosh'   : _math.acosh,
'atanh'   : _math.atanh,
'acoth'   : _acoth,
'asech'   : _asech,
'acsch'   : _acsch,

# left out due to obscurity. also probably mostly wrong :P
#'versin'	: lambda a: 1 - math.cos(a)
#'coversin'  : lambda a: 1 - math.sin(a)
#'haversin'  : lambda a: 0.5 - math.cos(a)/2
#'hacoversin': lambda a: 0.5 - math.sin(a)/2
#'exsec'	 : lambda a: 1/math.cos(a) - 1
#'excsc'	 : lambda a: 1/math.sin(a) - 1
#'chord'	 : lambda a: 2 * math.sin(a/2)
#'vercos'	: lambda a: 1 + math.cos(a)
#'covercos'  : lambda a: 1 + math.sin(a)
#'havercos'  : lambda a: 0.5 + math.cos(a)/2
#'hacovercos': lambda a: 0.5 + math.sin(a)/2

# complex
'real'	: _get_real, # get real lmao
'imag'	: _get_imag,
'phase'   : _cmath.phase,
'conj'	: _call_conjugate,

# boolean
'truth'   : _operator.truth,	   # 01
'not'	 : _operator.not_,		# 10
'and'	 : _operator.and_,		# 0001
'nimp'	: _nimp,				 # 0010
'ncon'	: _ncon,				 # 0100
'xor'	 : _operator.xor,		 # 0110
'or'	  : _operator.or_,		 # 0111
'nor'	 : _nor,				  # 1000
'xnor'	: _operator.eq,		  # 1001
'con'	 : _converse_implication, # 1011
'imp'	 : _implication,		  # 1101
'nand'	: _nand,				 # 1110

# comparative
'lt'	  : _operator.lt,
'le'	  : _operator.le,
'eq'	  : _operator.eq,
'ne'	  : _operator.ne,
'ge'	  : _operator.ge,
'gt'	  : _operator.gt,

# statistical
'mean'	: _mean,
'median'  : _median,
'mode'	: _mode,
'pmean'   : _generalized_mean,

# combinatorial
'comb'	: _math.comb,
'perm'	: _math.perm,

# hello there! lol

# bitwise
'bittruth': lambda a: a,
'bitnot'  : _operator.invert,	  # 10
'bitand'  : _operator.and_,		# 0001
'bitor'   : _operator.or_,		 # 0111
'bitnand' : _nand,				 # 1110
'bitnor'  : _nor,				  # 1000
'bitxor'  : _operator.xor,		 # 0110
'bitxnor' : _operator.eq,		  # 1001
'bitimp'  : _implication,		  # 1101
'bitcon'  : _converse_implication, # 1011
'bitnimp' : _nimp,				 # 0010
'bitncon' : _ncon,				 # 0100
'lshift'  : _operator.lshift,
'rshift'  : _operator.rshift,

# miscellaneous
'dist'	: _dist,
'any'	 : _builtins.any,
'all'	 : _builtins.all,
'len'	 : _builtins.len,
'range'   : _builtins.range,
'reversed': _builtins.reversed,
'sorted'  : _builtins.sorted,
'divmod'  : _builtins.divmod,
'call'	: _operator.call,
'matmul'  : _operator.matmul,
'concat'  : _operator.concat,
'sign'	: _signum,
'ifelse'  : _ifelse,
'fact'	: _math.factorial,
'gamma'   : _math.gamma,
'sumt'	: _sumtorial,
'gcd'	 : _math.gcd,
'lcm'	 : _math.lcm,
'clamp'   : _clamp,
'lerp'	: _lerp,
'unlerp'  : _unlerp,
'min'	 : _builtins.min,
'max'	 : _builtins.max,
'is'	  : _operator.is_,
'isnot'   : _operator.is_not,
#'erf'	 : _math.erf
#'erfc'	: _math.erfc
#'in'	  : 
#'notin'   : 
}


complex = default.copy()

complex.update({
# trigonometric
'sin'   : _cmath.sin,
'cos'   : _cmath.cos,
'tan'   : _cmath.tan,
'cot'   : _cot_cmath,
'sec'   : _sec_cmath,
'csc'   : _csc_cmath,
'asin'  : _cmath.asin,
'acos'  : _cmath.acos,
'atan'  : _cmath.atan,
'acot'  : _acot_cmath,
'asec'  : _asec_cmath,
'acsc'  : _acsc_cmath,

# hyperbolic
'sinh'  : _cmath.sinh,
'cosh'  : _cmath.cosh,
'tanh'  : _cmath.tanh,
'coth'  : _coth_cmath,
'sech'  : _sech_cmath,
'csch'  : _csch_cmath,
'asinh' : _cmath.asinh,
'acosh' : _cmath.acosh,
'atanh' : _cmath.atanh,
'acoth' : _acoth_cmath,
'asech' : _asech_cmath,
'acsch' : _acsch_cmath
})
"""

def in_open_interval(x:int|float, a:int|float, b:int|float):
	'x ∈ (a,b) | a < x < b'
	return a < x < b

def in_closed_interval(x:int|float, a:int|float, b:int|float):
	'x ∈ [a,b] | a <= x <= b'
	return a <= x <= b

def in_left_open_interval(x:int|float, a:int|float, b:int|float):
	'x ∈ (a,b] | a < x <= b'
	return a < x <= b

def in_right_open_interval(x:int|float, a:int|float, b:int|float):
	'x ∈ [a,b) | a <= x < b'
	return a <= x < b

from operator import xor, not_, and_, or_, eq as xnor

# constants --------------------------------------------------------------------

OMEGA		  = 0.56714329040978387299
GAMMA		  = 0.57721566490153286060
LN_2		   = 0.6931471805599453
CATALAN		= 0.9159655941772190150
ZETA_3		 = 1.20205690315959428539
SQRT_2		 = 1.4142135623730951
PHI			= 1.61803398874989484820
SQRT_3		 = 1.7320508075688772
LN_10		  = 2.302585092994046
E			  = 2.71828182845904523536
PI			 = 3.14159265358979323846
TAU			= 6.28318530717958647692
POS_INF		= float('inf')
NEG_INF		= float('-inf')
POS_ZERO	   = 0.0
NEG_ZERO	   = -0.0
POS_QNAN	   = float('nan')
NEG_QNAN	   = float('-nan')
#POS_SNAN	   = 
#NEG_SNAN	   = 
FLT_MAX		= (2 - 2**-23) * 2**127
FLT_MIN		= 2**-126
FLT_TRUE_MIN   = 2**-149
DBL_MAX		= (2 - 2**-52) * 2**1023
DBL_MIN		= 2**-1022
DBL_TRUE_MIN   = 2**-1074

# characters -------------------------------------------------------------------

LATIN_UPPER								= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LATIN_UPPER_SUPERSCRIPT					= 'ᴬᴮꟲᴰᴱꟳᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾꟴᴿ ᵀᵁⱽᵂ   '
LATIN_UPPER_SUPERSCRIPT_SMALL			  = ' 𐞄	𐞒𐞖ᶦ 𞀹ᶫ𞀻ᶰ   𐞪 𞁀ᶸ   𐞲 '
LATIN_LOWER_SUPERSCRIPT					= 'ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ𐞥ʳˢᵗᵘᵛʷˣʸᶻ'
LATIN_LOWER_SUBSCRIPT					  = 'ₐ 𞁞 ₑ  ₕᵢⱼₖₗₘₙₒₚ ᵣₛₜᵤᵥ ₓ  '
LATIN_LOWER								= 'abcdefghijklmnopqrstuvwxyz'
LATIN_BOLD_UPPER						   = '𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙'
LATIN_BOLD_LOWER						   = '𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳'
LATIN_ITALIC_UPPER						 = '𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍'
LATIN_ITALIC_LOWER						 = '𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧'
LATIN_BOLD_ITALIC_UPPER					= '𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁'
LATIN_BOLD_ITALIC_LOWER					= '𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛'
LATIN_SCRIPT_UPPER						 = '𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵'
LATIN_SCRIPT_LOWER						 = '𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏'
LATIN_BOLD_SCRIPT_UPPER					= '𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩'
LATIN_BOLD_SCRIPT_LOWER					= '𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃'
LATIN_FRAKTUR_UPPER						= '𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ'
LATIN_FRAKTUR_LOWER						= '𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷'
LATIN_FRAKTUR_BOLD_UPPER				   = '𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅'
LATIN_FRAKTUR_BOLD_LOWER				   = '𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟'
LATIN_SANS_SERIF_UPPER					 = '𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹'
LATIN_SANS_SERIF_LOWER					 = '𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓'
LATIN_SANS_SERIF_BOLD_UPPER				= '𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭'
LATIN_SANS_SERIF_BOLD_LOWER				= '𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇'
LATIN_SANS_SERIF_ITALIC_UPPER			  = '𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡'
LATIN_SANS_SERIF_ITALIC_LOWER			  = '𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻'
LATIN_SANS_SERIF_BOLD_ITALIC_UPPER		 = '𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕'
LATIN_SANS_SERIF_BOLD_ITALIC_LOWER		 = '𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯'
LATIN_MONOSPACE_UPPER					  = '𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉'
LATIN_MONOSPACE_LOWER					  = '𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣'
LATIN_DOUBLE_STRUCK_UPPER				  = '𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ'
LATIN_DOUBLE_STRUCK_LOWER				  = '𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫'
LATIN_DOUBLE_STRUCK_ITALIC_UPPER		   = '   ⅅ					  '
LATIN_DOUBLE_STRUCK_ITALIC_LOWER		   = '   ⅆⅇ   ⅈⅉ				'
GREEK_UPPER								= 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩϜϺͶϷͰϘͲͿϚ'
GREEK_UPPER_VARIANT						= '	   ϴ					 ϞϠ  '
GREEK_LOWER								= 'αβγδεζηθικλμνξοπρστυφχψωϝϻͷϸͱϙͳϳϛ'
GREEK_LOWER_VARIANT						= ' ϐ  ϵ  ϑ ϰ	 ϖϱς  ϕ		ϟϡ  '
GREEK_LOWER_SUPERSCRIPT					= ' ᵝᵞᵟᵋ  ᶿᶥ		   ᵠᵡ		   '
GREEK_LOWER_SUBSCRIPT					  = ' ᵦᵧ			 ᵨ   ᵩᵪ		   '
GREEK_BOLD_UPPER						   = '𝚨𝚩𝚪𝚫𝚬𝚭𝚮𝚯𝚰𝚱𝚲𝚳𝚴𝚵𝚶𝚷𝚸𝚺𝚻𝚼𝚽𝚾𝚿𝛀𝟊		'
GREEK_BOLD_UPPER_VARIANT				   = '	   𝚹						 '
GREEK_BOLD_LOWER						   = '𝛂𝛃𝛄𝛅𝛆𝛇𝛈𝛉𝛊𝛋𝛌𝛍𝛎𝛏𝛐𝛑𝛒𝛔𝛕𝛖𝛗𝛘𝛙𝛚𝟋		'
GREEK_BOLD_LOWER_VARIANT				   = '	𝛜  𝛝 𝛞	 𝛡𝛠𝛓  𝛟			'
GREEK_ITALIC_UPPER						 = '𝛢𝛣𝛤𝛥𝛦𝛧𝛨𝛩𝛪𝛫𝛬𝛭𝛮𝛯𝛰𝛱𝛲𝛴𝛵𝛶𝛷𝛸𝛹𝛺		 '
GREEK_ITALIC_UPPER_VARIANT				 = '	   𝛳						 '
GREEK_ITALIC_LOWER						 = '𝛼𝛽𝛾𝛿𝜀𝜁𝜂𝜃𝜄𝜅𝜆𝜇𝜈𝜉𝜊𝜋𝜌𝜎𝜏𝜐𝜑𝜒𝜓𝜔		 '
GREEK_ITALIC_LOWER_VARIANT				 = '	𝜖  𝜗 𝜘	 𝜛𝜚𝜍  𝜙			'
GREEK_BOLD_ITALIC_UPPER					= '𝜜𝜝𝜞𝜟𝜠𝜡𝜢𝜣𝜤𝜥𝜦𝜧𝜨𝜩𝜪𝜫𝜬𝜮𝜯𝜰𝜱𝜲𝜳𝜴		 '
GREEK_BOLD_ITALIC_UPPER_VARIANT			= '	   𝜭						 '
GREEK_BOLD_ITALIC_LOWER					= '𝜶𝜷𝜸𝜹𝜺𝜻𝜼𝜽𝜾𝜿𝝀𝝁𝝂𝝃𝝄𝝅𝝆𝝈𝝉𝝊𝝋𝝌𝝍𝝎		 '
GREEK_BOLD_ITALIC_LOWER_VARIANT			= '	𝝐  𝝑 𝝒	 𝝕𝝔𝝇  𝝓			'
GREEK_SANS_SERIF_BOLD_UPPER				= '𝝖𝝗𝝘𝝙𝝚𝝛𝝜𝝝𝝞𝝟𝝠𝝡𝝢𝝣𝝤𝝥𝝦𝝨𝝩𝝪𝝫𝝬𝝭𝝮		 '
GREEK_SANS_SERIF_BOLD_UPPER_VARIANT		= '	   𝝧						 '
GREEK_SANS_SERIF_BOLD_LOWER				= '𝝰𝝱𝝲𝝳𝝴𝝵𝝶𝝷𝝸𝝹𝝺𝝻𝝼𝝽𝝾𝝿𝞀𝞂𝞃𝞄𝞅𝞆𝞇𝞈		 '
GREEK_SANS_SERIF_BOLD_LOWER_VARIANT		= '	𝞊  𝞋 𝞌	 𝞏𝞎𝞁  𝞍			'
GREEK_SANS_SERIF_BOLD_ITALIC_UPPER		 = '𝞐𝞑𝞒𝞓𝞔𝞕𝞖𝞗𝞘𝞙𝞚𝞛𝞜𝞝𝞞𝞟𝞠𝞢𝞣𝞤𝞥𝞦𝞧𝞨		 '
GREEK_SANS_SERIF_BOLD_ITALIC_UPPER_VARIANT = '	   𝞡						 '
GREEK_SANS_SERIF_BOLD_ITALIC_LOWER		 = '𝞪𝞫𝞬𝞭𝞮𝞯𝞰𝞱𝞲𝞳𝞴𝞵𝞶𝞷𝞸𝞹𝞺𝞼𝞽𝞾𝞿𝟀𝟁𝟂		 '
GREEK_SANS_SERIF_BOLD_ITALIC_LOWER_VARIANT = '	𝟄  𝟅 𝟆	 𝟉𝟈𝞻  𝟇			'
GREEK_DOUBLE_STRUCK_UPPER				  = '  ℾ			ℿ ⅀			   '
GREEK_DOUBLE_STRUCK_LOWER				  = '  ℽ			ℼ				 '
HEBREW									 = 'ℵℶℷℸ'
DIGIT									  = '0123456789↊↋'
DIGIT_SUPERSCRIPT						  = '⁰¹²³⁴⁵⁶⁷⁸⁹  '
DIGIT_SUBSCRIPT							= '₀₁₂₃₄₅₆₇₈₉⏨ '
DIGIT_BOLD								 = '𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗  '
DIGIT_DOUBLE_STRUCK						= '𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡  '
DIGIT_SANS_SERIF						   = '𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫  '
DIGIT_SANS_SERIF_BOLD					  = '𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵  '
DIGIT_MONOSPACE							= '𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿  '
ROMAN_NUMERAL_UPPER						= ' ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫⅬⅭⅮⅯ'
ROMAN_NUMERAL_LOWER						= ' ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻⅼⅽⅾⅿ'
COUNTING_ROD_VERTICAL					  = '〇𝍩𝍪𝍫𝍬𝍭𝍮𝍯𝍰𝍱'
COUNTING_ROD_HORIZONTAL					= '〇𝍠𝍡𝍢𝍣𝍤𝍥𝍦𝍧𝍨'
COUNTING_ROD_NEGATIVE					  = '\u20E5'
TALLY_MARK								 = ' 𝍷   𝍸'
TALLY_MARK_IDEOGRAPHIC					 = ' 𝍲𝍳𝍴𝍵𝍶'
RECIPROCAL								 = '⅟'
FRACTION_0_BY							  = '   ↉	   '
FRACTION_1_BY							  = '  ½⅓¼⅕⅙⅐⅛⅑⅒'
FRACTION_2_BY							  = '   ⅔ ⅖	 '
FRACTION_3_BY							  = '	¾⅗  ⅜  '
FRACTION_4_BY							  = '	 ⅘	 '
FRACTION_5_BY							  = '	  ⅚ ⅝  '
FRACTION_7_BY							  = '		⅞  '
INCREMENT								  = '∆'
NABLA									  = '∇'
NABLA_BOLD								 = '𝛁'
NABLA_ITALIC							   = '𝛻'
NABLA_BOLD_ITALIC						  = '𝜵'
NABLA_SANS_SERIF_BOLD					  = '𝝯'
NABLA_SANS_SERIF_BOLD_ITALIC			   = '𝞩'
PARTIAL									= '∂'
PARTIAL_BOLD							   = '𝛛'
PARTIAL_ITALIC							 = '𝜕'
PARTIAL_BOLD_ITALIC						= '𝝏'
PARTIAL_SANS_SERIF_BOLD					= '𝞉'
PARTIAL_SANS_SERIF_BOLD_ITALIC			 = '𝟃'
PLUS_SUPERSCRIPT						   = '⁺'
PLUS_SUBSCRIPT							 = '₊'
MINUS_SUPERSCRIPT						  = '⁻'
MINUS_SUBSCRIPT							= '₋'
EQUAL_SUPERSCRIPT						  = '⁼'
EQUAL_SUBSCRIPT							= '₌'
PARENTHESIS_SUPERSCRIPT					= '⁽⁾'
PARENTHESIS_SUBSCRIPT					  = '₍₎'
CEIL									   = '⌈⌉'
FLOOR									  = '⌊⌋'
PARENTHESIS								= '()⏜⏝'
SQUARE_BRACKET							 = '[]⎴⎵⎶'
CURLY_BRACKET							  = '{}⏞⏟'
ANGLE_BRACKET							  = '⟨⟩'
DOUBLE_ANGLE_BRACKET					   = '⟪⟫'
CURVED_ANGLE_BRACKET					   = '⧼⧽'
GUILLEMET								  = '‹›'
DOUBLE_GUILLEMET						   = '«»'
LESS_THAN								  = '<'
NOT_LESS_THAN							  = '≮'
GREATER_THAN							   = '>'
NOT_GREATER_THAN						   = '≯'
LESS_THAN_OR_EQUAL						 = '≤'
NOT_LESS_THAN_NOR_EQUAL					= '≰'
GREATER_THAN_OR_EQUAL					  = '≥'
NOT_GREATER_THAN_NOR_EQUAL				 = '≱'
MUCH_LESS_THAN							 = '≪'
MUCH_GREATER_THAN						  = '≫'
EQUAL									  = '='
NOT_EQUAL								  = '≠'
ALMOST_EQUAL							   = '≈'
NOT_ALMOST_EQUAL						   = '≉'
IDENTICAL								  = '≡'
NOT_IDENTICAL							  = '≢'
PROPORTIONAL							   = '∝'
INFINITY								   = '∞'
SQUARE_ROOT								= '√'
CUBE_ROOT								  = '∛'
FOURTH_ROOT								= '∜'
THEREFORE								  = '∴'
BECAUSE									= '∵'
INTEGRAL								   = '∫'
DOUBLE_INTEGRAL							= '∬'
TRIPLE_INTEGRAL							= '∭'
QUADRUPLE_INTEGRAL						 = '⨌'
ANGLE									  = '∠'
RATIO									  = '∶'
PROPORTION								 = '∷'
PLUS									   = '+'
MINUS									  = '−'
PLUS_MINUS								 = '±'
MINUS_PLUS								 = '∓'
CIRCLED_PLUS							   = '⊕'
CIRCLED_MINUS							  = '⊖'
CIRCLED_TIMES							  = '⊗'
CIRCLED_DIVISION_SLASH					 = '⊘'
CIRCLED_DIVISION_SIGN					  = '⨸'
CIRCLED_DOT_OPERATOR					   = '⊙'
CIRCLED_EQUAL							  = '⊜'
SQUARED_PLUS							   = '⊠'
SQUARED_MINUS							  = '⊟'
SQUARED_TIMES							  = '⊞'
SQUARED_DOT_OPERATOR					   = '⊡'
TIMES									  = '×'
DIVISION_SLASH							 = '∕'
DIVISION_SIGN							  = '÷'
FRACTION								   = '⁄'
TILDE_OPERATOR							 = '∼'
DOT_OPERATOR							   = '⋅'
CROSS_PRODUCT							  = '⨯'
INTERSECTION							   = '∩'
UNION									  = '∪'
ELEMENT_OF								 = '∈'
ELEMENT_OF_SMALL						   = '∊'
NOT_ELEMENT_OF							 = '∉'
CONTAINS								   = '∋'
CONTAINS_SMALL							 = '∍'
NOT_CONTAINS							   = '∌'
SUBSET									 = '⊂'
SUPERSET								   = '⊃'
PROPER_SUBSET							  = '⊆'
PROPER_SUPERSET							= '⊇'
NOT_SUBSET								 = '⊄'
NOT_SUPERSET							   = '⊅'
DOWN_TACK								  = '⊤'
UP_TACK									= '⊥'
LEFT_TACK								  = '⊣'
RIGHT_TACK								 = '⊢'
DIVIDES									= '∣'
NOT_DIVIDES								= '∤'
PARALLEL								   = '∥'
PERPENDICULAR							  = '⟂'
NOT										= '¬'
AND										= '∧'
OR										 = '∨'
NAND									   = '⊼'
NOR										= '⊽'
XOR										= '⊻'
BIG_PARENTHESIS							= '⎛⎜⎝⎞⎟⎠'
BIG_SQUARE_BRACKET						 = '⎡⎢⎣⎤⎥⎦'
BIG_CURLY_BRACKET						  = '⎧⎨⎩⎪⎫⎬⎭⎰⎱'
BIG_INTEGRAL							   = '⌠⎮⌡'
BIG_BIG_SIGMA							  = '⎲⎳'
BIG_DOWN_TACK							  = '⟙'
BIG_UP_TACK								= '⟘'
BIG_CONJUNCTION							= '⋀'
BIG_DISJUNCTION							= '⋁'
BIG_INTERSECTION						   = '⋂'
BIG_UNION								  = '⋃'
BIG_CIRCLED_PLUS						   = '⨁'
BIG_CIRCLED_TIMES						  = '⨂'
BIG_CIRCLED_DOT_OPERATOR				   = '⨀'
BIG_PI									 = '∏'
BIG_SIGMA								  = '∑'
BIG_TIMES								  = '⨉'
EMPTY_SET								  = '∅'
ARROW									  = '←↑→↓↔↕↖↗↘↙'
ARROW_STROKE							   = '↚ ↛ ↮	 '
ARROW_DOUBLE							   = '⇐⇑⇒⇓⇔⇕⇖⇗⇘⇙'
ARROW_DOUBLE_STROKE						= '⇍ ⇏ ⇎	 '
ARROW_TRIPLE							   = '⇚ ⇛	   '
ARROW_HARPOON							  = '⇋⇌		'
ARROW_PAIRED							   = '⇇⇈⇉⇊	  '
ARROW_PAIRED_OPPOSITES					 = '⇄⇅⇆⇵	  '
ARROW_PAIRED_TRIPLE						= '⬱ ⇶	   '
ARROW_DASHED							   = '⇠⇡⇢⇣	  '
ARROW_WHITE								= '⇦⇧⇨⇩	  '
ELLIPSIS_VERTICAL						  = '⋮'
ELLIPSIS_HORIZONTAL						= '⋯'
ELLIPSIS_DIAGONAL_UP_RIGHT				 = '⋰'
ELLIPSIS_DIAGONAL_DOWN_RIGHT			   = '⋱'
DIAMETER								   = '⌀'
NUMERO									 = '№'
EULER_CONSTANT							 = 'ℇ'
DOTLESS_ITALIC_I						   = '𝚤'
DOTLESS_ITALIC_J						   = '𝚥'
CIRCLE_BLACK							   = '●'
CIRCLE_WHITE							   = '○'
CIRCLE_HEAVY							   = '⭘'
CIRCLE_LARGE_BLACK						 = '⬤'
CIRCLE_LARGE_WHITE						 = '◯'
CIRCLE_LARGE_HEAVY						 = '⭕'
ELLIPSE_HORIZONTAL_BLACK				   = '⬬'
ELLIPSE_HORIZONTAL_WHITE				   = '⬭'
ELLIPSE_VERTICAL_BLACK					 = '⬮'
ELLIPSE_VERTICAL_WHITE					 = '⬯'
TRIANGLE_UP_BLACK						  = '▲'
TRIANGLE_UP_WHITE						  = '△'
TRIANGLE_RIGHT_BLACK					   = '▶'
TRIANGLE_RIGHT_WHITE					   = '▷'
TRIANGLE_DOWN_BLACK						= '▼'
TRIANGLE_DOWN_WHITE						= '▽'
TRIANGLE_LEFT_BLACK						= '◀'
TRIANGLE_LEFT_WHITE						= '◁'
TRIANGLE_SMALL_UP_BLACK					= '▴'
TRIANGLE_SMALL_UP_WHITE					= '▵'
TRIANGLE_SMALL_RIGHT_BLACK				 = '▸'
TRIANGLE_SMALL_RIGHT_WHITE				 = '▹'
TRIANGLE_SMALL_DOWN_BLACK				  = '▾'
TRIANGLE_SMALL_DOWN_WHITE				  = '▿'
TRIANGLE_SMALL_LEFT_BLACK				  = '◂'
TRIANGLE_SMALL_LEFT_WHITE				  = '◃'
TRIANGLE_CENTRED_MEDIUM_UP_BLACK		   = '⯅'
TRIANGLE_CENTRED_MEDIUM_DOWN_BLACK		 = '⯆'
TRIANGLE_CENTRED_MEDIUM_LEFT_BLACK		 = '⯇'
TRIANGLE_CENTRED_MEDIUM_RIGHT_BLACK		= '⯈'
TRIANGLE_UPPER_LEFT_BLACK				  = '◤'
TRIANGLE_UPPER_LEFT_WHITE				  = '◸'
TRIANGLE_LOWER_LEFT_BLACK				  = '◣'
TRIANGLE_LOWER_LEFT_WHITE				  = '◺'
TRIANGLE_UPPER_RIGHT_BLACK				 = '◥'
TRIANGLE_UPPER_RIGHT_WHITE				 = '◹'
TRIANGLE_LOWER_RIGHT_BLACK				 = '◢'
TRIANGLE_LOWER_RIGHT_WHITE				 = '◿'
POINTER_RIGHT_BLACK						= '►'
POINTER_RIGHT_WHITE						= '▻'
POINTER_LEFT_BLACK						 = '◄'
POINTER_LEFT_WHITE						 = '◅'
SQUARE_BLACK							   = '■'
SQUARE_WHITE							   = '□'
SQUARE_MEDIUM_BLACK						= '◼'
SQUARE_MEDIUM_WHITE						= '◻'
SQUARE_SMALL_BLACK						 = '▪'
SQUARE_SMALL_WHITE						 = '▫'
SQUARE_VERY_SMALL_BLACK					= '⬝'
SQUARE_VERY_SMALL_WHITE					= '⬞'
SQUARE_CENTRED_BLACK					   = '⯀'
RECTANGLE_HORIZONTAL_BLACK				 = '▬'
RECTANGLE_HORIZONTAL_WHITE				 = '▭'
RECTANGLE_VERTICAL_BLACK				   = '▮'
RECTANGLE_VERTICAL_WHITE				   = '▯'
PARALLELOGRAM_BLACK						= '▰'
PARALLELOGRAM_WHITE						= '▱'
DIAMOND_BLACK							  = '◆'
DIAMOND_WHITE							  = '◇'
DIAMOND_MEDIUM_BLACK					   = '⬥'
DIAMOND_MEDIUM_WHITE					   = '⬦'
DIAMOND_SMALL_BLACK						= '⬩'
DIAMOND_CENTRED_BLACK					  = '⯁'
LOZENGE_BLACK							  = '⧫'
LOZENGE_WHITE							  = '◊'
LOZENGE_MEDIUM_BLACK					   = '⬧'
LOZENGE_MEDIUM_WHITE					   = '⬨'
LOZENGE_SMALL_BLACK						= '⬪'
LOZENGE_SMALL_WHITE						= '⬫'
CUSP_BLACK								 = '⯌'
CUSP_WHITE								 = '⯎'
CUSP_ROTATED_BLACK						 = '⯍'
CUSP_ROTATED_WHITE 						   = '⯏'
PENTAGON_BLACK							 = '⬟'
PENTAGON_WHITE							 = '⬠'
PENTAGON_RIGHT_BLACK					   = '⭓'
PENTAGON_RIGHT_WHITE					   = '⭔'
PENTAGON_DOWN_BLACK						= '⯂'
STAR_SMALL_BLACK						   = '⭑'
STAR_SMALL_WHITE						   = '⭒'
HEXAGON_VERTICAL_WHITE					 = '⬡'
HEXAGON_VERTICAL_BLACK					 = '⬢'
HEXAGON_HORIZONTAL_BLACK				   = '⬣'
OCTAGON_VERTICAL_BLACK					 = '⯄'
OCTAGON_HORIZONTAL_BLACK				   = '⯃'
#GREEK_NAME								 │ {'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega', 'digamma', 'san', 'tsan', 'sho', 'heta', 'koppa', 'sampi', 'yot', 'stigma'}

# starting from this is official -----------------------------------------------

# none of these functions should depend on each other

import math as _math
import cmath as _cmath

def add(a, b):
	'a + b also known as addition'
	return a + b

def sub(a, b):
	'a − b also known as subtraction also known as difference'
	return a - b

def mul(a, b):
	'a × b also known as multiplication also known as product also known as times'
	return a * b

def div(a, b):
	'a ∕ b also known as division'
	return a / b

def inc(x):
	'incrementation'
	if isinstance(x, complex):
		raise TypeError("complex numbers do not have an ordering")
	'++x also known as x + 1'
	return x + 1

def dec(x):
	'decrementation'
	if isinstance(x, complex):
		raise TypeError("complex numbers do not have an ordering")
	'−−x also known as x − 1'
	return x - 1

def neg(x):
	'−x also known as unary subtraction also known as additive inverse'
	return -x

def recip(x):
	'⅟x also known as reciprocal also known as unary division also known as multiplicative inverse'
	return 1/x

def mod(a, b):
	'modulus'
	if not (isinstance(a, int) and isinstance(b, int)):
		raise TypeError("modulus only deals with integers. perhaps you meant floorrem?")
	return a % b

def root(a, b):
	'nᵗʰ root also known as ᵇ√a also known as a ^ (⅟b) also known as inverse of exponentiation'
	return a ** (1/b)

def pow(a, b):
	'aᵇ also known as exponentiation'
	return a ** b

from math import exp
from math import exp2

def exp10(x):
	'exponentiation, base 10'
	return 10 ** x

def log(a, b):
	'logarithm also known as inverse of exponentiation'
	try:
		from math import log
		return log(a, b)
	except (ValueError, TypeError):
		from cmath import log
		return log(a, b)

def loge(x):
	'logarithm, base e'
	return _math.log(x)

from math import log2
from math import log10

def powm1(a, b):
	'a ** b - 1'
	return a ** b - 1

from math import expm1

def exp2m1(x):
	'2 ** x - 1'
	return 2 ** x - 1

def exp10m1(x):
	'10 ** x - 1'
	return 10 ** x - 1

def logp1(a, b):
	'log(a+1, b)'
	return _math.log(a+1, b)

from math import log1p as logep1

def log2p1(x):
	'log2(x+1)'
	return _math.log(x+1, 2)

def log10p1(x):
	'log10(x+1)'
	return _math.log(x+1, 10)

def sexp(a, b):
	'superexponentiation also known as tetration'
	raise NotImplementedError('i havent made this yet')

def sroot(a, b):
	'superroot also known as inverse of tetration'
	raise NotImplementedError('i havent made this yet')

def slog(a, b):
	'superlogarithm also known as inverse of tetration'
	raise NotImplementedError('i havent made this yet')

def parallel(a, b):
	'parallel operation also known as parallel addition'
	return a*b/(a+b)

from math import sqrt
from math import cbrt

def rsqrt(x):
	'1/sqrt(x)'
	return 1/_math.sqrt(x)

def rcbrt(x):
	'1/cbrt(x)'
	return 1/_math.cbrt(x)

from builtins import abs
from math import gcd
from math import lcm

def hyper(n, a, b):
	'return n-th hyperoperation of a, b'
	raise NotImplementedError('not made yet')

from math import floor
from math import ceil
from math import trunc

def away(x):
	'directed rounding to integer, away from ±0'
	raise NotImplementedError('not made yet')

from builtins import round
from operator import floordiv

def ceildiv(x):
	'division rounded to +∞'
	raise NotImplementedError('not made yet')

def truncdiv(x):
	'division rounded to ±0'
	raise NotImplementedError('not made yet')

def awaydiv(x):
	'division rounded away from ±0'
	raise NotImplementedError('not made yet')

def rounddiv(x):
	'round(div(a,b))'
	raise NotImplementedError('not made yet')

def floorrem(x):
	'remainder of floordiv'
	raise NotImplementedError('not made yet')

def ceilrem(x):
	'remainder of ceildiv'
	raise NotImplementedError('not made yet')

def truncrem(x):
	'remainder of truncdiv'
	raise NotImplementedError('not made yet')

def awayrem(x):
	'remainder of awaydiv'
	raise NotImplementedError('not made yet')

def roundrem(x):
	'remainder of rounddiv'
	raise NotImplementedError('not made yet')

def floordivrem(x):
	'return (floordiv, floorrem)'
	raise NotImplementedError('not made yet')

def ceildivrem(x):
	'return ( ceildiv,  ceilrem)'
	raise NotImplementedError('not made yet')
	
def truncdivrem(x):
	'return (truncdiv, truncrem)'
	raise NotImplementedError('not made yet')

def awaydivrem(x):
	'return ( awaydiv,  awayrem)'
	raise NotImplementedError('not made yet')

def rounddivrem(x):
	'return (rounddiv, roundrem)'
	raise NotImplementedError('not made yet')

# comparative

def lt(a, b):
	'a < b'
	return a < b

def le(a, b):
	'a ≤ b'
	return a <= b

def eq(a, b):
	'a = b'
	return a == b

def ne(a, b):
	'a ≠ b'
	return a != b

def ge(a, b):
	'a ≥ b'
	return a >= b

def gt(a, b):
	'a > b'
	return a > b

def clt(a, b):
	'component-wise less-than'
	return (a.real < b.real, a.imag < b.imag)

def cle(a, b):
	'component-wise less-than-or-equal-to'
	return (a.real <= b.real, a.imag <= b.imag)

def ceq(a, b):
	'component-wise equals'
	return (a.real == b.real, a.imag == b.imag)

def cne(a, b):
	'component-wise not-equals'
	return (a.real != b.real, a.imag != b.imag)

def cge(a, b):
	'component-wise greater-than-or-equals'
	return (a.real >= b.real, a.imag >= b.imag)

def cgt(a, b):
	'component-wise greater-than'
	return (a.real > b.real, a.imag > b.imag)

def mlt(a, b):
	'magnitudinal less-than. AKA |a| < |b|'
	return abs(a) < abs(b)

def mle(a, b):
	'magnitudinal less-than-or-equal-to. AKA |a| ≤ |b|'
	return abs(a) <= abs(b)

def meq(a, b):
	'magnitudinal equal-to. AKA |a| == |b|'
	return abs(a) == abs(b)

def mne(a, b):
	'magnitudinal not-equal-to. AKA |a| ≠ |b|'
	return abs(a) != abs(b)

def mlt(a, b):
	'magnitudinal greater-than-or-equal-to. AKA |a| ≥ |b|'
	return abs(a) >= abs(b)

def mlt(a, b):
	'magnitudinal greater-than. AKA |a| > |b|'
	return abs(a) > abs(b)

def cmp(a, b):
	'comparison. -1 if a < b, 0 if a == b, 1 if a > b'
	return (a > b) - (a < b)

def ccmp(a, b):
	'component-wise cmp'
	return ((a.real > b.real) - (a.real < b.real), (a.imag > b.imag) - (a.imag < b.imag))

def mcmp(a, b):
	'magnitudinal cmp'
	abs_a = abs(a)
	abs_b = abs(b)
	return (abs_a > abs_b) - (abs_a < abs_b)


def sin(a):
	'circular sine'
	if isinstance(a, complex):
		return _cmath.sin(a)
	else:
		return _math.sin(a)

# boolean ----------------------

from operator import not_
from operator import and_

def nand(a, b):
	'not(and(a, b))'
	return not(a and b)

from operator import or_

def nor(a, b):
	'not(or(a, b))'
	return not(a or b)

from operator import xor

def xnor(a, b):
	'not(xor(a, b))'
	return not(xor(a, b))

def imp(a, b):
	"material implication. aka 'not a or b'"
	return not a or b

def nimp(a, b):
	'not(imp(a, b))'
	return a and not b

def con(a, b):
	"converse implication"
	return not b or a

def ncon(a, b):
	'not(con(a, b))'
	return b and not a

# combinatorial ---------------

from math import factorial as fact

def sumt(x):
	'return sum of all numbers from 1 to x. like factorial but with addition'
	if isinstance(x, int): 
		return (x*(x+1))//2
	return (x*(x+1))/2

from math import comb
from math import perm

# interval -------------------

def clamp(x, a, b):
	'restrict x to [a ,b]. returns min(max(a, b), c)'
	return min(max(a, b), c)

def in_open_interval(x, a, b) -> bool:
	return a < x < b

def in_closed_interval(x, a, b) -> bool:
	return a <= x <= b

def in_left_open_interval(x, a, b) -> bool:
	return a < x <= b

def in_right_open_interval(x, a, b) -> bool:
	return a <= x < b

def lerp(x, a, b):
	'linear interpolation. maps [0, 1] to [a, b]'
	return a + x*(b-a)

def unlerp(y, a, b):
	'inverse of linear interpolation. maps [a, b] to [0, 1]'
	return (y - a)/(b-a)

def map(x, a, b, c, d):
	'map x from [a, b] to [c, d]. same as lerp(unlerp(x, a, b), c, d)'
	return c + (x-a)/(b-a)*(d-c)

# miscellaneous ------------------------

def any(*args):
	'variadic OR gate'
	return any(args)

def all(*args):
	'variadic AND gate'
	return all(args)

def sum(*args):
	'variadic addition'
	return sum(args)

def prod(*args):
	'variadic multiplication'
	return _math.prod(args)

# iterables --------------------------

from builtins import len as length

def concat(*iterables):
	'variadic concatenation'
	result = iterables[0]
	for iterable in iterables[1:]:
		result += iterable
	return result

from operator import contains

# sequences --------------------------

def head(stuff):
	return stuff[0]

def last(stuff):
	return stuff[-1]

def tail(stuff):
	return stuff[1:]

def init(stuff):
	return stuff[:-1]

def nth(stuff):
	return stuff[n]

def slice(stuff, a, b):
	raise NotImplementedError("not sure if to include or exclude a-th and b-th elements")
	return stuff[a, b]

# finished up to this ----------------------------------------------------------
