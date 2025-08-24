im tired of having unpredictable math ops in my programs. so i made this cross-language swiss army knife of math stuff.
unlike other math libraries, this one isnt specialized to a domain so its the widest-reaching one as far as i know.

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
name      │ explanation              │ example
──────────┼──────────────────────────┼────────────────────────────────
neg       │ negative                 │             - 2 = -2
inv       │ reciprocal               │             / 2 = 0.5
add       │ binary addition          │          -5 + 2 = -3
sub       │ binary subtraction       │          -5 - 2 = -7
mul       │ binary multiplication    │          -5 × 2 = -10
div       │ binary division          │          -5 ÷ 2 = -2.5
pow       │ binary exponentiation    │             -5² = 25
log       │ binary logarithm         │       log(-5,2) ≈ 2.322 + 4.532𝑖
exp       │ exponentiation base e    │          exp(2) ≈ 7.389056098930
exp2      │ exponentiation base 2    │         exp2(2) = 4
ln        │ logarithm base e         │           ln(2) ≈ 0.693147180559
log2      │ logarithm base 2         │         log2(2) = 1
log10     │ logarithm base 10        │        log10(2) ≈ 0.30103
floordiv  │ division rounded to -∞   │  floordiv(-5,2) = -3
mod       │ modulus                  │       mod(-5,2) =  1
ceildiv   │ division rounded up      │   ceildiv(-5,2) = -2
ceilmod   │ remaining of ceilmod     │   ceilmod(-5,2) = -1
quotient  │ division rounded to zero │  quotient(-5,2) = -2
remainder │ remaining of quotient    │ remainder(-5,2) = -1
root      │ root to arbitrary base   │      root(-5,2) ≈ -2.23606797
sqrt      │ square root (²√x)        │         sqrt(2) ≈ 1.4142135
cbrt      │ cube root (³√x)          │         cbrt(3) ≈ 1.44224957
abs       │ absolute value           │       abs(2+3i) ≈ 3.6055512754
gcd       │ greatest common divisor  │        gcd(2,3) = 1
lcm       │ lowest common multiple   │        lcm(2,3) = 6
hyper     │ hyperoperation           │    hyper(1,2,3) = 5
```
</details><details open><summary>comparative </summary>

```
name │ explanation              │ example  
─────┼──────────────────────────┼────────────────
lt   │ less than                │ 2 <  3 is true 
le   │ less than or equal to    │ 2 <= 3 is true
eq   │ equal to                 │ 2 == 3 is false
ne   │ not equal to             │ 2 != 3 is true
ge   │ greater than or equal to │ 2 >= 3 is false
gt   │ greater than             │ 2  > 3 is false
```
</details><details open><summary>trigonometric </summary>

```
name │ explanation           │ example
─────┼───────────────────────┼─────────────────────────
sin  │ circular sine         │  sin(1) = 0.8414709848
cos  │ circular cosine       │  cos(1) = 0.54030230586
tan  │ circular tangent      │  tan(1) = 1.55740772465
cot  │ circular cotangent    │  cot(1) = 0.642093
sec  │ circular secant       │  sec(1) = 1.85081571768
csc  │ circular cosecant     │  csc(1) = 1.18839510578
asin │ circular arcsine      │ asin(1) = 1.57079633
acos │ circular arccosine    │ acos(1) = 0
atan │ circular arctangent   │ atan(1) = 0.785398163 
acot │ circular arccotangent │ acot(1) = 0.785398163
asec │ circular arcsecant    │ asec(1) = 0
acsc │ circular arccosecant  │ acsc(1) = 1.57079633
```
</details><details open><summary>hyperbolic </summary>

```
name  │ explanation             │ example
──────┼─────────────────────────┼──────────
sinh  │ hyperbolic sine         │ 1.1752012
cosh  │ hyperbolic cosine       │ 1.5430806
tanh  │ hyperbolic tangent      │ 0.7615942
coth  │ hyperbolic cotangent    │ 1.3130353
sech  │ hyperbolic secant       │ 0.6480543
csch  │ hyperbolic cosecant     │ 0.8509181
asinh │ hyperbolic arcsine      │ 0.88137359
acosh │ hyperbolic arccosine    │ 0
atanh │ hyperbolic arctangent   │ infinity
acoth │ hyperbolic arccotangent │ infinity
asech │ hyperbolic arcsecant    │ 0
acsch │ hyperbolic arccosecant  │ 0.88137359
```
</details><details open><summary>rounding </summary>
```
name                 │ explanation      │ example            
─────────────────────┼──────────────────┼──────────────────────────────────────
round_ceil           │ towards +∞       │           round_ceil(-2.5) = -2
round_floor          │ towards -∞       │          round_floor(-2.5) = -3
round_up             │ away from 0      │             round_up(-2.5) = -3
round_down           │ towards 0        │           round_down(-2.5) = -2
round_half_ceil      │ tie towards +∞   │      round_half_ceil(-2.5) = -2
round_half_floor     │ tie towards -∞   │     round_half_floor(-2.5) = -3
round_half_up        │ tie away from 0  │        round_half_up(-2.5) = -3
round_half_down      │ tie towards 0    │      round_half_down(-2.5) = -2
round_half_even      │ tie towards even │      round_half_even(-2.5) = -2
round_half_odd       │ tie towards odd  │       round
half_odd(-2.5) = -3
round_half_alternate │ tie alternated   │ round_half_alternate(-2.5) = -2 or -3
round_half_random    │ tie randomized   │    round_half_random(-2.5) = -2 or -3
round_stochastic     │ probabilistic    │     round_stochastic(-2.5) = -2 or -3
```
</details><details open><summary>boolean </summary>

```
name  │ explanation   │ truth │ example
──────┼───────────────┼───────┼──────────
truth │ proposition   │    01 │     P = P (for casting to boolean)
not   │ negation      │    10 │   ¬¬P = P
and   │ conjunction   │  0001 │ F ∧ T = F
nand  │ not(and)      │  1110 │ F ↑ T = T
or    │ disjunction   │  0111 │ F ∨ T = T
nor   │ not(or)       │  1000 │ F ↓ T = F
xor   │ exclusive or  │  0110 │ F ↮ T = T
xnor  │ not(xor)      │  1001 │ F ↔ T = F
imp   │ implication   │  1101 │ F → T = T
nimp  │ not(imp)      │  0010 │ F ↛ T = F
con   │ converse      │  1011 │ F ← T = F
ncon  │ not(con)      │  0100 │ F ↚ T = T
```
</details><details open><summary>bitwise </summary>
bitwise operators must support direct binary bit manipulation of the datatype. even if it is an IEEE float, operate directly on the physical bits, not the logical value. if the data is not stored in binary, raise an error (since boolean algebra is only a binary algebra)

```
name     │ explanation           │ truth │ example
─────────┼───────────────────────┼───────┼────────────────────
bittrue  │ all ones              │       │
bitfalse │ all zeroes            │       │
bittruth │ truthiness            │    01 │             A =  A 
bitnot   │ negation              │    10 │            ~5 =  
bitand   │ conjunction           │  0001 │         3 ∧ 5 =    
bitnimp  │ not(imp)              │  0010 │      ¬(3 → 5) =    
bitncon  │ not(con)              │  0100 │      ¬(3 ← 5) =   
bitxor   │ exclusive disjunction │  0110 │         3 ⊻ 5 =  
bitor    │ disjunction           │  0111 │         3 ∨ 5 = 
bitnor   │ not(or)               │  1000 │      ¬(3 ∨ 5) = 
bitxnor  │ equivalence           │  1001 │         3 ↔ 5 = 
bitcon   │ converse implication  │  1011 │         3 ← 5 =   
bitimp   │ implication           │  1101 │         3 → 5 = 
bitnand  │ not(and)              │  1110 │      ¬(3 ∧ 5) = 
lshift   │ left shift            │       │   lshift(3,5) = 96
rshift   │ right shift           │       │   rshift(3,5) = 0
```
</details><details open><summary>complex </summary>

```
name  │ explanation    │ example
──────┼────────────────┼──────────────────────────
real  │ real part      │ 
imag  │ imaginary part │ 
phase │ argument       │ 
conj  │ conjugate      │ 
```
</details><details open><summary>combinatorial </summary>

name     │ explanation                        │ example
─────────┼────────────────────────────────────┼──────────────────────────
fact     │ factorial                          │                   5! = 120
sumt     │ sumtorial (sum of all ℤ⁺ up to n)  │              sumt(5) = 15
comb     │ combinations                       │            comb(3,4) = 
perm     │ permutations                       │            perm(3,4) = 

</details><details open><summary>miscellaneous </summary>

```
name     │ explanation                        │ example
─────────┼────────────────────────────────────┼──────────────────────────
ipart    │ integer part                       │                ipart = 
fpart    │ fractional part                    │                fpart = 
clamp    │ restrict within [a,b]              │   clamp(1.2, 0, 0.8) = 0.8
in_range │ true if in [a,b] else false        │     bounded(2.5,0,1) = False
lerp     │ linear interpolation               │      lerp(0.5, 2, 3) = 2.5
unlerp   │ inverse of linear interpolation    │    unlerp(2.5, 2, 3) = 0.5
map      │ map x in [a,b] to [c,d]            │ map(2.5, 2, 3, 4, 5) = 4.5
sgn      │ signum. -1 if <0, +1 if >0, else 0 │             sgn(0.5) = 1
```
<!--


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
	'unary │mat│'
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
name │ value
─────┼──────────────────────────
E    │ 2.71828182845904523536...
PI   │ 3.14159265358979323846...
TAU  │ 6.28318530717958647692...
INF  │ IEEE 754 inf
NAN  │ IEEE 754 nan
```
and also the following SI constants because why tf not
```
name    │ value (exact)
────────┼─────────────────────────────
SI_DVCS │ 9192631770
SI_C    │  299792458
SI_H    │          6.62607015  *10^−34
SI_E    │          1.602176634 *10^−19
SI_K    │          1.380649    *10^−23
SI_NA   │          6.02214076  *10^+23
SI_KCD  │        683
```

# characters
```
name                       │ value
───────────────────────────┼──────────────────────────
double_struck_number       │ 𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡
latin                      │ ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
greek                      │ ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρσςτυφχψω
italic_latin               │ 𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍𝑎𝑏𝑐𝑑𝑒𝑓𝑔 𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝚤𝚥
italic_greek               │ 𝛢𝛣𝛤𝛥𝛦𝛧𝛨𝛩𝛪𝛫𝛬𝛭𝛮𝛯𝛰𝛱𝛲𝛴𝛵𝛶𝛷𝛸𝛹𝛺𝛼𝛽𝛾𝛿𝜀𝜁𝜂𝜃𝜄𝜅𝜆𝜇𝜈𝜉𝜊𝜋𝜌𝜍𝜎𝜏𝜐𝜑𝜒𝜓𝜔𝛳𝛻𝜕𝜖𝜗𝜘𝜙𝜚𝜛
double_struck_latin        │ 𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫
double_struck_greek        │   ℾ            ℿ ⅀        ℽ            ℼ   
double_struck_italic_latin │  	ⅅ                         ⅆⅇ   ⅈⅉ
celsius                    │ ℃ (not same as °C)
fahrenheit                 │ ℉ (not same as °F)
kelvin                     │ K (not same as K)
dot_product                │ ⋅ (not same as ·)
cross_product              │ × (not same as x)
division                   │ ÷ 
truth                      │ ⊤ (not same as T)
falsity                    │ ⊥
negation                   │ ¬ 
conjunction                │ ∧ (not same as ^)
disjunction                │ ∨ (not same as v)
implication                │ → (not same as ->)
equivalence                │ ↔ (not same as <->)
n_ary_conjunction          │ ⋀ (not same as ∧)
n_ary_disjunction          │ ⋁ (not same as ∨)
angstrom                   │ Å (not same as Å) (non-conventional)
information                │ ℹ (not same as i)
numero                     │ № 
eulers_number              │ ℯ (not same as e)
euler_constant             │ ℇ (non-conventional)
planck_constant            │ ℎ (not same as h)
planck_constant_reduced    │ ℏ (not same as h̶)
ohm                        │ Ω 
mho                        │ ℧ 
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

