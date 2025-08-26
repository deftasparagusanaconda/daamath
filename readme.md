im tired of having unpredictable math ops in my programs. so i made this cross-language swiss army knife of math stuff.
unlike other math libraries, this one isnt specialized to a domain so its the widest-reaching one as far as i know.

# HOW IHNSTALL???!?!?

choose your language:
<details><summary>

## python </summary>

(NOT IMPLEMENTED YET)

install the python package through PyPI:

```
pip install swissmath
```
or
```
python -m pip install swissmath
```

</details><details><summary>

## java </summary>

(NOT IMPLEMENTED YET)

swissmath will be available as a java package. but im not sure where to host it yet

</details>

# operators

<details open><summary>arithmetic</summary>

complex numbers are fully supported but type will not always be promoted to complex. for example, log will promote to complex only when negative input is given. or sqrt(-4) will appropriately promote to a complex 2𝑖

```
name      │ explanation              │ example
──────────┼──────────────────────────┼────────────────────────────────
neg       │ negative                 │             - 2 = -2
recip     │ reciprocal               │             / 2 = 0.5
add       │ binary addition          │          -5 + 2 = -3
sub       │ binary subtraction       │          -5 - 2 = -7
mul       │ binary multiplication    │          -5 × 2 = -10
div       │ binary division          │          -5 ÷ 2 = -2.5
pow       │ binary exponentiation    │             -5² = 25
log       │ binary logarithm         │       log(-5,2) ≈ 2.322 + 4.532𝑖
floordiv  │ division rounded to -∞   │  floordiv(-5,2) = -3
mod       │ modulus                  │       mod(-5,2) =  1
quotient  │ division rounded to zero │  quotient(-5,2) = -2
remainder │ remaining of quotient    │ remainder(-5,2) = -1
exp       │ exponentiation base e    │          exp(2) ≈ 7.389056098930
exp2      │ exponentiation base 2    │         exp2(2) = 4
exp10     │ exponentiation base 10   │        exp10(2) = 100
expm1     │ exp(x)-1                 │        expm1(2) ≈ 6.38905609893065
exp2m1    │ exp2(x)-1                │       exp2m1(2) = 3
exp10m1   │ exp10(x)-1               │      exp10m1(2) = 99
hypot     │ euclidean norm           │  hypot(1, 2, 3) ≈ 3.7416573867739413
ln        │ logarithm base e         │           ln(2) ≈ 0.693147180559
log2      │ logarithm base 2         │         log2(2) = 1
log10     │ logarithm base 10        │        log10(2) ≈ 0.30103
lnp       │ ln(x+1)                  │          lnp(2) ≈ 1.0986122886681096
log2p     │ log2(x+1)                │        log2p(2) ≈ 1.584962500721156
log10p    │ log10(x+1)               │       log10p(2) ≈ 0.47712125471966244
root      │ root to arbitrary base   │      root(-5,2) ≈ -2.23606797
sqrt      │ square root (²√x)        │         sqrt(2) ≈ 1.4142135623730951
cbrt      │ cube root (³√x)          │         cbrt(2) ≈ 1.2599210498948732
rsqrt     │ reciprocal of sqrt(x)    │        rsqrt(2) ≈ 0.7071067811865475
rcbrt     │ reciprocal of cbrt(x)    │        rcbrt(2) ≈ 0.7937005259840997
abs       │ absolute value           │       abs(2+3i) ≈ 3.6055512754
gcd       │ greatest common divisor  │        gcd(2,3) = 1
lcm       │ lowest common multiple   │        lcm(2,3) = 6
hyper     │ hyperoperation           │  hyper(1, 2, 3) = 5
ieee_div  │ IEEE-754-style division  │   ieee_div(0,0) = QNAN
```
</details><details open><summary>comparative </summary>

```
name │ explanation              │ example  
─────┼──────────────────────────┼────────────────
lt   │ less than                │ 2 < 3 is true 
le   │ less than or equal to    │ 2 ≤ 3 is true
eq   │ equal to                 │ 2 = 3 is false
ne   │ not equal to             │ 2 ≠ 3 is true
ge   │ greater than or equal to │ 2 ≥ 3 is false
gt   │ greater than             │ 2 > 3 is false
```
</details><details open><summary>trigonometric </summary>

basic set:
```
name    │ explanation           │ example
────────┼───────────────────────┼─────────────────────────
sin     │ circular sine         │       sin(1) ≈ 0.8414709848
cos     │ circular cosine       │       cos(1) ≈ 0.54030230586
tan     │ circular tangent      │       tan(1) ≈ 1.55740772465
cot     │ circular cotangent    │       cot(1) ≈ 0.642093
sec     │ circular secant       │       sec(1) ≈ 1.85081571768
csc     │ circular cosecant     │       csc(1) ≈ 1.18839510578
asin    │ circular arcsine      │      asin(1) ≈ 1.57079633
acos    │ circular arccosine    │      acos(1) = 0
atan    │ circular arctangent   │      atan(1) ≈ 0.785398163
atan2   │ IEEE atan2            │   atan2(1,1) ≈ 0.785398163
acot    │ circular arccotangent │      acot(1) ≈ 0.785398163
asec    │ circular arcsecant    │      asec(1) = 0
acsc    │ circular arccosecant  │      acsc(1) ≈ 1.57079633
sinpi   │ sin(𝜋x)               │     sinpi(1) = 0
cospi   │ cos(𝜋x)               │     cospi(1) = -1
tanpi   │ tan(𝜋x)               │     tanpi(1) = 0
cotpi   │ cot(𝜋x)               │     cotpi(1) = ?
secpi   │ sec(𝜋x)               │     secpi(1) = -1
cscpi   │ csc(𝜋x)               │     cscpi(1) = ?
asinpi  │ asin(y)/𝜋             │    asinpi(1) = 0.5
acospi  │ acos(y)/𝜋             │    acospi(1) = 0
atanpi  │ atan(y)/𝜋             │    atanpi(1) = 0.25
atan2pi │ IEEE atan2/𝜋          │ atan2pi(1,1) = 0.25
acotpi  │ acot(y)/𝜋             │    acotpi(1) = 0.25
asecpi  │ asec(y)/𝜋             │    asecpi(1) = 0
acscpi  │ acsc(y)/𝜋             │    acscpi(1) = 0.5
```

extra set:
```
name            │ explanation               │ formula
────────────────┼───────────────────────────┼──────────────────────────────────────────────────────────
versin          │ versed sine               │          versin(x) = 1 - cos(x)
vercos          │ versed cosine             │          vercos(x) = 1 + cos(x)
coversin        │ co versed sine            │        coversin(x) = 1 - sin(x)
covercos        │ co versed cosine          │        covercos(x) = 1 + sin(x)
haversin        │ half versed sine          │        haversin(x) = (1 - cos(x))/2
havercos        │ half versed cosine        │        havercos(x) = (1 + cos(x))/2
hacoversin      │ half co versed sine       │      hacoversin(x) = (1 - sin(x))/2
hacovercos      │ half co versed cosine     │      hacovercos(x) = (1 + sin(x))/2
exsec           │ external secant           │           exsec(x) = sec(x) - 1
excsc           │ external cosecant         │           excsc(x) = csc(x) - 1
chord           │ chord length              │           chord(x) = 2 * sin(x/2)
arcchord        │ arc chord length          │        arcchord(y) = 2 * arcsin(x/2)
arcversin       │ arc versed sine           │       arcversin(y) = arccos(1-y)
arcvercos       │ arc versed cosine         │       arcvercos(y) = arccos(y-1)
arccoversin     │ arc co versed sine        │     arccoversin(y) = arcsin(1-y)
arccovercos     │ arc co versed cosine      │     arccovercos(y) = arcsin(y-1)
archaversin     │ arc half versed sine      │     archaversin(y) = arccos(1-2y)
archavercos     │ arc half versed cosine    │     archavercos(y) = arccos(2y-1)
archacoversin   │ arc half co versed sine   │   archacoversin(y) = arcsin(1-2y)
archacovercos   │ arc half co versed cosine │   archacovercos(y) = arcsin(2y-1)
versinpi        │ versin(𝜋x)                │        versinpi(x) = 1 - cos(𝜋x)
vercospi        │ vercos(𝜋x)                │        vercospi(x) = 1 + cos(𝜋x)
coversinpi      │ coversin(𝜋x)              │      coversinpi(x) = 1 - sin(𝜋x)
covercospi      │ covercos(𝜋x)              │      covercospi(x) = 1 + sin(𝜋x)
haversinpi      │ haversin(𝜋x)              │      haversinpi(x) = (1 - cos(𝜋x))/2
havercospi      │ havercos(𝜋x)              │      havercospi(x) = (1 + cos(𝜋x))/2
hacoversinpi    │ hacoversin(𝜋x)            │    hacoversinpi(x) = (1 - sin(𝜋x))/2
hacovercospi    │ hacovercos(𝜋x)            │    hacovercospi(x) = (1 + sin(𝜋x))/2
exsecpi         │ exsec(𝜋x)                 │         exsecpi(x) = sec(𝜋x) - 1
excscpi         │ excsc(𝜋x)                 │         excscpi(x) = csc(𝜋x) - 1
chordpi         │ chord(𝜋x)                 │         chordpi(x) = 2 * sin(𝜋x/2)
arcchordpi      │ arcchord(y)/𝜋             │      arcchordpi(y) = 2 * arcsin(𝜋x/2)
arcversinpi     │ arcversin(y)/𝜋            │     arcversinpi(y) = arccos(1-y)/𝜋
arcvercospi     │ arcvercos(y)/𝜋            │     arcvercospi(y) = arccos(y-1)/𝜋
arccoversinpi   │ arccoversin(y)/𝜋          │   arccoversinpi(y) = arcsin(1-y)/𝜋
arccovercospi   │ arccovercos(y)/𝜋          │   arccovercospi(y) = arcsin(y-1)/𝜋
archaversinpi   │ archaversin(y)/𝜋          │   archaversinpi(y) = arccos(1-2y)/𝜋
archavercospi   │ archavercos(y)/𝜋          │   archavercospi(y) = arccos(2y-1)/𝜋
archacoversinpi │ archacoversin(y)/𝜋        │ archacoversinpi(y) = arcsin(1-2y)/𝜋
archacovercospi │ archacovercos(y)/𝜋        │ archacovercospi(y) = arcsin(2y-1)/𝜋
```
currently i dont see a formula for arcexsec and arcexcsc yet. if you find one please let me know!

</details><details open><summary>hyperbolic </summary>

```
name  │ explanation             │ example
──────┼─────────────────────────┼───────────
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

an unified `round` function is intentionally not provided because a programmer often has to assume what kind of rounding is being used. this is not good
```
name                 │ explanation      │ example            
─────────────────────┼──────────────────┼──────────────────────────────────────
round_ceil           │ towards +∞       │           round_ceil(-2.5) = -2
round_floor          │ towards -∞       │          round_floor(-2.5) = -3
round_away           │ away from 0      │           round_away(-2.5) = -3
round_trunc          │ towards 0        │          round_trunc(-2.5) = -2
round_half_ceil      │ tie towards +∞   │      round_half_ceil(-2.5) = -2
round_half_floor     │ tie towards -∞   │     round_half_floor(-2.5) = -3
round_half_away      │ tie away from 0  │      round_half_away(-2.5) = -3
round_half_trunc     │ tie towards 0    │     round_half_trunc(-2.5) = -2
round_half_even      │ tie towards even │      round_half_even(-2.5) = -2
round_half_odd       │ tie towards odd  │       round_half_odd(-2.5) = -3
round_half_alternate │ tie alternated   │ round_half_alternate(-2.5) = -2 or -3
round_half_random    │ tie randomized   │    round_half_random(-2.5) = -2 or -3
round_stochastic     │ probabilistic    │     round_stochastic(-2.5) = -2 or -3
```
</details><details open><summary>boolean </summary>

`truth` is for casting something to a boolean. thus the other operators shall not allow non-boolean input

```
name  │ explanation   │ truth │ example
──────┼───────────────┼───────┼──────────
truth │ proposition   │    01 │     P = P
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

bitwise operators must support direct binary bit manipulation of the datatype. even if it is an IEEE float, operate directly on the physical bits, not the logical value. if the data is not stored in binary, raise an error (since boolean algebra is only a binary algebra). thus whether `bitnot` is according to two's complement or not is up to the implementation

`bittruth` is for casting some datatype to an iterable of booleans which represent its bits. the array will store most significant digit first

```
name     │ explanation  │ truth │ example
─────────┼──────────────┼───────┼──────────
bittruth │ proposition  │    01 │     5 = [⊤, ⊥, ⊤]
bitnot   │ negation     │    10 │   ~-5 = (probably 2)
bitand   │ conjunction  │  0001 │ 3 ∧ 5 = 
bitnand  │ not(and)     │  1110 │ 3 ↑ 5 = 
bitor    │ disjunction  │  0111 │ 3 ∨ 5 = 
bitnor   │ not(or)      │  1000 │ 3 ↓ 5 = 
bitxor   │ exclusive or │  0110 │ 3 ↮ 5 = 
bitxnor  │ not(xor)     │  1001 │ 3 ↔ 5 = 
bitimp   │ implication  │  1101 │ 3 → 5 = 
bitnimp  │ not(imp)     │  0010 │ 3 ↛ 5 = 
bitcon   │ converse     │  1011 │ 3 ← 5 = 
bitncon  │ not(con)     │  0100 │ 3 ↚ 5 = 
lshift   │ left shift   │       │ lshift(3,5) = 96
rshift   │ right shift  │       │ rshift(3,5) = 0
```
</details><details open><summary>complex </summary>

```
name  │ explanation    │ example
──────┼────────────────┼─────────────────────────
real  │ real part      │  real(2+3𝑖) = 2
imag  │ imaginary part │  imag(2+3𝑖) = 3
phase │ argument       │ phase(2+3𝑖) ≈ 0.98279372
conj  │ conjugate      │  conj(2+3𝑖) = 2-3𝑖 
```
</details><details open><summary>combinatorial </summary>

```
name     │ explanation                        │ example
─────────┼────────────────────────────────────┼──────────────────────────
fact     │ factorial                          │                   5! = 120
sumt     │ sumtorial (sum of all ℤ⁺ up to n)  │              sumt(5) = 15
comb     │ combinations                       │            comb(3,4) = 
perm     │ permutations                       │            perm(3,4) = 
```
</details><details open><summary>intervals </summary>

the `in_*_interval` functions are simply for readability, for when sometimes `in_open_range(x, a, b)` is easier to understand than `a < x < b`

```
name                   │ explanation                        │ example
───────────────────────┼────────────────────────────────────┼──────────────────────────────────────
clamp                  │ restrict within [a,b]              │            clamp(1.2, 0, 0.8) = 0.8
in_open_interval       │ a < x < b                          │       in_open_interval(3,1,3) = False
in_closed_interval     │ a ≤ x ≤ b                          │     in_closed_interval(3,1,3) = True
in_left_open_interval  │ a < x ≤ b                          │  in_left_open_interval(3,1,3) = True
in_right_open_interval │ a ≤ x < b                          │ in_right_open_interval(3,1,3) = False
lerp                   │ linear interpolation               │               lerp(0.5, 2, 3) = 2.5
unlerp                 │ inverse of linear interpolation    │             unlerp(2.5, 2, 3) = 0.5
map                    │ map x in [a,b] to [c,d]            │          map(2.5, 2, 3, 4, 5) = 4.5
```
</details><details open><summary>miscellaneous </summary>

`frange` is like numpy's `arange`
`parity` should operate on the direct bits of the datatype

```
name     │ explanation                            │ example
─────────┼────────────────────────────────────────┼──────────────────────────────────────────
signbit  │ false if +ve else true                 │          signbit(3) = T
copysign │ magnitude of a with sign of b          │      copysign(2, 3) = 2
any      │ n-ary OR gate                          │        any(F, T, F) = T
all      │ n-ary AND gate                         │        all(F, T, F) = F
min      │ minimum                                │        min(1, 2, 3) = 1
max      │ maximum                                │        max(1, 2, 3) = 3
fst      │ first element                          │        fst(1, 2, 3) = 1
snd      │ second element                         │        snd(1, 2, 3) = 2
sgn      │ signum. -1 if <0, +1 if >0, else 0     │            sgn(0.5) = 1
swap     │ swap variables in memory               │          swap(a, b) = (b, a)
parity   │ sum of 1 bits                          │           parity(5) = 2
frange   │ iterable of numbers in an interval     │  frange(0, 10, 2.5) = [0, 2.5, 5, 7.5]
linspace │ fixed number of numbers in an interval │ 
isinf    │ true if IEEE inf                       │ isinf(float('inf')) = True
isnan    │ true if IEEE nan                       │ isnan(float('nan')) = False
erf      │ error function                         │              erf(1) ≈ 0.8427007929497149
erfc     │ 1-erf(x)                               │             erfc(1) ≈ 0.15729920705028513
gamma    │ gamma function                         │          gamma(1.5) ≈ 0.886226925452758
lgamma   │ natural logarithm of gamma(x)          │         lgamma(999) ≈ 5898.313668430534
```

</details><details open><summary>statistics </summary>

```
name   │ explanation           │ example
───────┼───────────────────────┼──────────────────────────
mean   │ arithmetic mean       │ 
median │ middlemost element    │ 
mode   │ most frequent element │ 
gmean  │ geometric mean        │ 
hmean  │ harmonic mean         │ 
pmean  │ power mean            │ 
rms    │ root mean squared     │ 
var    │ variance              │ 
stdev  │ standard deviation    │ 
erf    │ error function        │ 
```

</details><details open><summary>fused operations </summary>

`fma` and `fms` are actual things but the rest are... well.. why not??
these operations do not actually aim to be accurate, theyre just convenient

```
name │ explanation   │ example │ formula
─────┼───────────────┼─────────┼──────────────────
faa  │ fused add add │         │ (a+b)+c
fas  │ fused add sub │         │ (a+b)-c
fam  │ fused add mul │         │ (a+b)*c
fad  │ fused add div │         │ (a+b)/c
fsa  │ fused sub add │         │ (a-b)+c
fss  │ fused sub sub │         │ (a-b)-c
fsm  │ fused sub mul │         │ (a-b)*c
fsd  │ fused sub div │         │ (a-b)/c
fma  │ fused mul add │         │ (a*b)+c
fms  │ fused mul sub │         │ (a*b)-c
fmm  │ fused mul mul │         │ (a*b)*c
fmd  │ fused mul div │         │ (a*b)/c
fda  │ fused div add │         │ (a/b)+c
fds  │ fused div sub │         │ (a/b)-c
fdm  │ fused div mul │         │ (a/b)*c
fdd  │ fused div div │         │ (a/b)/c
```
</details><details open><summary>vector </summary>

`neg` `inv` `add` `sub` are overloaded to support vectors
`mul` `div` are overloaded to perform scalar-and-vector operations

```
name              │ explanation              │ example 
──────────────────┼──────────────────────────┼─────────────────────
dot               │ dot product              │ (1,2,3)⋅(2,3,4) = 20
cross             │ cross product            │ (1,2,3)×(2,3,4) = (-1, 2,-1)
```

</details><details open><summary>matrix </summary>

`neg` `inv` `add` `sub` are overloaded to support matrices.
`mul` `div` are overloaded to perform scalar-and-matrix operations

```
name              │ explanation              │ example 
──────────────────┼──────────────────────────┼─────────
pinv              │ pseudoinverse            │ 
det               │ determinant              │ 
transpose         │ rows and columns swapped │ 
trace             │ sum of diagonal elements │ 
eigvals           │ eigenvalues              │
eigvecs           │ eigenvectors             │
eig               │ (eigvals(a), eigvecs(a)) │
matmul            │ matrix multiplication    │ 
matdiv            │ matrix division          │ 
hadmul            │ hadamard multiplication  │ 
haddiv            │ hadamard division        │ 
is_ragged         │                          │ 
is_square         │                          │ 
is_symmetric      │                          │ 
is_skew_symmetric │                          │ 
is_hermitian      │                          │

`hadpow` will not be provided until there is `matpow`
```

</details><details open><summary>tensor </summary>

`neg` `inv` `add` `sub` are overloaded to support tensors
`mul` `div` are overloaded to perform scalar-and-tensor operations

```
name      │ explanation   │ example 
──────────┼───────────────┼─────────
dimension │ dimensionality
```

<!--
call, matmul, concat, is, is_not, len, range, reversed, sorted, divmod,

def ifelse(a,b,c):
def piecewise(*args):
def summation(*args):
def product(*args):
def sigma_summation(expr, var, lower, upper):
def pi_product(expr, var, lower, upper):
def det(a):
def transpose(a):
def limit():
def definite_integral():
def indefinite_integral():
def derivative():
def partial_derivative():

#def aad(data, centre=_Literal['mean','median','mode'], measure=_):
#def pdev(data, p):

def _generalized_mean(p, *args):
	'returns the power mean for given p (first argument) (p=1: arithmetic, 0: geometric, -1: harmonic)'
	if p == 0:
		return _math.exp(sum(_math.log(x) for x in args)/len(args))
	return (sum(x**p for x in args)/len(args)) ** (1/p)

def _ifelse(a,b,c):
	'return b if a is true, otherwise return c'
	return b if a else c

def _piecewise(*args):
	'variadic([cond1, val1], [cond2, val2], ....)'
	raise NotImplementedError

def _sigma_summation(expr, var, lower, upper):
	'quadric Σ(expr, var, lower, upper)'
	return sum(expr(var=val) for value in range(lower, upper))

def _pi_product(expr, var, lower, upper):
	'quadric ∏(expr, var, lower, upper)'
	return _math.prod(expr(var=value) for value in range(lower, upper))

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

# miscellaneous
'len'     : _builtins.len,
'range'   : _builtins.range,
'reversed': _builtins.reversed,
'sorted'  : _builtins.sorted,
'divmod'  : _builtins.divmod,
'call'    : _operator.call,
'matmul'  : _operator.matmul,
'concat'  : _operator.concat,
'ifelse'  : _ifelse,
'is'      : _operator.is_,
'isnot'   : _operator.is_not,
#'in'      : 
#'notin'   : 
-->

</details>

# constants


```
name        │ explanation               │ value
────────────┼───────────────────────────┼───────────
E           │ euler's number            │ 2.71828182845904523536…
PI          │ archimedes' constant      │ 3.14159265358979323846…
TAU         │ PI*2                      │ 6.28318530717958647692…
EULER_GAMMA │ euler-mascheroni constant │ 0.57721566490153286060…
PHI         │ golden ratio              │ 1.61803398874989484820…
ZETA_3      │ apéry's constant          │ 1.20205690315959428539…
CATALAN     │ catalan's constant        │ 0.9159655941772190150…
OMEGA       │ omega constant            │ 0.56714329040978387299…
SQRT_2      │ pythagoras constant       │ 1.4142135623730951…
SQRT_3      │ square root of 3          │ 1.7320508075688772…
LN_2        │ natural logarithm of 2    │ 0.6931471805599453…
LN_10       │ natural logarithn of 10   │ 2.302585092994046…
POS_INF     │ IEEE 754 positive inf     │ +∞
NEG_INF     │ IEEE 754 negative inf     │ -∞
POS_ZERO    │ IEEE 754 positive zero    │ +0
NEG_ZERO    │ IEEE 754 negative zero    │ -0
QNAN        │ IEEE 754 quiet nan        │ qnan
SNAN        │ IEEE 754 signalling nan   │ snan
```
and also the following SI constants because why tf not
```
name    │ value (exact)
────────┼─────────────────────────────
SI_DVCS │ 9192631770
SI_C    │  299792458
SI_H    │          6.62607015  *10⁻³⁴
SI_E    │          1.602176634 *10⁻¹⁹
SI_K    │          1.380649    *10⁻²³
SI_NA   │          6.02214076  *10⁺²³
SI_KCD  │        683
```

# characters
```
name                       │ value
───────────────────────────┼────────────────────────────────────────────────────────────
number                     │ 0123456789↊↋
double_struck_number       │ 𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡
latin                      │ ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
greek                      │ ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρσςτυφχψω
italic_latin               │ 𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍𝑎𝑏𝑐𝑑𝑒𝑓𝑔 𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝚤𝚥
italic_greek               │ 𝛢𝛣𝛤𝛥𝛦𝛧𝛨𝛩𝛪𝛫𝛬𝛭𝛮𝛯𝛰𝛱𝛲𝛴𝛵𝛶𝛷𝛸𝛹𝛺𝛼𝛽𝛾𝛿𝜀𝜁𝜂𝜃𝜄𝜅𝜆𝜇𝜈𝜉𝜊𝜋𝜌𝜍𝜎𝜏𝜐𝜑𝜒𝜓𝜔𝛳𝛻𝜕𝜖𝜗𝜘𝜙𝜚𝜛
double_struck_latin        │ 𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫
double_struck_greek        │   ℾ            ℿ ⅀        ℽ            ℼ
double_struck_italic_latin │    ⅅ                         ⅆⅇ   ⅈⅉ
celsius                    │ ℃ (not same as °C)
fahrenheit                 │ ℉ (not same as °F)
kelvin                     │ K (not same as K) (do NOT use degree symbol °)
fahrenheit                 │ °R
dot_product                │ ⋅ (not same as ·)
cross_product              │ × (not same as x)
division                   │ ÷                 (unconventional. use /)
truth                      │ ⊤ (not same as T)
falsity                    │ ⊥
negation                   │ ¬
conjunction                │ ∧ (not same as ^)
disjunction                │ ∨ (not same as v)
implication                │ → (not same as ->)
equivalence                │ ↔ (not same as <->)
n_ary_conjunction          │ ⋀ (not same as ∧)
n_ary_disjunction          │ ⋁ (not same as ∨)
angstrom                   │ Å (not same as Å) (unconventional. use Å)
information                │ ℹ (not same as i)
numero                     │ № 
eulers_number              │ ℯ (not same as e) (unconventional. use e or 𝑒)
euler_constant             │ ℇ                 (unconventional. use γ or 𝛾)
planck_constant            │ ℎ (not same as h)
planck_constant_reduced    │ ℏ (not same as h̶)
ohm                        │ Ω 
mho                        │ ℧ 
```

use italic_latin and italic_greek when your software doesnt support italicizing. otherwise, use latin and greek and let it do the slanting thing for you  
the special symbols for constants and numbers like ℯ for euler's number are rarely used. if theres an italicized latin or greek version available, we (mathematicians) generally use those instead 

# conversions

because i forget sometimes
```
name                  │ formula
──────────────────────┼────────────────────────────────────────────────────────────
degree_to_radian      │ radian = degree * 𝜋 / 180
degree_to_turn        │   turn = degree / 360
radian_to_degree      │ degree = radian * 180 / 𝜋
radian_to_turn        │   turn = radian / 𝜏
turn_to_degree        │ degree = turn * 360
turn_to_radian        │ radian = turn * 𝜏
celsius_to_fahrenheit │ 
celsius_to_kelvin     │ 
celsius_to_rankine    │ 
fahrenheit_to_celsius │ 
fahrenheit_to_kelvin  │ 
fahrenheit_to_rankine │ 
kelvin_to_celsius     │ 
kelvin_to_fahrenheit  │ 
kelvin_to_rankine     │ 
rankine_to_celsius    │ 
rankine_to_fahrenheit │ 
rankine_to_kelvin     │ 
hour_to_time          │
```
ya :v thats pretty much it

this project is convenience > accuracy > predictability > features > performance so i dont really care how slow it does it, as long as it *does* it

motivation: sometimes i need the quotient of a division, but programs only give me truediv or floordiv. sometimes i juse need a neg function to use in a higher-order function, without resorting to a nameless lambda >:( sometimes i need floor and ceil. sometimes i need the min of a dataset. sometimes i want the mean of a database instead of writing sum/len

this project will take inspiration from [glm](https://github.com/icaven/glm) soon
