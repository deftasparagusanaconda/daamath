from itertools import islice
from math import nan
from fractions import Fraction

print('# posit32')
print()
print('<pre>')

for bitstring in [
        '01111111111111111111111111111111', # +maxPos
        '01111111111111111111111111111110', 
        '01111111111111111111111111111101',
        
        '01000000000000000000000000000010', 
        '01000000000000000000000000000001',
        '01000000000000000000000000000000', # +1.0
        '00111111111111111111111111111111', 
        '00111111111111111111111111111110', 
        '00111111111111111111111111111101', 
        
        '00000000000000000000000000000010', 
        '00000000000000000000000000000001', 
        '00000000000000000000000000000000', #  0.0
        '11111111111111111111111111111111', 
        '11111111111111111111111111111110', 
        '11111111111111111111111111111101', 
        
        '11000000000000000000000000000010', 
        '11000000000000000000000000000001', 
        '11000000000000000000000000000000', # -1.0
        '10111111111111111111111111111111', 
        '10111111111111111111111111111110', 
        '10111111111111111111111111111101', 
        
        '10000000000000000000000000000010', 
        '10000000000000000000000000000001', # -maxPos
        '10000000000000000000000000000000']:#  NaR

    # -----------
    # get S R E F
    # -----------
    
    it = iter(bitstring)
    
    S: str = next(it)
    
    R: str = next(it)
    for bit in it:
        if bit != R[-1]:
            break
        R += bit
    R0: str = R[-1]
    
    E: str = ''.join(islice(it, 2))
    F: str = ''.join(it)
    
    # -------------
    # get s r e f p
    # -------------
    
    s: int = int(S)
    r: int = len(R) - 1 if int(R0) else -len(R)
    e: int = int(E.ljust(2, '0'), base=2)
    f: Fraction = Fraction(int(F or '0', base=2), 2 ** len(F))
    
    p = ((nan if s else Fraction(0))
        if all(bit == '0' for bit in bitstring[1:])
        else ((1 - 3 * s) + f) * Fraction(2) ** ((1 - 2 * s) * (4 * r + e + s)))
    
    # -----
    # print
    # -----
    
    fancy_bits = (
        f'<span style="color: var(--dm-red)">{S.replace('0', '□').replace('1', '■')}</span>'
        f'<span style="color: var(--dm-yellow)">{R.replace('0', '□').replace('1', '■')}</span>'
        f'<span style="color: var(--dm-gray)">{(R[0]*(len(R)<31)).replace('0', '■').replace('1', '□')}</span>'
        f'<span style="color: var(--dm-green)">{E.replace('0', '□').replace('1', '■')}</span>'
        f'<span style="color: var(--dm-blue)">{F.replace('0', '□').replace('1', '■')}</span>')
    
    print(fancy_bits, '=', float(p))

print('</pre>')
