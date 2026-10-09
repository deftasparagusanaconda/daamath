from itertools import islice, chain
from fractions import Fraction

print('# posit8')
print()
print('<pre>')

for i in chain(range(2**7-1,-1,-1), range(2**8-1,2 ** 7-1, -1)):
    bits = bin(i)[2:].zfill(8)
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
    
    exponent_bits = ''.join(islice(it, 2))
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
    print(fancy_bits, '=', value)

print('</pre>')
