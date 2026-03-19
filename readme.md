<!-- implement something that can compare IEEE-754 values directly, instead of -0.0 == +0.0 being True, or nan(2) == nan(3) being False -->
<!-- implement something that can expose the direct bits of a datatype, like an int, float, char, str, etc -->
<!-- implement something that can generate a nan from a given integer payload-->
<!-- implement something that can take number prefixes like 0b 0d 0x 0t 0q 0o -->
<!-- bitwise ops should support: grouping (differentiates bitrev and byteswap), repr (2's complement by default) and floats should be treated as direct bits-->
<!-- daamath should have a strong no-aliases rule. that means no abs alias for norm, for example-->

a mathematician's spellbook. cross-language, highly predictable, highly mathematical

features: 
- cross-language consistency
- no implicit type promotion
- complete sets of functions
- mathematical unicode characters
- mathematical constants

# install

python:

```
pip install daamath
```

# functions

<details open><summary>hyperoperation</summary>

```
name        │ explanation              │ example
────────────┼──────────────────────────┼────────────────────────────────
inc         │ incrementation           │            ++3 =  4
dec         │ decrementation           │            --3 =  2
add         │ addition                 │          2 + 3 =  5
sub         │ subtraction              │          2 − 3 = −1
mul         │ multiplication           │          2 × 3 =  6
div         │ division                 │          2 ∕ 3 =  0.(6)
pow         │ exponentiation           │          2 ^ 3 =  8
log         │ logarithm                │        log₂(3) ≈ 1.58496250072
root        │ nᵗʰ root                 │            ²√3 ≈ 1.73205080757
spow        │ tetration                │     
slog        │ super-logarithm          │
sroot       │ super-root               │      
```

extra:

```
name        │ explanation              │ example
────────────┼──────────────────────────┼────────────────────────────────
ainv        │ additive inverse         │             −2 = −2
minv        │ multiplicative inverse   │             ⅟2 = 0.5
exp         │ exponentiation base 𝑒    │          e ^ 2 ≈ 7.389056098930
pow_2       │ exponentiation base 2    │          2 ^ 2 = 4
pow_10      │ exponentiation base 10   │         10 ^ 2 = 100
ln          │ logarithm base 𝑒         │        logₑ(2) ≈ 0.693147180559
log_2       │ logarithm base 2         │        log₂(2) = 1
log_10      │ logarithm base 10        │        log⏨(2) ≈ 0.30103
expm1       │ exp(a) − 1               │     exp(2) - 1 ≈ 6.38905609893065
ln1p        │ ln(1 + a)                │        ln(1p2) = 
parallel    │ parallel operator        │         −5 ∥ 2 = 3.(3)
gcd         │ greatest common divisor  │       gcd(2,3) = 1
lcm         │ lowest common multiple   │       lcm(2,3) = 6
hyper       │ hyperoperation           │   hyper(1,2,3) = 5
```

</details>
<details open><summary>rounding</summary>

```
name        │ explanation              │ example
────────────┼──────────────────────────┼────────────────────────────────
floor       │ round towards −∞         │       floor(1.5) = 1
ceil        │ round towards +∞         │        ceil(1.5) = 2
trunc       │ round towards 0          │       trunc(1.5) = 1
away        │ round away from 0        │        away(1.5) = 2
round       │ round to nearest integer │       round(1.5) = 2
round_floor │ tie break towards −∞     │ round_floor(1.5) = 1
round_ceil  │ tie break towards +∞     │  round_ceil(1.5) = 1
round_trunc │ tie break towards 0      │ round_trunc(1.5) = 1
round_away  │ tie break away from 0    │  round_away(1.5) = 1
round_even  │ tie break towards even   │  round_even(1.5) = 1
round_odd   │ tie break towards odd    │   round_odd(1.5) = 1
```

`mod(a, b)` is generalized by `rem(a, b, mode = floor)`
`abs(a)` is generalized by `norm_2(a)`
`sqrt(a)` is `root_2(a)`
`cbrt(a)` is `root_3(a)`

im not including these yet:
`floorp1`, `ceilm1`, `rsqrt`, `rcbrt`

if you need more exotic rounding or quantization, my [pyquantize](https://github.com/deftasparagusanaconda/pyquantize) tool does exactly that

`spow`, `sroot`, `sexp`, `slog` ~~are~~ will be based on kneser's extension  
`hyper` will not support non-integer inputs for n ≥ 4 (tetration and beyond). not until im smart enough to implement kneser's extension for these
commutative hyperoperations will be added once i have understood them enough to implement them. i like them much more anyway :P

</details>
<details open><summary>interval</summary>

```
name │ explanation   │ example  
─────┼───────────────┼────────────────────
lt   │ less than     │ 2 < 3 is true 
le   │ at most       │ 2 ≤ 3 is true
eq   │ equal to      │ 2 = 3 is false
ne   │ not equal to  │ 2 ≠ 3 is true
ge   │ at least      │ 2 ≥ 3 is false
gt   │ greater than  │ 2 > 3 is false
cc   │ in closed     │ 2 ∈ [2, 3] is true
co   │ in right-open │ 2 ∈ [2, 3) is true
oc   │ in left-open  │ 2 ∈ (2, 3] is false
oo   │ in open       │ 2 ∈ (2, 3) is false
```

`cmp` is generalized by `normalize`

</details><details open><summary>trigonometric </summary>

```
name  │ explanation             │ example
──────┼─────────────────────────┼────────────────────────────────────
csin  │ circular sine           │  csin(1) ≈ 0.8414709848
ccos  │ circular cosine         │  ccos(1) ≈ 0.54030230586
ctan  │ circular tangent        │  ctan(1) ≈ 1.55740772465
ccot  │ circular cotangent      │  ccot(1) ≈ 0.642093
csec  │ circular secant         │  csec(1) ≈ 1.85081571768
ccsc  │ circular cosecant       │  ccsc(1) ≈ 1.18839510578
acsin │ inverse csin            │ acsin(1) ≈ 1.57079633
accos │ inverse ccos            │ accos(1) = 0
actan │ inverse ctan            │ actan(1) ≈ 0.785398163
accot │ inverse ccot            │ accot(1) ≈ 0.785398163
acsec │ inverse csec            │ acsec(1) = 0
accsc │ inverse ccsc            │ accsc(1) ≈ 1.57079633
hsin  │ hyperbolic sine         │  hsin(1) ≈ 1.1752012
hcos  │ hyperbolic cosine       │  hcos(1) ≈ 1.5430806
htan  │ hyperbolic tangent      │  htan(1) ≈ 0.7615942
hcot  │ hyperbolic cotangent    │  hcot(1) ≈ 1.3130353
hsec  │ hyperbolic secant       │  hsec(1) ≈ 0.6480543
hcsc  │ hyperbolic cosecant     │  hcsc(1) ≈ 0.8509181
ahsin │ inverse hsin            │ ahsin(1) ≈ 0.88137359
ahcos │ inverse hcos            │ ahcos(1) = 0
ahtan │ inverse htan            │ ahtan(1) ≈ infinity
ahcot │ inverse hcot            │ ahcot(1) ≈ infinity
ahsec │ inverse hsec            │ ahsec(1) = 0
ahcsc │ inverse hcsc            │ ahcsc(1) ≈ 0.88137359
```

extra:

```
versin           │ versed sine               │           versin(x) = 1 − cos(x)
vercos           │ versed cosine             │           vercos(x) = 1 + cos(x)
coversin         │ co versed sine            │         coversin(x) = 1 − sin(x)
covercos         │ co versed cosine          │         covercos(x) = 1 + sin(x)
haversin         │ half versed sine          │         haversin(x) = (1 − cos(x))∕2
havercos         │ half versed cosine        │         havercos(x) = (1 + cos(x))∕2
hacoversin       │ half co versed sine       │       hacoversin(x) = (1 − sin(x))∕2
hacovercos       │ half co versed cosine     │       hacovercos(x) = (1 + sin(x))∕2
exsec            │ external secant           │            exsec(x) = sec(x) − 1
excsc            │ external cosecant         │            excsc(x) = csc(x) − 1
chord            │ chord length              │            chord(x) = 2 × sin(x∕2)
arcchord         │ arc chord length          │         arcchord(y) = 2 × arcsin(y∕2)
arcexsec         │ arc external secant       │         arcexsec(y) = arcsec(y+1)
arcexcsc         │ arc external cosecant     │         arcexcsc(y) = arccsc(y+1)
arcversin        │ arc versed sine           │        arcversin(y) = arccos(1−y)
arcvercos        │ arc versed cosine         │        arcvercos(y) = arccos(y−1)
arccoversin      │ arc co versed sine        │      arccoversin(y) = arcsin(1−y)
arccovercos      │ arc co versed cosine      │      arccovercos(y) = arcsin(y−1)
archaversin      │ arc half versed sine      │      archaversin(y) = arccos(1−2y)
archavercos      │ arc half versed cosine    │      archavercos(y) = arccos(2y−1)
archacoversin    │ arc half co versed sine   │    archacoversin(y) = arcsin(1−2y)
archacovercos    │ arc half co versed cosine │    archacovercos(y) = arcsin(2y−1)
atan2            │ IEEE atan2                │          atan2(1,1) ≈ 0.785398163
atan2pi          │ atan2∕𝜋                   │        atan2pi(1,1) = 
atan2tau         │ atan2∕𝜏                   │       atan2tau(1,1) = 
atan2d           │ atan2×360∕𝜏               │         atan2d(1,1) ≈ 
```

galilean trigonometric functions are not included because they are trivial, in that `sing(x) = x` and `cosg(x) = 1`

sinpi, sintau, sind, and other variants encourage bad mathematical literacy with radians. the function space also explodes combinatorially so i dont condone this

</details><details open><summary>logical </summary>

these logic gates are overloaded to perform bit-wise operations if int or float are given, and to perform set operations if set is given

```
name  │ explanation   │ truth │ example
──────┼───────────────┼───────┼──────────
not   │ negation      │    10 │    ¬⊤ = ⊥
and   │ conjunction   │  0001 │ ⊥ ∧ ⊤ = ⊥
or    │ disjunction   │  0111 │ ⊥ ∨ ⊤ = ⊤
xor   │ exclusive or  │  0110 │ ⊥ ⊻ ⊤ = ⊤
imp   │ implication   │  1101 │ ⊥ ⇒ ⊤ = ⊤
con   │ converse      │  1011 │ ⊥ ⇐ ⊤ = ⊥
nand  │ not(and)      │  1110 │ ⊥ ⊼ ⊤ = ⊤
nor   │ not(or)       │  1000 │ ⊥ ⊽ ⊤ = ⊥
nxor  │ not(xor)      │  1001 │ ⊥ ⊙ ⊤ = ⊥
nimp  │ not(imp)      │  0010 │ ⊥ ⇏ ⊤ = ⊥
ncon  │ not(con)      │  0100 │ ⊥ ⇍ ⊤ = ⊤
```

</details><details open><summary>complex </summary>

```
name  │ explanation    │ example
──────┼────────────────┼─────────────────────────
real  │ real part      │  real(2+3𝑖) = 2
imag  │ imaginary part │  imag(2+3𝑖) = 3
arg   │ argument       │   arg(2+3𝑖) ≈ 0.98279372
conj  │ conjugate      │  conj(2+3𝑖) = 2−3𝑖
```

`mag` is not implemented because `norm` already does that

</details><details open><summary>combinatorial </summary>

```
name     │ explanation  │ example
─────────┼──────────────┼────────────────
fact     │ factorial    │   5! = 120
sumt     │ sumtorial    │   sumt(5) = 15
comb     │ combinations │ comb(6,5) = 6
perm     │ permutations │ perm(6,5) = 720
```

`fact(x)` is not intended to take fractional input. use `gamma(x+1)` for that.

</details><details open><summary>bitwise </summary>

```
name         │ explanation                │ example
─────────────┼────────────────────────────┼────────────────
bitshift     │ bit-wise shift             │ bitshift(3,5) = 96
bitrev       │ bit-wise reverse           │   bitrev(3,5) = 
to_bitstring │ convert a datatype to bits │ 
popcount     │ hamming weight             │ popcount(5) = 2
parity       │ whether popcount(x)%2 == 1 │   parity(5) = False
ctz          │ count trailing zeroes      │ 
clz          │ count leading zeroes       │ 
lsb          │ lowest set bit             │ 
gray         │ convert to gray code       │ 
degray       │ inverse of gray            │ 
mask         │ bitmasking                 │ 
```

</details><details open><summary>intervals </summary>

```
name                   │ explanation              │ example
───────────────────────┼──────────────────────────┼──────────────────────────────────────
clamp                  │ restrict to [a,b]        │            clamp(1.2, 0, 0.8) = 0.8
lerp                   │ linear interpolation     │               lerp(2, 3, 0.5) = 2.5
plerp                  │ power-parameterized lerp │              plerp(2, 3, 0.5) = 
slerp                  │ spherical lerp           │              slerp(2, 3, 0.5) = 
unlerp                 │ inverse of lerp          │             unlerp(2, 3, 0.5) = 0.5
unplerp                │ inverse of plerp         │            unplerp(2, 3, 0.5) = 
unslerp                │ inverse of slerp         │            unslerp(2, 3, 0.5) = 
map                    │ map x in [a,b] to [c,d]  │          map(2.5, 2, 3, 4, 5) = 4.5
pmap                   │ plerp(unplerp(x,a,b,c,d) │         pmap(2.5, 2, 3, 4, 5) = 
smap                   │ slerp(unslerp(x,a,b,c,d) │         smap(2.5, 2, 3, 4, 5) = 
```

</details><details open><summary>miscellaneous </summary>

`frange` is like numpy's `arange`  
`linrange` is like numpy's `linrange`
`parity` should operate on the direct bits of the datatype

```
name      │ explanation                            │ example
──────────┼────────────────────────────────────────┼──────────────────────────────────────────
nan       │ create an IEEE 754 nan with payload    │              nan(3) = 0x
normalize │ normalize a vector                     │  normalize(1, 2, 3) ≈ (0.26726, 0.53452, 0.80178)
norm      │ Lp norm                                │       norm(1, 2, 3) ≈ 3.7416573867739413
signbit   │ false if +ve else true                 │          signbit(3) = T
copysign  │ magnitude of a with sign of b          │      copysign(2, 3) = 2
sgn       │ signum. −1 if <0, +1 if >0, else 0     │            sgn(0.5) = 1
swap      │ swap variables in memory               │          swap(a, b) = (b, a)
frange    │ iterable of numbers in an interval     │  frange(0, 10, 2.5) = [0, 2.5, 5, 7.5]
linspace  │ fixed number of numbers in an interval │ 
isinf     │ true if IEEE inf                       │ isinf(float('inf')) = True
isnan     │ true if IEEE nan                       │ isnan(float('nan')) = False
erf       │ error function                         │              erf(1) ≈ 0.8427007929497149
erfc      │ 1−erf(x)                               │             erfc(1) ≈ 0.15729920705028513
gamma     │ gamma function                         │          gamma(1.5) ≈ 0.886226925452758
lgamma    │ natural logarithm of gamma(x)          │         lgamma(999) ≈ 5898.313668430534
erf       │ error function                         │ 
cmpmap    │ p, q, r if a < b, a = b, a > b         │   
```
</details><details open><summary>aggregations </summary>

these collape an iterable into a single value

```
any       │ n-ary OR gate         │        any(F, T, F) = T
all       │ n-ary AND gate        │        all(F, T, F) = F
min       │ minimum               │        min(1, 2, 3) = 1
max       │ maximum               │        max(1, 2, 3) = 3
mean      │ arithmetic mean       │ 
median    │ middlemost element    │ 
mode      │ most frequent element │ 
gmean     │ geometric mean        │ 
hmean     │ harmonic mean         │ 
pmean     │ power mean            │ 
rms       │ root mean squared     │ 
var       │ variance              │ 
stdev     │ standard deviation    │ 
```

</details><details open><summary>collections </summary>

these are all pure functions and never mutate the original collection

```
length    │ how many elements
count     │ how many elements passing a predicate
concat    │ join iterables (join sequences in order)
contains  │ whether b is in a
isEmpty   │ whether collection is empty
isUnique  │ whether all elements are distinct
isLength  │ whether it has exactly n length
isCount   │ whether it has exactly n count
hasLength │ whether it has at least n length
hasCount  │ whether it has at least n count
```

concat is variadic

<details open><summary>sequences </summary>

```
head         │ first element
last         │ last element
tail         │ all except head
init         │ all except last
nth          │ element at n-th index
take         │ first n elements
drop         │ all except first n elements
slice        │ all elements from m to n
split_at     │ split by index
split_by     │ split by a predicate function
prepend      │ add an element to the start
append       │ add an element to the end
reversed     │ return a reversed version
sorted       │ return a sorted version
isSorted     │ if elements are sorted by an ordering predicate
isAscending  │ if sorted in ascending
isDescending │ if sorted in descending
```

</details><details open><summary>sets </summary>

operations like taking union, intersection, etc are already overloaded in the boolean functions

```
```

</details><details open><summary>vector </summary>

`neg` `inv` `add` `sub` are overloaded to support vectors  
`mul` `div` are overloaded to perform scalar-and-vector operations

```
name              │ explanation              │ example 
──────────────────┼──────────────────────────┼─────────────────────────────
dot               │ dot product              │ (1,2,3)⋅(2,3,4) = 20
cross             │ cross product            │ (1,2,3)×(2,3,4) = (−1, 2,−1)
```

</details><details open><summary>matrix </summary>

`neg` `inv` `add` `sub` are overloaded to support matrices  
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
```
`hadpow` will not be provided until there is `matpow`

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
name         │ explanation                      │ value                    
─────────────┼──────────────────────────────────┼──────────────────────────
OMEGA        │ omega constant                   │ ≈ 0.56714329040978387299…
GAMMA        │ euler-mascheroni constant        │ ≈ 0.57721566490153286060…
LN_2         │ natural logarithm of 2           │ ≈ 0.6931471805599453…
CATALAN      │ catalan's constant               │ ≈ 0.9159655941772190150…
ZETA_3       │ apéry's constant                 │ ≈ 1.20205690315959428539…
SQRT_2       │ pythagoras constant              │ ≈ 1.4142135623730951…
PHI          │ golden ratio                     │ ≈ 1.61803398874989484820…
SQRT_3       │ square root of 3                 │ ≈ 1.7320508075688772…
LN_10        │ natural logarithn of 10          │ ≈ 2.302585092994046…
E            │ euler's number                   │ ≈ 2.71828182845904523536…
PI           │ archimedes' constant             │ ≈ 3.14159265358979323846…
TAU          │ PI*2                             │ ≈ 6.28318530717958647692…
```

floating point:

```
POS_INF      │ IEEE 754 positive inf            │ +∞
NEG_INF      │ IEEE 754 negative inf            │ −∞
POS_ZERO     │ IEEE 754 positive zero           │ +0.0
NEG_ZERO     │ IEEE 754 negative zero           │ −0.0
NAN          │ IEEE 754 +ve qnan, payload = 0   │ nan
FLT_MAX      │ largest normal float             │ (2 − 2⁻²³) × 2⁺¹²⁷
FLT_MIN      │ smallest normal float            │ 2⁻¹²⁶
FLT_TRUE_MIN │ smallest subnormal float         │ 2⁻¹⁴⁹
DBL_MAX      │ largest normal double            │ (2 − 2⁻⁵²) × 2⁺¹⁰²³
DBL_MIN      │ smallest normal double           │ 2⁻¹⁰²²
DBL_TRUE_MIN │ smallest subnormal double        │ 2⁻¹⁰⁷⁴
```

more exotic 'nan' values are available by using `nan` in the miscellaneous functions section
<!--
SI_DVCS      │ hyperfine transition freq  │ 9192631770
SI_C         │ speed of light             │ 299792458
SI_H         │ planck constant            │ 6.62607015  × 10⁻³⁴
SI_E         │ elementary charge          │ 1.602176634 × 10⁻¹⁹
SI_K         │ boltzmann constant         │ 1.380649    × 10⁻²³
SI_NA        │ avogadro constant          │ 6.02214076  × 10⁺²³
SI_KCD       │ luminous efficacy          │ 683
-->

# characters

these tables are not just tabulations of unicode characters. their ordering and grouping gives them unique usefulness beyond just referring to a character by its name

```
name                                       │ value
───────────────────────────────────────────┼─────────────────────────── 
ASCII                                      │                                  !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ 
ASCII_SMALL                                │                                  ﹗ ﹟﹩﹪﹠ ﹙﹚﹡﹢﹐﹣﹒           ﹕﹔﹤﹦﹥﹖﹫                          ﹨                          ﹛ ﹜ 
ASCII_SUPERSCRIPT                          │                                         ⁽⁾ ⁺ ⁻  ⁰¹²³⁴⁵⁶⁷⁸⁹   ⁼   ᴬᴮꟲᴰᴱꟳᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾꟴᴿ ᵀᵁⱽᵂ         ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ𐞥ʳˢᵗᵘᵛʷˣʸᶻ     
ASCII_SUPERSCRIPT_SMALL                    │                                                                   𐞄    𐞒𐞖ᶦ 𞀹ᶫ𞀻ᶰ   𐞪 𞁀ᶸ   𐞲                                      
ASCII_SUBSCRIPT                            │                                         ₍₎ ₊ ₋  ₀₁₂₃₄₅₆₇₈₉   ₌                                   ₐ 𞁞 ₑ  ₕᵢⱼₖₗₘₙₒₚ ᵣₛₜᵤᵥ ₓ       
ASCII_VISIBLE                              │ ␀␁␂␃␄␅␆␇␈␉␊␋␌␍␎␏␐␑␒␓␔␕␖␗␘␙␚␛␜␝␞␟␠!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~␡
ASCII_FULLWIDTH                            │                                  ！＂＃＄％＆＇（）＊＋，－．／０１２３４５６７８９：；＜＝＞？＠ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ［＼］＾＿｀ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ｛｜｝～
<!-- ASCII_HALFWIDTH -->
                                           │
LATIN_UPPER                                │ ABCDEFGHIJKLMNOPQRSTUVWXYZ
LATIN_UPPER_SUPERSCRIPT                    │ ᴬᴮꟲᴰᴱꟳᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾꟴᴿ ᵀᵁⱽᵂ   
LATIN_UPPER_SUPERSCRIPT_SMALL              │  𐞄    𐞒𐞖ᶦ 𞀹ᶫ𞀻ᶰ   𐞪 𞁀ᶸ   𐞲 
LATIN_LOWER_SUPERSCRIPT                    │ ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ𐞥ʳˢᵗᵘᵛʷˣʸᶻ
LATIN_LOWER_SUBSCRIPT                      │ ₐ 𞁞 ₑ  ₕᵢⱼₖₗₘₙₒₚ ᵣₛₜᵤᵥ ₓ  
LATIN_LOWER                                │ abcdefghijklmnopqrstuvwxyz
LATIN_BOLD_UPPER                           │ 𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙
LATIN_BOLD_LOWER                           │ 𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳
LATIN_ITALIC_UPPER                         │ 𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍
LATIN_ITALIC_LOWER                         │ 𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧
LATIN_BOLD_ITALIC_UPPER                    │ 𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁
LATIN_BOLD_ITALIC_LOWER                    │ 𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛
LATIN_SCRIPT_UPPER                         │ 𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵
LATIN_SCRIPT_LOWER                         │ 𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏
LATIN_BOLD_SCRIPT_UPPER                    │ 𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩
LATIN_BOLD_SCRIPT_LOWER                    │ 𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃
LATIN_FRAKTUR_UPPER                        │ 𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ
LATIN_FRAKTUR_LOWER                        │ 𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷
LATIN_FRAKTUR_BOLD_UPPER                   │ 𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅
LATIN_FRAKTUR_BOLD_LOWER                   │ 𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟
LATIN_SANS_SERIF_UPPER                     │ 𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹
LATIN_SANS_SERIF_LOWER                     │ 𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓
LATIN_SANS_SERIF_BOLD_UPPER                │ 𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭
LATIN_SANS_SERIF_BOLD_LOWER                │ 𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇
LATIN_SANS_SERIF_ITALIC_UPPER              │ 𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡
LATIN_SANS_SERIF_ITALIC_LOWER              │ 𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻
LATIN_SANS_SERIF_BOLD_ITALIC_UPPER         │ 𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕
LATIN_SANS_SERIF_BOLD_ITALIC_LOWER         │ 𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯
LATIN_MONOSPACE_UPPER                      │ 𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉
LATIN_MONOSPACE_LOWER                      │ 𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣
LATIN_DOUBLE_STRUCK_UPPER                  │ 𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ
LATIN_DOUBLE_STRUCK_LOWER                  │ 𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫
LATIN_DOUBLE_STRUCK_ITALIC_UPPER           │    ⅅ                      
LATIN_DOUBLE_STRUCK_ITALIC_LOWER           │    ⅆⅇ   ⅈⅉ                
LATIN_UPPER_OUTLINED                       │ 𜳖𜳗𜳘𜳙𜳚𜳛𜳜𜳝𜳞𜳟𜳠𜳡𜳢𜳣𜳤𜳥𜳦𜳧𜳨𜳩𜳪𜳫𜳬𜳭𜳮𜳯
LATIN_PARENTHESIZED_LOWER                  │ ⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵
LATIN_CIRCLED_UPPER                        │ ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ
LATIN_CIRCLED_LOWER                        │ ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ 
                                           │
GREEK_UPPER                                │ ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩϜϺͶϷͰϘͲͿϚ
GREEK_UPPER_VARIANT                        │        ϴ                     ϞϠ  
GREEK_LOWER                                │ αβγδεζηθικλμνξοπρστυφχψωϝϻͷϸͱϙͳϳϛ
GREEK_LOWER_VARIANT                        │  ϐ  ϵ  ϑ ϰ     ϖϱς  ϕ        ϟϡ  
GREEK_LOWER_SUPERSCRIPT                    │  ᵝᵞᵟᵋ  ᶿᶥ           ᵠᵡ           
GREEK_LOWER_SUBSCRIPT                      │  ᵦᵧ             ᵨ   ᵩᵪ           
GREEK_BOLD_UPPER                           │ 𝚨𝚩𝚪𝚫𝚬𝚭𝚮𝚯𝚰𝚱𝚲𝚳𝚴𝚵𝚶𝚷𝚸𝚺𝚻𝚼𝚽𝚾𝚿𝛀𝟊        
GREEK_BOLD_UPPER_VARIANT                   │        𝚹                         
GREEK_BOLD_LOWER                           │ 𝛂𝛃𝛄𝛅𝛆𝛇𝛈𝛉𝛊𝛋𝛌𝛍𝛎𝛏𝛐𝛑𝛒𝛔𝛕𝛖𝛗𝛘𝛙𝛚𝟋        
GREEK_BOLD_LOWER_VARIANT                   │     𝛜  𝛝 𝛞     𝛡𝛠𝛓  𝛟            
GREEK_ITALIC_UPPER                         │ 𝛢𝛣𝛤𝛥𝛦𝛧𝛨𝛩𝛪𝛫𝛬𝛭𝛮𝛯𝛰𝛱𝛲𝛴𝛵𝛶𝛷𝛸𝛹𝛺         
GREEK_ITALIC_UPPER_VARIANT                 │        𝛳                         
GREEK_ITALIC_LOWER                         │ 𝛼𝛽𝛾𝛿𝜀𝜁𝜂𝜃𝜄𝜅𝜆𝜇𝜈𝜉𝜊𝜋𝜌𝜎𝜏𝜐𝜑𝜒𝜓𝜔         
GREEK_ITALIC_LOWER_VARIANT                 │     𝜖  𝜗 𝜘     𝜛𝜚𝜍  𝜙            
GREEK_BOLD_ITALIC_UPPER                    │ 𝜜𝜝𝜞𝜟𝜠𝜡𝜢𝜣𝜤𝜥𝜦𝜧𝜨𝜩𝜪𝜫𝜬𝜮𝜯𝜰𝜱𝜲𝜳𝜴         
GREEK_BOLD_ITALIC_UPPER_VARIANT            │        𝜭                         
GREEK_BOLD_ITALIC_LOWER                    │ 𝜶𝜷𝜸𝜹𝜺𝜻𝜼𝜽𝜾𝜿𝝀𝝁𝝂𝝃𝝄𝝅𝝆𝝈𝝉𝝊𝝋𝝌𝝍𝝎         
GREEK_BOLD_ITALIC_LOWER_VARIANT            │     𝝐  𝝑 𝝒     𝝕𝝔𝝇  𝝓            
GREEK_SANS_SERIF_BOLD_UPPER                │ 𝝖𝝗𝝘𝝙𝝚𝝛𝝜𝝝𝝞𝝟𝝠𝝡𝝢𝝣𝝤𝝥𝝦𝝨𝝩𝝪𝝫𝝬𝝭𝝮         
GREEK_SANS_SERIF_BOLD_UPPER_VARIANT        │        𝝧                         
GREEK_SANS_SERIF_BOLD_LOWER                │ 𝝰𝝱𝝲𝝳𝝴𝝵𝝶𝝷𝝸𝝹𝝺𝝻𝝼𝝽𝝾𝝿𝞀𝞂𝞃𝞄𝞅𝞆𝞇𝞈         
GREEK_SANS_SERIF_BOLD_LOWER_VARIANT        │     𝞊  𝞋 𝞌     𝞏𝞎𝞁  𝞍            
GREEK_SANS_SERIF_BOLD_ITALIC_UPPER         │ 𝞐𝞑𝞒𝞓𝞔𝞕𝞖𝞗𝞘𝞙𝞚𝞛𝞜𝞝𝞞𝞟𝞠𝞢𝞣𝞤𝞥𝞦𝞧𝞨         
GREEK_SANS_SERIF_BOLD_ITALIC_UPPER_VARIANT │        𝞡                         
GREEK_SANS_SERIF_BOLD_ITALIC_LOWER         │ 𝞪𝞫𝞬𝞭𝞮𝞯𝞰𝞱𝞲𝞳𝞴𝞵𝞶𝞷𝞸𝞹𝞺𝞼𝞽𝞾𝞿𝟀𝟁𝟂         
GREEK_SANS_SERIF_BOLD_ITALIC_LOWER_VARIANT │     𝟄  𝟅 𝟆     𝟉𝟈𝞻  𝟇            
GREEK_DOUBLE_STRUCK_UPPER                  │   ℾ            ℿ ⅀               
GREEK_DOUBLE_STRUCK_LOWER                  │   ℽ            ℼ                 
                                           │
DIGIT                                      │ 0123456789↊↋         
DIGIT_SUPERSCRIPT                          │ ⁰¹²³⁴⁵⁶⁷⁸⁹           
DIGIT_SUBSCRIPT                            │ ₀₁₂₃₄₅₆₇₈₉           
DIGIT_BOLD                                 │ 𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗           
DIGIT_DOUBLE_STRUCK                        │ 𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡           
DIGIT_SANS_SERIF                           │ 𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫           
DIGIT_SANS_SERIF_BOLD                      │ 𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵           
DIGIT_MONOSPACE                            │ 𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿           
DIGIT_SEGMENTED                            │ 🯰🯱🯲🯳🯴🯵🯶🯷🯸🯹           
DIGIT_OUTLINED                             │ 𜳰𜳱𜳲𜳳𜳴𜳵𜳶𜳷𜳸𜳹           
DIGIT_PARENTHESIZED                        │  ⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇
DIGIT_FULL_STOP                            │  ⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖⒗⒘⒙⒚⒛
DIGIT_CIRCLED                              │ ⓪①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳
DIGIT_CIRCLED_NEGATIVE                     │ ⓿❶❷❸❹❺❻❼❽❾❿⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴
DIGIT_CIRCLED_SANS_SERIF                   │  ➀➁➂➃➄➅➆➇➈➉          
DIGIT_CIRCLED_SANS_SERIF_NEGATIVE          │  ➊➋➌➍➎➏➐➑➒➓          
DIGIT_DOUBLE_CIRCLED                       │  ⓵⓶⓷⓸⓹⓺⓻⓼⓽⓾          
                                           │
ROMAN_NUMERAL_UPPER                        │  ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ        ⅬⅭⅮⅯ
ROMAN_NUMERAL_LOWER                        │  ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻ        ⅼⅽⅾⅿ
COUNTING_ROD_VERTICAL                      │ 〇𝍩𝍪𝍫𝍬𝍭𝍮𝍯𝍰𝍱
COUNTING_ROD_HORIZONTAL                    │ 〇𝍠𝍡𝍢𝍣𝍤𝍥𝍦𝍧𝍨
COUNTING_ROD_NEGATIVE                      │ (U+20E5)
TALLY_MARK                                 │  𝍷   𝍸
TALLY_MARK_IDEOGRAPHIC                     │  𝍲𝍳𝍴𝍵𝍶
DECIMAL_EXPONENT                           │ ⏨
HEBREW                                     │ ℵℶℷℸ
RECIPROCAL                                 │ ⅟
                                           │
FRACTION_0_BY                              │    ↉       
FRACTION_1_BY                              │   ½⅓¼⅕⅙⅐⅛⅑⅒
FRACTION_2_BY                              │    ⅔ ⅖     
FRACTION_3_BY                              │     ¾⅗  ⅜  
FRACTION_4_BY                              │      ⅘     
FRACTION_5_BY                              │       ⅚ ⅝  
FRACTION_7_BY                              │         ⅞  
INCREMENT                                  │ ∆
                                           │
NABLA                                      │ ∇
NABLA_BOLD                                 │ 𝛁
NABLA_ITALIC                               │ 𝛻
NABLA_BOLD_ITALIC                          │ 𝜵
NABLA_SANS_SERIF_BOLD                      │ 𝝯
NABLA_SANS_SERIF_BOLD_ITALIC               │ 𝞩
                                           │
PARTIAL                                    │ ∂
PARTIAL_BOLD                               │ 𝛛
PARTIAL_ITALIC                             │ 𝜕
PARTIAL_BOLD_ITALIC                        │ 𝝏
PARTIAL_SANS_SERIF_BOLD                    │ 𝞉
PARTIAL_SANS_SERIF_BOLD_ITALIC             │ 𝟃
                                           │
BRACKET_ROUND                              │ ()⏜⏝
BRACKET_ROUND_DOUBLE                       │ ⸨⸩
BRACKET_ROUND_WHITE                        │⦅ ⦆
BRACKET_ROUND_SMALL                        │ ﹙﹚
BRACKET_ROUND_SUPERSCRIPT                  │ ⁽⁾
BRACKET_ROUND_SUBSCRIPT                    │ ₍₎
BRACKET_ROUND_HALF_TOP                     │ ⹙⹚
BRACKET_ROUND_HALF_BOTTOM                  │ ⹛⹜
BRACKET_ROUND_FLATTENED                    │ ⟮⟯
BRACKET_ROUND_ORNATE                       │ ﴾﴿
BRACKET_ROUND_ORNAMENT_MEDIUM              │ ❨❩
BRACKET_ROUND_ORNAMENT_MEDIUM_FLATTENED    │ ❪❫
BRACKET_ROUND_FULLWIDTH                    │ （）
BRACKET_ROUND_FULLWIDTH_WHITE              │ ｟｠
BRACKET_ROUND_PRESENTATION                 │ ︵︶
BRACKET_ROUND_BIG                          │ ⎛⎜⎝⎞⎟⎠
                                           │
BRACKET_SQUARE                             │ []⎴⎵
BRACKET_SQUARE_WHITE                       │ ⟦⟧
BRACKET_SQUARE_BOTTOM_OVER_TOP             │ ⎶  (shouldnt... the top be over the bottom? xd)
BRACKET_SQUARE_QUILL                       │ ⁅⁆
BRACKET_SQUARE_UNDERBAR                    │ ⦋⦌
BRACKET_SQUARE_TICK_TOP                    │ ⦍⦐
BRACKET_SQUARE_TICK_BOTTOM                 │ ⦏⦎
BRACKET_SQUARE_STROKE                      │ ⹕⹖
BRACKET_SQUARE_STROKE_DOUBLE               │ ⹗⹘
BRACKET_SQUARE_FULLWIDTH                   │ ［］
BRACKET_SQUARE_FULLWIDTH_WHITE             │ 〚〛
BRACKET_SQUARE_PRESENTATION                │ ﹇﹈
BRACKET_SQUARE_BIG                         │ ⎡⎢⎣⎤⎥⎦
                                           │
BRACKET_CURLY                              │ {}⏞⏟
BRACKET_CURLY_WHITE                        │ ⦃⦄
BRACKET_CURLY_ORNAMENT_MEDIUM              │ ❴❵
BRACKET_CURLY_FULLWIDTH                    │ ｛｝
BRACKET_CURLY_SMALL                        │ ﹛﹜
BRACKET_CURLY_PRESENTATION                 │ ︷︸
BRACKET_CURLY_BIG                          │ ⎧⎨⎩⎫⎬⎭⎪⎰⎱
                                           │
BRACKET_ANGLE                              │ ⟨⟩
BRACKET_ANGLE_DOTTED                       │ ⦑⦒
BRACKET_ANGLE_CURVED                       │ ⧼⧽
BRACKET_ANGLE_FULLWIDTH                    │ ＜＞
BRACKET_ANGLE_FULLWIDTH                    │ 〈〉
BRACKET_ANGLE_PRESENTATION                 │ ︿﹀
                                           │
BRACKET_ANGLE_DOUBLE                       │ ⟪⟫
BRACKET_ANGLE_ORNAMENT_MEDIUM              │ ❬❭
BRACKET_ANGLE_ORNAMENT_HEAVY               │ ❰❱
BRACKET_QUOTATION_MARK_ORNAMENT_HEAVY      │ ❮❯
BRACKET_ANGLE_DOUBLE_FULLWIDTH             │ 《》
BRACKET_ANGLE_DOUBLE_PRESENTATION          │ ︽︾
                                           │
BRACKET_LENTICULAR_FULLWIDTH_BLACK         │ 【】
BRACKET_LENTICULAR_FULLWIDTH_WHITE         │ 〖〗
BRACKET_LENTICULAR_PRESENTATION_BLACK      │ ︻︼
BRACKET_LENTICULAR_PRESENTATION_WHITE      │ ︗︘
                                           │
BRACKET_TORTOISE_SHELL_BLACK               │ ⦗⦘⏠⏡
BRACKET_TORTOISE_SHELL_WHITE               │ ⟬⟭
BRACKET_TORTOISE_SHELL_SMALL               │ ﹝﹞
BRACKET_TORTOISE_SHELL_FULLWIDTH_BLACK     │ 〔〕
BRACKET_TORTOISE_SHELL_FULLWIDTH_WHITE     │ 〘〙
BRACKET_TORTOISE_SHELL_ORNAMENT_LIGHT      │ ❲❳
BRACKET_TORTOISE_SHELL_PRESENTATION        │ ︹︺
                                           │
BRACKET_CORNER_TOP                         │ ⌜⌝
BRACKET_CORNER_BOTTOM                      │ ⌞⌟
BRACKET_CORNER_DOT                         │ ⟓⟔
BRACKET_CORNER_HALFWIDTH                   │ ｢｣
BRACKET_CORNER_PRESENTATION                │ ﹁﹂
BRACKET_CORNER_PRESENTATION_WHITE          │ ﹃﹄
BRACKET_CORNER_FULLWIDTH                   │ 「」
BRACKET_CORNER_FULLWIDTH_WHITE             │ 『』
                                           │
BRACKET_CEIL                               │ ⌈⌉
BRACKET_FLOOR                              │ ⌊⌋
BRACKET_VERTICAL_BOX_LINE                  │ ⎸⎹
BRACKET_IMAGE                              │ ⦇⦈
BRACKET_BINDING                            │ ⦉⦊
BRACKET_ARC_INEQUALITY                     │ ⦓⦔
BRACKET_ARC_INEQUALITY_DOUBLE              │ ⦕⦖
BRACKET_WIGGLY_FENCE                       │ ⧘⧙
BRACKET_WIGGLY_FENCE_DOUBLE                │ ⧚⧛
BRACKET_HALF_TOP                           │ ⸢⸣
BRACKET_HALF_BOTTOM                        │ ⸤⸥
BRACKET_PARAPHRASE_LOW                     │ ⸜⸝
BRACKET_OGHAM_FEATHER                      │ ᚛᚜
BRACKET_GUG_RTAGS                          │ ༺༻
BRACKET_ANG_KHANG                          │ ༼༽
BRACKET_SUBSTITUTION                       │ ⸂⸃
BRACKET_SUBSTITUTION_DOTTED                │ ⸄⸅
BRACKET_TRANSPOSITION                      │ ⸉⸊
BRACKET_OMISSION_RAISED                    │ ⸌⸍
BRACKET_SIDEWAYS_U                         │ ⸦⸧
BRACKET_PRIME_QUOTATION_DOUBLE             │ 〝〞
BRACKET_GUILLEMET                          │ ‹›
BRACKET_GUILLEMET_DOUBLE                   │ «»
<!-- CROP                                       │ ⌌⌍⌎⌏ -->
                                           │
OPERATOR_RING                              │ ∘ (not same as °)
OPERATOR_ASTERISK                          │ ∗ (not same as *)
OPERATOR_BULLET                            │ ∙ (not same as .)
OPERATOR_TILDE                             │ ∼ (not same as ~)
OPERATOR_TILDE_REVERSED                    │ ∽
OPERATOR_DOT                               │ ⋅ (not same as ·)
OPERATOR_DOT_SQUARED                       │ ⊡
OPERATOR_DOT_CIRCLED                       │ ⊙
OPERATOR_DOT_CIRCLED_BIG                   │ ⨀ (not same as ⊙)
OPERATOR_REVERSE_SOLIDUS                   │ ⧵
OPERATOR_DIAMOND                           │ ⋄
OPERATOR_STAR                              │ ⋆
OPERATOR_TRIPLE_COLON                      │ ⫶
                                           │
FOR_ALL                                    │ ∀
COMPLEMENT                                 │ ∁
EXISTS                                     │ ∃
EXISTS_STROKE                              │ ∄
PROPORTIONAL                               │ ∝
INFINITY                                   │ ∞
ROOT                                       │ √∛∜
PRIME                                      │ ′″‴⁗
PRIME_REVERSED                             │ ‵‶‷
                                           │
WREATH_PRODUCT                             │ ≀
THEREFORE                                  │ ∴
BECAUSE                                    │ ∵
RATIO                                      │ ∶ (not same as :)
PROPORTION                                 │ ∷ (not same as ::)
ANGLE                                      │ ∠
                                           │
PLUS                                       │ +
PLUS_DOUBLE                                │ ⧺
PLUS_TRIPLE                                │ ⧻
PLUS_DOT                                   │ ∔
PLUS_UNDERBAR                              │ ±
PLUS_OVERBAR                               │ ∓
PLUS_OVERBAR_DOUBLE                        │ ⩱
PLUS_UNDERBAR_DOUBLE                       │ ⩲
PLUS_SQUARED                               │ ⊠
PLUS_CIRCLED                               │ ⊕
PLUS_BIG_CIRCLED                           │ ⨁ (not same as ⊕)
                                           │
BAR                                        │ − (minus)
TILDE                                      │ ~ 
TILDE_STROKE                               │ ≁
TILDE_REVERSE                              │ ∽
BAR_BAR                                    │ = (equals)
BAR_BAR_DOUBLED                            │ ⩵
BAR_BAR_TRIPLED                            │ ⩶
BAR_BAR_STROKE                             │ ≠
BAR_TILDE                                  │ ≂
TILDE_BAR                                  │ ≃
TILDE_BAR_STROKE                           │ ≄
TILDE_REVERSE_BAR                          │ ⋍
TILDE_TILDE                                │ ≈
TILDE_TILDE_STROKE                         │ ≉
BAR_BAR_BAR                                │ ≡
BAR_BAR_BAR_STROKE                         │ ≢
BAR_BAR_TILDE                              │ ⩳
TILDE_BAR_BAR                              │ ≅
TILDE_BAR_BAR_STROKE                       │ ≇≆
TILDE_REVERSE_BAR_BAR                      │ ≌
TILDE_BAR_TILDE                            │ ⩬
TILDE_TILDE_BAR                            │ ≊
TILDE_TILDE_TILDE                          │ ≋
BAR_BAR_BAR_BAR                            │ ≣
TILDE_TILDE_BAR_BAR                        │ ⩰
BAR_OVERDOT                                │ ∸
BAR_SQUARED                                │ ⊟
BAR_CIRCLED                                │ ⊖
                                           │
TIMES                                      │ × (not same as x)
TIMES_BIG                                  │ ⨉ (not same as ×)
TIMES_SQUARED                              │ ⊞
TIMES_CIRCLED                              │ ⊗
TIMES_BIG_CIRCLED                          │ ⨂ (not same as ⊗)
                                           │
DIVISION_SLASH                             │ ∕ (not same as /)
DIVISION_SIGN                              │ ÷ (unconventional. use ∕)
FRACTION                                   │ ⁄ (not same as ∕)
CROSS_PRODUCT                              │ ⨯ (not same as ×)
COPRODUCT                                  │ ⨿
INTERIOR_PRODUCT                           │ ⨼
INTERIOR_RIGHT                             │ ⨽
N_ARY_PRODUCT                              │ ∏
N_ARY_COPRODUCT                            │ ∐
N_ARY_SUMMATION                            │ ∑ (not same as Σ)
SET_MINUS                                  │ ∖
                                           │
WEDGE                                      │ <>∧∨
WEDGE_STROKE                               │ ≮≯
WEDGE_DASH                                 │   ⩜⩝
WEDGE_STEM                                 │   ⩚⩛
WEDGE_DOT                                  │ ⋖⋗⟑⟇
WEDGE_CIRCLE                               │ ⩹⩺
WEDGE_QUESTION_MARK                        │ ⩻⩼
WEDGE_OVERBAR                              │ ⋜⋝⊼⊽
WEDGE_OVERBAR_SLANT                        │ ⪕⪖
WEDGE_OVERBAR_SLANT_AND_DOT                │ ⪗⪘
WEDGE_OVERBAR_DOUBLE                       │ ⪙⪚⩞⩢
WEDGE_UNDERBAR                             │ ≤≥⩟⊻
WEDGE_UNDERBAR_SLANT                       │ ⩽⩾
WEDGE_UNDERBAR_DOUBLE                      │ ≦≧⩠⩣
WEDGE_STROKE_UNDERBAR                      │ ≰≱
WEDGE_DOUBLE                               │ ≪≫
WEDGE_DOUBLE_NEST                          │ ⪡⪢⩓⩔
WEDGE_DOUBLE_UNDERBAR                      │ ⪣
WEDGE_CLOSED                               │ ⪦⪧
WEDGE_CLOSED_UNDERBAR_SLANT                │ ⪨⪩
WEDGE_DOUBLE_INTERSECT                     │   ⩕⩖
WEDGE_TRIPLE                               │ ⋘⋙
WEDGE_TRIPLE_NEST                          │ ⫷⫸ 
WEDGE_BIG                                  │   ⋀⋁
WEDGE_FULLWIDTH                            │ ＜＞
WEDGE_CIRCLED                              │ ⧀⧁
WEDGE_SQUARED                              │   ⟎⟏
                                           │
CURVE                                      │ ≺≻⋏⋎
CURVE_DOUBLE                               │ ⪻⪼
CURVE_STROKE                               │ ⊀⊁
CURVE_UNDERBAR_SLANT                       │ ≼≽
CURVE_UNDERBAR                             │ ⪯⪰
CURVE_OVERBAR_SLANT                        │ ⋞⋟
CURVE_STROKE_UNDERBAR_SLANT                │ ⋠⋡
CURVE_OVERBAR_CURVED                       │ ⋞⋟

SET                                        │ ⊂⊃∩∪
SET_OPEN                                   │ ⟃⟄    (perhaps should be SET_CIRCLE?)
SET_DOT                                    │ ⪽⪾
SET_STROKE                                 │ ⊄⊅
SET_DOUBLE                                 │ ⋐⋑⋒⋓
SET_UNDERBAR                               │ ⊆⊇
SET_UNDERTILDE                             │ ⫇⫈
SET_UNDERTILDE_DOUBLE                      │ ⫉⫊
SET_UNDERPLUS                              │ ⪿⫀
SET_UNDERTIMES                             │ ⫁⫂
SET_UNDERBAR_DOUBLE                        │ ⫅⫆
SET_UNDERBAR_DOUBLE_STROKE                 │ ⫋⫌
SET_OVERBAR                                │   ⩂⩃
SET_STROKE_UNDERBAR                        │ ⊈⊉
SET_UNDERBAR_STROKE                        │ ⊊⊋
SET_CLOSED                                 │ ⫏⫐
SET_BIG                                    │   ⋂⋃
                                           │
SOLIDUS                                    │ /\
SOLIDUS_DOUBLE                             │ ⫽
SOLIDUS_BIG                                │ ⧸⧹
SOLIDUS_OVERBAR                            │ ⧶
SOLIDUS_DASH                               │ ⧷
SOLIDUS_CIRCLED                            │ ⦸
                                           │
IN                                         │ ∈∋⫙⟒
IN_STROKE                                  │ ∉∌
IN_OVERBAR                                 │ ⋶⋽
IN_UNDERBAR                                │ ⋸
IN_SMALL                                   │ ∊∍
IN_SMALL_OVERBAR                           │ ⋷⋾
                                           │ 
TACK                                       │ ⊢⊣⊤⊥⟛
TACK_DOUBLE                                │   ⫪⫫⟚
TACK_SHORT                                 │  ⫞⫟⫠
TACK_LONG                                  │ ⟝⟞   
TACK_BIG                                   │   ⟙⟘ 
                                           │
TRIANGLE                                   │ ⊲⊳
TRIANGLE_UNDERBAR                          │ ⊴⊵
TRIANGLE_STROKE                            │ ⋪⋫
TRIANGLE_STROKE_UNDERBAR                   │ ⋬⋭
TRIANGLE_BIG                               │ ⨞ 
                                           │
BOX                                        │ ⊏⊐⊓⊔
BOX_DOUBLE                                 │   ⩎⩏
BOX_UNDERBAR                               │ ⊑⊒
BOX_STROKE_UNDERBAR                        │ ⋢⋣
BOX_UNDERBAR_STROKE                        │ ⋤⋥
BOX_BIG                                    │   ⨅⨆
                                           │
INTEGRAL                                   │ ∫∬∭⨌
INTEGRAL_CLOSED                            │ ∮∯∰
INTEGRAL_OVERBAR                           │ ⨛
INTEGRAL_UNDERBAR                          │ ⨜
INTEGRAL_BIG                               │ ⌠⎮⌡
                                           │
DIVIDES                                    │ ∣
NOT_DIVIDES                                │ ∤
PARALLEL                                   │ ∥
NOT_PARALLEL                               │ ∦

VERTICAL_LINE                              │ |
VERTICAL_LINE_WHITE                        │ ⫾
VERTICAL_LINE_BIG_WHITE                    │ ⫿
VERTICAL_LINE_DOUBLE                       │ ‖ (not same as ||)
VERTICAL_BAR_CIRCLED                       │ ⦶

INTERCALATE                                │ ⊺ (not same as T)
PERPENDICULAR                              │ ⟂ (not same as ⊥)
EMPTY_SET                                  │ ∅ (not same as θ)
DIAMETER                                   │ ⌀ (not same as ∅)
NUMERO                                     │ №
EULER_CONSTANT                             │ ℇ (unconventional. use γ or 𝛾)
DOTLESS_ITALIC_I                           │ 𝚤
DOTLESS_ITALIC_J                           │ 𝚥
SHUFFLE_PRODUCT                            │ ⧢
TINY                                       │ ⧾
MINY                                       │ ⧿
DEGREE                                     │ °
                                           │
NOT                                        │ ¬
NOT_REVERSED                               │ ⌐
NOT_TURNED                                 │ ⌙
                                           │
BIG_BIG_SIGMA                              │ ⎲⎳
                                           │
CIRCLED_DIVISION_SLASH                     │ ⊘
CIRCLED_DIVISION_SIGN                      │ ⨸ (unconventional. use ⊘)
CIRCLED_EQUAL                              │ ⊜
CIRCLED_PARALLEL                           │ ⦷
CIRCLED_PERPENDICULAR                      │ ⦹
CIRCLED_LESS_THAN                          │ 
CIRCLED_GREATER_THAN                       │ 
CIRCLED_TRIANGLE                           │ ⎊
                                           │
ASTERISK_SQUARED                           │ ⧆
CIRCLE_SQUARED                             │ ⧇
SQUARE_SQUARED                             │ ⧈
                                           │
ARROW                                      │ ←→↑↓↔↕↖↗↘↙
ARROW_STROKE                               │ ↚↛  ↮
ARROW_WAVE                                 │ ↜↝  ↭
ARROW_SQUIGGLE                             │ ⇜⇝ 
ARROW_TWO_HEADED                           │ ↞↠↟↡
ARROW_TAIL                                 │ ↢↣ 
ARROW_FROM_BAR                             │ ↤↦↥↧
ARROW_TO_BAR                               │ ⇤⇥⤒⤓
ARROW_UP_DOWN_WITH_BASE                    │ ↨
ARROW_HOOK                                 │ ↩↪ 
ARROW_LOOP                                 │ ↫↬ 
ARROW_ZIGZAG                               │    ↯

<!-- ↰↱↲↳↴↵↶↷↸↹↼↽↾↿⇀⇁⇂⇃ -->⬎⬏⬐⬑
ARROW_LONG                                 │ ⟵⟶  ⟷
ARROW_LONG_FROM_BAR                        │ ⟻⟼
ARROW_LONG_SQUIGGLE                        │  ⟿
ARROW_DOUBLE_LONG                          │ ⟸⟹  ⟺
ARROW_DOUBLE                               │ ⇐⇒⇑⇓⇔⇕⇖⇗⇘⇙
ARROW_DOUBLE_STROKE                        │ ⇍⇏  ⇎
ARROW_TRIPLE                               │ ⇚⇛⤊⤋
ARROW_DOUBLE_FROM_BAR                      │ ⟽⟾
ARROW_QUADRUPLE                            │ ⭅⭆
ARROW_HARPOON                              │ ⇋⇌
ARROW_DOUBLED                              │ ⇇⇉⇈⇊
ARROW_DOUBLED_OPPOSITES                    │ ⇄⇆⇅⇵
ARROW_TRIPLED                              │ ⬱⇶ 
ARROW_DASH                                 │ ⇠⇢⇡⇣
ARROW_WHITE                                │ ⇦⇨⇧⇩⬄⇳⬁⬀⬂⬃
ARROW_BLACK                                │ ⬅⮕⬆⬇⬌⬍⬉⬈⬊⬋
ARROW_OPEN_HEADED                          │ ⇽⇾  ⇿
ARROW_ANTI_CLOCKWISE                       │ ↺
ARROW_CLOCKWISE                            │ ↻
ARROW_VERTICAL_STROKE                      │ ⇷⇸  ⇹
ARROW_VERTICAL_STROKE_DOUBLE               │ ⇺⇻  ⇼
                                           │
ELLIPSIS_VERTICAL                          │ ⋮
ELLIPSIS_HORIZONTAL                        │ ⋯
ELLIPSIS_DIAGONAL_UP                       │ ⋰
ELLIPSIS_DIAGONAL_DOWN                     │ ⋱
                                           │
CIRCLE_BLACK                               │ ●
CIRCLE_WHITE                               │ ○
CIRCLE_HEAVY                               │ ⭘
CIRCLE_LARGE_BLACK                         │ ⬤
CIRCLE_LARGE_WHITE                         │ ◯
CIRCLE_LARGE_HEAVY                         │ ⭕
                                           │
ELLIPSE_HORIZONTAL_BLACK                   │ ⬬
ELLIPSE_HORIZONTAL_WHITE                   │ ⬭
ELLIPSE_VERTICAL_BLACK                     │ ⬮
ELLIPSE_VERTICAL_WHITE                     │ ⬯
                                           │
TRIANGLE_BLACK                             │ ◀▶▲▼◤◥◣◢
TRIANGLE_WHITE                             │ ◁▷△▽◸◹◺◿
TRIANGLE_SMALL_BLACK                       │ ◂▸▴▾
TRIANGLE_SMALL_WHITE                       │ ◃▹▵▿
TRIANGLE_CENTRED_MEDIUM_BLACK              │ ⯇⯈⯅⯆
TRIANGLE_UNDERBAR                          │   ⧋
                                           │
POINTER_BLACK                              │ ◄►
POINTER_WHITE                              │ ◅▻
                                           │
SQUARE_BLACK                               │ ■
SQUARE_WHITE                               │ □
SQUARE_MEDIUM_BLACK                        │ ◼
SQUARE_MEDIUM_WHITE                        │ ◻
SQUARE_SMALL_BLACK                         │ ▪
SQUARE_SMALL_WHITE                         │ ▫
SQUARE_VERY_SMALL_BLACK                    │ ⬝
SQUARE_VERY_SMALL_WHITE                    │ ⬞
SQUARE_CENTRED_BLACK                       │ ⯀
                                           │
RECTANGLE_HORIZONTAL_BLACK                 │ ▬
RECTANGLE_HORIZONTAL_WHITE                 │ ▭
RECTANGLE_VERTICAL_BLACK                   │ ▮
RECTANGLE_VERTICAL_WHITE                   │ ▯
                                           │
PARALLELOGRAM_BLACK                        │ ▰
PARALLELOGRAM_WHITE                        │ ▱
                                           │
DIAMOND_BLACK                              │ ◆
DIAMOND_WHITE                              │ ◇
DIAMOND_MEDIUM_BLACK                       │ ⬥
DIAMOND_MEDIUM_WHITE                       │ ⬦
DIAMOND_SMALL_BLACK                        │ ⬩
DIAMOND_CENTRED_BLACK                      │ ⯁
DIAMOND_WHITE_DOTTED                       │ ⟐ 
                                           │
LOZENGE_BLACK                              │ ⧫
LOZENGE_WHITE                              │ ◊
LOZENGE_MEDIUM_BLACK                       │ ⬧
LOZENGE_MEDIUM_WHITE                       │ ⬨
LOZENGE_SMALL_BLACK                        │ ⬪ (colour reversed)
LOZENGE_SMALL_WHITE                        │ ⬫ (colour reversed)
                                           │
CUSP_BLACK                                 │ ⯌
CUSP_WHITE                                 │ ⯎
CUSP_ROTATED_BLACK                         │ ⯍
CUSP_ROTATED_WHITE                         │ ⯏
                                           │
PENTAGON_BLACK                             │ ⬟
PENTAGON_WHITE                             │ ⬠
PENTAGON_RIGHT_BLACK                       │ ⭓
PENTAGON_RIGHT_WHITE                       │ ⭔
PENTAGON_DOWN_BLACK                        │ ⯂
                                           │
STAR_SMALL_BLACK                           │ ⭑
STAR_SMALL_WHITE                           │ ⭒
                                           │
HEXAGON_VERTICAL_WHITE                     │ ⬡
HEXAGON_VERTICAL_BLACK                     │ ⬢
HEXAGON_HORIZONTAL_BLACK                   │ ⬣
                                           │
OCTAGON_VERTICAL_BLACK                     │ ⯄
OCTAGON_HORIZONTAL_BLACK                   │ ⯃
                                           │
SQUARE_HPA                                 │ ㍱
SQUARE_DA                                  │ ㍲
SQUARE_AU                                  │ ㍳
SQUARE_BAR                                 │ ㍴
SQUARE_OV                                  │ ㍵
SQUARE_PC                                  │ ㍶
SQUARE_DM                                  │ ㍷
SQUARE_DM_SQUARED                          │ ㍸
SQUARE_DM_CUBED                            │ ㍹
SQUARE_IU                                  │ ㍺
SQUARE_PA_AMPS                             │ ㎀
SQUARE_NA                                  │ ㎁
SQUARE_MU_A                                │ ㎂
SQUARE_MA                                  │ ㎃
SQUARE_KA                                  │ ㎄
SQUARE_KB                                  │ ㎅
SQUARE_MB                                  │ ㎆
SQUARE_GB                                  │ ㎇
SQUARE_CAL                                 │ ㎈
SQUARE_KCAL                                │ ㎉
SQUARE_PF                                  │ ㎊
SQUARE_NF                                  │ ㎋
SQUARE_MU_F                                │ ㎌
SQUARE_MU_G                                │ ㎍
SQUARE_MG                                  │ ㎎
SQUARE_KG                                  │ ㎏
SQUARE_HZ                                  │ ㎐
SQUARE_KHZ                                 │ ㎑
SQUARE_MHZ                                 │ ㎒
SQUARE_GHZ                                 │ ㎓
SQUARE_THZ                                 │ ㎔
SQUARE_MU_L                                │ ㎕
SQUARE_ML                                  │ ㎖
SQUARE_DL                                  │ ㎗
SQUARE_KL                                  │ ㎘
SQUARE_FM                                  │ ㎙
SQUARE_NM                                  │ ㎚
SQUARE_MU_M                                │ ㎛
SQUARE_MM                                  │ ㎜
SQUARE_CM                                  │ ㎝
SQUARE_KM                                  │ ㎞
SQUARE_MM_SQUARED                          │ ㎟
SQUARE_CM_SQUARED                          │ ㎠
SQUARE_M_SQUARED                           │ ㎡
SQUARE_KM_SQUARED                          │ ㎢
SQUARE_MM_CUBED                            │ ㎣
SQUARE_CM_CUBED                            │ ㎤
SQUARE_M_CUBED                             │ ㎥
SQUARE_KM_CUBED                            │ ㎦
SQUARE_M_OVER_S                            │ ㎧
SQUARE_M_OVER_S_SQUARED                    │ ㎨
SQUARE_PA                                  │ ㎩
SQUARE_KPA                                 │ ㎪
SQUARE_MPA                                 │ ㎫
SQUARE_GPA                                 │ ㎬
SQUARE_RAD                                 │ ㎭
SQUARE_RAD_OVER_S                          │ ㎮
SQUARE_RAD_OVER_S_SQUARED                  │ ㎯
SQUARE_PS                                  │ ㎰
SQUARE_NS                                  │ ㎱
SQUARE_MU_S                                │ ㎲
SQUARE_MS                                  │ ㎳
SQUARE_PV                                  │ ㎴
SQUARE_NV                                  │ ㎵
SQUARE_MU_V                                │ ㎶
SQUARE_MV                                  │ ㎷
SQUARE_KV                                  │ ㎸
SQUARE_MV_MEGA                             │ ㎹
SQUARE_PW                                  │ ㎺
SQUARE_NW                                  │ ㎻
SQUARE_MU_W                                │ ㎼
SQUARE_MW                                  │ ㎽
SQUARE_KW                                  │ ㎾
SQUARE_MW_MEGA                             │ ㎿
SQUARE_K_OHM                               │ ㏀
SQUARE_M_OHM                               │ ㏁
SQUARE_AM                                  │ ㏂
SQUARE_BQ                                  │ ㏃
SQUARE_CC                                  │ ㏄
SQUARE_CD                                  │ ㏅
SQUARE_C_OVER_KG                           │ ㏆
SQUARE_CO                                  │ ㏇
SQUARE_DB                                  │ ㏈
SQUARE_GY                                  │ ㏉
SQUARE_HA                                  │ ㏊
SQUARE_HP                                  │ ㏋
SQUARE_IN                                  │ ㏌
SQUARE_KK                                  │ ㏍
SQUARE_KM                                  │ ㏎
SQUARE_KT                                  │ ㏏
SQUARE_LM                                  │ ㏐
SQUARE_LN                                  │ ㏑
SQUARE_LOG                                 │ ㏒
SQUARE_LX                                  │ ㏓
SQUARE_MB_SMALL                            │ ㏔
SQUARE_MIL                                 │ ㏕
SQUARE_MOL                                 │ ㏖
SQUARE_PH                                  │ ㏗
SQUARE_PM                                  │ ㏘
SQUARE_PPM                                 │ ㏙
SQUARE_PR                                  │ ㏚
SQUARE_SR                                  │ ㏛
SQUARE_SV                                  │ ㏜
SQUARE_WB                                  │ ㏝
SQUARE_V_OVER_M                            │ ㏞
SQUARE_A_OVER_M                            │ ㏟
SQUARE_GAL                                 │ ㏿
                                           │
BRAILLE                                    │ ⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿⡀⡁⡂⡃⡄⡅⡆⡇⡈⡉⡊⡋⡌⡍⡎⡏⡐⡑⡒⡓⡔⡕⡖⡗⡘⡙⡚⡛⡜⡝⡞⡟⡠⡡⡢⡣⡤⡥⡦⡧⡨⡩⡪⡫⡬⡭⡮⡯⡰⡱⡲⡳⡴⡵⡶⡷⡸⡹⡺⡻⡼⡽⡾⡿⢀⢁⢂⢃⢄⢅⢆⢇⢈⢉⢊⢋⢌⢍⢎⢏⢐⢑⢒⢓⢔⢕⢖⢗⢘⢙⢚⢛⢜⢝⢞⢟⢠⢡⢢⢣⢤⢥⢦⢧⢨⢩⢪⢫⢬⢭⢮⢯⢰⢱⢲⢳⢴⢵⢶⢷⢸⢹⢺⢻⢼⢽⢾⢿⣀⣁⣂⣃⣄⣅⣆⣇⣈⣉⣊⣋⣌⣍⣎⣏⣐⣑⣒⣓⣔⣕⣖⣗⣘⣙⣚⣛⣜⣝⣞⣟⣠⣡⣢⣣⣤⣥⣦⣧⣨⣩⣪⣫⣬⣭⣮⣯⣰⣱⣲⣳⣴⣵⣶⣷⣸⣹⣺⣻⣼⣽⣾⣿
BRAILLE_ALTERNATE                          │ ⠀⠁⠈⠉⠂⠃⠊⠋⠐⠑⠘⠙⠒⠓⠚⠛⠄⠅⠌⠍⠆⠇⠎⠏⠔⠕⠜⠝⠖⠗⠞⠟⠠⠡⠨⠩⠢⠣⠪⠫⠰⠱⠸⠹⠲⠳⠺⠻⠤⠥⠬⠭⠦⠧⠮⠯⠴⠵⠼⠽⠶⠷⠾⠿⡀⡁⡈⡉⡂⡃⡊⡋⡐⡑⡘⡙⡒⡓⡚⡛⡄⡅⡌⡍⡆⡇⡎⡏⡔⡕⡜⡝⡖⡗⡞⡟⡠⡡⡨⡩⡢⡣⡪⡫⡰⡱⡸⡹⡲⡳⡺⡻⡤⡥⡬⡭⡦⡧⡮⡯⡴⡵⡼⡽⡶⡷⡾⡿⢀⢁⢈⢉⢂⢃⢊⢋⢐⢑⢘⢙⢒⢓⢚⢛⢄⢅⢌⢍⢆⢇⢎⢏⢔⢕⢜⢝⢖⢗⢞⢟⢠⢡⢨⢩⢢⢣⢪⢫⢰⢱⢸⢹⢲⢳⢺⢻⢤⢥⢬⢭⢦⢧⢮⢯⢴⢵⢼⢽⢶⢷⢾⢿⣀⣁⣈⣉⣂⣃⣊⣋⣐⣑⣘⣙⣒⣓⣚⣛⣄⣅⣌⣍⣆⣇⣎⣏⣔⣕⣜⣝⣖⣗⣞⣟⣠⣡⣨⣩⣢⣣⣪⣫⣰⣱⣸⣹⣲⣳⣺⣻⣤⣥⣬⣭⣦⣧⣮⣯⣴⣵⣼⣽⣶⣷⣾⣿
                                           │
LINE_EXTENSION                             │ ⎯⏐
BOX_LIGHT                                  │ ─│┌┐└┘├┤┬┴┼╴╵╶╷╱╲╳
BOX_ARC                                    │ ─│╭╮╰╯├┤┬┴┼╴╵╶╷╱╲╳
BOX_HEAVY                                  │ ━┃┏┓┗┛┣┫┳┻╋╸╹╺╻   ╼╾╽╿┍┎┑┒┕┖┙┚┝┞┟┠┡┢┥┦┧┨┩┪┭┮┯┰┱┲┵┶┷┸┹┺┽┾┿╀╁╂╃╄╅╆╇╈╉╊
BOX_DOUBLE                                 │ ═║╔╗╚╝╠╣╦╩╬           ╒╓╕╖╘╙╛╜╞  ╟  ╡  ╢    ╤╥    ╧╨    ╪  ╫
BOX_LIGHT_DOUBLE                           │ ╌╎
BOX_LIGHT_TRIPLE                           │ ┄┆
BOX_LIGHT_QUADRUPLE                        │ ┈┊
BOX_HEAVY_DOUBLE                           │ ╍╏
BOX_HEAVY_TRIPLE                           │ ┅┇
BOX_HEAVY_QUADRUPLE                        │ ┉┋
                                           │
THIRD_LEFT                                 │  🯏🯎█
EIGHTH_LOWER                               │  ▁▂▃▄▅▆▇█
EIGHTH_UPPER                               │  ▔🮂🮃▀🮄🮅🮆█
EIGHTH_LEFT                                │  ▏▎▍▌▋▊▉█
EIGHTH_RIGHT                               │  ▕🮇🮈▐🮉🮊🮋█
SHADE_FOURTH                               │  ░▒▓█
ONE_SIXTEENTH                              │ 𜺐𜺑𜺒𜺓𜺔𜺕𜺖𜺗𜺘𜺙𜺚𜺛𜺜𜺝𜺞𜺟
ONE_EIGHTH_VERTICAL                        │ ▏🭰🭱🭲🭳🭴🭵▕
ONE_EIGHTH_HORIZONTAL                      │ ▔🭶🭷🭸🭹🭺🭻▁
                                           │
QUADRANT                                   │  ▘▝▀▖▌▞▛▗▚▐▜▄▙▟█
QUADRANT_SEPARATED                         │  𜰡𜰢𜰣𜰤𜰥𜰦𜰧𜰨𜰩𜰪𜰫𜰬𜰭𜰮𜰯
SEXTANT                                    │  🬀🬁🬂🬃🬄🬅🬆🬇🬈🬉🬊🬋🬌🬍🬎🬏🬐🬑🬒🬓▌🬔🬕🬖🬗🬘🬙🬚🬛🬜🬝🬞🬟🬠🬡🬢🬣🬤🬥🬦🬧▐🬨🬩🬪🬫🬬🬭🬮🬯🬰🬱🬲🬳🬴🬵🬶🬷🬸🬹🬺🬻█
SEXTANT_SEPARATED                          │  𜹑𜹒𜹓𜹔𜹕𜹖𜹗𜹘𜹙𜹚𜹛𜹜𜹝𜹞𜹟𜹠𜹡𜹢𜹣𜹤𜹥𜹦𜹧𜹨𜹩𜹪𜹫𜹬𜹭𜹮𜹯𜹰𜹱𜹲𜹳𜹴𜹵𜹶𜹷𜹸𜹹𜹺𜹻𜹼𜹽𜹾𜹿𜺀𜺁𜺂𜺃𜺄𜺅𜺆𜺇𜺈𜺉𜺊𜺋𜺌𜺍𜺎𜺏
OCTANT                                     │  𜺨𜺫🮂𜴀▘𜴁𜴂𜴃𜴄▝𜴅𜴆𜴇𜴈▀𜴉𜴊𜴋𜴌🯦𜴍𜴎𜴏𜴐𜴑𜴒𜴓𜴔𜴕𜴖𜴗𜴘𜴙𜴚𜴛𜴜𜴝𜴞𜴟🯧𜴠𜴡𜴢𜴣𜴤𜴥𜴦𜴧𜴨𜴩𜴪𜴫𜴬𜴭𜴮𜴯𜴰𜴱𜴲𜴳𜴴𜴵🮅𜺣𜴶𜴷𜴸𜴹𜴺𜴻𜴼𜴽𜴾𜴿𜵀𜵁𜵂𜵃𜵄▖𜵅𜵆𜵇𜵈▌𜵉𜵊𜵋𜵌▞𜵍𜵎𜵏𜵐▛𜵑𜵒𜵓𜵔𜵕𜵖𜵗𜵘𜵙𜵚𜵛𜵜𜵝𜵞𜵟𜵠𜵡𜵢𜵣𜵤𜵥𜵦𜵧𜵨𜵩𜵪𜵫𜵬𜵭𜵮𜵯𜵰𜺠𜵱𜵲𜵳𜵴𜵵𜵶𜵷𜵸𜵹𜵺𜵻𜵼𜵽𜵾𜵿𜶀𜶁𜶂𜶃𜶄𜶅𜶆𜶇𜶈𜶉𜶊𜶋𜶌𜶍𜶎𜶏▗𜶐𜶑𜶒𜶓▚𜶔𜶕𜶖𜶗▐𜶘𜶙𜶚𜶛▜𜶜𜶝𜶞𜶟𜶠𜶡𜶢𜶣𜶤𜶥𜶦𜶧𜶨𜶩𜶪𜶫▂𜶬𜶭𜶮𜶯𜶰𜶱𜶲𜶳𜶴𜶵𜶶𜶷𜶸𜶹𜶺𜶻𜶼𜶽𜶾𜶿𜷀𜷁𜷂𜷃𜷄𜷅𜷆𜷇𜷈𜷉𜷊𜷋𜷌𜷍𜷎𜷏𜷐𜷑𜷒𜷓𜷔𜷕𜷖𜷗𜷘𜷙𜷚▄𜷛𜷜𜷝𜷞▙𜷟𜷠𜷡𜷢▟𜷣▆𜷤𜷥█
CELSIUS                                    │ ℃ (not same as °C)
FAHRENHEIT                                 │ ℉ (not same as °F)
KELVIN                                     │ K (not same as K) (do NOT use degree symbol °)
```
<!--
GREEK_NAME                                 │ {'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega', 'digamma', 'san', 'tsan', 'sho', 'heta', 'koppa', 'sampi', 'yot', 'stigma'}
angstrom                   │ Å (not same as Å) (unconventional. use Å)
ohm                        │ Ω 
mho                        │ ℧ 
-->

BRACKET_ANGLE '〈〉' are deprecated in unicode

i have no experience with the archaic greek letters

use these special characters only if you will display them without typesetting. generally try to rely on typesetting software if it is available

character conversion helper functions may be included later. for now, storing them as string constants is pretty good

# conversions

because i forget sometimes

```
name         │ formula
─────────────┼────────────────────────────────────────────────────────────
 deg_to_rad  │  rad = deg * 𝜏 ∕ 360
 deg_to_turn │ turn = deg ∕ 360
 rad_to_deg  │  deg = rad * 360 ∕ 𝜏
 rad_to_turn │ turn = rad ∕ 𝜏
turn_to_deg  │  deg = turn * 360
turn_to_rad  │  rad = turn * 𝜏
             │
 amp_to_db   │   db = 20 * ㏒⏨(amp)
  db_to_amp  │  amp = 10 ^ (db / 20)
 pow_to_db   │   db = 10 * ㏒⏨(pow)
  db_to_pow  │  pow = 10 ^ (db / 10)
             │
  hz_to_midi │ midi = 69 + 12 * ㏒₂(hz / 440)
midi_to_hz   │   hz = 440 * 2 ^ ((midi - 69) / 12)
  hz_to_oct  │  oct = ㏒₂(hz)
 oct_to_hz   │   hz = 2 ^ hz
  hz_to_gw   │   gw = 
  gw_to_hz   │   hz = 
  hz_to_mel  │  mel = 2595 * ㏒⏨(1 + hz / 700)
 mel_to_hz   │   hz = 700 * 10 ^ (mel / 2595 - 1)
  hz_to_bark │ bark = 13 * arctan(0.00076 * hz) + 3.5 * arctan((hz / 7500)²)
bark_to_hz   │   hz = 
  hz_to_erbs │ erbs = 11.17268 * ln(1 + (46.06538 * f) / (f + 14678.49))
erbs_to_hz   │   hz = 676170.4 / (47.06538 - e ^ (0.08950404 * erbs)) - 14678.49
             │
  lerp_freq  │ lerp with [20, 20000] Hz defaults
unlerp_freq  │ unlerp with [20, 20000] Hz defaults
```

ya :v thats pretty much it

this project is convenience > accuracy > predictability > features > performance so i dont really care how slow it does it, as long as it *does* it.

special cases like 0/0 are handled according to how *you* like it, using a global variable, kinda like numpy. you tell the library how to behave and it obeys cause its a good library :)

motivation: sometimes i need the quotient of a division, but programs only give me truediv or floordiv. sometimes i juse need a neg function to use in a higher-order function, without resorting to a nameless lambda >:( sometimes i need floor and ceil. sometimes i need the min of a dataset. sometimes i want the mean of a database instead of writing sum/len. daamath solves all of that. it gives me everything that a language is missing, and makes maths feel more like a second language. i can speak maths within the programming language im working in. thats why i love daamath.

this project will take inspiration from [glm](https://github.com/icaven/glm) soon
