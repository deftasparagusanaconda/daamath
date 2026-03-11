# these operators dont treat nested lists as tensors. do you know why?
# because the tensor object should know itself how to do basic math ops. an operator is an operator.. an object should know what to do with an operator.
# its also because this tensor mechanism is hard to scale across languages

import math, cmath, functools
from numbers import Number, Real
from typing import Literal

'''
instead of:
                    root   sroot
                     |      |
                    pow -- spow -- …
                  /
inc -- add -- mul   
 |      |      |  \
dec    sub    div   exp -- sexp -- …
                     |      |
                    log    slog 

we should have:
X       h0X     h1X     h2X     h3X     h4X     h5X     …
c       ++b     a + b   a * b   a ^ b   a ↑ b   a ⇑ b   …
b       --c     c - a   c / a   c L b   …       …       …
a       N/A     c - b   c / b   c √ b   …       …       …

where we X is the variable we solve for in the equation a  b = c
'''

# NOTE: i expect these function signatures: 
# hXc(a, b)
# hXb(c, a)
# hXa(c, b)
#
# i could make it a cycle of variables like so:
# hXc(a, b)
# hXb(c, a)
# hXa(b, c)
#
# but this would imply that the three variables are involved in a cyclic relation a → b → c → a when, really, they are involved in a 2 → 1 relation a, b → c. thats why when solving for b and a, we make it intentionally asymmetric. and the only way to do that is to have the first signature set i proposed

#h0c = functools.partial(h1c, a = 1)
def h0c(b):
	'++b, incrementation'
	return b + 1
inc = h0c
	
#h0b = functools.partial(h1b, x = 1)
def h0b(c):
	'--c, decrementation'
	return c - 1
dec = h0b

def h1c(a, b):
	'a + b, addition'
	return a + b
add = h1c

# because addition is commutative, it has only one inverse
# so we shall make one callable, and give two aliases
def sub(x, y):
	'x - y, subtraction'
	return x - y
h1b = h1a = sub

def h2c(a, b):
	'a * b, multiplication'
	return a * b
mul = h2c

# because multiplication is commutative, it has only one inverse
# so we shall make one callable, and give two aliases
def div(x, y):
	'x / y, division'
	return x / y
h2b = h2a = div

def h3c(a, b):
	'a ^ b, exponentiation'
	return a ** b
pow = h3c

def h3b(c, a):
	'log_a(c), logarithm'
	# c = a ^ b
	try:    return math.log(c, a)
	except: return cmath.log(c, a)
log = h3b

def h3a(c, b):
	'c ^ (1 / b), n-th root'
	# c = a ^ b
	return c ** (1 / b)
root = h3a

def h4c(a, b):
	'tetration, superexponentiation'
	raise NotImplementedError
spow = h4c

def h4b(c, a):
	'superlogarithm'
	raise NotImplementedError
slog = h4b

def h4a(c, b):
	'superroot'
	raise NotImplementedError
sroot = h4a

def hyper(
		fst: Number, 
		snd: Number, 
		n: int, 
		solve: Literal['a', 'b', 'c'] = 'c', 
		) -> Number:
	match solve:
		case 'a':
			match n:
				case 0: raise Exception('this operation simply does not exist in mathematics')
				case 1: return h1a(fst, snd)
				case 2: return h2a(fst, snd)
				case 3: return h3a(fst, snd)
				case 4: return h4a(fst, snd)
				case _: raise NotImplementedError
		case 'b':
			match n:
				case 0: return h0b(snd)
				case 1: return h1b(fst, snd)
				case 2: return h2b(fst, snd)
				case 3: return h3b(fst, snd)
				case 4: return h4b(fst, snd)
				case _: raise NotImplementedError
		case 'c':
			match n:
				case 0: return h0c(snd)
				case 1: return h1c(fst, snd)
				case 2: return h2c(fst, snd)
				case 3: return h3c(fst, snd)
				case 4: return h4c(fst, snd)
				case _: raise NotImplementedError
		case _:
			raise ValueError("invalid solve parameter. must be one of {'a', 'b', 'c'}")

# prebound functions ----------------------------------------------------------

# additive inverse, since addition has both left and right identities
#h1b_c0 = h1a_c0 = functools.partial(_sub, x = 0)
def ainv(y):
	return -y
h1b_c0 = h1a_c0 = ainv

# multiplicative inverse, since multiplication has both left and right identities
#h2b_c1 = h2a_c1 = functools.partial(_div, x = 1)
def minv(y):
	return 1 / y
h2b_c1 = h2a_c1 = minv
