# boolean

since boolean algebra has only two elements {[<code>false</code>], [<code>true</code>]}, we can easily enumerate all the possible functions in a very neat way: with n inputs, we have 2<sup>n</sup> possible permutations, for which we have 2<sup>2<sup>n</sup></sup> functions. 

with n = 1, we have 4 unary functions:

| F | T | name | 
| - | - | - |
| ❌ | ❌ | [<code>false</code>] |
| ❌ | ✅ | [<code>identity</code>] |
| ✅ | ❌ | [<code>not</code>](#not) |
| ✅ | ✅ | [<code>true</code>] |

[false] and [true] are constant functions, so they are stored as constants instead

with n = 2, we have 16 binary functions (ordered partially by hamming weight, then totally by corresponding binary):

| FF | FT | TF | TT | name |
| - | - | - | - | - |
| ❌ | ❌ | ❌ | ❌ | <code>[false]</code> |
| ❌ | ❌ | ❌ | ✅ | <code>[and](#and)</code> |
| ❌ | ❌ | ✅ | ❌ | <code>[nimp](#nimp)</code> |
| ❌ | ✅ | ❌ | ❌ | <code>[ncon](#ncon)</code> |
| ✅ | ❌ | ❌ | ❌ | <code>[nor](#nor)</code> |
| ❌ | ❌ | ✅ | ✅ | <code>[fst]</code> |
| ❌ | ✅ | ❌ | ✅ | <code>[snd]</code> |
| ❌ | ✅ | ✅ | ❌ | <code>[xor](#xor)</code> |
| ✅ | ❌ | ❌ | ✅ | <code>[xnor](#xnor)</code> |
| ✅ | ❌ | ✅ | ❌ | <code>[nsnd]</code> |
| ✅ | ✅ | ❌ | ❌ | <code>[nfst]</code> |
| ❌ | ✅ | ✅ | ✅ | <code>[or](#or)</code>  |
| ✅ | ❌ | ✅ | ✅ | <code>[con](#con)</code> |
| ✅ | ✅ | ❌ | ✅ | <code>[imp](#imp)</code> |
| ✅ | ✅ | ✅ | ❌ | <code>[nand](#nand)</code> |
| ✅ | ✅ | ✅ | ✅ | <code>[true]</code> |

with n = 3, we suddenly have 256 ternary functions. since there are so many, and because they can be composed from binary functions anyway, daamath does not maintain functions of [arity](https://en.wikipedia.org/wiki/Arity?wprov=sfla1) ≥ 3.  
<!--
### nullary functions
| output | name |
| - | - |
| ❌ | false |
| ✅ | true |

there are technically boolean functions with zero inputs but they are better modelled as constants, in daamath.constants.

### unary functions
| 0 | 1 | name | 
| - | - | - |
| ❌ | ❌ | false (nullary) |
| ❌ | ✅ | id |
| ✅ | ❌ | not |
| ✅ | ✅ | true (nullary) |

the `id` function is useless because writing `id(value)` is the same as writing `value` directly

thus we have one useful unary function

### binary functions
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

thus we have 10 useful binary functions
-->
## API implementation

#### [not](https://en.wikipedia.org/wiki/Negation?wprov=sfla1)
negation is [involutive](https://en.wikipedia.org/wiki/Involution_%28mathematics%29?wprov=sfla1). if you apply it twice, it gives you the original value. 
#### [and](https://en.wikipedia.org/wiki/Logical_conjunction?wprov=sfla1)
    being associative, conjunction has a variadic version `all`. can also be thought of as intersection of sets
#### [or](https://en.wikipedia.org/wiki/Logical_disjunction?wprov=sfla1)
    being associative, disjunction has a variadic version `any`. can also be thought of as union of sets.
#### [xor](https://en.wikipedia.org/wiki/Exclusive_or?wprov=sfla1)
    being associative, exclusive disjunction has a variadic version `parity_odd`. can also be thought of as symmonric difference of sets
#### [imp](https://en.wikipedia.org/wiki/Material_conditional?wprov=sfla1)
    material implication is distinctly directional. can also be thought of as difference of sets
#### [con](https://en.wikipedia.org/wiki/Converse_%28logic%29?wprov=sfla1)
    same as `imp(second, first)`. can also be thought of as difference of sets
#### [nand](https://en.wikipedia.org/wiki/Sheffer_stroke?wprov=sfla1)
    not(and(first, second))
#### [nor](https://en.wikipedia.org/wiki/Logical_NOR?wprov=sfla1)
    not(or(first, second))
#### [nxor](https://en.wikipedia.org/wiki/Logical_biconditional?wprov=sfla1)
    not(xor(first, second)). being associative, it has a variadic version `parity_even`
#### nimp
    not(imp(first, second))
#### ncon
    not(con(first, second))
#### nfst
	not(fst(first, second))
#### nsnd
	not(snd(first, second))

## type support

in fact, these logical functions can be applied to more than just logical values. we can apply them to integers in 2's complement bitwise, and also to sets. for example, in python, `daamath.and` supports bool, int, and set as input. in C, `dm_and` supports bool and int, applying them logically or bitwise respectively.

## notes
[`nxor`](#nxor) is used instead of `xnor` to preserve consistency.

[<code>false</code>]: /daamath/specification/constants/boolean#false 
[<code>true</code>]: /daamath/specification/constants/boolean#true
[<code>identity</code>]: /daamath/specification/functions/special#identity
[fst]: /daamath/specification/functions/computational#fst
[snd]: /daamath/specification/functions/computational#snd
