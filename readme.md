im tired of having unpredictable math ops in my programs. so i made this cross-language swiss army knife of math stuff. 

# HOW IHNSTALL???!?!?

choose your language:
<details><summary>

## python </summary>

```
pip install swissmath
```
or
```
python -m pip install swissmath
```

</details>


# operators

<details open><summary>arithmetic</summary>

```
name      | explanation              | example
----------+--------------------------+--------------------------------
neg       | negative                 |             - 2 = -2
inv       | reciprocal               |             / 2 = 0.5
add       | binary addition          |          -5 + 2 = -3
sub       | binary subtraction       |          -5 - 2 = -7
mul       | binary multiplication    |          -5 * 2 = -10
div       | binary division          |          -5 / 2 = -2.5
pow       | binary exponentiation    |          -5 ^ 2 = 25
log       | binary logarithm         |       log(-5,2) = 2.322 + 4.532i
exp       | exponentiation base e    | 
exp2      | exponentiation base 2    | 
ln        | logarithm base e         | 
log2      | logarithm base 2         | 
log10     | logarithm base 10        | 
floordiv  | division rounded down    |  floordiv(-5,2) = -3
modulus   | remaining of floordiv    |   modulus(-5,2) = 1
quotient  | division rounded to zero |  quotient(-5,2) = -2
remainder | remaining of quotient    | remainder(-5,2) = -1

root
sqrt
cbrt
abs
floor
round
ceil
gcd
lcm
```
</details><details open><summary>comparative </summary>

```
name | explanation              | example  
-----+--------------------------+----------------
lt   | less than                | 2 <  3 is true 
le   | less than or equal to    | 2 <= 3 is true
eq   | equal to                 | 2 == 3 is false
ne   | not equal to             | 2 != 3 is true
ge   | greater than or equal to | 2 >= 3 is false
gt   | greater than             | 2  > 3 is false
``` 
</details><details open><summary>trigonometric </summary>

```
name | explanation           | example
-----+-----------------------+----------
sin  | circular sine         |  sin(1) = 0.8414709848
cos  | circular cosine       |  cos(1) = 0.54030230586
tan  | circular tangent      |  tan(1) = 1.55740772465
cot  | circular cotangent    |  cot(1) = 0.642093
sec  | circular secant       |  sec(1) = 1.85081571768
csc  | circular cosecant     |  csc(1) = 1.18839510578
asin | circular arcsine      | asin(1) = 1.57079633
acos | circular arccosine    | acos(1) = 0
atan | circular arctangent   | atan(1) = 0.785398163 
acot | circular arccotangent | acot(1) = 0.785398163
asec | circular arcsecant    | asec(1) = 0
acsc | circular arccosecant  | acsc(1) = 1.57079633
```
</details><details open><summary>hyperbolic </summary>

```
name  | explanation             | example
------+-------------------------+----------
sinh  | hyperbolic sine         | 1.1752012
cosh  | hyperbolic cosine       | 1.5430806
tanh  | hyperbolic tangent      | 0.7615942
coth  | hyperbolic cotangent    | 1.3130353
sech  | hyperbolic secant       | 0.6480543
csch  | hyperbolic cosecant     | 0.8509181
asinh | hyperbolic arcsine      | 0.88137359
acosh | hyperbolic arccosine    | 0
atanh | hyperbolic arctangent   | infinity
acoth | hyperbolic arccotangent | infinity
asech | hyperbolic arcsecant    | 0
acsch | hyperbolic arccosecant  | 0.88137359
```
</details><details open><summary>boolean </summary>

```
name  | explanation           | truth | example            
------+-----------------------+-------+-----------------
truth | truthiness            |    FT |           A =  A 
not   | negation              |    TF |          ¬F =  T  
and   | conjunction           |  FFFT |       F ∧ T =  F  
nimp  | not(imp)              |  FFTF |    ¬(F → T) =  F  
fst   | first                 |  FFTT |    fst(A,B) =  A  
ncon  | not(con)              |  FTFF |    ¬(F ← T) =  T  
snd   | second                |  FTFT |    snd(A,B) =  B  
xor   | exclusive disjunction |  FTTF |      F ⊕ T =  T 
or    | disjunction           |  FTTT |       F ∨ T =  T  
nor   | not(or)               |  TFFF |    ¬(F ∨ T) =  F  
xnor  | equivalence           |  TFFT |      F ⊙ T =  F 
nsnd  | not(snd)              |  TFTF | ¬(snd(A,B)) = ¬B  
con   | converse implication  |  TFTT |       F ← T =  F  
nfst  | not(fst)              |  TTFF | ¬(fst(F,T)) = ¬A
imp   | implication           |  TTFT |       F → T =  T  
nand  | not(and)              |  TTTF |    ¬(F ∧ T) =  T
```
</details><details open><summary>bitwise </summary>

```
name     | explanation           | truth | example
---------+-----------------------+-------+-----------------
bittruth | truthiness            |    01 |             A =  A 
bitnot   | negation              |    10 |            ~5 =  
bitand   | conjunction           |  0001 |         3 ∧ 5 =    
bitnimp  | not(imp)              |  0010 |      ¬(3 → 5) =    
bitfst   | first                 |  0011 |   bitfst(A,B) =  A  
bitncon  | not(con)              |  0100 |      ¬(3 ← 5) =    
bitsnd   | second                |  0101 |   bitsnd(A,B) =  B  
bitxor   | exclusive disjunction |  0110 |        3 ⊕ 5 =  
bitor    | disjunction           |  0111 |         3 ∨ 5 = 
bitnor   | not(or)               |  1000 |      ¬(3 ∨ 5) = 
bitxnor  | equivalence           |  1001 |        3 ⊙ 5 =  
bitnsnd  | not(snd)              |  1010 |  bitnsnd(A,B) = ¬B  
bitcon   | converse implication  |  1011 |         3 ← 5 =   
bitnfst  | not(fst)              |  1100 |  bitnfst(A,B) = ¬A
bitimp   | implication           |  1101 |         3 → 5 = 
bitnand  | not(and)              |  1110 |      ¬(3 ∧ 5) = 
bitleft  | left shift            |       |  bitleft(3,5) = 96
bitright | right shift           |       | bitright(3,5) = 0
```
</details><details open><summary>complex </summary>

```
name  | explanation    | example
------+----------------+---------------------------
real  | real part      | 
imag  | imaginary part | 
phase | argument       | 
conj  | conjugate      | 
```
</details><details open><summary>miscellaneous </summary>

```
name   | explanation                        | example
-------+------------------------------------+---------------------------
ipart  | integer part
fpart  | fractional part
fact   | factorial                          | 
sumt   | sumtorial (sum of all Z up to n)   | 
comb   | combinations                       | 
perm   | permutations                       | 
clamp  | restrict within [a,b]              |   clamp(1.2, 0, 0.8) = 0.8
lerp   | linear interpolation               |      lerp(0.5, 2, 3) = 2.5
unlerp | inverse of linear interpolation    |    unlerp(2.5, 2, 3) = 0.5
map    | map x in [a,b] to [c,d]            | map(2.5, 2, 3, 4, 5) = 4.5
sgn    | signum. -1 if <0, +1 if >0, else 0 | 
```

<!--
truncative ???
	floor: round down to nearest integer    floor(2.5) = 2
	round: to nearest integer, half to even round(2.5) = 2
	ceil : round up to nearest integer       ceil(2.5) = 3
	ipart: integer part      ipart(-2.5) = -2
	fpart: fractional part   fpart(-2.5) = 0.5


call, matmul, concat, is, is_not, any, all, len, range, reversed, sorted, divmod, min, max, floor, ceil, ipart, exp, exp2, log10, log2, log, sqrt, cbrt, comb, perm, fact, gamma, gcd, lcm, phase, mean, median, mode, var, stdev, inv
def ifelse(a,b,c):
def abs(*args):
def piecewise(*args):
def summation(*args):
def product(*args):
def sigma_summation(expr, var, lower, upper):
def pi_product(expr, var, lower, upper):
def det(a):
def transpose(a):
def dot_product(a, b):
def cross_product(a, b):
def limit():
def definite_integral():
def indefinite_integral():
def derivative():
def partial_derivative():
def sumt(x):

def pmean(data, p):
def rms(data):
#def aad(data, centre=_Literal['mean','median','mode'], measure=_):
#def pdev(data, p):

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


def _ifelse(a,b,c):
	'return b if a is true, otherwise return c'
	return b if a else c

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

def _dist(*args):
	'euclidean distance in n dimensions'
	from math import sqrt
	return sqrt(sum(arg**2 for arg in args))

#default = _DotDict()



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

# hello there! lol

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
#'erf'     : _math.erf
#'erfc'    : _math.erfc
#'in'      : 
#'notin'   : 
-->


</details>

# constants
```
name | value
-----+-------------------------------
E    | 2.71828182845904523536...
PI   | 3.14159265358979323846...
TAU  | 6.28318530717958647692...
INF  | IEEE 754 inf
NAN  | IEEE 754 nan
```
and also the following SI constants because why tf not
```
name    | value (exact)
--------+----------------------------
SI_DVCS | 9192631770
SI_C    |  299792458
SI_H    |          6.62607015  *10^−34
SI_E    |          1.602176634 *10^−19
SI_K    |          1.380649    *10^−23
SI_NA   |          6.02214076  *10^+23
SI_KCD  |        683
```


# conversions

because i forget sometimes
```
mps_to_kmph
kmph_to_mps
celsius_to_fahrenheit
celsius_to_kelvin
celsius_to_rankine
fahrenheit_to_celsius
fahrenheit_to_kelvin
fahrenheit_to_rankine
kelvin_to_celsius
kelvin_to_fahrenheit
kelvin_to_rankine
rankine_to_celsius
rankine_to_fahrenheit
rankine_to_kelvin
```


ya thats pretty much it  

this project is convenience > predictability > features > performance so i dont really care how slow it does it, as long as it *does* it

motivation: sometimes i need the quotient of a division, but programs only give me truediv or floordiv. sometimes i juse need a neg function to use in a higher-order function, without resorting to a nameless lambda >:( sometimes i need floor and ceil. sometimes i need the min of a dataset. sometimes i want the mean of a database instead of writing sum/len

