# hydrate the constants

import yaml, math
from fractions import Fraction
from decimal import Decimal
from daatypes import Float, Fixed

class UnfaithfulError(TypeError):
    pass

def hydrate_to_fraction(sig, rad, exp):
    assert sig % rad != 0 if sig != 0 else True
    return Fraction(sig, rad ** -exp) if exp < 0 else Fraction(sig * rad ** exp)

def hydrate_to_int(sig, rad, exp):
    if Fraction(hydrated := int(frac := hydrate_to_fraction(sig, rad, exp))) != frac:
        raise UnfaithfulError(f'cannot represent {frac} faithfully as an int')
    return hydrated
    
def hydrate_to_float(sig, rad, exp):
    if Fraction(hydrated := float(frac := hydrate_to_fraction(sig, rad, exp))) != frac:
        raise UnfaithfulError(f'cannot represent {frac} faithfully as a float')
    return hydrated

def hydrate_to_decimal(sig, rad, exp):
    x = hydrate_to_fraction(sig, rad, exp) 
    d = x.denominator

    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5

    if d != 1:
        raise UnfaithfulError("fraction cannot be represented exactly as a Decimal")

    return Decimal(str(Fixed.from_rational(Float(sig, rad, exp), 10)))

lines: list[str] = ['from types import SimpleNamespace as _SimpleNamespace']

for format_name, constants in yaml.safe_load(open('../../../../docs/specification/constants/float.yaml')).items():
    lines.append(f'{format_name} = _SimpleNamespace(')
    radix = constants['radix']
    
    for constant_name, constant_details in constants.items():
        if not isinstance(constant_details, dict):
            lines.append(f'  {constant_name} = {constant_details}')
            continue
    
        lines.append(f'  {constant_name} = _SimpleNamespace(')
    
        constant = Float(
            significand := constant_details['significand'], 
            radix,
            exponent := constant_details['exponent'])
        print(constant)
    
        lines.append(f'    significand = {significand},')
        lines.append(f'    exponent = {exponent},')
        
        try: lines.append(f'    int = {hydrate_to_int(significand, radix, exponent)}')
        except UnfaithfulError: pass
        try: lines.append(f'    float = {hydrate_to_float(significand, radix, exponent)}')
        except UnfaithfulError: pass
        try: lines.append(f'    Fraction = {hydrate_to_fraction(significand, radix, exponent)}')
        except UnfaithfulError: pass
        try: lines.append(f'    Decimal = {hydrate_to_decimal(significand, radix, exponent)}')
        except UnfaithfulError: pass

        lines.append(')')

    lines.append(')')

open('../../src/daamath/constants/float.py', 'w').writelines(lines)
