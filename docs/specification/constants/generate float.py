from decimal import Decimal, getcontext
from fractions import Fraction
from numbers import Rational

# enough precision for binary128
getcontext().prec = 20000

# ai-generated most of this. it agreed with the values i sourced myself though

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

def rational_to_binary(x: Rational, precision: int) -> str:
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
    
def binary(name: str, bits: int, precision: int, emin: int, emax: int):
    """
    bits      total storage bits (16, 32, 64, 128, ...)
    precision significand bits including the hidden bit
    emin      minimum normal exponent
    emax      maximum normal exponent
    """

    two = Decimal(2)

    epsilon = two ** (-(precision - 1))
    normal_min = two ** emin
    subnormal_min = two ** (emin - (precision - 1))
    normal_max = (two - epsilon) * (two ** emax)
    subnormal_max = (Decimal(1) - epsilon) * normal_min
    
    epsilon = rational_to_binary(Fraction(epsilon), precision)
    normal_min = rational_to_binary(Fraction(normal_min), precision)
    subnormal_min = rational_to_binary(Fraction(subnormal_min), precision)
    normal_max = rational_to_binary(Fraction(normal_max), precision)
    subnormal_max = rational_to_binary(Fraction(subnormal_max), precision)
    
    print(f'\n{name}:')
    print(f'  epsilon: {epsilon} # 2 ^ -{precision - 1}')
    print( '  min:')
    print(f'    normal: {normal_min} # 2 ^ {emin}')
    print(f'    subnormal: {subnormal_min} # 2 ^ {emin - (precision - 1)}')
    print( '  max:')
    print(f'    normal: {normal_max} # (2 − 2 ^ -{precision - 1}) × 2 ^ {emax}')
    print(f'    subnormal: {subnormal_max} # (1 − 2 ^ -{precision - 1}) × 2 ^ {emin}')

def decimal(name: str, digits: int, emin: int, emax: int):
    """
    digits  significant decimal digits
    emin    minimum normal exponent
    emax    maximum normal exponent
    """

    ten = Decimal(10)

    epsilon = Decimal(5) * (ten ** (-digits))
    normal_min = ten ** emin
    subnormal_min = ten ** (emin - (digits - 1))
    normal_max = (ten - ten ** (1 - digits)) * (ten ** emax)
    subnormal_max = (Decimal(1) - ten ** (1 - digits)) * normal_min

    print(f"{name}:")
    print(f"  epsilon: '{epsilon:.{digits - 1}e}' # 5 × 10 ^ -{digits}")
    print( "  min:")
    print(f"    normal: '{normal_min:.{digits - 1}e}' # 10 ^ {emin}")
    print(f"    subnormal: '{subnormal_min:.{digits - 1}e}' # 10 ^ {emin - (digits - 1)}")
    print( "  max:")
    print(f"    normal: '{normal_max:.{digits - 1}e}' # (10 − 10 ^ -{digits - 1}) × 10 ^ {emax}")
    print(f"    subnormal: '{subnormal_max:.{digits - 1}e}' # (1 − 10 ^ -{digits - 1}) × 10 ^ {emin}")

# these values are IEEE 754 spec. i also verified them with my daatypes project

binary('f16', 16, 11, -14, 15)
binary('f32', 32, 24, -126, 127)
binary('f64', 64, 53, -1022, 1023)
binary('f128', 128, 113, -16382, 16383)
binary('f256', 256, 237, -262142, 262143)

decimal('d32', 7, -95, 96)
decimal('d64', 16, -383, 384)
decimal('d128', 34, -6143, 6144)
