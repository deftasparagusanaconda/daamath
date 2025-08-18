from operator import add, sub, mul, truediv as div, pos, neg, mod, floordiv, truth, xor, not_, and_, or_, eq as xnor, lt, le, eq, ne, ge, gt, lshift, rshift, call, matmul, concat, is_, is_not
from builtins import pow, round, any, all, len, range, reversed, sorted, divmod, min, max
from math import floor, ceil, trunc as ipart, exp, exp2, log10, log2, log, sqrt, cbrt, comb, perm, factorial as fact, gamma, gcd, lcm
from cmath import phase
from statistics import mean, median, mode

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
	'return the absolute value, of whatever value/abomination you passed'
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

# ---------------------------

def pmean(data, p=1):
	'returns the power mean (p=1: arithmetic, 0: geometric, -1: harmonic)'
	if p == 1:
		return mean(data)
	if p == 0:
		return exp(sum(log(x) for x in data)/len(data))
	return (sum(x**p for x in data)/len(data)) ** (1/p)

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
