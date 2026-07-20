---
hide:
  - toc
---

# ieee754

daamath maintains [approximations] in the 5 basic [IEEE 754] formats. those 5 formats are described here:

| format | radix | precision | emin   | emax   |
| ------ | ----- | --------- | ------ | ------ |
| [binary32] | 2 | 24 | -126 | 127 |
| [binary64] | 2 | 53 | -1022 | 1023 |
| [binary128] | 2 | 113 | -16382 | 16383 |
| [decimal64] | 10 | 16 | -383 | 384 |
| [decimal128] | 10 | 34 | -6143 | 6144 |

the significand always has a non-zero leading digit. but in formats with radix == 2, the leading digit of the significand is always 1, since that is the only non-zero leading digit possible. so they can afford one extra digit of precision by assuming an implicit leading bit.

| format | epsilon      | normal_min     | normal_max                                      | subnormal_min  | subnormal_max                                   |
| ------ | ------------ | -------------- | ----------------------------------------------- | -------------- | ----------------------------------------------- |
| [binary32] | 1 * 2 ^ -23 | 1 * 2 ^ -126 | 16777215 * 2 ^ 104 | 1 * 2 ^ -149 | 8388607 * 2 ^ -149 |
| [binary64] | 1 * 2 ^ -52 | 1 * 2 ^ -1022 | 9007199254740991 * 2 ^ 971 | 1 * 2 ^ -1074 | 4503599627370495 * 2 ^ -1074 |
| [binary128] | 1 * 2 ^ -112 | 1 * 2 ^ -16382 | 10384593717069655257060992658440191 * 2 ^ 16271 | 1 * 2 ^ -16494 | 5192296858534827628530496329220095 * 2 ^ -16494 |
| [decimal64] | 1 * 10 ^ -15 | 1 * 10 ^ -383 | 9999999999999999 * 10 ^ 369 | 1 * 10 ^ -398 | 999999999999999 * 10 ^ -398 |
| [decimal128] | 1 * 10 ^ -33 | 1 * 10 ^ -6143 | 9999999999999999999999999999999999 * 10 ^ 6111 | 1 * 10 ^ -6176 | 999999999999999999999999999999999 * 10 ^ -6176 |

these constants are generated from:

```python
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
```

[approximations]: approximations.md
[binary16]: https://en.wikipedia.org/wiki/Half-precision_floating-point_format
[binary32]: https://en.wikipedia.org/wiki/Single-precision_floating-point_format
[binary64]: https://en.wikipedia.org/wiki/Double-precision_floating-point_format
[binary128]: https://en.wikipedia.org/wiki/Quadruple-precision_floating-point_format
[binary256]: https://en.wikipedia.org/wiki/Octuple-precision_floating-point_format
[decimal32]: https://en.wikipedia.org/wiki/Decimal32_floating-point_format
[decimal64]: https://en.wikipedia.org/wiki/Decimal64_floating-point_format
[decimal128]: https://en.wikipedia.org/wiki/Decimal128_floating-point_format
[IEEE 754]: https://en.wikipedia.org/wiki/IEEE_754
