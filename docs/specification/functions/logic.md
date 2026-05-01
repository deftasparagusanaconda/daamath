# logic

we deal with binary truths like: false or true, ✅ or ❌, F or T, 0 or 1, ⊤ or ⊥, OFF or ON, etc. we can create functions on these truth values. 

## introduction

we can construct all the possible gates in a very neat way: with n inputs, we have 2^n possible permutations. for 2^n permutations, we have 2^2^n gates. 

with n = 0, we have 2 nullary gates:

| output | name |
| - | - |
| ❌ | false |
| ✅ | true |

with n = 1, we have 4 unary gates:

| F | T | name | 
| - | - | - |
| ❌ | ❌ | <del>false</del> |
| ❌ | ✅ | <del>truth</del> |
| ✅ | ❌ | [not](#not) |
| ✅ | ✅ | <del>true</del> |

with n = 2, we have 16 binary gates:

| FF | FT | TF | TT | name |
| - | - | - | - | - |
| ❌ | ❌ | ❌ | ❌ | <del>false</del> |
| ❌ | ❌ | ❌ | ✅ | [and](#and) |
| ❌ | ❌ | ✅ | ❌ | [nimp](#nimp) |
| ❌ | ❌ | ✅ | ✅ | <del>snd</del> |
| ❌ | ✅ | ❌ | ❌ | [ncon](#ncon) |
| ❌ | ✅ | ❌ | ✅ | <del>fst</del> |
| ❌ | ✅ | ✅ | ❌ | [xor](#xor) |
| ❌ | ✅ | ✅ | ✅ | [or](#or) |
| ✅ | ❌ | ❌ | ❌ | [nor](#nor) |
| ✅ | ❌ | ❌ | ✅ | [nxor](#nxor) |
| ✅ | ❌ | ✅ | ❌ | <del>nfst</del> |
| ✅ | ❌ | ✅ | ✅ | [con](#con) |
| ✅ | ✅ | ❌ | ❌ | <del>nsnd</del> |
| ✅ | ✅ | ❌ | ✅ | [imp](#imp) |
| ✅ | ✅ | ✅ | ❌ | [nand](#nand) |
| ✅ | ✅ | ✅ | ✅ | <del>true</del> |

with n = 3, we suddenly have 256 ternary gates. since there are so many, and because they can be composed from binary gates anyway, daamath does not maintain gates of [arity](https://en.wikipedia.org/wiki/Arity?wprov=sfla1) > 2.  
<!--
### nullary gates
| output | name |
| - | - |
| ❌ | false |
| ✅ | true |

there are technically boolean gates with zero inputs but they are better modelled as constants, in daamath.constants.

### unary gates
| 0 | 1 | name | 
| - | - | - |
| ❌ | ❌ | false (nullary) |
| ❌ | ✅ | id |
| ✅ | ❌ | not |
| ✅ | ✅ | true (nullary) |

the `id` gate is useless because writing `id(value)` is the same as writing `value` directly

thus we have one useful unary gate

### binary gates
| A | B | name |
| - | - | - |
| ❌ | ❌ | Neither |
| ❌ | ✅ | Second |
| ✅ | ❌ | First |
| ✅ | ✅ | Both |

| N | S | F | B | name |
| - | - | - | - | - |
| ❌ | ❌ | ❌ | ❌ | false (nullary) |
| ❌ | ❌ | ❌ | ✅ | all |
| ❌ | ❌ | ✅ | ❌ | ncon |
| ❌ | ❌ | ✅ | ✅ | fst (unary) |
| ❌ | ✅ | ❌ | ❌ | nimp |
| ❌ | ✅ | ❌ | ✅ | snd (unary) | 
| ❌ | ✅ | ✅ | ❌ | xor |
| ❌ | ✅ | ✅ | ✅ | or |
| ✅ | ❌ | ❌ | ❌ | nor |
| ✅ | ❌ | ❌ | ✅ | nxor |
| ✅ | ❌ | ✅ | ❌ | nsnd (unary) |
| ✅ | ❌ | ✅ | ✅ | con |
| ✅ | ✅ | ❌ | ❌ | nfst (unary) |
| ✅ | ✅ | ❌ | ✅ | imp |
| ✅ | ✅ | ✅ | ❌ | nand |
| ✅ | ✅ | ✅ | ✅ | true (nullary) |

fst, snd, nfst, nsnd are useless because writing `fst(first, second)` `snd(first, second)` `nfst(first, second)` `nsnd(first, second)` are the same as writing `first` `second` `not(first)` `not(second)` directly

thus we have 10 useful binary gates
-->
## API implementation

#### [not](https://en.wikipedia.org/wiki/Negation?wprov=sfla1)(value):
negation is [involutive](https://en.wikipedia.org/wiki/Involution_%28mathematics%29?wprov=sfla1). if you apply it twice, it gives you the original value. 
#### [and](https://en.wikipedia.org/wiki/Logical_conjunction?wprov=sfla1)(first, second):
    being associative, conjunction has a variadic version `all`. can also be thought of as intersection of sets
#### [or](https://en.wikipedia.org/wiki/Logical_disjunction?wprov=sfla1)(first, second):
    being associative, disjunction has a variadic version `any`. can also be thought of as union of sets.
#### [xor](https://en.wikipedia.org/wiki/Exclusive_or?wprov=sfla1)(first, second):
    being associative, exclusive disjunction has a variadic version `parity_odd`. can also be thought of as symmonric difference of sets
#### [imp](https://en.wikipedia.org/wiki/Material_conditional?wprov=sfla1)(first, second):
    material implication is distinctly directional. can also be thought of as difference of sets
#### [con](https://en.wikipedia.org/wiki/Converse_%28logic%29?wprov=sfla1)(first, second):
    same as `imp(second, first)`. can also be thought of as difference of sets
#### [nand](https://en.wikipedia.org/wiki/Sheffer_stroke?wprov=sfla1)(first, second):
    not(and(first, second))
#### [nor](https://en.wikipedia.org/wiki/Logical_NOR?wprov=sfla1)(first, second):
    not(or(first, second))
#### [nxor](https://en.wikipedia.org/wiki/Logical_biconditional?wprov=sfla1)(first, second):
    not(xor(first, second)). being associative, it has a variadic version `parity_even`
#### nimp(first, second):
    not(imp(first, second))
#### ncon(first. second):
    not(con(first, second))

## type support

in fact, these logical gates can be applied to more than just logical values. we can apply them to integers in 2's complement bitwise, and also to sets. for example, in python, `daamath.and` supports bool, int, and set as input. in C, `dm_and` supports bool and int, applying them logically or bitwise respectively.

## notes
`nxor` is used instead of `xnor` to preserve consistency.

