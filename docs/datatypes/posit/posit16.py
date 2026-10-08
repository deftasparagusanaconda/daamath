from softposit import posit16
from itertools import islice
from fractions import Fraction

es = 1

print('# posit16')
print()
print('<pre>')
for bits in [
        '0111111111111111', # +maxPos
        '0111111111111110', 
        '0111111111111101',
        
        '0100000000000010', 
        '0100000000000001',
        '0100000000000000', # +1.0
        '0011111111111111', 
        '0011111111111110', 
        '0011111111111101', 

        '0000000000000010', 
        '0000000000000001', 
        '0000000000000000', #  0.0
        '1111111111111111', 
        '1111111111111110', 
        '1111111111111101', 

        '1100000000000010', 
        '1100000000000001', 
        '1100000000000000', # -1.0
        '1011111111111111', 
        '1011111111111110', 
        '1011111111111101', 

        '1000000000000010', 
        '1000000000000001', # -maxPos
        '1000000000000000']:#  NaR
    
    # -------------------------------------------
    # split into sign, regime, exponent, fraction
    # -------------------------------------------
    
    it = iter(bits)
    
    sign_bits = next(it)
    
    regime_bits = next(it)
    for bit in it:
        regime_bits += bit
        if bit != regime_bits[0]:
            break
    
    exponent_bits = ''.join(islice(it, es))
    fraction_bits = ''.join(it)
    
    # ----------------
    # decode the value
    # ----------------
    
    sign = {'0': +1, '1': -1}[sign_bits]
    regime = len(regime_bits) - 2
    exponent = int(exponent_bits or '0', base=2)
    fraction = Fraction(int(fraction_bits or '0', base=2), 2 ** len(fraction_bits))

    value = sign * (1 + fraction) * (2 ** (1 + exponent)) ** regime

    # -----
    # print
    # -----
    
    fancy_bits = (
        f'<span style="color: var(--dm-red)">{sign_bits.replace('0', '□').replace('1', '■')}</span>'
        f'<span style="color: var(--dm-yellow)">{regime_bits.replace('0', '□').replace('1', '■')}</span>'
        f'<span style="color: var(--dm-green)">{exponent_bits.replace('0', '□').replace('1', '■')}</span>'
        f'<span style="color: var(--dm-blue)">{fraction_bits.replace('0', '□').replace('1', '■')}</span>')
    
    from decimal import Decimal, getcontext
    getcontext().prec = 99
    print(fancy_bits, '=', posit16(bits=int(bits, base=2)), '=', Decimal(value.numerator) / Decimal(value.denominator))
print('</pre>')
