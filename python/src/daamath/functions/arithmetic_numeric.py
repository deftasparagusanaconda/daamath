from numbers import Number
import math

try:
	from math import fma
except ImportError:
	def fma(a: Number, b: Number, c: Number) -> Number:
		'a * b + c'
		return a * b + c

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

def powe(a: Number) -> Number:
	return a ** math.e

def pow2(a: Number) -> Number:
	return a ** 2

def pow3(a: Number) -> Number:
	return a ** 3

def pow10(a: Number) -> Number:
	return a ** 10

def roote(a: Number) -> Number:
	return a ** (1 / math.e)

def root2(a: Number) -> Number:
	try:	return math.sqrt(a)
	except:	return cmath.sqrt(a)

def root3(a: Number) -> Number:
	try:	return math.cbrt(a)
	except: return a ** (1 / 3)

def root10(a: Number) -> Number:
	return a ** 0.1

def expe(a: Number) -> Number:
	try:	return math.exp(a)
	except: return cmath.exp(a)

def exp2(a: Number) -> Number:
	try:	return math.exp2(a)
	except:	return 2 ** a

def exp3(a: Number) -> Number:
	return 3 ** a

def exp10(a: Number) -> Number:
	return 10 ** a

def loge(a: Number) -> Number:
	try:	return math.log(a)
	except: return cmath.log(a)

def log2(a: Number) -> Number:
	try:	return math.log2(a)
	except:	return cmath.log(a, 2)

def log3(a: Number) -> Number:
	try:	return math.log(a, 3)
	except:	return cmath.log(a, 3)

def log10(a: Number) -> Number:
	try:	return math.log10(a)
	except: return cmath.log10(a)

# ------------------------------------------------------------------------------

def powm1(a: Number, b: Number) -> Number:
	return math.expm1(math.log(a) * b)

def root1p(a: Number, b: Number) -> Number:
	return math.exp(math.log1p(a) / b)

def expm1(a: Number, b: Number) -> Number:
	return b ** a - 1

def log1p(a: Number, b: Number) -> Number:
	try:	return math.log(1 + a, b)
	except:	return cmath.log(1 + a, b)

# ------------------------------------------------------------------------------

def powem1(a: Number) -> Number:
	return math.expm1(math.log(a) * math.e)

def pow2m1(a: Number) -> Number:
	return math.expm1(math.log(a) * 2)

def pow3m1(a: Number) -> Number:
	return math.expm1(math.log(a) * 3)

def pow10m1(a: Number) -> Number:
	return math.expm1(math.log(a) * 10)

def roote1p(a: Number) -> Number:
	return math.exp(math.log1p(a) / math.e)

def root21p(a: Number) -> Number:
	return math.exp(math.log1p(a) / 2)

def root31p(a: Number) -> Number:
	return math.exp(math.log1p(a) / 3)

def root101p(a: Number) -> Number:
	return math.exp(math.log1p(a) / 10)

def expem1(a: Number) -> Number:
	try:	return math.expm1(a)
	except: return cmath.exp(a) - 1

def exp2m1(a: Number) -> Number:
	try:	return math.exp2(a) - 1
	except:	return 2 ** a - 1

def exp3m1(a: Number) -> Number:
	return 3 ** a - 1

def exp10m1(a: Number) -> Number:
	return 10 ** a - 1

def loge1p(a: Number) -> Number:
	try:	return math.log1p(a)
	except: return cmath.log(1 + a)

def log21p(a: Number) -> Number:
	try:	return math.log2(1 + a)
	except:	return cmath.log(1 + a, 2)

def log31p(a: Number) -> Number:
	try:	return math.log(1 + a, 3)
	except:	return cmath.log(1 + a, 3)

def log101p(a: Number) -> Number:
	try:	return math.log10(1 + a)
	except: return cmath.log10(1 + a)
