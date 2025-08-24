// arithmetic primitives are: byte, short, int, long, float, double
// six types. so thats 6^1 for unary operators, 6^2 for binary, 6^3 for ternary, etc
// preserves int, long, float, double, byte to int, short to int, and always promotes to wider type
// type casting is explicitly mentioned even if java implicitly promotes them; only unless the input type already matches the output type

// types are promoted before operation for operand fairness. for example: 
// static float mul(int a, float b)

package swissmath;

public final class SwissMath
{	private SwissMath() {}
		
	// by convention, byte and short are promoted to int, because they hardly support normal arithmetic
	static int    add(byte   a, byte   b) { return (int   )a+(int   )b; }
	static int    add(byte   a, short  b) { return (int   )a+(int   )b; }
	static int    add(byte   a, int    b) { return (int   )a+        b; }
	static long   add(byte   a, long   b) { return (long  )a+        b; }
	static float  add(byte   a, float  b) { return (float )a+        b; }
	static double add(byte   a, double b) { return (double)a+        b; }
	static int    add(short  a, byte   b) { return (int   )a+(int   )b; }
	static int    add(short  a, short  b) { return (int   )a+(int   )b; }
	static int    add(short  a, int    b) { return (int   )a+        b; }
	static long   add(short  a, long   b) { return (long  )a+        b; }
	static float  add(short  a, float  b) { return (float )a+        b; }
	static double add(short  a, double b) { return (double)a+        b; }
	static int    add(int    a, byte   b) { return         a+(int   )b; }
	static int    add(int    a, short  b) { return         a+(int   )b; }
	static int    add(int    a, int    b) { return         a+        b; }
	static long   add(int    a, long   b) { return (long  )a+        b; }
	static float  add(int    a, float  b) { return (float )a+        b; }
	static double add(int    a, double b) { return (double)a+        b; }
	static long   add(long   a, byte   b) { return         a+(long  )b; }
	static long   add(long   a, short  b) { return         a+(long  )b; }
	static long   add(long   a, int    b) { return         a+(long  )b; }
	static long   add(long   a, long   b) { return         a+        b; }
	static float  add(long   a, float  b) { return (float )a+        b; }
	static double add(long   a, double b) { return (double)a+        b; }
	static float  add(float  a, byte   b) { return         a+(float )b; }
	static float  add(float  a, short  b) { return         a+(float )b; }
	static float  add(float  a, int    b) { return         a+(float )b; }
	static float  add(float  a, long   b) { return         a+(float )b; }
	static float  add(float  a, float  b) { return         a+        b; }
	static double add(float  a, double b) { return (double)a+        b; }
	static double add(double a, byte   b) { return         a+(double)b; }
	static double add(double a, short  b) { return         a+(double)b; }
	static double add(double a, int    b) { return         a+(double)b; }
	static double add(double a, long   b) { return         a+(double)b; }
	static double add(double a, float  b) { return         a+(double)b; }
	static double add(double a, double b) { return         a+        b; }
	
	static int    sub(byte   a, byte   b) { return (int   )a-(int   )b; }
	static int    sub(byte   a, short  b) { return (int   )a-(int   )b; }
	static int    sub(byte   a, int    b) { return (int   )a-        b; }
	static long   sub(byte   a, long   b) { return (long  )a-        b; }
	static float  sub(byte   a, float  b) { return (float )a-        b; }
	static double sub(byte   a, double b) { return (double)a-        b; }
	static int    sub(short  a, byte   b) { return (int   )a-(int   )b; }
	static int    sub(short  a, short  b) { return (int   )a-(int   )b; }
	static int    sub(short  a, int    b) { return (int   )a-        b; }
	static long   sub(short  a, long   b) { return (long  )a-        b; }
	static float  sub(short  a, float  b) { return (float )a-        b; }
	static double sub(short  a, double b) { return (double)a-        b; }
	static int    sub(int    a, byte   b) { return         a-(int   )b; }
	static int    sub(int    a, short  b) { return         a-(int   )b; }
	static int    sub(int    a, int    b) { return         a-        b; }
	static long   sub(int    a, long   b) { return (long  )a-        b; }
	static float  sub(int    a, float  b) { return (float )a-        b; }
	static double sub(int    a, double b) { return (double)a-        b; }
	static long   sub(long   a, byte   b) { return         a-(long  )b; }
	static long   sub(long   a, short  b) { return         a-(long  )b; }
	static long   sub(long   a, int    b) { return         a-(long  )b; }
	static long   sub(long   a, long   b) { return         a-        b; }
	static float  sub(long   a, float  b) { return (float )a-        b; }
	static double sub(long   a, double b) { return (double)a-        b; }
	static float  sub(float  a, byte   b) { return         a-(float )b; }
	static float  sub(float  a, short  b) { return         a-(float )b; }
	static float  sub(float  a, int    b) { return         a-(float )b; }
	static float  sub(float  a, long   b) { return         a-(float )b; }
	static float  sub(float  a, float  b) { return         a-        b; }
	static double sub(float  a, double b) { return (double)a-        b; }
	static double sub(double a, byte   b) { return         a-(double)b; }
	static double sub(double a, short  b) { return         a-(double)b; }
	static double sub(double a, int    b) { return         a-(double)b; }
	static double sub(double a, long   b) { return         a-(double)b; }
	static double sub(double a, float  b) { return         a-(double)b; }
	static double sub(double a, double b) { return         a-        b; }
	
	static int    mul(byte   a, byte   b) { return (int   )a*(int   )b; }
	static int    mul(byte   a, short  b) { return (int   )a*(int   )b; }
	static int    mul(byte   a, int    b) { return (int   )a*        b; }
	static long   mul(byte   a, long   b) { return (long  )a*        b; }
	static float  mul(byte   a, float  b) { return (float )a*        b; }
	static double mul(byte   a, double b) { return (double)a*        b; }
	static int    mul(short  a, byte   b) { return (int   )a*(int   )b; }
	static int    mul(short  a, short  b) { return (int   )a*(int   )b; }
	static int    mul(short  a, int    b) { return (int   )a*        b; }
	static long   mul(short  a, long   b) { return (long  )a*        b; }
	static float  mul(short  a, float  b) { return (float )a*        b; }
	static double mul(short  a, double b) { return (double)a*        b; }
	static int    mul(int    a, byte   b) { return         a*(int   )b; }
	static int    mul(int    a, short  b) { return         a*(int   )b; }
	static int    mul(int    a, int    b) { return         a*        b; }
	static long   mul(int    a, long   b) { return (long  )a*        b; }
	static float  mul(int    a, float  b) { return (float )a*        b; }
	static double mul(int    a, double b) { return (double)a*        b; }
	static long   mul(long   a, byte   b) { return         a*(long  )b; }
	static long   mul(long   a, short  b) { return         a*(long  )b; }
	static long   mul(long   a, int    b) { return         a*(long  )b; }
	static long   mul(long   a, long   b) { return         a*        b; }
	static float  mul(long   a, float  b) { return (float )a*        b; }
	static double mul(long   a, double b) { return (double)a*        b; }
	static float  mul(float  a, byte   b) { return         a*(float )b; }
	static float  mul(float  a, short  b) { return         a*(float )b; }
	static float  mul(float  a, int    b) { return         a*(float )b; }
	static float  mul(float  a, long   b) { return         a*(float )b; }
	static float  mul(float  a, float  b) { return         a*        b; }
	static double mul(float  a, double b) { return (double)a*        b; }
	static double mul(double a, byte   b) { return         a*(double)b; }
	static double mul(double a, short  b) { return         a*(double)b; }
	static double mul(double a, int    b) { return         a*(double)b; }
	static double mul(double a, long   b) { return         a*(double)b; }
	static double mul(double a, float  b) { return         a*(double)b; }
	static double mul(double a, double b) { return         a*        b; }

	// a true division always returns at least a float
	static float  div(byte   a, byte   b) { return (float )a/(float )b; }
	static float  div(byte   a, short  b) { return (float )a/(float )b; }
	static float  div(byte   a, int    b) { return (float )a/(float )b; }
	static float  div(byte   a, long   b) { return (float )a/(float )b; }
	static float  div(byte   a, float  b) { return (float )a/        b; }
	static double div(byte   a, double b) { return (double)a/        b; }
	static float  div(short  a, byte   b) { return (float )a/(float )b; }
	static float  div(short  a, short  b) { return (float )a/(float )b; }
	static float  div(short  a, int    b) { return (float )a/(float )b; }
	static float  div(short  a, long   b) { return (float )a/(float )b; }
	static float  div(short  a, float  b) { return (float )a/        b; }
	static double div(short  a, double b) { return (double)a/        b; }
	static float  div(int    a, byte   b) { return (float )a/(float )b; }
	static float  div(int    a, short  b) { return (float )a/(float )b; }
	static float  div(int    a, int    b) { return (float )a/(float )b; }
	static float  div(int    a, long   b) { return (float )a/(float )b; }
	static float  div(int    a, float  b) { return (float )a/        b; }
	static double div(int    a, double b) { return (double)a/        b; }
	static float  div(long   a, byte   b) { return (float )a/(float )b; }
	static float  div(long   a, short  b) { return (float )a/(float )b; }
	static float  div(long   a, int    b) { return (float )a/(float )b; }
	static float  div(long   a, long   b) { return (float )a/(float )b; }
	static float  div(long   a, float  b) { return (float )a/        b; }
	static double div(long   a, double b) { return (double)a/        b; }
	static float  div(float  a, byte   b) { return         a/(float )b; }
	static float  div(float  a, short  b) { return         a/(float )b; }
	static float  div(float  a, int    b) { return         a/(float )b; }
	static float  div(float  a, long   b) { return         a/(float )b; }
	static float  div(float  a, float  b) { return         a/        b; }
	static double div(float  a, double b) { return (double)a/        b; }
	static double div(double a, byte   b) { return         a/(double)b; }
	static double div(double a, short  b) { return         a/(double)b; }
	static double div(double a, int    b) { return         a/(double)b; }
	static double div(double a, long   b) { return         a/(double)b; }
	static double div(double a, float  b) { return         a/(double)b; }
	static double div(double a, double b) { return         a/        b; }

	static float  neg(byte   a) { return 1/(float)a; }
	static float  neg(short  a) { return 1/(float)a; }
	static float  neg(int    a) { return 1/(float)a; }
	static float  neg(long   a) { return 1/(float)a; }
	static float  neg(float  a) { return 1/       a; }
	static double neg(double a) { return 1/       a; }

	static int    inv(byte   a) { return -(int)a; }
	static int    inv(short  a) { return -(int)a; }
	static int    inv(int    a) { return -     a; }
	static long   inv(long   a) { return -     a; }
	static float  inv(float  a) { return -     a; }
	static double inv(double a) { return -     a; }
}	
	
/*	

# numeric
	'mod'     : _operator.mod,
	'floordiv': _operator.floordiv,
	'abs'     : _operator.abs,
	'square'  : _square,
	'cube'    : _cube,
	'pow'     : _builtins.pow,
	'floor'   : _math.floor,
	'round'   : _builtins.round,
	'ceil'    : _math.ceil,
	'ipart'   : _math.trunc,
	'fpart'   : _fractional_part,
	'exp'     : _math.exp,
	'exp2'    : _math.exp2,
	'log10'   : _math.log10,
	'log2'    : _math.log2,
	'log'     : _math.log,
	'sqrt'    : _math.sqrt,
	'cbrt'    : _math.cbrt,
	'root'    : _root,

# trigonometric
	'sin'     : _math.sin,
	'cos'     : _math.cos,
	'tan'     : _math.tan,
	'cot'     : _cot,
	'sec'     : _sec,
	'csc'     : _csc,
	'asin'    : _math.asin,
	'acos'    : _math.acos,
	'atan'    : _math.atan,
	'acot'    : _acot,
	'asec'    : _asec,
	'acsc'    : _acsc,

# hyperbolic
	'sinh'    : _math.sinh,
	'cosh'    : _math.cosh,
	'tanh'    : _math.tanh,
	'coth'    : _coth,
	'sech'    : _sech,
	'csch'    : _csch,
	'asinh'   : _math.asinh,
	'acosh'   : _math.acosh,
	'atanh'   : _math.atanh,
	'acoth'   : _acoth,
	'asech'   : _asech,
	'acsch'   : _acsch,

# left out due to obscurity. also probably mostly wrong :P
#'versin'    : lambda a: 1 - math.cos(a)
#'coversin'  : lambda a: 1 - math.sin(a)
#'haversin'  : lambda a: 0.5 - math.cos(a)/2
#'hacoversin': lambda a: 0.5 - math.sin(a)/2
#'exsec'     : lambda a: 1/math.cos(a) - 1
#'excsc'     : lambda a: 1/math.sin(a) - 1
#'chord'     : lambda a: 2 * math.sin(a/2)
#'vercos'    : lambda a: 1 + math.cos(a)
#'covercos'  : lambda a: 1 + math.sin(a)
#'havercos'  : lambda a: 0.5 + math.cos(a)/2
#'hacovercos': lambda a: 0.5 + math.sin(a)/2

# complex
	'real'    : _get_real, # get real lmao
	'imag'    : _get_imag,
	'phase'   : _cmath.phase,
	'conj'    : _call_conjugate,

# boolean
	'truth'   : _operator.truth,       # 01
	'not'     : _operator.not_,        # 10
	'and'     : _operator.and_,        # 0001
	'nimp'    : _nimp,                 # 0010
	'ncon'    : _ncon,                 # 0100
	'xor'     : _operator.xor,         # 0110
	'or'      : _operator.or_,         # 0111
	'nor'     : _nor,                  # 1000
	'xnor'    : _operator.eq,          # 1001
	'con'     : _converse_implication, # 1011
	'imp'     : _implication,          # 1101
	'nand'    : _nand,                 # 1110

# comparative
	'lt'      : _operator.lt,
	'le'      : _operator.le,
	'eq'      : _operator.eq,
	'ne'      : _operator.ne,
	'ge'      : _operator.ge,
	'gt'      : _operator.gt,

# statistical
	'mean'    : _mean,
	'median'  : _median,
	'mode'    : _mode,
	'pmean'   : _generalized_mean,

# combinatorial
	'comb'    : _math.comb,
	'perm'    : _math.perm,

# hello there! lol

# bitwise
	'bittruth': lambda a: a,
	'bitnot'  : _operator.invert,      # 10
	'bitand'  : _operator.and_,        # 0001
	'bitor'   : _operator.or_,         # 0111
	'bitnand' : _nand,                 # 1110
	'bitnor'  : _nor,                  # 1000
	'bitxor'  : _operator.xor,         # 0110
	'bitxnor' : _operator.eq,          # 1001
	'bitimp'  : _implication,          # 1101
	'bitcon'  : _converse_implication, # 1011
	'bitnimp' : _nimp,                 # 0010
	'bitncon' : _ncon,                 # 0100
	'lshift'  : _operator.lshift,
	'rshift'  : _operator.rshift,

# miscellaneous
	'dist'    : _dist,
	'any'     : _builtins.any,
	'all'     : _builtins.all,
	'len'     : _builtins.len,
	'range'   : _builtins.range,
	'reversed': _builtins.reversed,
	'sorted'  : _builtins.sorted,
	'divmod'  : _builtins.divmod,
	'call'    : _operator.call,
	'matmul'  : _operator.matmul,
	'concat'  : _operator.concat,
	'sign'    : _signum,
	'ifelse'  : _ifelse,
	'fact'    : _math.factorial,
	'gamma'   : _math.gamma,
	'sumt'    : _sumtorial,
	'gcd'     : _math.gcd,
	'lcm'     : _math.lcm,
	'clamp'   : _clamp,
	'lerp'    : _lerp,
	'unlerp'  : _unlerp,
	'min'     : _builtins.min,
	'max'     : _builtins.max,
	'is'      : _operator.is_,
	'isnot'   : _operator.is_not,
	'erf'     : _math.erf
	'erfc'    : _math.erfc
	'in'      : 
	'notin'   : 
}



	//from typing import Literal as _Literal
	/*
	from operator import add, sub, mul, truediv as div, pos, neg, mod, floordiv, truth, xor, not_, and_, or_, eq as xnor, lt, le, eq, ne, ge, gt, lshift, rshift, call, matmul, concat, is_, is_not
from builtins import pow, round, any, all, len, range, reversed, sorted, divmod, min, max
from math import floor, ceil, trunc as ipart, exp, exp2, log10, log2, log, sqrt, cbrt, comb, perm, factorial as fact, gamma, gcd, lcm
from cmath import phase
from statistics import mean, median, mode, variance as var, stdev

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

def conj(x):
	'return the conjugate of a number'
	return x.conjugate()

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
	return sum(range(1, a+1))

def sgn(a):
	'return -1 if negative, 0 if zero, 1 if positive. also known as signum'
	return (a>0) - (a<0)

# boolean      ---------------------------

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
	return 1/_cmath.tan(x)

def sec(x):
	'trigonometric secant (using cmath)'
	return 1/_cmath.cos(x)

def csc(x):
	'trigonometric cosecant (using cmath)'
	return 1/_cmath.sin(x)

def acot(x):
	'inverse trigonometric cotangent (using cmath)'
	return _cmath.atan(1/x)

def asec(x):
	'inverse trigonometric secant (using cmath)'
	return _cmath.acos(1/x)

def acsc(x):
	'inverse trigonometric cosecant (using cmath)'
	return _cmath.asin(1/x)

# hyperbolic -----------------------

def coth(x):
	'hyperbolic cotangent (using cmath)'
	return 1/_cmath.tanh(x)

def sech(x):
	'hyperbolic secant (using cmath)'
	return 1/_cmath.cosh(x)

def csch(x):
	'hyperbolic cosecant (using cmath)'
	return 1/_cmath.sinh(x)

def acoth(x):
	'inverse hyperbolic cotangent (using cmath)'
	return _cmath.atanh(1/x)

def asech(x):
	'inverse hyperbolic secant (using cmath)'
	return _cmath.acosh(1/x)

def acsch(x):
	'inverse hyperbolic cosecant (using cmath)'
	return _cmath.asinh(1/x)

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
'bitnot'  : _operator.invert,      # 10
'bitand'  : _operator.and_,        # 0001
'bitor'   : _operator.or_,         # 0111
'bitnand' : _nand,                 # 1110
'bitnor'  : _nor,                  # 1000
'bitxor'  : _operator.xor,         # 0110
'bitxnor' : _operator.eq,          # 1001
'bitimp'  : _implication,          # 1101
'bitcon'  : _converse_implication, # 1011
'bitnimp' : _nimp,                 # 0010
'bitncon' : _ncon,                 # 0100
"""
*/

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
*/
