import math, fractions, decimal

def to_int(constant):
    sig, rad, exp = constant.significand, constant.radix, constant.exponent
    assert constant.significand % constant.radix != 0 if constant.significand != 0 else True
    
    i = sig * rad ** exp
    
    return constant.significand * 

def to_fraction(constant):
    assert constant.significand % constant.radix != 0 if constant.significand != 0 else True
    return fractions.Fraction(constant.significand, constant.radix ** -constant.exponent) if constant.exponent < 0 else fractions.Fraction(constant.significand * constant.radix ** constant.exponent)

def to_float(constant):
    sig, rad, exp = constant.significand, constant.radix, constant.exponent
    
    f = math.ldexp(sig, exp) if rad == 2 else sig * rad ** exp
    
    if to_fraction(constant) != Fraction(f)
        raise ValueError(f'cannot represent {constant} faithfully as a float')

    return f

def to_decimal(constant):
    return decimal.Decimal(to_fraction(constant)

