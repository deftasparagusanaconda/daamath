# numeric

there are a few useful pre-curried functions in math:

| name | decomposition | notation |
| - | - | - |
| <code>[sqrt](sqrt)(c)</code> | <code>[root]\(c, 2)</code> | $\sqrt{c}$ |
| <code>[cbrt](cbrt)(c)</code> | <code>[root]\(c,  3)</code> | $\sqrt[3]{c}$ |
| <code>[log2](log2)(c)</code> | <code>[log]\(c,  2)</code> | $\log_2(c)$ |
| <code>[log10](log10)(c)</code> | <code>[log]\(c, 10)</code> | $\log_10(c)$ |
| <code>[ln](ln)(c)</code> | <code>[log]\(c,  [e])</code> | $\ln(c)$ |
| <code>[exp](exp)(b)</code> | <code>[pow]\([e],  b)</code> | $\mathrm e^b$ |
| <code>[ln1p](ln1p)(c)</code> | <code>[ln](ln)([add]\(1, c))</code> | $\ln(1 + c)$ |
| <code>[expm1](expm1)(b)</code> | <code>[sub]\([exp](exp)(b), 1)</code> |$\mathrm e ^ b - 1$ |
| <code>[fma](fma)(a, b, c)</code> | <code>[add]\([mul]\(a, b), c)</code> | $ab + c$ |

[add]: ../arithmetic/add
[sub]: ../arithmetic/sub
[mul]: ../arithmetic/mul
[pow]: ../arithmetic/pow
[root]: ../arithmetic/root
[log]: ../arithmetic/log
[e]: /constants/math#euler_bernoulli
