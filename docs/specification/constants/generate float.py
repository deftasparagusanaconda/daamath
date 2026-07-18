#from daatypes import Float
import sys

sys.set_int_max_str_digits(10000)

for format_name, radix, prec, emin, emax in [
        # IEEE 754 basic formats only. no interchange formats.
        #('f16', 2, 11, -14, 15),
        ('f32', 2, 24, -126, 127),
        ('f64', 2, 53, -1022, 1023),
        ('f128', 2, 113, -16382, 16383),
        #('f256', 2, 237, -262142, 262143),
        #('d32', 10, 7, -95, 96),
        ('d64', 10, 16, -383, 384),
        ('d128', 10, 34, -6143, 6144)]:
    print(f'\n{format_name}:')
    print(f'  radix:', radix)
    print(f'  precision:', prec)
    print(f'  emin:', emin)
    print(f'  emax:', emax)
    
    for constant_name, constant in {
        'epsilon': (1, radix, 1 - prec),
        'normal_min': (1, radix, emin), 
        'normal_max': (radix ** prec - 1, radix, emax - prec + 1), 
        'subnormal_min': (1, radix, emin - prec + 1), 
        'subnormal_max': (radix ** (prec - 1) - 1, radix, emin - prec + 1), 
    }.items():
        significand, radix, exponent = constant
        print(f'  {constant_name}:')
        print(f'    significand: {significand}')
        print(f'    radix: {radix}')
        print(f'    exponent: {exponent}')
    
