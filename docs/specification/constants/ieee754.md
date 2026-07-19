---
hide:
  - toc
---

# ieee754

daamath maintains constants in the 5 basic [IEEE 754] formats. those 5 formats are described here:

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

[binary16]: https://en.wikipedia.org/wiki/Half-precision_floating-point_format
[binary32]: https://en.wikipedia.org/wiki/Single-precision_floating-point_format
[binary64]: https://en.wikipedia.org/wiki/Double-precision_floating-point_format
[binary128]: https://en.wikipedia.org/wiki/Quadruple-precision_floating-point_format
[binary256]: https://en.wikipedia.org/wiki/Octuple-precision_floating-point_format
[decimal32]: https://en.wikipedia.org/wiki/Decimal32_floating-point_format
[decimal64]: https://en.wikipedia.org/wiki/Decimal64_floating-point_format
[decimal128]: https://en.wikipedia.org/wiki/Decimal128_floating-point_format
[IEEE 754]: https://en.wikipedia.org/wiki/IEEE_754
