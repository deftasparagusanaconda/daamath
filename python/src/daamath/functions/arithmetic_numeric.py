import math, cmath, functools
from numbers import Number, Real
from .arithmetic import pow, root, log

try:
	from math import fma
except ImportError:
	def fma(a: Number, b: Number, c: Number) -> Number:
		'a * b + c'
		return a * b + c
'''
def abs_sq(a: Number) -> Real:
	if isinstance(x, Complex):
		return x.real * x.real + x.imag * x.imag 
	else:
		return abs(a) ** 2
'''
# ------------------------------------------------------------------------------

# we maintain basically a matrix of:
# 
#       | e     | 2     | 3     | 10     | 
# ------+-------+-------+-------+--------+------------
# powX  | powe  | pow2  | pow3  | pow10  | a ^ b
# rootX | roote | root2 | root3 | root10 | a ^ (1 / b)
# expX  | expe  | exp2  | exp3  | exp10  | b ^ a
# logX  | loge  | log2  | log3  | log10  | logb(a)
# 
# we also maintain another matrix of:
# 
#         | e       | 2       | 3       | 10       |   
# --------+---------+---------+---------+----------+------------------
# powXm1  | powem1  | pow2m1  | pow3m1  | pow10m1  | a ^ b - 1
# rootX1p | roote1p | root21p | root31p | root101p | (1 + a) ^ (1 / b)
# expXm1  | expem1  | exp2m1  | exp3m1  | exp10m1  | b ^ a - 1
# logX1p  | loge1p  | log21p  | log31p  | log101p  | logb(1 + a)
#
# which are derived from:
# powm1(a, b)  = a ^ b - 1         = expm1(log(a) * b)
# root1p(a, b) = (1 + a) ^ (1 / b) = exp(log1p(a) / b)
# expm1(a, b)  = b ^ a - 1         
# log1p(a, b)  = logb(1 + a)       

pow_e   = functools.partial(pow, b = math.e)
pow_2   = functools.partial(pow, b = 2)
pow_3   = functools.partial(pow, b = 3)
pow_10  = functools.partial(pow, b = 10)
root_e  = functools.partial(root, b = math.e)

def root_2(a: Number) -> Number:
	try:	return math.sqrt(a)
	except:	return cmath.sqrt(a)

def root_3(a: Number) -> Number:
	try:	return math.cbrt(a)
	except: return a ** (1 / 3)

root_10 = functools.partial(root, b = 10)

def exp_e(a: Number) -> Number:
	try:	return math.exp(a)
	except: return cmath.exp(a)

def exp_2(a: Number) -> Number:
	try:	return math.exp2(a)
	except:	return 2 ** a

exp_3 = functools.partial(pow, a = 3)
exp_10 = functools.partial(pow, a = 10)

def log_e(a: Number) -> Number:
	try:	return math.log(a)
	except: return cmath.log(a)

def log_2(a: Number) -> Number:
	try:	return math.log2(a)
	except:	return cmath.log(a, 2)

log_3 = functools.partial(log, b = 3)

def log_10(a: Number) -> Number:
	try:	return math.log10(a)
	except: return cmath.log10(a)

# ------------------------------------------------------------------------------

def pow_m1(a: Number, b: Number) -> Number:
	return math.expm1(math.log(a) * b)

def root_1p(a: Number, b: Number) -> Number:
	return math.exp(math.log1p(a) / b)

def exp_m1(a: Number, b: Number) -> Number:
	return b ** a - 1

def log_1p(a: Number, b: Number) -> Number:
	try:	return math.log(1 + a, b)
	except:	return cmath.log(1 + a, b)

# ------------------------------------------------------------------------------

def pow_e_m1(a: Number) -> Number:
	return math.expm1(math.log(a) * math.e)

pow_2_m1 = functools.partial(pow_m1, b = 2)
pow_3_m1 = functools.partial(pow_m1, b = 3)
pow_10_m1 = functools.partial(pow_m1, b = 10)

root_e_1p = functools.partial(root_1p, b = math.e)
root_2_1p = functools.partial(root_1p, b = 2)
root_3_1p = functools.partial(root_1p, b = 3)
root_10_1p = functools.partial(root_1p, b = 10)

def exp_e_m1(a: Number) -> Number:
	try:	return math.expm1(a)
	except: return cmath.exp(a) - 1

def exp_2_m1(a: Number) -> Number:
	try:	return math.exp2(a) - 1
	except:	return 2 ** a - 1

exp_3_m1 = functools.partial(exp_m1, b = 3)
exp_10_m1 = functools.partial(exp_m1, b = 10)

def log_e_1p(a: Number) -> Number:
	try:	return math.log1p(a)
	except: return cmath.log(1 + a)

def log_2_1p(a: Number) -> Number:
	try:	return math.log2(1 + a)
	except:	return cmath.log(1 + a, 2)

log_3_1p = functools.partial(log_1p, b = 3)

def log_10_1p(a: Number) -> Number:
	try:	return math.log10(1 + a)
	except: return cmath.log10(1 + a)

# -----------------------------------------------------------------------------
