#from daatypes import Float
import sys

sys.set_int_max_str_digits(10000)

fact_table = [[]]
derived_table = [[]]

for format_name, radix, prec, emin, emax in [
        # IEEE 754 basic formats only. no interchange formats.
        #('binary16', 2, 11, -14, 15),
        ('binary32', 2, 24, -126, 127),
        ('binary64', 2, 53, -1022, 1023),
        ('binary128', 2, 113, -16382, 16383),
        #('binary256', 2, 237, -262142, 262143),
        #('decimal32', 10, 7, -95, 96),
        ('decimal64', 10, 16, -383, 384),
        ('decimal128', 10, 34, -6143, 6144)]:
    print(f'\n{format_name}:')
    print(f'  nan: .nan')
    print(f'  pos_inf: +.inf')
    print(f'  neg_inf: -.inf')
    print(f'  pos_zero: +0.0')
    print(f'  neg_zero: -0.0')
    print(f'  radix:', radix)
    print(f'  precision:', prec)
    print(f'  emin:', emin)
    print(f'  emax:', emax)

    fact_table.append([format_name, radix, prec, emin, emax])

    derived_row = [format_name]
    
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
        
        derived_row.append(f'{significand} * {radix} ^ {exponent}')

    derived_table.append(derived_row)

print('| format | radix | precision | emin   | emax   |')
print('| ------ | ----- | --------- | ------ | ------ |')
for row in fact_table:
    print('| ' + ' | '.join(map(str, row)) + ' |')

print('| format | epsilon      | normal_min     | normal_max                                      | subnormal_min  | subnormal_max                                   |')
print('| ------ | ------------ | -------------- | ----------------------------------------------- | -------------- | ----------------------------------------------- |')
for row in derived_table:
    print('| ' + ' | '.join(map(str, row)) + ' |')
