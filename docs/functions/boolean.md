# boolean

we have 1 + 10 useful boolean functions: [`not`](#not), [`and`](#and) [`or`](#or) [`xor`](#xor) [`imp`](#imp) [`con`](#con) [`nand`](#nand) [`nor`](#nor) [`nxor`](#nxor) [`nimp`](#nimp) [`ncon`](#ncon)

we can neatly enumerate all the possible boolean functions: with n inputs, we have 2<sup>n</sup> possible permutations, for which we have 2<sup>2<sup>n</sup></sup> functions. 

# nullary functions

we have 2<sup>2<sup>0</sup></sup> = 2 nullary "functions":

| name | value | symbol | description |
| - | - | - | - |
| [<code>false</code>] | ❌ | ⊥ | boolean bottom element | 
| [<code>true</code>] | ✅ | ⊤ | boolean top element |

these are stored as constants instead

# unary functions

with n = 1 inputs, we have 2<sup>2<sup>1</sup></sup> = 4 unary functions:

| name | F T | symbol | description |
| - | - | - | - |
| [<code>false</code>] | ❌❌ | ⊥ | constant always-false function |
| [<code>id</code>] | ❌✅ | id | identity |
| <span id="not"></span>[<code>not</code>](#not) | ✅❌ | ¬ | [negation](https://en.wikipedia.org/wiki/Negation) | 
| [<code>true</code>] | ✅✅ | ⊤ | constants always-true function |

[`not`](#not) is the only useful non-degenerate function here

# binary functions 

with n = 2 inputs, we have 2<sup>2<sup>2</sup></sup> = 16 binary functions:

| name | FF FT TF TT | symbol | description |
| - | - | - | - |
| [<code>false</code>] | ❌❌❌❌ | ⊥ | constant always-false function | 
| <span id="and"></span>[<code>and</code>](#and) | ❌❌❌✅ | ∧ | [conjunction](https://en.wikipedia.org/wiki/Logical_conjunction) |
| <span id="nimp"></span>[<code>nimp</code>](#nimp) | ❌❌✅❌ | ↛ | [abjunction](https://en.wikipedia.org/wiki/Material_nonimplication) |
| <span id="ncon"></span>[<code>ncon</code>](#ncon) | ❌✅❌❌ | ↚ | [converse abjunction](https://en.wikipedia.org/wiki/Converse_nonimplication) |
| <span id="nor"></span>[<code>nor</code>](#nor) | ✅❌❌❌ | ↓ | [joint denial](https://en.wikipedia.org/wiki/Logical_NOR) |
| [<code>fst</code>] | ❌❌✅✅ | π~1~ | first argument |
| [<code>snd</code>] | ❌✅❌✅ | π~2~ | second argument |
| <span id="xor"></span>[<code>xor</code>](#xor) | ❌✅✅❌ | ↮ | [exclusive disjunction](https://en.wikipedia.org/wiki/Exclusive_or) |
| <span id="nxor"></span>[<code>nxor</code>](#nxor) | ✅❌❌✅ | ↔  | [material biconditional](https://en.wikipedia.org/wiki/Material_biconditional) |
| <code>nsnd</code> | ✅❌✅❌ | ¬π~2~ | ¬first argument |
| <code>nfst</code> | ✅✅❌❌ | ¬π~1~ | ¬second argument |
| <span id="or"></span>[<code>or</code>](#or)  | ❌✅✅✅ | ∨ | [disjunction](https://en.wikipedia.org/wiki/Logical_disjunction) |
| <span id="con"></span>[<code>con</code>](#con) | ✅❌✅✅ | ← | [converse material implication](https://en.wikipedia.org/wiki/Converse_%28logic%29) |
| <span id="imp"></span>[<code>imp</code>](#imp) | ✅✅❌✅ | → | [material implication](https://en.wikipedia.org/wiki/Material_conditional?wprov=sfla1) |
| <span id="nand"></span>[<code>nand</code>](#nand) | ✅✅✅❌ | ↑ | [alternative denial](https://en.wikipedia.org/wiki/Sheffer_stroke) |
| [<code>true</code>] | ✅✅✅✅ | ⊤ | constant always-true function |

[<code>fst</code>], [<code>snd</code>], <code>nsnd</code>, <code>nfst</code> are degenerate functions

# ternary functions and beyond

with n = 3 inputs, we have 2<sup>2<sup>3</sup></sup> = 256 ternary functions. since there are so many, and because they can be composed from binary functions anyway, daamath does not maintain functions of n ≥ 3.
<!--
---

# functions

## not
negation is involutive. 
## and
and is the meet of the boolean lattice. its variadic extension is vand.
## or
or is the join of the boolean lattice. its variadic extension is vor.
## xor
its variadic extension is vxor
## imp
it is useful for its asymmetry, unlike the other ones
## con
it is useful for its asymmetry, unlike the other ones
## nand
nand(a, b) = not(and(a, b))
## nor
nor(a, b) = not(or(a, b))
## nxor
nxor(a, b) = not(xor(a, b)). its variadic extension is vnxor.
## nimp
nimp(a, b) = not(imp(a, b))
## ncon
ncon(a, b) = not(con(a, b))
-->


[<code>false</code>]: /daamath/constants/boolean#false 
[<code>true</code>]: /daamath/constants/boolean#true
[<code>id</code>]: /daamath/functions/special#identity
[<code>fst</code>]: /daamath/functions/special#fst
[<code>snd</code>]: /daamath/functions/special#snd
