# these operators dont treat nested lists as tensors. do you know why?
# because the tensor object should know itself how to do basic math ops. an operator is an operator.. an object should know what to do with an operator.
# its also because this tensor mechanism is hard to scale across languages

import math, cmath, functools
from numbers import Number, Real
from typing import Literal
from ..exceptions import DomainError

'''
instead of:
                     root   sroot
                      |      |
                     pow -- spow -- …
                   /
succ -- add -- mul   
 |       |      |  \
pred    sub    div   exp -- sexp -- …
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
def succ(b):
    'c = ++b, successor. the 0th hyperoperation'
    c = b + 1

    if type(c) != type(b):
        raise DomainError(succ, (b, ), c)

    return c
    
#h0b = functools.partial(h1b, x = 1)
def pred(c):
    'b = --c, predecessor. the inverse of the 0th hyperoperation'
    b = c - 1

    if type(b) != type(c):
        raise DomainError(pred, (c, ), b)

    return c
    
def add(a, b):
    'c = a + b, addition. the 1st hyperoperation'
    if type(a) != type(b):
        raise TypeError(f'{a} and {b} must be same type')

    c = a + b

    if type(a) != type(c):
        raise DomainError(add, (a, b), c)
    
    return c

def sub(c, a):
    'b = c - a, left subtraction. the inverse of the 1st hyperoperation'
    if type(c) != type(a):
        raise TypeError(f'{c} and {a} must be same type')
    
    b = c - a
    
    if type(b) != type(c):
        raise DomainError(sub, (c, a), b)
    
    return b

def mul(a, b):
    'c = a * b, multiplication. the 2nd hyperoperation'
    if type(a) != type(b):
        raise TypeError(f'{a} and {b} must be same type')

    c = a * b

    if type(c) != type(a):
        raise DomainError(mul, (a, b), c)
    
    return c

def div(c, a):
    'b = c / a, left division. the inverse of the 2nd hyperoperation'
    if type(c) != type(a):
        raise TypeError(f'{c} and {a} must be same type')

    if isinstance(a, int) and a % b != 0:
        raise DomainError
    b = c / a
    
    if type(b) != type(c):
        raise DomainError(div, (c, a), b)

    return b

def pow(a, b):
    'c = a ^ b, power, exponentiation. the 3rd hyperoperation'
    if type(a) != type(b):
        raise TypeError(f'{a} and {b} must be same type')

    c = a ** b
    
    if type(c) != type(a):
        raise DomainError(pow, (a, b), c)

    return c

def log(a, c):
    'b = log_a(c), logarithm. the inverse of the 3rd hyperoperation that solves for b'
    # c = a ^ b
    if type(a) != type(c):
        raise TypeError(f'{a} and {c} must be same type')

    try:
        b = math.log(c, a)
    except:
        b = cmath.log(c, a)

    if type(b) != type(a):
        raise DomainError(log, (a, c), b)

    return b
    
def root(b, c):
    'a = b √ c, n-th root. the inverse of the 3rd hyperoperation that solves for a'
    if type(b) != type(c):
        raise TypeError(f'{b} and {c} must be same type')
    # c = a ^ b
    a = c ** (1 / b)
    
    if type(a) != type(b):
        raise DomainError(root, (b, c), a)

    return a

def spow(a, b):
    'c = a ↑ b, tetration, superexponentiation, the 4th hyperoperation'
    if type(a) != type(b):
        raise TypeError(f'{a} and {b} must be same type')

    raise NotImplementedError
    
    if type(c) != type(a):
        raise DomainError(spow, (a, b), c)
    
    return c

def slog(a, c):
    'b = slog_a(c), superlogarithm, the inverse of the 4th hyperoperation'
    if type(a) != type(c):
        raise TypeError(f'{a} and {c} must be same type')

    raise NotImplementedError
    
    if type(b) != type(a):
        raise DomainError(slog, (a, c), b)
    
    return b

def sroot(b, c):
    'superroot. idfk what this is supposed to be in terms of code'
    if type(b) != type(c):
        raise TypeError(f'{b} and {c} must be same type')

    raise NotImplementedError

    if type(b) != type(a):
        raise DomainError(slog, (b, c), a)
    
    return a


'''
# this thing is just a novelty
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
'''
