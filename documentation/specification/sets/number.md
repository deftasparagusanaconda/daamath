# number

```yaml
number:
  naturals:
    description: natural numbers starting from zero
    symbol: ℕ
    indicator: λx | x ∈ ℤ ∧ x ≥ 0
    cardinality: ℵ₀
    wellorders: 
      natural: 
        description: increasing magnitude
        relation: λ(a,b) | a ≤ b
        ordinality: ω
        ordinal_of: λx | x
        element_at: λx | x
        covers: λ(a,b) | a + 1 == b
        least: 0
        greatest:
        successor: λx | x + 1
        predecessor: λx | x − 1

  integers:
    description: equivalence classes of a + b = c + d where a, b, c, d ∈ ℕ
    symbol: ℤ
    indicator: λx | x ∈ ℚ ∧ 1 ∣ x
    cardinality: ℵ₀
    wellorders:
      magnitudinal_positive_first:
        description: increasing magnitude, with +1 after 0
        example:
          - 0 
          - +1
          - -1
          - +2
          - -2
          - …
        ordinality: ω
        element_at: λx | {x == 0 | 0, 2 ∣ x | − ⌊(x + 1) / 2⌋, 2 ∤ x | ⌊(x + 1) / 2⌋}
        ordinal_of: λx | {x == 0 | 0, x < 0 | −2 * x, x > 0 | 2 * x − 1}
  
  rationals:
    description: equivalence classes of a × b = c × d where a, b, c, d ∈ ℤ
    symbol: ℚ

  reals:
    description: a dense totally-ordered set
    symbol: ℝ

  complexes:
    description: a normed division vector algebra made from cayley-dickson construction of a pair of reals
    symbol: ℂ

  quaternions:
    description: a normed division vector algebra made from cayley-dickson construction of a pair of complexes
    symbol: ℍ # "Hamilton"

  octonions:
    description: a normed division vector algebra made from cayley-dickson construction of a pair of quaternions
    symbol: 𝕆

  # datatypes
  # float:
  #   description: IEEE 754 binary/decimal float

  
  #   symbol: 
  #
```
