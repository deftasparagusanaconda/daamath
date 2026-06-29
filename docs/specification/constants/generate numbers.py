# TODO: add some functionality so that you can generate the absolute error of the nearest from the actual. thus you could support midpoint-ball intervals
#
# NOTE: we could have an algorithm store all the residuals down to the format's emin but for f256, that would mean storing roughly 1000 f256 constants just to exhaust down to emin. for 30 constants that takes up about 1MiB. just for residuals no one will use. thats why daamath only stores constants up to 1 level of residue. its enough to make a bound interval and a ball interval anyway.

import mpmath, decimal
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

constants = dict(
        archimedes = mpmath.pi,
        euler = mpmath.e,
        golden = mpmath.phi,
        silver = 1 + mpmath.sqrt(2),
        euler_mascheroni = mpmath.euler,
        catalan = mpmath.catalan,
        apery = mpmath.apery,
        khinchin = mpmath.khinchin,
        glaisher = mpmath.glaisher,
        mertens = mpmath.mertens ,
        twinprime = mpmath.twinprime,
        turn    = mpmath.pi * 2,   # instead of tau, which is just a greek letter
        degree = mpmath.degree,
        gradian = mpmath.pi * 2 / 400,
        minute  = mpmath.pi * 2 / 21600,
        second  = mpmath.pi * 2 / 129600)

for k, v in constants.items():
    constants[k] = str(v)

# precisions of the ieee formats that i want to store
binary_formats = {'f16': 11, 'f32': 24, 'f64': 53, 'f128': 113, 'f256': 237}
decimal_formats = {'d32': 7, 'd64': 16, 'd128': 34}

decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
for constant_name, constant in constants.items():
    print(f'\n{constant_name.upper()}:')

    constant_fraction = Fraction(constant)
    constant_decimal = Decimal(constant)

    for format_name, precision in binary_formats.items():
        print(f'  {format_name}:')

        # nearest
        nearest: str = rational_to_bin(constant_fraction, precision)
        print(f'    nearest: "{nearest}"')

        # error
        nearest: Rational = bin_to_rational(nearest)
        error: Rational = constant_fraction - nearest
        error: str = rational_to_bin(error, precision)
        print(f'    error: "{error}"')

    for format_name, precision in decimal_formats.items():
        print(f'  {format_name}:')
        decimal.getcontext().prec = precision

        # nearest
        nearest = f'{constant_decimal * 1:e}'
        print(f'    nearest: "{nearest}"')

        # error
        nearest: Decimal = Decimal(nearest) 
        error: Rational = constant_decimal - nearest
        error: str = f'{Decimal(error) * 1:e}'
        print(f'    error: "{error}"')
