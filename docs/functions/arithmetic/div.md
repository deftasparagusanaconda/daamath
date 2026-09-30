# `div`

given an equation $a ⋅ b = c$, [divison](https://en.wikipedia.org/wiki/Division_(mathematics)) solves for a or b: $a = \dfrac cb$ and $b = \dfrac ca$. if a or b have a multiplicative inverse ÷a or ÷b, division can be defined as: $a = c ⋅ ÷b$ or $b = a = c ⋅ ÷b$

```python
import daamath.mul.bigint as mul
import daamath.div.bigint as div

mul(2, 3) # 6
div(6, 3) # 2
div(6, 2) # 3
```

`div` is available iff `mul` is commutative, since ldiv and rdiv would behave exactly the same, and we sometimes want to specify "*the* division" instead of having to specify [`ldiv`] (left division) or [`rdiv`] (right division).

# div.bigint

division is rarely closed in the integers. the result of division is an integer iff their [`gcd`]()

# div.binaryX.

division is rarely closed on finite subsets of the reals.

## div.binaryX.nearest



# div.complexX.

division is rarely closed on finite subsets of the reals

[`mul`]: ../mul.md
[`ldiv`]: ../ldiv.md
[`rdiv`]: ../rdiv.md
