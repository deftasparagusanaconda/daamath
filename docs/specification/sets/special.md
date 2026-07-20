# special

# nothing

```yaml
description: the empty null set of nothing
symbol: ∅
indicator: λx | ⊥
cardinality: 0
```

# everything

```yaml
description: the universal set of everything
symbol: ξ
indicator: λx | ⊤
cardinality: (idk)
```

# boolean

```yaml
    description: primitives of 2-element boolean algebra
    symbol: 𝔹
    indicator: λx | x == ⊥ ∨ x == ⊤
    cardinality: 2
    elements:
      'false': false
      'true': true
    wellorders:
      false_true:
        example:
          - false
          - true
        ordinality: 2
        element_at: λx | bool(x)
        ordinal_of: λx | int(x)
      true_false:
        example:
          - true
          - false
        ordinality: 2
        element_at: λx | ¬bool(x)
        ordinal_of: λx | int(¬x)
```
