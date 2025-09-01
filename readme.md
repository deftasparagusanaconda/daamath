im tired of having unpredictable math ops in my programs. so i made this cross-language swiss army knife of math stuff.
unlike other math libraries, this one isnt specialized to a domain so its the widest-reaching one as far as i know.

# HOW IHNSTALL???!?!?

choose your language:
<details><summary>

## python </summary>

(NOT IMPLEMENTED YET)

install the python package through PyPI:

```
pip install daamath
```
or
```
python -m pip install daamath
```

</details><details><summary>

## java </summary>

(NOT IMPLEMENTED YET)

daamath will be available as a java package. but im not sure where to host it yet

</details>

# operators

<details open><summary>arithmetic</summary>

complex numbers are fully supported but type will not always be promoted to complex. for example, log will promote to complex only when negative input is given. or sqrt(-4) will appropriately promote to a complex 2𝑖

```
name      │ explanation              │ example
──────────┼──────────────────────────┼────────────────────────────────
inc       │ increment                │             ++2 = 3
dec       │ decrement                │             −−2 = 1
neg       │ additive inverse         │             − 2 = −2
inv       │ multiplicative inverse   │             ∕ 2 = 0.5
add       │ addition                 │          −5 + 2 = −3
sub       │ subtraction              │          −5 − 2 = −7
mul       │ multiplication           │          −5 × 2 = −10
div       │ division                 │          −5 ÷ 2 = −2.5
pow       │ exponentiation           │             −5² = 25
log       │ logarithm                │       log(−5,2) ≈ 2.322 + 4.532𝑖
root      │ nᵗʰ root                 │      root(−5,2) ≈ −2.23606797
floordiv  │ division rounded to −∞   │  floordiv(−5,2) = −3
mod       │ modulus                  │       mod(−5,2) =  1
quotient  │ division rounded to ±0   │  quotient(−5,2) = −2
remainder │ remaining of quotient    │ remainder(−5,2) = −1
parallel  │ parallel operator        │  parallel(−5,2) = 3.(3)
exp       │ exponentiation base e    │          exp(2) ≈ 7.389056098930
exp2      │ exponentiation base 2    │         exp2(2) = 4
exp10     │ exponentiation base 10   │        exp10(2) = 100
ln        │ logarithm base e         │           ln(2) ≈ 0.693147180559
log2      │ logarithm base 2         │         log2(2) = 1
log10     │ logarithm base 10        │        log10(2) ≈ 0.30103
expm1     │ exp(x) − 1               │        expm1(2) ≈ 6.38905609893065
exp2m1    │ exp2(x) − 1              │       exp2m1(2) = 3
exp10m1   │ exp10(x) − 1             │      exp10m1(2) = 99
lnp       │ ln(x + 1)                │          lnp(2) ≈ 1.0986122886681096
log2p     │ log2(x + 1)              │        log2p(2) ≈ 1.584962500721156
log10p    │ log10(x + 1)             │       log10p(2) ≈ 0.47712125471966244
sqrt      │ square root (√x)         │         sqrt(2) ≈ 1.4142135623730951
cbrt      │ cube root (∛x)           │         cbrt(2) ≈ 1.2599210498948732
rsqrt     │ reciprocal of sqrt(x)    │        rsqrt(2) ≈ 0.7071067811865475
rcbrt     │ reciprocal of cbrt(x)    │        rcbrt(2) ≈ 0.7937005259840997
abs       │ absolute value           │       abs(2+3𝑖) ≈ 3.6055512754
gcd       │ greatest common divisor  │        gcd(2,3) = 1
lcm       │ lowest common multiple   │        lcm(2,3) = 6
hyper     │ hyperoperation           │  hyper(1, 2, 3) = 5
ieee_div  │ IEEE-754-style division  │   ieee_div(0,0) = QNAN
hypot     │ euclidean norm           │  hypot(1, 2, 3) ≈ 3.7416573867739413
ceil      │ directed rounding to +∞  │   ceil(1.23, 1) = 1.3
trunc     │ directed rounding to ±0  │  trunc(1.23, 1) = 1.2
floor     │ directed rounding to −∞  │  floor(1.23, 1) = 1.2
round     │ to nearest, tie to even  │  round(1.23, 1) = 1.1
```

tetration is yet a new operation, and there is no standard convention on which tetration is the most agreed upon. thus `tet`, `sexp`, `sroot`, `slog` are not yet implemented

i have not yet decided on a name for the variadic version of `parallel`

</details><details open><summary>comparative </summary>

```
name │ explanation                             │ example  
─────┼─────────────────────────────────────────┼────────────────────
lt   │ less than                               │ 2 < 3 is true 
le   │ less than or equal to                   │ 2 ≤ 3 is true
eq   │ equal to                                │ 2 = 3 is false
ne   │ not equal to                            │ 2 ≠ 3 is true
ge   │ greater than or equal to                │ 2 ≥ 3 is false
gt   │ greater than                            │ 2 > 3 is false
clt  │ component-wise less than                │ 2+3𝑖 < 4+3𝑖 is (T,F)
cle  │ component-wise less than or equal to    │ 2+3𝑖 ≤ 4+3𝑖 is (T,T)
ceq  │ component-wise equal to                 │ 2+3𝑖 = 4+3𝑖 is (F,T)
cne  │ component-wise not equal to             │ 2+3𝑖 ≠ 4+3𝑖 is (T,F)
cge  │ component-wise greater than or equal to │ 2+3𝑖 ≥ 4+3𝑖 is (F,T)
cgt  │ component-wise greater than             │ 2+3𝑖 > 4+3𝑖 is (F,F)
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
acot    │ circular arccotangent │      acot(1) ≈ 0.785398163
asec    │ circular arcsecant    │      asec(1) = 0
acsc    │ circular arccosecant  │      acsc(1) ≈ 1.57079633
sinpi   │ sin(𝜋x)               │     sinpi(1) = 0
cospi   │ cos(𝜋x)               │     cospi(1) = −1
tanpi   │ tan(𝜋x)               │     tanpi(1) = 0
cotpi   │ cot(𝜋x)               │     cotpi(1) = ?
secpi   │ sec(𝜋x)               │     secpi(1) = −1
cscpi   │ csc(𝜋x)               │     cscpi(1) = ?
asinpi  │ asin(y)∕𝜋             │    asinpi(1) = 0.5
acospi  │ acos(y)∕𝜋             │    acospi(1) = 0
atanpi  │ atan(y)∕𝜋             │    atanpi(1) = 0.25
acotpi  │ acot(y)∕𝜋             │    acotpi(1) = 0.25
asecpi  │ asec(y)∕𝜋             │    asecpi(1) = 0
acscpi  │ acsc(y)∕𝜋             │    acscpi(1) = 0.5
sind    │ sin(𝜋x∕180)           │     sind(1) = 
cosd    │ cos(𝜋x∕180)           │     cosd(1) = 
tand    │ tan(𝜋x∕180)           │     tand(1) = 
cotd    │ cot(𝜋x∕180)           │     cotd(1) = 
secd    │ sec(𝜋x∕180)           │     secd(1) = 
cscd    │ csc(𝜋x∕180)           │     cscd(1) = 
asind   │ asin(y)×180∕𝜋         │    asind(1) = 
acosd   │ acos(y)×180∕𝜋         │    acosd(1) = 
atand   │ atan(y)×180∕𝜋         │    atand(1) = 
acotd   │ acot(y)×180∕𝜋         │    acotd(1) = 
asecd   │ asec(y)×180∕𝜋         │    asecd(1) = 
acscd   │ acsc(y)×180∕𝜋         │    acscd(1) = 
atan2   │ IEEE atan2            │   atan2(1,1) ≈ 0.785398163
atan2pi │ IEEE atan2∕𝜋          │ atan2pi(1,1) = 0.25
atan2d  │ IEEE atan2×180∕𝜋      │  atan2d(1,1) ≈ 
```

extra set:

```
name            │ explanation               │ formula
────────────────┼───────────────────────────┼──────────────────────────────────────────────────────────
versin          │ versed sine               │          versin(x) = 1 − cos(x)
vercos          │ versed cosine             │          vercos(x) = 1 + cos(x)
coversin        │ co versed sine            │        coversin(x) = 1 − sin(x)
covercos        │ co versed cosine          │        covercos(x) = 1 + sin(x)
haversin        │ half versed sine          │        haversin(x) = (1 − cos(x))∕2
havercos        │ half versed cosine        │        havercos(x) = (1 + cos(x))∕2
hacoversin      │ half co versed sine       │      hacoversin(x) = (1 − sin(x))∕2
hacovercos      │ half co versed cosine     │      hacovercos(x) = (1 + sin(x))∕2
exsec           │ external secant           │           exsec(x) = sec(x) − 1
excsc           │ external cosecant         │           excsc(x) = csc(x) − 1
chord           │ chord length              │           chord(x) = 2 × sin(x∕2)
arcchord        │ arc chord length          │        arcchord(y) = 2 × arcsin(y∕2)
arcexsec        │ arc external secant       │        arcexsec(y) = arcsec(y+1)
arcexcsc        │ arc external cosecant     │        arcexcsc(y) = arccsc(y+1)
arcversin       │ arc versed sine           │       arcversin(y) = arccos(1−y)
arcvercos       │ arc versed cosine         │       arcvercos(y) = arccos(y−1)
arccoversin     │ arc co versed sine        │     arccoversin(y) = arcsin(1−y)
arccovercos     │ arc co versed cosine      │     arccovercos(y) = arcsin(y−1)
archaversin     │ arc half versed sine      │     archaversin(y) = arccos(1−2y)
archavercos     │ arc half versed cosine    │     archavercos(y) = arccos(2y−1)
archacoversin   │ arc half co versed sine   │   archacoversin(y) = arcsin(1−2y)
archacovercos   │ arc half co versed cosine │   archacovercos(y) = arcsin(2y−1)
versinpi        │ versin(𝜋x)                │        versinpi(x) = 1 − cos(𝜋x)
vercospi        │ vercos(𝜋x)                │        vercospi(x) = 1 + cos(𝜋x)
coversinpi      │ coversin(𝜋x)              │      coversinpi(x) = 1 − sin(𝜋x)
covercospi      │ covercos(𝜋x)              │      covercospi(x) = 1 + sin(𝜋x)
haversinpi      │ haversin(𝜋x)              │      haversinpi(x) = (1 − cos(𝜋x))∕2
havercospi      │ havercos(𝜋x)              │      havercospi(x) = (1 + cos(𝜋x))∕2
hacoversinpi    │ hacoversin(𝜋x)            │    hacoversinpi(x) = (1 − sin(𝜋x))∕2
hacovercospi    │ hacovercos(𝜋x)            │    hacovercospi(x) = (1 + sin(𝜋x))∕2
exsecpi         │ exsec(𝜋x)                 │         exsecpi(x) = sec(𝜋x) − 1
excscpi         │ excsc(𝜋x)                 │         excscpi(x) = csc(𝜋x) − 1
chordpi         │ chord(𝜋x)                 │         chordpi(x) = 2 × sin(𝜋x∕2)
arcchordpi      │ arcchord(y)∕𝜋             │      arcchordpi(y) = 2 × arcsin(y∕2)∕𝜋
arcexsecpi      │ arcexsecpi(x)∕𝜋           │      arcexsecpi(y) = arcsec(y+1)∕𝜋
arcexcscpi      │ arcexcscpi(x)∕𝜋           │      arcexcscpi(y) = arccsc(y+1)∕𝜋
arcversinpi     │ arcversin(y)∕𝜋            │     arcversinpi(y) = arccos(1−y)∕𝜋
arcvercospi     │ arcvercos(y)∕𝜋            │     arcvercospi(y) = arccos(y−1)∕𝜋
arccoversinpi   │ arccoversin(y)∕𝜋          │   arccoversinpi(y) = arcsin(1−y)∕𝜋
arccovercospi   │ arccovercos(y)∕𝜋          │   arccovercospi(y) = arcsin(y−1)∕𝜋
archaversinpi   │ archaversin(y)∕𝜋          │   archaversinpi(y) = arccos(1−2y)∕𝜋
archavercospi   │ archavercos(y)∕𝜋          │   archavercospi(y) = arccos(2y−1)∕𝜋
archacoversinpi │ archacoversin(y)∕𝜋        │ archacoversinpi(y) = arcsin(1−2y)∕𝜋
archacovercospi │ archacovercos(y)∕𝜋        │ archacovercospi(y) = arcsin(2y−1)∕𝜋
versind         │ versin(𝜋x∕180)            │         versind(x) = 1 − cos(𝜋x∕180)
vercosd         │ vercos(𝜋x∕180)            │         vercosd(x) = 1 + cos(𝜋x∕180)
coversind       │ coversin(𝜋x∕180)          │       coversind(x) = 1 − sin(𝜋x∕180)
covercosd       │ covercos(𝜋x∕180)          │       covercosd(x) = 1 + sin(𝜋x∕180)
haversind       │ haversin(𝜋x∕180)          │       haversind(x) = (1 − cos(𝜋x∕180))∕2
havercosd       │ havercos(𝜋x∕180)          │       havercosd(x) = (1 + cos(𝜋x∕180))∕2
hacoversind     │ hacoversin(𝜋x∕180)        │     hacoversind(x) = (1 − sin(𝜋x∕180))∕2
hacovercosd     │ hacovercos(𝜋x∕180)        │     hacovercosd(x) = (1 + sin(𝜋x∕180))∕2
exsecd          │ exsec(𝜋x∕180)             │          exsecd(x) = sec(𝜋x∕180) − 1
excscd          │ excsc(𝜋x∕180)             │          excscd(x) = csc(𝜋x∕180) − 1
chordd          │ chord(𝜋x∕180)             │          chordd(x) = 2 × sin(𝜋x∕180∕2)
arcchordd       │ arcchord(y)×180∕𝜋         │       arcchordd(y) = 2 × arcsin(y∕2)×180∕𝜋
arcexsecd       │ arcexsec(x)×180∕𝜋         │       arcexsecd(y) = arcsec(y+1)×180∕𝜋
arcexcscd       │ arcexcsc(x)×180∕𝜋         │       arcexcscd(y) = arccsc(y+1)×180∕𝜋
arcversind      │ arcversin(y)×180∕𝜋        │      arcversind(y) = arccos(1−y)×180∕𝜋
arcvercosd      │ arcvercos(y)×180∕𝜋        │      arcvercosd(y) = arccos(y−1)×180∕𝜋
arccoversind    │ arccoversin(y)×180∕𝜋      │    arccoversind(y) = arcsin(1−y)×180∕𝜋
arccovercosd    │ arccovercos(y)×180∕𝜋      │    arccovercosd(y) = arcsin(y−1)×180∕𝜋
archaversind    │ archaversin(y)×180∕𝜋      │    archaversind(y) = arccos(1−2y)×180∕𝜋
archavercosd    │ archavercos(y)×180∕𝜋      │    archavercosd(y) = arccos(2y−1)×180∕𝜋
archacoversind  │ archacoversin(y)×180∕𝜋    │  archacoversind(y) = arcsin(1−2y)×180∕𝜋
archacovercosd  │ archacovercos(y)×180∕𝜋    │  archacovercosd(y) = arcsin(2y−1)×180∕𝜋
```

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

</details><details open><summary>boolean </summary>

```
name  │ explanation   │ truth │ example
──────┼───────────────┼───────┼──────────
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

```
name     │ explanation  │ truth │ example
─────────┼──────────────┼───────┼──────────
bitnot   │ negation     │    10 │   ~−5 = (probably 2)
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
conj  │ conjugate      │  conj(2+3𝑖) = 2−3𝑖 
```

</details><details open><summary>combinatorial </summary>

```
name     │ explanation                        │ example
─────────┼────────────────────────────────────┼──────────────────────────
fact     │ factorial                          │                   5! = 120
sumt     │ sumtorial (sum of all ℤ⁺ up to n)  │              sumt(5) = 15
comb     │ combinations                       │            comb(6,5) = 6
perm     │ permutations                       │            perm(6,5) = 720
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
sgn      │ signum. −1 if <0, +1 if >0, else 0     │            sgn(0.5) = 1
swap     │ swap variables in memory               │          swap(a, b) = (b, a)
parity   │ sum of 1 bits                          │           parity(5) = 2
frange   │ iterable of numbers in an interval     │  frange(0, 10, 2.5) = [0, 2.5, 5, 7.5]
linspace │ fixed number of numbers in an interval │ 
isinf    │ true if IEEE inf                       │ isinf(float('inf')) = True
isnan    │ true if IEEE nan                       │ isnan(float('nan')) = False
erf      │ error function                         │              erf(1) ≈ 0.8427007929497149
erfc     │ 1−erf(x)                               │             erfc(1) ≈ 0.15729920705028513
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
fas  │ fused add sub │         │ (a+b)−c
fam  │ fused add mul │         │ (a+b)*c
fad  │ fused add div │         │ (a+b)∕c
fsa  │ fused sub add │         │ (a−b)+c
fss  │ fused sub sub │         │ (a−b)−c
fsm  │ fused sub mul │         │ (a−b)*c
fsd  │ fused sub div │         │ (a−b)∕c
fma  │ fused mul add │         │ (a*b)+c
fms  │ fused mul sub │         │ (a*b)−c
fmm  │ fused mul mul │         │ (a*b)*c
fmd  │ fused mul div │         │ (a*b)∕c
fda  │ fused div add │         │ (a∕b)+c
fds  │ fused div sub │         │ (a∕b)−c
fdm  │ fused div mul │         │ (a∕b)*c
fdd  │ fused div div │         │ (a∕b)∕c
```

</details><details open><summary>vector </summary>

`neg` `inv` `add` `sub` are overloaded to support vectors
`mul` `div` are overloaded to perform scalar-and-vector operations

```
name              │ explanation              │ example 
──────────────────┼──────────────────────────┼─────────────────────
dot               │ dot product              │ (1,2,3)⋅(2,3,4) = 20
cross             │ cross product            │ (1,2,3)×(2,3,4) = (−1, 2,−1)
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
name         │ explanation                │ value
─────────────┼────────────────────────────┼───────────
E            │ euler's number             │ ≈ 2.71828182845904523536…
PI           │ archimedes' constant       │ ≈ 3.14159265358979323846…
TAU          │ PI*2                       │ ≈ 6.28318530717958647692…
GAMMA        │ euler-mascheroni constant  │ ≈ 0.57721566490153286060…
PHI          │ golden ratio               │ ≈ 1.61803398874989484820…
ZETA_3       │ apéry's constant           │ ≈ 1.20205690315959428539…
CATALAN      │ catalan's constant         │ ≈ 0.9159655941772190150…
OMEGA        │ omega constant             │ ≈ 0.56714329040978387299…
SQRT_2       │ pythagoras constant        │ ≈ 1.4142135623730951…
SQRT_3       │ square root of 3           │ ≈ 1.7320508075688772…
LN_2         │ natural logarithm of 2     │ ≈ 0.6931471805599453…
LN_10        │ natural logarithn of 10    │ ≈ 2.302585092994046…
POS_INF      │ IEEE 754 positive inf      │ +∞
NEG_INF      │ IEEE 754 negative inf      │ −∞
POS_ZERO     │ IEEE 754 positive zero     │ +0
NEG_ZERO     │ IEEE 754 negative zero     │ −0
QNAN         │ IEEE 754 quiet nan         │ qnan
SNAN         │ IEEE 754 signalling nan    │ snan
FLT_MAX      │ largest normal float       │ (2 − 2⁻²³) × 2⁺¹²⁷
FLT_MIN      │ smallest normal float      │ 2⁻¹²⁶
FLT_TRUE_MIN │ smallest subnormal float   │ 2⁻¹⁴⁹
DBL_MAX      │ largest normal double      │ (2 − 2⁻⁵²) × 2⁺¹⁰²³
DBL_MIN      │ smallest normal double     │ 2⁻¹⁰²²
DBL_TRUE_MIN │ smallest subnormal double  │ 2⁻¹⁰⁷⁴
```
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
```
name                                       │ value
───────────────────────────────────────────┼────────────────────────────────────────────────────────────
latin_upper                                │ ABCDEFGHIJKLMNOPQRSTUVWXYZ
latin_upper_superscript                    │ ᴬᴮꟲᴰᴱꟳᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾꟴᴿ ᵀᵁⱽᵂ
latin_upper_superscript_small              │  𐞄    𐞒𐞖ᶦ 𞀹ᶫ𞀻ᶰ   𐞪 𞁀ᶸ   𐞲
latin_lower_superscript                    │ ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖ𐞥ʳˢᵗᵘᵛʷˣʸᶻ
latin_lower_subscript                      │ ₐ 𞁞 ₑ  ₕᵢⱼₖₗₘₙₒₚ ᵣₛₜᵤᵥ ₓ
latin_lower                                │ abcdefghijklmnopqrstuvwxyz
latin_bold_upper                           │ 𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙
latin_bold_lower                           │ 𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳
latin_italic_upper                         │ 𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍
latin_italic_lower                         │ 𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝚤𝚥
latin_bold_italic_upper                    │ 𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁
latin_bold_italic_lower                    │ 𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛
latin_script_upper                         │ 𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵
latin_script_lower                         │ 𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏
latin_bold_script_upper                    │ 𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩
latin_bold_script_lower                    │ 𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃
latin_fraktur_upper                        │ 𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ
latin_fraktur_lower                        │ 𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷
latin_fraktur_bold_upper                   │ 𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅
latin_fraktur_bold_lower                   │ 𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟
latin_sans_serif_upper                     │ 𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹
latin_sans_serif_lower                     │ 𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓
latin_sans_serif_bold_upper                │ 𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭
latin_sans_serif_bold_lower                │ 𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇
latin_sans_serif_italic_upper              │ 𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡
latin_sans_serif_italic_lower              │ 𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻
latin_sans_serif_bold_italic_upper         │ 𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕
latin_sans_serif_bold_italic_lower         │ 𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯
latin_monospace_upper                      │ 𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉
latin_monospace_lower                      │ 𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣
latin_double_struck_upper                  │ 𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ
latin_double_struck_lower                  │ 𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫
latin_double_struck_italic_upper           │    ⅅ                      
latin_double_struck_italic_lower           │    ⅆⅇ   ⅈⅉ                
greek_names                                │ {alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega', 'digamma', 'san', 'tsan', 'sho', 'heta', 'koppa', 'sampi', 'yot', 'stigma'}
greek_upper                                │ ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩϜϺͶϷͰϘͲͿϚ
greek_upper_variant                        │        ϴ                     ϞϠ
greek_lower                                │ αβγδεζηθικλμνξοπρστυφχψωϝϻͷϸͱϙͳϳϛ
greek_lower_variant                        │  ϐ  ϵ  ϑ ϰ     ϖϱς  ϕ        ϟϡ
greek_lower_superscript                    │  ᵝᵞᵟᵋ  ᶿᶥ           ᵠᵡ
greek_lower_subscript                      │  ᵦᵧ             ᵨ   ᵩᵪ
greek_bold_upper                           │ 𝚨𝚩𝚪𝚫𝚬𝚭𝚮𝚯𝚰𝚱𝚲𝚳𝚴𝚵𝚶𝚷𝚸𝚺𝚻𝚼𝚽𝚾𝚿𝛀𝟊
greek_bold_upper_variant                   │        𝚹
greek_bold_lower                           │ 𝛂𝛃𝛄𝛅𝛆𝛇𝛈𝛉𝛊𝛋𝛌𝛍𝛎𝛏𝛐𝛑𝛒𝛔𝛕𝛖𝛗𝛘𝛙𝛚𝟋
greek_bold_lower_variant                   │     𝛜  𝛝 𝛞     𝛡𝛠𝛓  𝛟
greek_italic_upper                         │ 𝛢𝛣𝛤𝛥𝛦𝛧𝛨𝛩𝛪𝛫𝛬𝛭𝛮𝛯𝛰𝛱𝛲𝛴𝛵𝛶𝛷𝛸𝛹𝛺
greek_italic_upper_variant                 │        𝛳
greek_italic_lower                         │ 𝛼𝛽𝛾𝛿𝜀𝜁𝜂𝜃𝜄𝜅𝜆𝜇𝜈𝜉𝜊𝜋𝜌𝜎𝜏𝜐𝜑𝜒𝜓𝜔
greek_italic_lower_variant                 │     𝜖  𝜗 𝜘     𝜛𝜚𝜍  𝜙
greek_bold_italic_upper                    │ 𝜜𝜝𝜞𝜟𝜠𝜡𝜢𝜣𝜤𝜥𝜦𝜧𝜨𝜩𝜪𝜫𝜬𝜮𝜯𝜰𝜱𝜲𝜳𝜴
greek_bold_italic_upper_variant            │        𝜭
greek_bold_italic_lower                    │ 𝜶𝜷𝜸𝜹𝜺𝜻𝜼𝜽𝜾𝜿𝝀𝝁𝝂𝝃𝝄𝝅𝝆𝝈𝝉𝝊𝝋𝝌𝝍𝝎
greek_bold_italic_lower_variant            │     𝝐  𝝑 𝝒     𝝕𝝔𝝇  𝝓
greek_sans_serif_bold_upper                │ 𝝖𝝗𝝘𝝙𝝚𝝛𝝜𝝝𝝞𝝟𝝠𝝡𝝢𝝣𝝤𝝥𝝦𝝨𝝩𝝪𝝫𝝬𝝭𝝮
greek_sans_serif_bold_upper_variant        │        𝝧
greek_sans_serif_bold_lower                │ 𝝰𝝱𝝲𝝳𝝴𝝵𝝶𝝷𝝸𝝹𝝺𝝻𝝼𝝽𝝾𝝿𝞀𝞂𝞃𝞄𝞅𝞆𝞇𝞈
greek_sans_serif_bold_lower_variant        │     𝞊  𝞋 𝞌     𝞏𝞎𝞁  𝞍
greek_sans_serif_bold_italic_upper         │ 𝞐𝞑𝞒𝞓𝞔𝞕𝞖𝞗𝞘𝞙𝞚𝞛𝞜𝞝𝞞𝞟𝞠𝞢𝞣𝞤𝞥𝞦𝞧𝞨
greek_sans_serif_bold_italic_upper_variant │        𝞡
greek_sans_serif_bold_italic_lower         │ 𝞪𝞫𝞬𝞭𝞮𝞯𝞰𝞱𝞲𝞳𝞴𝞵𝞶𝞷𝞸𝞹𝞺𝞼𝞽𝞾𝞿𝟀𝟁𝟂
greek_sans_serif_bold_italic_lower_variant │     𝟄  𝟅 𝟆     𝟉𝟈𝞻  𝟇
greek_double_struck_upper                  │   ℾ            ℿ ⅀
greek_double_struck_lower                  │   ℽ            ℼ
hebrew                                     │ ℵℶℷℸ
digits                                     │ 0123456789↊↋
digits_superscript                         │ ⁰¹²³⁴⁵⁶⁷⁸⁹
digits_subscript                           │ ₀₁₂₃₄₅₆₇₈₉
digits_bold                                │ 𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗
digits_double_struck                       │ 𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡
digits_sans_serif                          │ 𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫
digits_sans_serif_bold                     │ 𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵
digits_monospace                           │ 𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿
increment                                  │ ∆
nabla                                      │ ∇
nabla_bold                                 │ 𝛁
nabla_italic                               │ 𝛻
nabla_bold_italic                          │ 𝜵
nabla_sans_serif_bold                      │ 𝝯
nabla_sans_serif_bold_italic               │ 𝞩
partial                                    │ ∂
partial_bold                               │ 𝛛
partial_italic                             │ 𝜕
partial_bold_italic                        │ 𝝏
partial_sans_serif_bold                    │ 𝞉
partial_sans_serif_bold_italic             │ 𝟃
plus_superscript                           │ ⁺
plus_subscript                             │ ₊
minus_superscript                          │ ⁻
minus_subscript                            │ ₋
equals_superscript                         │ ⁼
equals_subscript                           │ ₌
parenthesis_superscript                    │ ⁽⁾
parenthesis_left_subscript                 │ ₍₎
ceil                                       │ ⌈⌉
floor                                      │ ⌊⌋
parenthesis                                │ ()⏜⏝
square_bracket                             │ []⎴⎵⎶
curly_bracket                              │ {}⏞⏟
angle_bracket                              │ ⟨⟩
double_angle_bracket                       │ ⟪⟫
curved_angle_bracket                       │ ⧼⧽
guillemet                                  │ ‹›
double_guillemet                           │ «»
big_parenthesis                            │ ⎛⎜⎝⎞⎟⎠
big_square_bracket                         │ ⎡⎢⎣⎤⎥⎦
big_curly_bracket                          │ ⎧⎨⎩⎪⎫⎬⎭⎰⎱
big_integral                               │ ⌠⎮⌡
big_sigma                                  │ ⎲⎳
minus                                      │ − (not same as -)
plus_minus                                 │ ±
almost_equals                              │ ≈
proportional                               │ ∝
infinity                                   │ ∞
square_root                                │ √
cube_root                                  │ ∛
fourth_root                                │ ∜
therefore                                  │ ∴
because                                    │ ∵
integral                                   │ ∫∬∭⨌
angle                                      │ ∠
ratio                                      │ ∶ (not same as :)
proportion                                 │ ∷ (not same as ::)
minus_plus                                 │ ∓
dot_product                                │ ⋅ (not same as ·)
multiplication                             │ × (not same as x)
cross_product                              │ ⨯ (not same as ×)
division                                   │ ∕ (not same as /) (÷ is deprecated)
intersection                               │ ∩ (not same as n)
union                                      │ ∪ (not same as u)
subset                                     │ ⊂ (not same as c)
superset                                   │ ⊃
down_tack                                  │ ⊤ (not same as T)
up_tack                                    │ ⊥ 
left_tack                                  │ ⊣ 
right_tack                                 │ ⊢
big_down_tack                              │ ⟙ (not same as ⊤)
big_up_tack                                │ ⟘ (not same as ⊥)
perpendicular                              │ ⟂ (not same as ⊥)
negation                                   │ ¬
conjunction                                │ ∧ (not same as ^)
disjunction                                │ ∨ (not same as v)
implication                                │ → (not same as ->)
equivalence                                │ ↔ (not same as <->)
n_ary_conjunction                          │ ⋀ (not same as ∧)
n_ary_disjunction                          │ ⋁ (not same as ∨)
n_ary_union                                │ ⋃ (not same as ∪)
empty_set                                  │ ∅ (not same as θ)
less_than_or_equal_to                      │ ≤
greater_than_or_equal_to                   │ ≥
much_less_than                             │ ≪
much_greater_than                          │ ≫
sine                                       │ ∿
diameter                                   │ ⌀ (not same as ∅)
information                                │ ℹ (not same as i)
numero                                     │ № 
euler_constant                             │ ℇ                 (unconventional. use γ or 𝛾)
```
<!--
angstrom                   │ Å (not same as Å) (unconventional. use Å)
ohm                        │ Ω 
mho                        │ ℧ 
celsius                    │ ℃ (not same as °C)
fahrenheit                 │ ℉ (not same as °F)
kelvin                     │ K (not same as K) (do NOT use degree symbol °)
rankine                    │ °R
-->

i have no experience with the archaic greek letters

use these special characters only if you will display them without typesetting. generally try to rely on typesetting software if it is available

character conversion helper functions may be included later. for now, storing them as string constants is pretty good

# conversions

because i forget sometimes

```
name                  │ formula
──────────────────────┼────────────────────────────────────────────────────────────
degree_to_radian      │ radian = degree * 𝜋 ∕ 180
degree_to_turn        │   turn = degree ∕ 360
radian_to_degree      │ degree = radian * 180 ∕ 𝜋
radian_to_turn        │   turn = radian ∕ 𝜏
turn_to_degree        │ degree = turn * 360
turn_to_radian        │ radian = turn * 𝜏
```

ya :v thats pretty much it

this project is convenience > accuracy > predictability > features > performance so i dont really care how slow it does it, as long as it *does* it

motivation: sometimes i need the quotient of a division, but programs only give me truediv or floordiv. sometimes i juse need a neg function to use in a higher-order function, without resorting to a nameless lambda >:( sometimes i need floor and ceil. sometimes i need the min of a dataset. sometimes i want the mean of a database instead of writing sum/len

this project will take inspiration from [glm](https://github.com/icaven/glm) soon

<!--
 ⌠ 
 ⎮ 
 ⌡ 

⎛⎜⎝⎞⎟⎠ 	

⎡ 	
⎢ 	
⎣ 	

⎤ 	
⎥ 	
⎦ 	

⎧ 
⎪
⎨ 	
⎪
⎩ 	 	

⎫ 	
⎪
⎬ 	
⎪
⎭ 	

⎰
⎱
-->
