# numeric

there are a few functions needed specifically for better numerical performance:

| name | decomposition | notation | common names |
| - | - | - | - |
| <code>[sqrt](sqrt)(c)</code> | <code>[root]\(c, 2)</code> | $\sqrt{c}$ |
| <code>[cbrt](cbrt)(c)</code> | <code>[root]\(c,  3)</code> | $\sqrt[3]{c}$ |
| <code>[lb](lb)(c)</code> | <code>[log]\(c,  2)</code> | $\log_2(c)$ | log2
| <code>[lg](lg)(c)</code> | <code>[log]\(c, 10)</code> | $\log_{10}(c)$ | log10
| <code>[ln](ln)(c)</code> | <code>[log]\(c,  [e])</code> | $\log_{\mathrm e}(c)$ | log
| <code>[exp](exp)(b)</code> | <code>[pow]\([e],  b)</code> | $\mathrm e^b$ |
| <code>[ln1p](ln1p)(c)</code> | <code>[ln](ln)([add]\(1, c))</code> | $\ln(1 + c)$ | log1p
| <code>[expm1](expm1)(b)</code> | <code>[sub]\([exp](exp)(b), 1)</code> |$\mathrm e ^ b - 1$ |
| <code>[fma](fma)(a, b, c)</code> | <code>[add]\([mul]\(a, b), c)</code> | $ab + c$ |
| <code>[radius](radius)(x, y)</code> |  | $\sqrt{x^2 + y^2}$ | hypot
| <code>[angle](angle)(x, y)</code> |  |  | atan2

[add]: ../arithmetic/add
[sub]: ../arithmetic/sub
[mul]: ../arithmetic/mul
[pow]: ../arithmetic/pow
[root]: ../arithmetic/root
[log]: ../arithmetic/log
[e]: /constants/math#euler_bernoulli
