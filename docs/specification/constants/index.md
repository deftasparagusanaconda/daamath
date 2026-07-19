# constants

a constant is something whose value doesnt depend on anything and doesnt change unless the universe changes. under this definition, daamath has a few kinds of constants:

# rational approximations

an irrational constant may be stored as a rational approximation:

- each constant has 5 [IEEE 754] basic formats: [f32], [f64], [f128], [d64], [d128]
- each format has 2 residuals: the [nearest_even]-rounded value and the error of that rounded value
- each residual has 3 integers: significand, radix, exponent

the advantages of this are:

- the approximation is explicit, and not implicit in machine/language datatype
- a box (lower, upper) or a ball (centre, radius) interval can be constructed
- the constant can be easily hydrated into a float/fraction/string/int/interval/…

for convenience, an implementation may also store hydrated versions of the integer triple

the following irrational constants are approximated:

# examples

```
# get τ as an f16 approximation

TAU = dm.TAU.f16.nearest
```

```
# create e as a box interval of f64

E = dm.E.f32.nearest          
E = (dm.pred(E), E) if dm.E.f32.error < 0 else (E, dm.succ(E))           
```

```
# create e as a ball interval of f32

E = dm.ball(centre=dm.E.f32.nearest, radius=abs(dm.E.f32.error))
```


# notes

the rational approximations are stored as three integers. this is actually slightly redundant because rationals only need two integers (or three natural numbers!). but storing two ginormous integers is less efficient than the three handle-able integers because they match the structure of the float datatypes better.

# rant

`DIV_X_Y` seemed like a good idea until i realized the space blows up and i have to start making arbitrary decisions on where to stop. this is bad. daamath shouldnt make assumptions unless they are mathematically sound and clear. if you want `DIV_1_PI`, make it yourself: `div(1, pi)` or `minv(pi)`

[f16]: https://en.wikipedia.org/wiki/Half-precision_floating-point_format
[f32]: https://en.wikipedia.org/wiki/Single-precision_floating-point_format
[f64]: https://en.wikipedia.org/wiki/Double-precision_floating-point_format
[f128]: https://en.wikipedia.org/wiki/Quadruple-precision_floating-point_format
[f256]: https://en.wikipedia.org/wiki/Octuple-precision_floating-point_format
[d32]: https://en.wikipedia.org/wiki/Decimal32_floating-point_format
[d64]: https://en.wikipedia.org/wiki/Decimal64_floating-point_format
[d128]: https://en.wikipedia.org/wiki/Decimal128_floating-point_format
[IEEE 754]: https://en.wikipedia.org/wiki/IEEE_754
[τ]: https://en.wikipedia.org/wiki/Tau
