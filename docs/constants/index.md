# constants

in $\text{mathematics}$, we usually manipulate things symbolically, and constants are exact. for example, $\mathrm π = 3.141592653589793238462643383279502884197169399375…$

in `programming`, we usually manipulate things numerically, and constants are approximate. for example `math.pi` in python is <code><span style="color: var(--dm-green)">3.141592653589793</span><span style="color: var(--dm-red)">115997963468544185161590576171875</span></code>

<!--we cannot pretend that an approximation is the exact value. this is clear from how $\sin(\mathrm π) = 0$ but `math.sin(math.pi)` in python is <code><span style="color: var(--dm-green)">0.000000000000000</span><span style="color: var(--dm-red)">122464679914735320717376402945839660462569212467758006379625612680683843791484832763671875</span></code> so we store constants as approximations.

we have **51** constants from [Wikipedia](https://en.wikipedia.org/wiki/List_of_mathematical_constants) and [MathWorld](https://mathworld.wolfram.com/) up to **5050** decimal digits:

| name | eponyms | formula | decimal | notes |
| ---- | ------- | ------- | ------- | ----- |
{{ math_constants() }}

exceptions:

* the [🇳🇴 Viggo Brun](https://no.wikipedia.org/wiki/Viggo_Brun) constant $\href{https://en.wikipedia.org/wiki/Brun%27s_theorem}{\mathrm B_2} := \left.\displaystyle\sum \left(\dfrac 1p + \dfrac 1q\right)\;\right\vert\;\href{https://no.wikipedia.org/wiki/Tvillingprimtall}{\begin{aligned} &p, q \in \mathbb P \\ &p + 2 = q \end{aligned}}$ ≈ [1.902160583104…](https://oeis.org/A065421) is excluded because we do not know enough digits to saturate the precision of the datatypes
<!--* constants like 0, 1, -1, 2, ½ are not stored since their construction is trivial--><!-- i excluded this because its stating the obvious -->

# implementation

the decimal expansion of a constant is stored trunc-rounded to exactly 5050 (5040 for divisibility and github space constraints, 10 for leeway) [significant figures](https://en.wikipedia.org/wiki/Significant_figures) as raw ASCII/UTF-8 text in [scientific notation](https://en.wikipedia.org/wiki/Scientific_notation), by the regex `[+-][1-9].[0-9]{5049}E[+-][0-9]+`

a datatype correctly approximates a constant $\class{dm-yellow}{c} = \class{dm-cyan}{s} ⋅ 10^{\class{dm-magenta}{e}}$ if both bounds of the interval $\begin{aligned}\lbrack \class{dm-yellow}{c}, 10^{\class{dm-magenta}{e}-5049} + \class{dm-yellow}{c}) \text{ if } \class{dm-magenta}{s} > 0 \\ (\class{dm-yellow}{c} - 10^{\class{dm-magenta}{e}-5049}, \class{dm-yellow}{c}\rbrack \text{ if } \class{dm-magenta}{s} < 0 \end{aligned}$ round to the same value in that datatype

an implementation should store only pre-compiled constants in a datatype. it should not ship the constants as strings, since a user should interact with constants only as datatype approximations.

you ^^cannot^^ use an approximation get another approximation, like casting an binary64 constant to binary32 because [double rounding error](https://www.exploringbinary.com/double-rounding-errors-in-floating-point-conversions/) can occur

finally, the page for each constant is generated using:
```python
--8<--  "py files/generate constants files.py"
```

<!--# constants

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
# get τ as an f32 approximation in the float datatype

TAU = dm.hartl.binary16.nearest.float
```

```
# create e as a box interval of f64

E = dm.euler_bernoulli.binary64.nearest
residual = dm.euler_bernoulli.binary64.residual
E = (dm.pred(E), E) if residual < 0 else (E, dm.succ(E))
```

```
# create e as a ball interval of f32

E = (dm.euler_bernoulli.binary32.nearest.float, abs(dm.euler_bernoulli.binary32.residual.float))
```

<!--
# notes

the rational approximations are stored as three integers. this is actually slightly redundant because rationals only need two integers (or three natural numbers!). but storing two ginormous integers is less efficient than the three handle-able integers because they match the structure of the float datatypes better.

# rant

`DIV_X_Y` seemed like a good idea until i realized the space blows up and i have to start making arbitrary decisions on where to stop. this is bad. daamath shouldnt make assumptions unless they are mathematically sound and clear. if you want `DIV_1_PI`, make it yourself: `div(1, pi)` or `minv(pi)`

# naming

constants should not be written in uppercase. if constants should be immutable during runtime, that should be enforced by a guard, not by its name. 
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
-->

{{ yaml_source(page) }}
