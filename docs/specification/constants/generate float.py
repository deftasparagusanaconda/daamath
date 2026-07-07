# from decimal import Decimal, getcontext
# from fractions import Fraction
# from numbers import Rational
# from daatypes import Float
'''
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
''' 
for name, radix, prec, emin, emax in [
        # IEEE 754 basic formats only. no interchange formats.
        #('f16', 2, 11, -14, 15),
        ('f32', 2, 24, -126, 127),
        ('f64', 2, 53, -1022, 1023),
        ('f128', 2, 113, -16382, 16383),
        #('f256', 2, 237, -262142, 262143),
        #('d32', 10, 7, -95, 96),
        ('d64', 10, 16, -383, 384),
        ('d128', 10, 34, -6143, 6144)]:
    print(f'\n{name}:')
    print('  pos:')
    print('    zero:')
    print('    inf:')
    print('    qnan:')
    print('    snan:')
    print('  neg:')
    print('    zero:')
    print('    inf:')
    print('    qnan:')
    print('    snan:')
    print('  epsilon:')
    print('    significand:', 1)
    print('    radix:', radix)
    print('    exponent:', 1 - prec)
    print('  min:')
    print('    normal:')
    print('      significand:', 1)
    print('      radix:', radix)
    print('      exponent:', emin)
    print('    subnormal:')
    print('      significand:', 1)
    print('      radix:', radix)
    print('      exponent:', emin - prec + 1)
    print('  max:')
    print('    normal:')
    print('      significand:', radix ** prec - 1)
    print('      radix:', radix)
    print('      exponent:', emax - prec + 1)
    print('    subnormal:')
    print('      significand:', radix ** (prec - 1) - 1)
    print('      radix:', radix)
    print('      exponent:', emin - prec + 1)
