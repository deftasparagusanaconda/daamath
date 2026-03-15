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
def inc(b):
    'c = ++b, incrementation. the 0th hyperoperation'
    return b + 1
    
#h0b = functools.partial(h1b, x = 1)
def dec(c):
    'b = --c, decrementation. the inverse of the 0th hyperoperation'
    return c - 1
    
def add(a, b):
    'c = a + b, addition. the 1st hyperoperation'
    return a + b

def sub(c, a):
    'b = c - a, left subtraction. the inverse of the 1st hyperoperation'
    return c - a

def mul(a, b):
    'c = a * b, multiplication. the 2nd hyperoperation'
    return a * b

def div(c, a):
    'b = c / a, left division. the inverse of the 2nd hyperoperation'
    return c / a

def pow(a, b):
    'c = a ^ b, power, exponentiation. the 3rd hyperoperation'
    return a ** b

def log(c, a):
    'b = log_a(c), logarithm. the inverse of the 3rd hyperoperation that solves for b'
    # c = a ^ b
    try:    return math.log(c, a)
    except: return cmath.log(c, a)

def root(c, b):
    'a = c ^ (1 / b), n-th root. the inverse of the 3rd hyperoperation that solves for a'
    # c = a ^ b
    return c ** (1 / b)

def spow(a, b):
    'c = a ↑ b, tetration, superexponentiation, the 4th hyperoperation'
    raise NotImplementedError

def slog(c, a):
    'b = slog_a(c), superlogarithm, the inverse of the 4th hyperoperation'
    raise NotImplementedError

def sroot(c, b):
    'superroot. idfk what this is supposed to be in terms of code'
    raise NotImplementedError

def hyper(
        left: Number, 
        right: Number, 
        n: int, 
        solve: Literal['a', 'b', 'c'] = 'c', 
        ) -> Number:
    match solve:
        case 'a':
            match n:
                case 0: raise ArithmeticError('this operation simply does not exist in mathematics')
                case 1: return h1a(left, right)
                case 2: return h2a(left, right)
                case 3: return h3a(left, right)
                case 4: return h4a(left, right)
                case _: raise NotImplementedError
        case 'b':
            match n:
                case 0: return h0b(right)
                case 1: return h1b(left, right)
                case 2: return h2b(left, right)
                case 3: return h3b(left, right)
                case 4: return h4b(left, right)
                case _: raise NotImplementedError
        case 'c':
            match n:
                case 0: return h0c(right)
                case 1: return h1c(left, right)
                case 2: return h2c(left, right)
                case 3: return h3c(left, right)
                case 4: return h4c(left, right)
                case _: raise NotImplementedError
        case _:
            raise ValueError("invalid solve parameter. must be one of {'a', 'b', 'c'}")
