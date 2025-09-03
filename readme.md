<!-- implement something that can compare IEEE-754 values directly, instead of -0.0 == +0.0 being True-->
<!-- implement something that can expose the direct bits of a datatype, like an int, float, char, str, etc-->

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
name        │ explanation              │ example
────────────┼──────────────────────────┼────────────────────────────────
inc         │ increment                │            ++2 = 3
dec         │ decrement                │            −−2 = 1
neg         │ additive inverse         │             −2 = −2
inv         │ multiplicative inverse   │             ⅟2 = 0.5
mod         │ modulus                  │         −5 % 2 =  1
add         │ addition                 │         −5 + 2 = −3
sub         │ subtraction              │         −5 − 2 = −7
mul         │ multiplication           │         −5 × 2 = −10
div         │ division                 │         −5 ∕ 2 = −2.5
pow         │ exponentiation           │            −5² = 25
root        │ nᵗʰ root                 │     root(−5,2) ≈ 2.23606797𝑖
log         │ logarithm                │      log(−5,2) ≈ 2.322 + 4.532𝑖
sexp        │ tetration                │     sexp(-5,2) = 
sroot       │ super-root               │    sroot(-5,2) = 
slog        │ super-logarith           │     slog(-5,2) = 
parallel    │ parallel operator        │ parallel(−5,2) = 3.(3)
exp         │ exponentiation base e    │         exp(2) ≈ 7.389056098930
exp2        │ exponentiation base 2    │        exp2(2) = 4
exp10       │ exponentiation base 10   │       exp10(2) = 100
ln          │ logarithm base e         │          ln(2) ≈ 0.693147180559
log2        │ logarithm base 2         │        log2(2) = 1
log10       │ logarithm base 10        │       log10(2) ≈ 0.30103
expm1       │ exp(x) − 1               │       expm1(2) ≈ 6.38905609893065
exp2m1      │ exp2(x) − 1              │      exp2m1(2) = 3
exp10m1     │ exp10(x) − 1             │     exp10m1(2) = 99
lnp         │ ln(x + 1)                │         lnp(2) ≈ 1.0986122886681096
log2p       │ log2(x + 1)              │       log2p(2) ≈ 1.584962500721156
log10p      │ log10(x + 1)             │      log10p(2) ≈ 0.47712125471966244
sqrt        │ square root (√x)         │        sqrt(2) ≈ 1.4142135623730951
cbrt        │ cube root (∛x)           │        cbrt(2) ≈ 1.2599210498948732
rsqrt       │ reciprocal of sqrt(x)    │       rsqrt(2) ≈ 0.7071067811865475
rcbrt       │ reciprocal of cbrt(x)    │       rcbrt(2) ≈ 0.7937005259840997
abs         │ absolute value           │      abs(2+3𝑖) ≈ 3.6055512754
gcd         │ greatest common divisor  │       gcd(2,3) = 1
lcm         │ lowest common multiple   │       lcm(2,3) = 6
hyper       │ hyperoperation           │ hyper(1, 2, 3) = 5
ieee_div    │ IEEE-754-style division  │  ieee_div(0,0) = QNAN
floor       │ directed round to −∞     │ floor(1.23, 1) = 1.2
ceil        │ directed round to +∞     │  ceil(1.23, 1) = 1.3
trunc       │ directed round to ±0     │ trunc(1.23, 1) = 1.2
away        │ directed round away ±0   │  away(1.23, 1) = 1.3
round       │ to nearest, tie to even  │ round(1.23, 1) = 1.1
floordiv    │ division rounded to −∞   │ floordiv(−5,2) = −3
ceildiv     │ division rounded to +∞   │  ceildiv(-5,2) = -2
truncdiv    │ division rounded to ±0   │ truncdiv(−5,2) = −2
awaydiv     │ division rounded away ±0 │  awaydiv(-5,2) = -3
rounddiv    │ round(div(a,b))          │ rounddiv(-5,2) = -2
floorrem    │ remainder of floordiv    │ floorrem(-5,2) = 
ceilrem     │ remainder of ceildiv     │  ceilrem(-5,2) = 
truncrem    │ remainder of truncdiv    │ truncrem(−5,2) = −1
awayrem     │ remainder of awaydiv     │  awayrem(-5,2) = 
roundrem    │ remainder of rounddiv    │ roundrem(-5,2) = 
floordivrem │ remainder of floordiv    │ floorrem(-5,2) = 
ceildivrem  │ remainder of ceildiv     │  ceilrem(-5,2) = 
truncdivrem │ remainder of truncdiv    │ truncrem(−5,2) = −1
awaydivrem  │ remainder of awaydiv     │  awayrem(-5,2) = 
rounddivrem │ remainder of rounddiv    │ roundrem(-5,2) = 
```

if you need more exotic rounding or quantization, my [pyquantize](https://github.com/deftasparagusanaconda/pyquantize) tool does exactly that

i have not yet decided on a name for the variadic version of `parallel`, so it is not implemented yet

`sexp`, `sroot`, `slog` ~~are~~ will be based on kneser's extension  
a separate `pent` (pentation) will not be provided. but you are free to ask if you want it  
`hyper` will not support non-integer inputs for n ≥ 4 (tetration and beyond). not until im smart enough to implement kneser's extension for these
commutative hyperoperations will be added once i have understood them enough to implement them. i like them much more anyway :P


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
name            │ explanation               │ example
────────────────┼───────────────────────────┼───────────────────────────────────
sin             │ circular sine             │             sin(1) ≈ 0.8414709848
cos             │ circular cosine           │             cos(1) ≈ 0.54030230586
tan             │ circular tangent          │             tan(1) ≈ 1.55740772465
cot             │ circular cotangent        │             cot(1) ≈ 0.642093
sec             │ circular secant           │             sec(1) ≈ 1.85081571768
csc             │ circular cosecant         │             csc(1) ≈ 1.18839510578
asin            │ circular arcsine          │            asin(1) ≈ 1.57079633
acos            │ circular arccosine        │            acos(1) = 0
atan            │ circular arctangent       │            atan(1) ≈ 0.785398163
acot            │ circular arccotangent     │            acot(1) ≈ 0.785398163
asec            │ circular arcsecant        │            asec(1) = 0
acsc            │ circular arccosecant      │            acsc(1) ≈ 1.57079633
sinpi           │ sin(𝜋x)                   │           sinpi(1) = 0
cospi           │ cos(𝜋x)                   │           cospi(1) = −1
tanpi           │ tan(𝜋x)                   │           tanpi(1) = 0
cotpi           │ cot(𝜋x)                   │           cotpi(1) = ?
secpi           │ sec(𝜋x)                   │           secpi(1) = −1
cscpi           │ csc(𝜋x)                   │           cscpi(1) = ?
asinpi          │ asin(y)∕𝜋                 │          asinpi(1) = 0.5
acospi          │ acos(y)∕𝜋                 │          acospi(1) = 0
atanpi          │ atan(y)∕𝜋                 │          atanpi(1) = 0.25
acotpi          │ acot(y)∕𝜋                 │          acotpi(1) = 0.25
asecpi          │ asec(y)∕𝜋                 │          asecpi(1) = 0
acscpi          │ acsc(y)∕𝜋                 │          acscpi(1) = 0.5
sind            │ sin(𝜋x∕180)               │            sind(1) = 
cosd            │ cos(𝜋x∕180)               │            cosd(1) = 
tand            │ tan(𝜋x∕180)               │            tand(1) = 
cotd            │ cot(𝜋x∕180)               │            cotd(1) = 
secd            │ sec(𝜋x∕180)               │            secd(1) = 
cscd            │ csc(𝜋x∕180)               │            cscd(1) = 
asind           │ asin(y)×180∕𝜋             │           asind(1) = 
acosd           │ acos(y)×180∕𝜋             │           acosd(1) = 
atand           │ atan(y)×180∕𝜋             │           atand(1) = 
acotd           │ acot(y)×180∕𝜋             │           acotd(1) = 
asecd           │ asec(y)×180∕𝜋             │           asecd(1) = 
acscd           │ acsc(y)×180∕𝜋             │           acscd(1) = 
atan2           │ IEEE atan2                │         atan2(1,1) ≈ 0.785398163
atan2pi         │ IEEE atan2∕𝜋              │       atan2pi(1,1) = 0.25
atan2d          │ IEEE atan2×180∕𝜋          │        atan2d(1,1) ≈ 
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

galilean trigonometric functions are not included because they are trivial, in that `sing(x) = x` and `cosg(x) = 1`

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
nand  │ not(and)      │  1110 │ F ⊼ T = T
or    │ disjunction   │  0111 │ F ∨ T = T
nor   │ not(or)       │  1000 │ F ⊽ T = F
xor   │ exclusive or  │  0110 │ F ⊻ T = T
xnor  │ not(xor)      │  1001 │ F ⊙ T = F
imp   │ implication   │  1101 │ F ⇒ T = T
nimp  │ not(imp)      │  0010 │ F ⇏ T = F
con   │ converse      │  1011 │ F ⇐ T = F
ncon  │ not(con)      │  0100 │ F ⇍ T = T
```

</details><details open><summary>bitwise </summary>

bitwise operators must support direct binary bit manipulation of the datatype. even if it is an IEEE float, operate directly on the physical bits, not the logical value. if the data is not stored in binary, raise an error (since boolean algebra is only a binary algebra). thus whether `bitnot` is according to two's complement or not is up to the implementation

```
name     │ explanation  │ truth │ example
─────────┼──────────────┼───────┼──────────
bitnot   │ negation     │    10 │    ~5 = (probably 2)
bitand   │ conjunction  │  0001 │ 3 ∧ 5 = 
bitnand  │ not(and)     │  1110 │ 3 ⊼ 5 = 
bitor    │ disjunction  │  0111 │ 3 ∨ 5 = 
bitnor   │ not(or)      │  1000 │ 3 ⊽ 5 = 
bitxor   │ exclusive or │  0110 │ 3 ⊻ 5 = 
bitxnor  │ not(xor)     │  1001 │ 3 ⊙ 5 = 
bitimp   │ implication  │  1101 │ 3 ⇒ 5 = 
bitnimp  │ not(imp)     │  0010 │ 3 ⇏ 5 = 
bitcon   │ converse     │  1011 │ 3 ⇐ 5 = 
bitncon  │ not(con)     │  0100 │ 3 ⇍ 5 = 
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

the `in_*_interval` functions are simply for readability, for when sometimes, for example, `in_open_interval(x, a, b)` is easier to understand than `a < x < b`

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
`linrange` is like numpy's `linrange`
`parity` should operate on the direct bits of the datatype

```
name      │ explanation                            │ example
──────────┼────────────────────────────────────────┼──────────────────────────────────────────
to_bitstring│
normalize │ normalize a vector                     │ 
norm      │ euclidean norm                         │  norm(1, 2, 3) ≈ 3.7416573867739413
signbit   │ false if +ve else true                 │          signbit(3) = T
copysign  │ magnitude of a with sign of b          │      copysign(2, 3) = 2
any       │ n-ary OR gate                          │        any(F, T, F) = T
all       │ n-ary AND gate                         │        all(F, T, F) = F
min       │ minimum                                │        min(1, 2, 3) = 1
max       │ maximum                                │        max(1, 2, 3) = 3
fst       │ first element                          │        fst(1, 2, 3) = 1
snd       │ second element                         │        snd(1, 2, 3) = 2
sgn       │ signum. −1 if <0, +1 if >0, else 0     │            sgn(0.5) = 1
swap      │ swap variables in memory               │          swap(a, b) = (b, a)
parity    │ sum of 1 bits                          │           parity(5) = 2
frange    │ iterable of numbers in an interval     │  frange(0, 10, 2.5) = [0, 2.5, 5, 7.5]
linspace  │ fixed number of numbers in an interval │ 
isinf     │ true if IEEE inf                       │ isinf(float('inf')) = True
isnan     │ true if IEEE nan                       │ isnan(float('nan')) = False
erf       │ error function                         │              erf(1) ≈ 0.8427007929497149
erfc      │ 1−erf(x)                               │             erfc(1) ≈ 0.15729920705028513
gamma     │ gamma function                         │          gamma(1.5) ≈ 0.886226925452758
lgamma    │ natural logarithm of gamma(x)          │         lgamma(999) ≈ 5898.313668430534
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
──────────────────┼──────────────────────────┼─────────────────────────────
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
POS_INF      │ IEEE 754 positive inf            │ +∞
NEG_INF      │ IEEE 754 negative inf            │ −∞
POS_ZERO     │ IEEE 754 positive zero           │ +0.0
NEG_ZERO     │ IEEE 754 negative zero           │ −0.0
POS_QNAN     │ IEEE 754 positive quiet nan      │ +qnan
NEG_QNAN     │ IEEE 754 negative quiet nan      │ -qnan
POS_SNAN     │ IEEE 754 positive signalling nan │ +snan
NEG_SNAN     │ IEEE 754 negative signalling nan │ +snan
FLT_MAX      │ largest normal float             │ (2 − 2⁻²³) × 2⁺¹²⁷
FLT_MIN      │ smallest normal float            │ 2⁻¹²⁶
FLT_TRUE_MIN │ smallest subnormal float         │ 2⁻¹⁴⁹
DBL_MAX      │ largest normal double            │ (2 − 2⁻⁵²) × 2⁺¹⁰²³
DBL_MIN      │ smallest normal double           │ 2⁻¹⁰²²
DBL_TRUE_MIN │ smallest subnormal double        │ 2⁻¹⁰⁷⁴
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
HEBREW                                     │ ℵℶℷℸ
DIGIT                                      │ 0123456789↊↋
DIGIT_SUPERSCRIPT                          │ ⁰¹²³⁴⁵⁶⁷⁸⁹  
DIGIT_SUBSCRIPT                            │ ₀₁₂₃₄₅₆₇₈₉  
DIGIT_BOLD                                 │ 𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗  
DIGIT_DOUBLE_STRUCK                        │ 𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡  
DIGIT_SANS_SERIF                           │ 𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫  
DIGIT_SANS_SERIF_BOLD                      │ 𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵  
DIGIT_MONOSPACE                            │ 𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿  
ROMAN_NUMERAL_UPPER                        │  ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫⅬⅭⅮⅯ
ROMAN_NUMERAL_LOWER                        │  ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹⅺⅻⅼⅽⅾⅿ
COUNTING_ROD_VERTICAL                      │ 〇𝍩𝍪𝍫𝍬𝍭𝍮𝍯𝍰𝍱
COUNTING_ROD_HORIZONTAL                    │ 〇𝍠𝍡𝍢𝍣𝍤𝍥𝍦𝍧𝍨
COUNTING_ROD_NEGATIVE                      │ (U+20E5)
TALLY_MARK                                 │  𝍷   𝍸
TALLY_MARK_IDEOGRAPHIC                     │  𝍲𝍳𝍴𝍵𝍶
RECIPROCAL                                 │ ⅟
FRACTION_0_BY                              │    ↉       
FRACTION_1_BY                              │   ½⅓¼⅕⅙⅐⅛⅑⅒
FRACTION_2_BY                              │    ⅔ ⅖     
FRACTION_3_BY                              │     ¾⅗  ⅜  
FRACTION_4_BY                              │      ⅘     
FRACTION_5_BY                              │       ⅚ ⅝  
FRACTION_7_BY                              │         ⅞  
INCREMENT                                  │ ∆
NABLA                                      │ ∇
NABLA_BOLD                                 │ 𝛁
NABLA_ITALIC                               │ 𝛻
NABLA_BOLD_ITALIC                          │ 𝜵
NABLA_SANS_SERIF_BOLD                      │ 𝝯
NABLA_SANS_SERIF_BOLD_ITALIC               │ 𝞩
PARTIAL                                    │ ∂
PARTIAL_BOLD                               │ 𝛛
PARTIAL_ITALIC                             │ 𝜕
PARTIAL_BOLD_ITALIC                        │ 𝝏
PARTIAL_SANS_SERIF_BOLD                    │ 𝞉
PARTIAL_SANS_SERIF_BOLD_ITALIC             │ 𝟃
PLUS_SUPERSCRIPT                           │ ⁺
PLUS_SUBSCRIPT                             │ ₊
MINUS_SUPERSCRIPT                          │ ⁻
MINUS_SUBSCRIPT                            │ ₋
EQUAL_SUPERSCRIPT                          │ ⁼
EQUAL_SUBSCRIPT                            │ ₌
PARENTHESIS_SUPERSCRIPT                    │ ⁽⁾
PARENTHESIS_SUBSCRIPT                      │ ₍₎
CEIL                                       │ ⌈⌉
FLOOR                                      │ ⌊⌋
PARENTHESIS                                │ ()⏜⏝
SQUARE_BRACKET                             │ []⎴⎵⎶
CURLY_BRACKET                              │ {}⏞⏟
ANGLE_BRACKET                              │ ⟨⟩
DOUBLE_ANGLE_BRACKET                       │ ⟪⟫
CURVED_ANGLE_BRACKET                       │ ⧼⧽
GUILLEMET                                  │ ‹›
DOUBLE_GUILLEMET                           │ «»
LESS_THAN                                  │ <
NOT_LESS_THAN                              │ ≮
GREATER_THAN                               │ >
NOT_GREATER_THAN                           │ ≯
LESS_THAN_OR_EQUAL                         │ ≤
NOT_LESS_THAN_NOR_EQUAL                    │ ≰
GREATER_THAN_OR_EQUAL                      │ ≥
NOT_GREATER_THAN_NOR_EQUAL                 │ ≱
MUCH_LESS_THAN                             │ ≪
MUCH_GREATER_THAN                          │ ≫
EQUAL                                      │ =
NOT_EQUAL                                  │ ≠
ALMOST_EQUAL                               │ ≈
NOT_ALMOST_EQUAL                           │ ≉
IDENTICAL                                  │ ≡
NOT_IDENTICAL                              │ ≢
PROPORTIONAL                               │ ∝
INFINITY                                   │ ∞
SQUARE_ROOT                                │ √
CUBE_ROOT                                  │ ∛
FOURTH_ROOT                                │ ∜
THEREFORE                                  │ ∴
BECAUSE                                    │ ∵
INTEGRAL                                   │ ∫
DOUBLE_INTEGRAL                            │ ∬
TRIPLE_INTEGRAL                            │ ∭
QUADRUPLE_INTEGRAL                         │ ⨌
ANGLE                                      │ ∠
RATIO                                      │ ∶ (not same as :)
PROPORTION                                 │ ∷ (not same as ::)
PLUS                                       │ +
MINUS                                      │ − (not same as -)
PLUS_MINUS                                 │ ±
MINUS_PLUS                                 │ ∓
CIRCLED_PLUS                               │ ⊕
CIRCLED_MINUS                              │ ⊖
CIRCLED_TIMES                              │ ⊗
CIRCLED_DIVISION_SLASH                     │ ⊘
CIRCLED_DIVISION_SIGN                      │ ⨸ (unconventional. use ⊘)
CIRCLED_DOT_OPERATOR                       │ ⊙
CIRCLED_EQUAL                              │ ⊜
SQUARED_PLUS                               │ ⊠
SQUARED_MINUS                              │ ⊟
SQUARED_TIMES                              │ ⊞
SQUARED_DOT_OPERATOR                       │ ⊡
TIMES                                      │ × (not same as x)
DIVISION_SLASH                             │ ∕ (not same as /)
DIVISION_SIGN                              │ ÷ (unconventional. use ∕)
FRACTION                                   │ ⁄ (not same as ∕)
TILDE_OPERATOR                             │ ∼ (not same as ~)
DOT_OPERATOR                               │ ⋅ (not same as ·)
CROSS_PRODUCT                              │ ⨯ (not same as ×)
INTERSECTION                               │ ∩ (not same as n)
UNION                                      │ ∪ (not same as u)
ELEMENT_OF                                 │ ∈
ELEMENT_OF_SMALL                           │ ∊ (not same as ∈)
NOT_ELEMENT_OF                             │ ∉
CONTAINS                                   │ ∋
CONTAINS_SMALL                             │ ∍ (not same as ∋)
NOT_CONTAINS                               │ ∌
SUBSET                                     │ ⊂ (not same as c)
SUPERSET                                   │ ⊃
PROPER_SUBSET                              │ ⊆
PROPER_SUPERSET                            │ ⊇
NOT_SUBSET                                 │ ⊄
NOT_SUPERSET                               │ ⊅
DOWN_TACK                                  │ ⊤ (not same as T)
UP_TACK                                    │ ⊥
LEFT_TACK                                  │ ⊣
RIGHT_TACK                                 │ ⊢
DIVIDES                                    │ ∣ (not same as |)
NOT_DIVIDES                                │ ∤
PARALLEL                                   │ ∥ (not same as ||)
PERPENDICULAR                              │ ⟂ (not same as ⊥)
NOT                                        │ ¬
AND                                        │ ∧ (not same as ^)
OR                                         │ ∨ (not same as v)
NAND                                       │ ⊼
NOR                                        │ ⊽
XOR                                        │ ⊻
BIG_PARENTHESIS                            │ ⎛⎜⎝⎞⎟⎠
BIG_SQUARE_BRACKET                         │ ⎡⎢⎣⎤⎥⎦
BIG_CURLY_BRACKET                          │ ⎧⎨⎩⎪⎫⎬⎭⎰⎱
BIG_INTEGRAL                               │ ⌠⎮⌡
BIG_BIG_SIGMA                              │ ⎲⎳
BIG_DOWN_TACK                              │ ⟙ (not same as ⊤)
BIG_UP_TACK                                │ ⟘ (not same as ⊥)
BIG_CONJUNCTION                            │ ⋀ (not same as ∧)
BIG_DISJUNCTION                            │ ⋁ (not same as ∨)
BIG_INTERSECTION                           │ ⋂ (not same as ∩)
BIG_UNION                                  │ ⋃ (not same as ∪)
BIG_CIRCLED_PLUS                           │ ⨁ (not same as ⊕)
BIG_CIRCLED_TIMES                          │ ⨂ (not same as ⊗)
BIG_CIRCLED_DOT_OPERATOR                   │ ⨀ (not same as ⊙)
BIG_PI                                     │ ∏ (not same as Π)
BIG_SIGMA                                  │ ∑ (not same as Σ)
BIG_TIMES                                  │ ⨉ (not same as ×)
EMPTY_SET                                  │ ∅ (not same as θ)
ARROW                                      │ ←↑→↓↔↕↖↗↘↙
ARROW_STROKE                               │ ↚ ↛ ↮
ARROW_DOUBLE                               │ ⇐⇑⇒⇓⇔⇕⇖⇗⇘⇙
ARROW_DOUBLE_STROKE                        │ ⇍ ⇏ ⇎
ARROW_TRIPLE                               │ ⇚ ⇛
ARROW_HARPOON                              │ ⇋⇌
ARROW_PAIRED                               │ ⇇⇈⇉⇊
ARROW_PAIRED_OPPOSITES                     │ ⇄⇅⇆⇵
ARROW_PAIRED_TRIPLE                        │ ⬱ ⇶
ARROW_DASHED                               │ ⇠⇡⇢⇣
ARROW_WHITE                                │ ⇦⇧⇨⇩
ELLIPSIS_VERTICAL                          │ ⋮
ELLIPSIS_HORIZONTAL                        │ ⋯
ELLIPSIS_DIAGONAL_UP_RIGHT                 │ ⋰
ELLIPSIS_DIAGONAL_DOWN_RIGHT               │ ⋱
DIAMETER                                   │ ⌀ (not same as ∅)
NUMERO                                     │ №
EULER_CONSTANT                             │ ℇ (unconventional. use γ or 𝛾)
DOTLESS_ITALIC_I                           │ 𝚤
DOTLESS_ITALIC_J                           │ 𝚥
CIRCLE_BLACK                               │ ●
CIRCLE_WHITE                               │ ○
CIRCLE_HEAVY                               │ ⭘
CIRCLE_LARGE_BLACK                         │ ⬤
CIRCLE_LARGE_WHITE                         │ ◯
CIRCLE_LARGE_HEAVY                         │ ⭕
ELLIPSE_HORIZONTAL_BLACK                   │ ⬬
ELLIPSE_HORIZONTAL_WHITE                   │ ⬭
ELLIPSE_VERTICAL_BLACK                     │ ⬮
ELLIPSE_VERTICAL_WHITE                     │ ⬯
TRIANGLE_UP_BLACK                          │ ▲
TRIANGLE_UP_WHITE                          │ △
TRIANGLE_RIGHT_BLACK                       │ ▶
TRIANGLE_RIGHT_WHITE                       │ ▷
TRIANGLE_DOWN_BLACK                        │ ▼
TRIANGLE_DOWN_WHITE                        │ ▽
TRIANGLE_LEFT_BLACK                        │ ◀
TRIANGLE_LEFT_WHITE                        │ ◁
TRIANGLE_SMALL_UP_BLACK                    │ ▴
TRIANGLE_SMALL_UP_WHITE                    │ ▵
TRIANGLE_SMALL_RIGHT_BLACK                 │ ▸
TRIANGLE_SMALL_RIGHT_WHITE                 │ ▹
TRIANGLE_SMALL_DOWN_BLACK                  │ ▾
TRIANGLE_SMALL_DOWN_WHITE                  │ ▿
TRIANGLE_SMALL_LEFT_BLACK                  │ ◂
TRIANGLE_SMALL_LEFT_WHITE                  │ ◃
TRIANGLE_CENTRED_MEDIUM_UP_BLACK           │ ⯅
TRIANGLE_CENTRED_MEDIUM_DOWN_BLACK         │ ⯆
TRIANGLE_CENTRED_MEDIUM_LEFT_BLACK         │ ⯇
TRIANGLE_CENTRED_MEDIUM_RIGHT_BLACK        │ ⯈
TRIANGLE_UPPER_LEFT_BLACK                  │ ◤
TRIANGLE_UPPER_LEFT_WHITE                  │ ◸
TRIANGLE_LOWER_LEFT_BLACK                  │ ◣
TRIANGLE_LOWER_LEFT_WHITE                  │ ◺
TRIANGLE_UPPER_RIGHT_BLACK                 │ ◥
TRIANGLE_UPPER_RIGHT_WHITE                 │ ◹
TRIANGLE_LOWER_RIGHT_BLACK                 │ ◢
TRIANGLE_LOWER_RIGHT_WHITE                 │ ◿
POINTER_RIGHT_BLACK                        │ ►
POINTER_RIGHT_WHITE                        │ ▻
POINTER_LEFT_BLACK                         │ ◄
POINTER_LEFT_WHITE                         │ ◅
SQUARE_BLACK                               │ ■
SQUARE_WHITE                               │ □
SQUARE_MEDIUM_BLACK                        │ ◼
SQUARE_MEDIUM_WHITE                        │ ◻
SQUARE_SMALL_BLACK                         │ ▪
SQUARE_SMALL_WHITE                         │ ▫
SQUARE_VERY_SMALL_BLACK                    │ ⬝
SQUARE_VERY_SMALL_WHITE                    │ ⬞
SQUARE_CENTRED_BLACK                       │ ⯀
RECTANGLE_HORIZONTAL_BLACK                 │ ▬
RECTANGLE_HORIZONTAL_WHITE                 │ ▭
RECTANGLE_VERTICAL_BLACK                   │ ▮
RECTANGLE_VERTICAL_WHITE                   │ ▯
PARALLELOGRAM_BLACK                        │ ▰
PARALLELOGRAM_WHITE                        │ ▱
DIAMOND_BLACK                              │ ◆
DIAMOND_WHITE                              │ ◇
DIAMOND_MEDIUM_BLACK                       │ ⬥
DIAMOND_MEDIUM_WHITE                       │ ⬦
DIAMOND_SMALL_BLACK                        │ ⬩
DIAMOND_CENTRED_BLACK                      │ ⯁
LOZENGE_BLACK                              │ ⧫
LOZENGE_WHITE                              │ ◊
LOZENGE_MEDIUM_BLACK                       │ ⬧
LOZENGE_MEDIUM_WHITE                       │ ⬨
LOZENGE_SMALL_BLACK                        │ ⬪ (colour reversed)
LOZENGE_SMALL_WHITE                        │ ⬫ (colour reversed)
CUSP_BLACK                                 │ ⯌
CUSP_WHITE                                 │ ⯎
CUSP_ROTATED_BLACK                         │ ⯍
CUSP_ROTATED_WHITE 	                       │ ⯏
PENTAGON_BLACK                             │ ⬟
PENTAGON_WHITE                             │ ⬠
PENTAGON_RIGHT_BLACK                       │ ⭓
PENTAGON_RIGHT_WHITE                       │ ⭔
PENTAGON_DOWN_BLACK                        │ ⯂ 
STAR_SMALL_BLACK                           │ ⭑
STAR_SMALL_WHITE                           │ ⭒
HEXAGON_VERTICAL_WHITE                     │ ⬡
HEXAGON_VERTICAL_BLACK                     │ ⬢
HEXAGON_HORIZONTAL_BLACK                   │ ⬣
OCTAGON_VERTICAL_BLACK                     │ ⯄
OCTAGON_HORIZONTAL_BLACK                   │ ⯃
```
<!--
GREEK_NAME                                 │ {'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega', 'digamma', 'san', 'tsan', 'sho', 'heta', 'koppa', 'sampi', 'yot', 'stigma'}
angstrom                   │ Å (not same as Å) (unconventional. use Å)
-->

<!--
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
degree_to_radian      │ radian = degree * 𝜏 ∕ 360
degree_to_turn        │   turn = degree ∕ 360
radian_to_degree      │ degree = radian * 360 ∕ 𝜏
radian_to_turn        │   turn = radian ∕ 𝜏
turn_to_degree        │ degree = turn * 360
turn_to_radian        │ radian = turn * 𝜏
```

ya :v thats pretty much it

this project is convenience > accuracy > predictability > features > performance so i dont really care how slow it does it, as long as it *does* it.

special cases like 0/0 are handled according to how *you* like it, using a global variable. 

motivation: sometimes i need the quotient of a division, but programs only give me truediv or floordiv. sometimes i juse need a neg function to use in a higher-order function, without resorting to a nameless lambda >:( sometimes i need floor and ceil. sometimes i need the min of a dataset. sometimes i want the mean of a database instead of writing sum/len

this project will take inspiration from [glm](https://github.com/icaven/glm) soon
