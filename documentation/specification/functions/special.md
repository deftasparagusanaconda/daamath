# special

some functions in set theory have special status

| name | domain | codomain | input | output | description |
| - | - | - | - | - | - |
| id | [ξ] | [ξ] | x | x | the identity function, that returns whatever is given to it |
| eq | [ξ]×[ξ] | 𝔹 | a, b | a == b | two objects are mathematically the same |
| is | [ξ]×[ξ] | 𝔹 | a, b | a is b | a is the same object as b |

`eq` and `is` are comparable to `ev`, which also checks equality but specifically under a certain ordering.

## identity

identity: [ξ] → [ξ] x | x | the identity function, that returns whatever is given to it |
description: the identity function. it returns whatever is given to it

## is

the `is` function tells you whether a is b. a and b can compare equivalent via [eq] but identify different via [is]

this is important for languages where 

# yaml

here is a yaml file, usable for generating code for an implementation
<details><summary>yaml</summary>
```yaml
--8<-- "./docs/specification/functions/special.yaml"
```
</details>

[ξ]: 
[𝔹]: 
