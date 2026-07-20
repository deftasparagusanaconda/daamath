---
hide:
  - toc
---

# cayley_dickson

the [cayley dickson construction][cdc] gives us some important basis units

| name | common symbols | description | 
| - | - | - |
| <code><a href="https://en.wikipedia.org/wiki/Imaginary_unit">cayley_dickson_1_1</a></code> | i (in math), j (in engineering) | 1th basis of the 1th iteration of the cayley dickson construction. also known as imaginary basis unit of the [complex numbers](https://en.wikipedia.org/wiki/Complex_number) |
<!--
| `cayley_dickson_1_1`j | | [split-complex](https://en.wikipedia.org/wiki/Split-complex_number) imaginary unit |
| ε | | [dual](https://en.wikipedia.org/wiki/Dual_number) imaginary unit |
-->

```yaml
# cayley_dickson:
#   - name: real
#     symbol: ℝ
#     bases: [one]
#
#   - name: complex
#     symbol: ℂ
#     bases: [one, i]
#
#   - name: quaternion
#     symbol: ℍ # named after Sir William Rowan *Hamilton*
#     bases: [one, i, j, k]
#
#   - name: octonion
#     symbol: 𝕆
#     bases: [e0, e1, e2, e3, e4, e5, e6, e7]

cayley_dickson:
  - [one]
  - [one, i]
  - [one, i, j, k]
  - [one, e1, e2, e3, e4, e5, e6, e7]
```

[cdc]: https://en.wikipedia.org/wiki/Cayley%E2%80%93Dickson_construction
