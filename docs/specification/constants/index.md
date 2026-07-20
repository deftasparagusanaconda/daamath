# constants

a constant is something whose value doesnt depend on anything and doesnt change unless the universe changes. under this definition, daamath has a few kinds of constants:

# rational approximations

an irrational constant may be stored as a rational approximation:

- each constant has 5 [IEEE 754] basic formats: [f32], [f64], [f128], [d64], [d128]
- each format has 2 residuals: the [nearest_even]-rounded value and the error of that rounded value
- each residual has 3 integers: significand, radix, exponent

the advantages of this are:

- the approximation is explicit, and not implicit in machine/language datatype
- a box (lower, upper) or a ball (centre, radius) interval can be constructed
- the constant can be easily hydrated into a float/fraction/string/int/interval/…

for convenience, an implementation may also store hydrated versions of the integer triple

the following irrational constants are approximated:

# examples

```
# get τ as an f16 approximation

TAU = dm.TAU.f16.nearest
```

```
# create e as a box interval of f64

E = dm.E.f32.nearest          
E = (dm.pred(E), E) if dm.E.f32.error < 0 else (E, dm.succ(E))           
```

```
# create e as a ball interval of f32

E = dm.ball(centre=dm.E.f32.nearest, radius=abs(dm.E.f32.error))
```


# notes

the rational approximations are stored as three integers. this is actually slightly redundant because rationals only need two integers (or three natural numbers!). but storing two ginormous integers is less efficient than the three handle-able integers because they match the structure of the float datatypes better.

# rant

`DIV_X_Y` seemed like a good idea until i realized the space blows up and i have to start making arbitrary decisions on where to stop. this is bad. daamath shouldnt make assumptions unless they are mathematically sound and clear. if you want `DIV_1_PI`, make it yourself: `div(1, pi)` or `minv(pi)`

# sources

the approximations are generated from:

```python
# NOTE: we could have an algorithm store all the residuals down to the format's emin but for f256, that would mean storing roughly 1000 f256 constants just to exhaust down to emin. for 30 constants that takes up about 1MiB. just for residuals no one will use. thats why daamath only stores constants up to 1 level of residue. its enough to make a bound interval and a ball interval anyway.

import math, mpmath
from daatypes import Float, Fixed
from typing import Any

def metallic(n, plus_else_minus_root: bool):
    return (n + mpmath.sqrt(n * n + 4)) / 2 if plus_else_minus_root else (n - mpmath.sqrt(n * n + 4)) / 2 

def liouville_10(n):
    factorials = {math.factorial(i) for i in range(n)}
    return '0.' + ''.join(str(int(i in factorials)) for i in range(1, math.factorial(n - 1) + 1))

def feigenbaum_alpha(digits: int):
    'https://sprott.physics.wisc.edu/phys505/feigen.htm'
    return '-2.5029078750958928222839028732182157863812713767271499773361920567792354631795902067032996497464338341295952318699958547239421823777854451792728633149933725781121635948795037447812609973805986712397117373289276654044010306698313834600094139322364490657889951220584317250787337746308785342428535198858750004235824691874082042817009017148230518216216194131998560661293827426497098440844701008054549677936760888126446406885181552709324007542506497157047047541993283178364533256241537869395712509706638797949265462313767459189098131167524342211101309131278371609511583412308415037164997020224681219644081216686527458043026245782561067150138521821644953254334987348741335279581535101658360545576351327650181078119483694595748502373982354526256327794753972699020128915166457939420198920248803394051699686551494477396533876979741232354061781989611249409599035312899773361184984737794610842883329383390395090089140863515256268033814146692799133107433497051435452013446434264752001621384610729922641994332772918977769053802596851'[:digits]

def feigenbaum_delta(digits: int):
    'https://sprott.physics.wisc.edu/phys505/feigen.htm'
    return '4.6692016091029906718532038204662016172581855774757686327456513430041343302113147371386897440239480138171659848551898151344086271420279325223124429888908908599449354632367134115324817142199474556443658237932020095610583305754586176522220703854106467494942849814533917262005687556659523398756038256372256480040951071283890611844702775854285419801113440175002428585382498335715522052236087250291678860362674527213399057131606875345083433934446103706309452019115876972432273589838903794946257251289097948986768334611626889116563123474460575179539122045562472807095202198199094558581946136877445617396074115614074243754435499204869180982648652368438702799649017397793425134723808737136211601860128186102056381818354097598477964173900328936171432159878240789776614391395764037760537119096932066998361984288981837003229412030210655743295550388845849737034727532121925706958414074661841981961006129640161487712944415901405467941800198133253378592493365883070459999938375411726563553016862529032210862320550634510679399023341675'[:digits]

mpmath.mp.dps = 300
# NOTE: "why do we need 300? this is madness!"
# madness? THIS    IS    SPARTAAAA!!!
# yes we genuinely need 300 because, assuming our constants have an exponent close to 0, f256 has 237 binary precision, which is roughly 237 * log10(2) ≈ 71.34 decimal digits. we will also want to store the residual. that means we need 71.34*2=142 or so. and remember that this is assuming our constants are close to 0 exponent. so yes, 300 is needed.

constants: dict[str, Any] = {
    'metallic_1_plus_root' : metallic(1, True), # golden ratio
    'metallic_2_plus_root' : metallic(2, True), # silver ratio
    'metallic_3_plus_root' : metallic(3, True), # bronze ratio
    'metallic_1_minus_root': metallic(1, False), 
    'metallic_2_minus_root': metallic(2, False), 
    'metallic_3_minus_root': metallic(3, False), 
    'apery'                : mpmath.zeta(3),
    'champernowne_10'      : '0.' + ''.join(str(i) for i in range(1, 200)),
    'liouville_10'         : liouville_10(7),
    
    # https://mpmath.org/doc/current/functions/constants.html
    'archimedes'       : mpmath.pi,
    'euler'            : mpmath.e,
    'euler_mascheroni' : mpmath.euler,
    'catalan'          : mpmath.catalan,
    'khinchin'         : mpmath.khinchin,
    'glaisher_kinkelin': mpmath.glaisher,
    'mertens'          : mpmath.mertens ,
    'twin_prime'       : mpmath.twinprime,
    'plastic'          : mpmath.findroot(lambda x: x**3 - x - 1, 1.3),
    'gompertz'         : mpmath.e * mpmath.e1(1),
    
    'feigenbaum_alpha': feigenbaum_alpha(mpmath.mp.dps),
    'feigenbaum_delta': feigenbaum_delta(mpmath.mp.dps),
    
    # angles w.r.t. radians — the most natural unit of angle ever :)
    'turn'   : mpmath.pi * 2,   # instead of tau, which is just a greek letter
    'degree' : mpmath.pi * 2 / 360,
    'gradian': mpmath.pi * 2 / 400,
    'minute' : mpmath.pi * 2 / 21600,
    'second' : mpmath.pi * 2 / 129600}

# sort alphabetically
constants: dict[str, Any] = dict(sorted(constants.items()))

# convert to Float
for constant_name, v in constants.items():
    constants[constant_name] = Float.from_str(str(v), radix = 10)

# (radix, precision) of the five basic IEEE 754 formats
formats = {'f32' : ( 2,  24),
           'f64' : ( 2,  53),
           'f128': ( 2, 113),
           'd64' : (10,  16),
           'd128': (10,  34)}

# stored as lines
markdown_table: list[str] = []

for constant_name, constant in constants.items():
    print(f'\n{constant_name}:')

    for format_name, format_details in formats.items():
        radix, precision = format_details
        nearest = Float.from_rational(constant, radix, precision)
        residual = Float.from_rational(constant - nearest, radix, precision)
        
        print(f'  {format_name}:')
        print(f'    nearest:')
        print(f'      significand: {nearest.significand}')
        print(f'      radix: {nearest.radix}')
        print(f'      exponent: {nearest.exponent}')
        print(f'    residual:')
        print(f'      significand: {residual.significand}')
        print(f'      radix: {residual.radix}')
        print(f'      exponent: {residual.exponent}')

        markdown_table.append(str(Fixed.from_rational(nearest, nearest.radix)))

for line in markdown_table:
    print(line)
```

[f16]: https://en.wikipedia.org/wiki/Half-precision_floating-point_format
[f32]: https://en.wikipedia.org/wiki/Single-precision_floating-point_format
[f64]: https://en.wikipedia.org/wiki/Double-precision_floating-point_format
[f128]: https://en.wikipedia.org/wiki/Quadruple-precision_floating-point_format
[f256]: https://en.wikipedia.org/wiki/Octuple-precision_floating-point_format
[d32]: https://en.wikipedia.org/wiki/Decimal32_floating-point_format
[d64]: https://en.wikipedia.org/wiki/Decimal64_floating-point_format
[d128]: https://en.wikipedia.org/wiki/Decimal128_floating-point_format
[IEEE 754]: https://en.wikipedia.org/wiki/IEEE_754
[τ]: https://en.wikipedia.org/wiki/Tau
