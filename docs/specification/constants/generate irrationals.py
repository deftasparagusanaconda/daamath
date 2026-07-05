# NOTE: we could have an algorithm store all the residuals down to the format's emin but for f256, that would mean storing roughly 1000 f256 constants just to exhaust down to emin. for 30 constants that takes up about 1MiB. just for residuals no one will use. thats why daamath only stores constants up to 1 level of residue. its enough to make a bound interval and a ball interval anyway.

import math, mpmath, decimal
from fractions import Fraction
from numbers import Rational
from decimal import Decimal

# past this point most of it is ai generated (not all)
# i dont know how it works, but i checked the results and they were correct. so it freakin works. somehow. so yeah. 
#
# "nice code senator. why dont you back it up with an explanation?"
# "my explanation is that i ai generated it the fuck up"

xor = lambda a, b: (a and not b) or (not a and b)

def to_nearest(n: int, d: int) -> int:
    q, r = divmod(n, d)
    twice = 2 * r

    if twice < d:
        return q
    elif twice > d:
        return q + 1
    else:
        raise Exception(f'a... a tie?? i didnt expect this. what did you do??? something anomalous... does your constant terminate?!? check this: {n=}, {d=}')
        #return q if q % 2 == 0 else q + 1

# cause rational_to_bin needed it
def pow2(e: int) -> Fraction:
    return Fraction(1 << e, 1) if e >= 0 else Fraction(1, 1 << -e)

def rational_to_bin(x: Rational, precision: int) -> str:
    if x == 0:
        return '+0p+0'
    elif x < 0:
        negative = True
        x *= -1
    else:
        negative = False
    
    # find exponent e such that 2^e <= x < 2^(e+1)
    e = x.numerator.bit_length() - x.denominator.bit_length()
    
    if x < pow2(e):
        e -= 1
    
    # scale x so that the rounded integer has `precision` bits
    # significand ≈ x / 2^(e - precision + 1)
    shift = precision - 1 - e
    
    if shift >= 0:
        n = x.numerator << shift
        d = x.denominator
    else:
        n = x.numerator
        d = x.denominator << (-shift)

    significand = to_nearest(n, d)

    # rounding can overflow: 1.111... -> 10.000...
    if significand == (1 << precision):
        significand >>= 1
        e += 1

    significand = ('-' if xor(significand < 0, negative) else '+') + bin(abs(significand))[2:]
    e = ('-' if e < 0 else '+') + bin(abs(e))[2:]
    
    return f'{significand[:2]}.{significand[2:]}p{e}'

# okay past THIS point i hand-made everything okay? not ai generated anymore

def bin_to_rational(string: str) -> Rational:
    if 'p' in string:
        sig, exp = string.split('p', maxsplit=1)
    elif 'e' in string:
        sig, exp = string.split('e', maxsplit=1)
    else:
        raise ValueError('e or p not found in string. i dont know where your exponent starts')

    sig = sig.replace('.', '')
    
    precision = len(sig.lstrip('+-'))
    sig, exp = int(sig, base=2), int(exp, base=2)
    
    exp -= precision - 1

    if exp < 0:
        return Fraction(sig, 2 ** -exp)
    else:
        return Fraction(sig * 2 ** exp)
    
# https://mpmath.org/doc/current/functions/constants.html
mpmath.mp.dps = 300
# NOTE: "why do we need 300, your grace?"
# ...
# "this is madness!"
# madness? THIS    IS    SPARTAAAA!!!
# yes we genuinely need 300 because, assuming our constants have an exponent close to 0, f256 has 237 binary precision, which is roughly 237 * log10(2) ≈ 71.34 decimal digits. we will also want to store the residual. that means we need 71.34*2=142 or so. and remember that this is assuming our constants are close to 0 exponent. so yes, 300 is needed.

def metallic(n):
    'metallic means'
    return (n + mpmath.sqrt(n * n + 4)) / 2

def liouville_10(n):
    factorials = {math.factorial(i) for i in range(n)}
    return '0.' + ''.join(str(int(i in factorials)) for i in range(1, math.factorial(n - 1) + 1))

constants: dict[str, str | Any] = dict(
        metallic_1 = metallic(1), # golden ratio
        metallic_2 = metallic(2), # silver ratio
        metallic_3 = metallic(3), # bronze ratio
        zeta_3 = mpmath.zeta(3), # apery's constant
        zeta_5 = mpmath.zeta(5),
        champernowne_10 = ''.join(str(i) for i in range(1, 200)),
        liouville_10 = liouville_10(7),
        
        archimedes = mpmath.pi,
        eulers_number = mpmath.e,
        euler_mascheroni = mpmath.euler,
        catalan    = mpmath.catalan,
        khinchin   = mpmath.khinchin,
        glaisher   = mpmath.glaisher,
        mertens    = mpmath.mertens ,
        twin_prime = mpmath.twinprime,
        plastic    = mpmath.findroot(lambda x: x**3 - x - 1, 1.3),
        gompertz = mpmath.e * mpmath.e1(1),
        
        #https://sprott.physics.wisc.edu/phys505/feigen.htm
        feigenbaum_alpha = '-2.5029078750958928222839028732182157863812713767271499773361920567792354631795902067032996497464338341295952318699958547239421823777854451792728633149933725781121635948795037447812609973805986712397117373289276654044010306698313834600094139322364490657889951220584317250787337746308785342428535198858750004235824691874082042817009017148230518216216194131998560661293827426497098440844701008054549677936760888126446406885181552709324007542506497157047047541993283178364533256241537869395712509706638797949265462313767459189098131167524342211101309131278371609511583412308415037164997020224681219644081216686527458043026245782561067150138521821644953254334987348741335279581535101658360545576351327650181078119483694595748502373982354526256327794753972699020128915166457939420198920248803394051699686551494477396533876979741232354061781989611249409599035312899773361184984737794610842883329383390395090089140863515256268033814146692799133107433497051435452013446434264752001621384610729922641994332772918977769053802596851',
        feigenbaum_delta = '4.6692016091029906718532038204662016172581855774757686327456513430041343302113147371386897440239480138171659848551898151344086271420279325223124429888908908599449354632367134115324817142199474556443658237932020095610583305754586176522220703854106467494942849814533917262005687556659523398756038256372256480040951071283890611844702775854285419801113440175002428585382498335715522052236087250291678860362674527213399057131606875345083433934446103706309452019115876972432273589838903794946257251289097948986768334611626889116563123474460575179539122045562472807095202198199094558581946136877445617396074115614074243754435499204869180982648652368438702799649017397793425134723808737136211601860128186102056381818354097598477964173900328936171432159878240789776614391395764037760537119096932066998361984288981837003229412030210655743295550388845849737034727532121925706958414074661841981961006129640161487712944415901405467941800198133253378592493365883070459999938375411726563553016862529032210862320550634510679399023341675',
        
        # angles w.r.t. radians — the most natural unit of angle ever :)
        turn       = mpmath.pi * 2,   # instead of tau, which is just a greek letter
        degree     = mpmath.pi * 2 / 360,
        gradian    = mpmath.pi * 2 / 400,
        minute     = mpmath.pi * 2 / 21600,
        second     = mpmath.pi * 2 / 129600)

constants: dict[str, str] = {k: str(v) for k, v in constants.items()}

for k, v in constants.items():
    print(f'| {k} | {v[:100]} |')

# precisions of the ieee formats that i want to store
binary_formats = {'f16': 11, 'f32': 24, 'f64': 53, 'f128': 113, 'f256': 237}
decimal_formats = {'d32': 7, 'd64': 16, 'd128': 34}

decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
for constant_name, constant in constants.items():
    print(f'\n{constant_name}:')

    constant_fraction = Fraction(constant)
    constant_decimal = Decimal(constant)

    for format_name, precision in binary_formats.items():
        print(f'  {format_name}:')

        # nearest
        nearest: str = rational_to_bin(constant_fraction, precision)
        print(f'    nearest: "{nearest}"')

        # residual
        nearest: Rational = bin_to_rational(nearest)
        residual: Rational = constant_fraction - nearest
        residual: str = rational_to_bin(residual, precision)
        print(f'    residual: "{residual}"')

    for format_name, precision in decimal_formats.items():
        print(f'  {format_name}:')
        decimal.getcontext().prec = precision

        # nearest
        nearest = f'{constant_decimal * 1:e}'
        print(f'    nearest: "{nearest}"')

        # residual
        nearest: Decimal = Decimal(nearest) 
        residual: Rational = constant_decimal - nearest
        residual: str = f'{Decimal(residual) * 1:e}'
        print(f'    residual: "{residual}"')
