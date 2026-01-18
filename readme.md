<!-- implement something that can compare IEEE-754 values directly, instead of -0.0 == +0.0 being True, or nan(2) == nan(3) being False -->
<!-- implement something that can expose the direct bits of a datatype, like an int, float, char, str, etc -->
<!-- implement something that can generate a nan from a given integer payload-->
<!-- implement something that can take number prefixes like 0b 0d 0x 0t 0q 0o -->
<!-- bitwise ops should support: grouping (differentiates bitrev and byteswap), repr (2's complement by default) and floats should be treated as direct bits-->

daamath is my personal counterpart
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

complex numbers are fully supported but type will not always be promoted to complex. for example, log will promote to complex only when negative input is given. or sqrt(−4) will appropriately promote to a complex 2𝑖

```
name        │ explanation              │ example
────────────┼──────────────────────────┼────────────────────────────────
add         │ addition                 │         −5 + 2 = −3
sub         │ subtraction              │         −5 − 2 = −7
mul         │ multiplication           │         −5 × 2 = −10
div         │ division                 │         −5 ∕ 2 = −2.5
inc         │ increment                │            ++2 = 3
dec         │ decrement                │            −−2 = 1
neg         │ additive inverse         │             −2 = −2
inv         │ multiplicative inverse   │             ⅟2 = 0.5
mod         │ modulus                  │         −5 % 2 =  1
root        │ nᵗʰ root                 │    root(−5, 2) ≈ 2.23606797𝑖
pow         │ exponentiation           │            −5² = 25
exp         │ exponentiation base 𝑒    │         exp(2) ≈ 7.389056098930
exp2        │ exponentiation base 2    │        exp2(2) = 4
exp10       │ exponentiation base 10   │       exp10(2) = 100
log         │ logarithm                │     log(−5, 2) ≈ 2.322 + 4.532𝑖
loge        │ logarithm base 𝑒         │        logₑ(2) ≈ 0.693147180559
log2        │ logarithm base 2         │        log₂(2) = 1
log10       │ logarithm base 10        │        log⏨(2) ≈ 0.30103
powm1       │ pow(a, b) − 1            │   powm1(−5, 2) = 
expm1       │ exp(a) − 1               │       expm1(2) ≈ 6.38905609893065
exp2m1      │ exp2(a) − 1              │      exp₂m1(2) = 3
exp10m1     │ exp10(a) − 1             │      exp⏨m1(2) = 99
logp1       │ log(abs + 1, b)          │       logp1(2) = 
logep1      │ loge(a + 1)              │      logₑp1(2) ≈ 
log2p1      │ log2(a + 1)              │      log₂p1(2) ≈ 
log10p1     │ log10(a + 1)             │      log⏨p1(2) ≈ 
sexp        │ tetration                │     sexp(−5,2) = 
sroot       │ super-root               │    sroot(−5,2) = 
slog        │ super-logarith           │     slog(−5,2) = 
parallel    │ parallel operator        │ parallel(−5,2) = 3.(3)
sqrt        │ square root (√x)         │        sqrt(2) ≈ 1.4142135623730951
cbrt        │ cube root (∛x)           │        cbrt(2) ≈ 1.2599210498948732
rsqrt       │ reciprocal of sqrt(x)    │       rsqrt(2) ≈ 0.7071067811865475
rcbrt       │ reciprocal of cbrt(x)    │       rcbrt(2) ≈ 0.7937005259840997
abs         │ absolute value           │      abs(2+3𝑖) ≈ 3.6055512754
gcd         │ greatest common divisor  │       gcd(2,3) = 1
lcm         │ lowest common multiple   │       lcm(2,3) = 6
hyper       │ hyperoperation           │  hyper(1, 2,3) = 5
floor       │ directed round to −∞     │  floor(1.23,1) = 1.2
floor1p     │ floor(x) + 1             │ floor1p(1.2,1) =
ceil        │ directed round to +∞     │   ceil(1.23,1) = 1.3
ceil1m      │ ceil(x) - 1              │  ceil1m(1.2,1) =
trunc       │ directed round to ±0     │  trunc(1.23,1) = 1.2
away        │ directed round away ±0   │   away(1.23,1) = 1.3
round       │ to nearest, tie to even  │  round(1.23,1) = 1.1
floordiv    │ division rounded to −∞   │ floordiv(−5,2) = −3
ceildiv     │ division rounded to +∞   │  ceildiv(−5,2) = −2
truncdiv    │ division rounded to ±0   │ truncdiv(−5,2) = −2
awaydiv     │ division rounded away ±0 │  awaydiv(−5,2) = −3
rounddiv    │ round(div(a,b))          │ rounddiv(−5,2) = −2
floorrem    │ remainder of floordiv    │ floorrem(−5,2) = 
ceilrem     │ remainder of  ceildiv    │  ceilrem(−5,2) = 
truncrem    │ remainder of truncdiv    │ truncrem(−5,2) = 
awayrem     │ remainder of  awaydiv    │  awayrem(−5,2) = 
roundrem    │ remainder of rounddiv    │ roundrem(−5,2) = 
floordivrem │ (floordiv, floorrem)     │ floorrem(−5,2) = 
ceildivrem  │ ( ceildiv,  ceilrem)     │  ceilrem(−5,2) = 
truncdivrem │ (truncdiv, truncrem)     │ truncrem(−5,2) = 
awaydivrem  │ ( awaydiv,  awayrem)     │  awayrem(−5,2) = 
rounddivrem │ (rounddiv, roundrem)     │ roundrem(−5,2) = 
```

`log` always takes number and base, because mathematicians assume it is logₑ(x) while engineers assume it is log⏨(x). this causes problems. this problem does not occur for exponentiation as, following convention, we have `pow` and `exp` separately for xʸ and eˣ respectively.

`modulus` will not allow non-integer input. it is based on modular arithmetic, which only concerns integers. `floorrem` gives the same results but works for fractional input

if you need more exotic rounding or quantization, my [pyquantize](https://github.com/deftasparagusanaconda/pyquantize) tool does exactly that

i have not yet decided on a name for the variadic version of `parallel`, so it is not implemented yet

`sexp`, `sroot`, `slog` ~~are~~ will be based on kneser's extension  
a separate `pent` (pentation) will not be provided. but you are free to ask if you want it  
`hyper` will not support non-integer inputs for n ≥ 4 (tetration and beyond). not until im smart enough to implement kneser's extension for these
commutative hyperoperations will be added once i have understood them enough to implement them. i like them much more anyway :P

</details><details open><summary>comparative </summary>

```
name │ explanation        │ example  
─────┼────────────────────┼────────────────────
lt   │ less than          │ 2 < 3 is true 
le   │ at most            │ 2 ≤ 3 is true
eq   │ equal to           │ 2 = 3 is false
ne   │ not equal to       │ 2 ≠ 3 is true
ge   │ at least           │ 2 ≥ 3 is false
gt   │ greater than       │ 2 > 3 is false
clt  │ component-wise lt  │ 2+3𝑖 < 4+3𝑖 is (T,F)
cle  │ component-wise le  │ 2+3𝑖 ≤ 4+3𝑖 is (T,T)
ceq  │ component-wise eq  │ 2+3𝑖 = 4+3𝑖 is (F,T)
cne  │ component-wise ne  │ 2+3𝑖 ≠ 4+3𝑖 is (T,F)
cge  │ component-wise ge  │ 2+3𝑖 ≥ 4+3𝑖 is (F,T)
cgt  │ component-wise gt  │ 2+3𝑖 > 4+3𝑖 is (F,F)
mlt  │ magnitudinal lt    │ 2 < 3 is true 
mle  │ magnitudinal le    │ 2 ≤ 3 is true
meq  │ magnitudinal eq    │ 2 = 3 is false
mne  │ magnitudinal ne    │ 2 ≠ 3 is true
mge  │ magnitudinal ge    │ 2 ≥ 3 is false
mgt  │ magnitudinal gt    │ 2 > 3 is false
cmp  │ comparison         │ 2 <=> 3 is -1
ccmp │ component-wise cmp │ 2 <=> 3 is (-1)
mcmp │ magnitudinal cmp   │ 2 <=> 3 is -1
```

</details><details open><summary>trigonometric </summary>

```
name             │ explanation               │ example
─────────────────┼───────────────────────────┼────────────────────────────────────
sin              │ circular sine             │              sin(1) ≈ 0.8414709848
cos              │ circular cosine           │              cos(1) ≈ 0.54030230586
tan              │ circular tangent          │              tan(1) ≈ 1.55740772465
cot              │ circular cotangent        │              cot(1) ≈ 0.642093
sec              │ circular secant           │              sec(1) ≈ 1.85081571768
csc              │ circular cosecant         │              csc(1) ≈ 1.18839510578
asin             │ circular arcsine          │             asin(1) ≈ 1.57079633
acos             │ circular arccosine        │             acos(1) = 0
atan             │ circular arctangent       │             atan(1) ≈ 0.785398163
acot             │ circular arccotangent     │             acot(1) ≈ 0.785398163
asec             │ circular arcsecant        │             asec(1) = 0
acsc             │ circular arccosecant      │             acsc(1) ≈ 1.57079633
<!--
sinpi            │ sin(𝜋x)                   │            sinpi(1) = 0
cospi            │ cos(𝜋x)                   │            cospi(1) = −1
tanpi            │ tan(𝜋x)                   │            tanpi(1) = 0
cotpi            │ cot(𝜋x)                   │            cotpi(1) = ?
secpi            │ sec(𝜋x)                   │            secpi(1) = −1
cscpi            │ csc(𝜋x)                   │            cscpi(1) = ?
asinpi           │ asin(y)∕𝜋                 │           asinpi(1) = 0.5
acospi           │ acos(y)∕𝜋                 │           acospi(1) = 0
atanpi           │ atan(y)∕𝜋                 │           atanpi(1) = 0.25
acotpi           │ acot(y)∕𝜋                 │           acotpi(1) = 0.25
asecpi           │ asec(y)∕𝜋                 │           asecpi(1) = 0
acscpi           │ acsc(y)∕𝜋                 │           acscpi(1) = 0.5
sintau           │ sin(𝜏x)                   │           sintau(1) = 
costau           │ cos(𝜏x)                   │           costau(1) = 
tantau           │ tan(𝜏x)                   │           tantau(1) = 
cottau           │ cot(𝜏x)                   │           cottau(1) = 
sectau           │ sec(𝜏x)                   │           sectau(1) = 
csctau           │ csc(𝜏x)                   │           csctau(1) = 
asintau          │ asin(y)∕𝜏                 │          asintau(1) = 
acostau          │ acos(y)∕𝜏                 │          acostau(1) = 
atantau          │ atan(y)∕𝜏                 │          atantau(1) = 
acottau          │ acot(y)∕𝜏                 │          acottau(1) = 
asectau          │ asec(y)∕𝜏                 │          asectau(1) = 
acsctau          │ acsc(y)∕𝜏                 │          acsctau(1) = 
sind             │ sin(𝜏x∕360)               │             sind(1) = 
cosd             │ cos(𝜏x∕360)               │             cosd(1) = 
tand             │ tan(𝜏x∕360)               │             tand(1) = 
cotd             │ cot(𝜏x∕360)               │             cotd(1) = 
secd             │ sec(𝜏x∕360)               │             secd(1) = 
cscd             │ csc(𝜏x∕360)               │             cscd(1) = 
asind            │ asin(y)×360∕𝜏             │            asind(1) = 
acosd            │ acos(y)×360∕𝜏             │            acosd(1) = 
atand            │ atan(y)×360∕𝜏             │            atand(1) = 
acotd            │ acot(y)×360∕𝜏             │            acotd(1) = 
asecd            │ asec(y)×360∕𝜏             │            asecd(1) = 
acscd            │ acsc(y)×360∕𝜏             │            acscd(1) = 
-->
atan2            │ IEEE atan2                │          atan2(1,1) ≈ 0.785398163
<!--
atan2pi          │ atan2∕𝜋                   │        atan2pi(1,1) = 
atan2tau         │ atan2∕𝜏                   │       atan2tau(1,1) = 
atan2d           │ atan2×360∕𝜏               │         atan2d(1,1) ≈ 
-->
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
<!--
versinpi         │ versin(𝜋x)                │         versinpi(x) = 1 − cos(𝜋x)
vercospi         │ vercos(𝜋x)                │         vercospi(x) = 1 + cos(𝜋x)
coversinpi       │ coversin(𝜋x)              │       coversinpi(x) = 1 − sin(𝜋x)
covercospi       │ covercos(𝜋x)              │       covercospi(x) = 1 + sin(𝜋x)
haversinpi       │ haversin(𝜋x)              │       haversinpi(x) = (1 − cos(𝜋x))∕2
havercospi       │ havercos(𝜋x)              │       havercospi(x) = (1 + cos(𝜋x))∕2
hacoversinpi     │ hacoversin(𝜋x)            │     hacoversinpi(x) = (1 − sin(𝜋x))∕2
hacovercospi     │ hacovercos(𝜋x)            │     hacovercospi(x) = (1 + sin(𝜋x))∕2
exsecpi          │ exsec(𝜋x)                 │          exsecpi(x) = sec(𝜋x) − 1
excscpi          │ excsc(𝜋x)                 │          excscpi(x) = csc(𝜋x) − 1
chordpi          │ chord(𝜋x)                 │          chordpi(x) = 2 × sin(𝜋x∕2)
arcchordpi       │ arcchord(y)∕𝜋             │       arcchordpi(y) = 2 × arcsin(y∕2)∕𝜋
arcexsecpi       │ arcexsecpi(x)∕𝜋           │       arcexsecpi(y) = arcsec(y+1)∕𝜋
arcexcscpi       │ arcexcscpi(x)∕𝜋           │       arcexcscpi(y) = arccsc(y+1)∕𝜋
arcversinpi      │ arcversin(y)∕𝜋            │      arcversinpi(y) = arccos(1−y)∕𝜋
arcvercospi      │ arcvercos(y)∕𝜋            │      arcvercospi(y) = arccos(y−1)∕𝜋
arccoversinpi    │ arccoversin(y)∕𝜋          │    arccoversinpi(y) = arcsin(1−y)∕𝜋
arccovercospi    │ arccovercos(y)∕𝜋          │    arccovercospi(y) = arcsin(y−1)∕𝜋
archaversinpi    │ archaversin(y)∕𝜋          │    archaversinpi(y) = arccos(1−2y)∕𝜋
archavercospi    │ archavercos(y)∕𝜋          │    archavercospi(y) = arccos(2y−1)∕𝜋
archacoversinpi  │ archacoversin(y)∕𝜋        │  archacoversinpi(y) = arcsin(1−2y)∕𝜋
archacovercospi  │ archacovercos(y)∕𝜋        │  archacovercospi(y) = arcsin(2y−1)∕𝜋
versintau        │ versin(𝜏x)                │        versintau(x) = 1 − cos(𝜏x)
vercostau        │ vercos(𝜏x)                │        vercostau(x) = 1 + cos(𝜏x)
coversintau      │ coversin(𝜏x)              │      coversintau(x) = 1 − sin(𝜏x)
covercostau      │ covercos(𝜏x)              │      covercostau(x) = 1 + sin(𝜏x)
haversintau      │ haversin(𝜏x)              │      haversintau(x) = (1 − cos(𝜏x))∕2
havercostau      │ havercos(𝜏x)              │      havercostau(x) = (1 + cos(𝜏x))∕2
hacoversintau    │ hacoversin(𝜏x)            │    hacoversintau(x) = (1 − sin(𝜏x))∕2
hacovercostau    │ hacovercos(𝜏x)            │    hacovercostau(x) = (1 + sin(𝜏x))∕2
exsectau         │ exsec(𝜏x)                 │         exsectau(x) = sec(𝜏x) − 1
excsctau         │ excsc(𝜏x)                 │         excsctau(x) = csc(𝜏x) − 1
chordtau         │ chord(𝜏x)                 │         chordtau(x) = 2 × sin(𝜏x∕2)
arcchordtau      │ arcchord(y)∕𝜏             │      arcchordtau(y) = 2 × arcsin(y∕2)∕𝜏
arcexsectau      │ arcexsectau(x)∕𝜏          │      arcexsectau(y) = arcsec(y+1)∕𝜏
arcexcsctau      │ arcexcsctau(x)∕𝜏          │      arcexcsctau(y) = arccsc(y+1)∕𝜏
arcversintau     │ arcversin(y)∕𝜏            │     arcversintau(y) = arccos(1−y)∕𝜏
arcvercostau     │ arcvercos(y)∕𝜏            │     arcvercostau(y) = arccos(y−1)∕𝜏
arccoversintau   │ arccoversin(y)∕𝜏          │   arccoversintau(y) = arcsin(1−y)∕𝜏
arccovercostau   │ arccovercos(y)∕𝜏          │   arccovercostau(y) = arcsin(y−1)∕𝜏
archaversintau   │ archaversin(y)∕𝜏          │   archaversintau(y) = arccos(1−2y)∕𝜏
archavercostau   │ archavercos(y)∕𝜏          │   archavercostau(y) = arccos(2y−1)∕𝜏
archacoversintau │ archacoversin(y)∕𝜏        │ archacoversintau(y) = arcsin(1−2y)∕𝜏
archacovercostau │ archacovercos(y)∕𝜏        │ archacovercostau(y) = arcsin(2y−1)∕𝜏
versind          │ versin(𝜏x∕360)            │          versind(x) = 1 − cos(𝜏x∕360)
vercosd          │ vercos(𝜏x∕360)            │          vercosd(x) = 1 + cos(𝜏x∕360)
coversind        │ coversin(𝜏x∕360)          │        coversind(x) = 1 − sin(𝜏x∕360)
covercosd        │ covercos(𝜏x∕360)          │        covercosd(x) = 1 + sin(𝜏x∕360)
haversind        │ haversin(𝜏x∕360)          │        haversind(x) = (1 − cos(𝜏x∕360))∕2
havercosd        │ havercos(𝜏x∕360)          │        havercosd(x) = (1 + cos(𝜏x∕360))∕2
hacoversind      │ hacoversin(𝜏x∕360)        │      hacoversind(x) = (1 − sin(𝜏x∕360))∕2
hacovercosd      │ hacovercos(𝜏x∕360)        │      hacovercosd(x) = (1 + sin(𝜏x∕360))∕2
exsecd           │ exsec(𝜏x∕360)             │           exsecd(x) = sec(𝜏x∕360) − 1
excscd           │ excsc(𝜏x∕360)             │           excscd(x) = csc(𝜏x∕360) − 1
chordd           │ chord(𝜏x∕360)             │           chordd(x) = 2 × sin(𝜏x∕360∕2)
arcchordd        │ arcchord(y)×360∕𝜏         │        arcchordd(y) = 2 × arcsin(y∕2)×360∕𝜏
arcexsecd        │ arcexsec(x)×360∕𝜏         │        arcexsecd(y) = arcsec(y+1)×360∕𝜏
arcexcscd        │ arcexcsc(x)×360∕𝜏         │        arcexcscd(y) = arccsc(y+1)×360∕𝜏
arcversind       │ arcversin(y)×360∕𝜏        │       arcversind(y) = arccos(1−y)×360∕𝜏
arcvercosd       │ arcvercos(y)×360∕𝜏        │       arcvercosd(y) = arccos(y−1)×360∕𝜏
arccoversind     │ arccoversin(y)×360∕𝜏      │     arccoversind(y) = arcsin(1−y)×360∕𝜏
arccovercosd     │ arccovercos(y)×360∕𝜏      │     arccovercosd(y) = arcsin(y−1)×360∕𝜏
archaversind     │ archaversin(y)×360∕𝜏      │     archaversind(y) = arccos(1−2y)×360∕𝜏
archavercosd     │ archavercos(y)×360∕𝜏      │     archavercosd(y) = arccos(2y−1)×360∕𝜏
archacoversind   │ archacoversin(y)×360∕𝜏    │   archacoversind(y) = arcsin(1−2y)×360∕𝜏
archacovercosd   │ archacovercos(y)×360∕𝜏    │   archacovercosd(y) = arcsin(2y−1)×360∕𝜏
-->
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

these boolean functions are overloaded to perform bit-wise operations if int or float are given, and to perform set operations if set is given

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
fact     │ factorial                          │           5! = 120
sumt     │ sumtorial (sum of all ℤ⁺ up to n)  │      sumt(5) = 15
comb     │ combinations                       │    comb(6,5) = 6
perm     │ permutations                       │    perm(6,5) = 720
```

`fact(x)` is not intended to take fractional input. use `gamma(x+1)` for that.

</details><details open><summary>bitwise </summary>

```
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

the `in_*_interval` functions are simply for readability, for when sometimes, for example, `in_open_interval(x, a, b)` is easier to understand than `a < x < b`

```
name                   │ explanation              │ example
───────────────────────┼──────────────────────────┼──────────────────────────────────────
clamp                  │ restrict to [a,b]        │            clamp(1.2, 0, 0.8) = 0.8
in_open_interval       │ a < x < b                │       in_open_interval(3,1,3) = False
in_closed_interval     │ a ≤ x ≤ b                │     in_closed_interval(3,1,3) = True
in_left_open_interval  │ a < x ≤ b                │  in_left_open_interval(3,1,3) = True
in_right_open_interval │ a ≤ x < b                │ in_right_open_interval(3,1,3) = False
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

motivation: sometimes i need the quotient of a division, but programs only give me truediv or floordiv. sometimes i juse need a neg function to use in a higher-order function, without resorting to a nameless lambda >:( sometimes i need floor and ceil. sometimes i need the min of a dataset. sometimes i want the mean of a database instead of writing sum/len

this project will take inspiration from [glm](https://github.com/icaven/glm) soon
