# relational

when a binary relation `rel(a, b)` is defined on a carrier set, we can combine `rel(a, b)` and `rel(b, a)` using the binary [boolean functions][boolean] to get many useful functions. to name these combined functions, we'll use the common partial ordering relation ≤ (less than or equal to), but note that the binary relation can be anything: an equivalence relation, a partial ordering, a pre-order, et cetera.

| name | combiner | ∦ < > ∼ | symbol | description |
| - | - | - | - | - |
| [<code>false</code>] | [<code>false</code>] | ❌❌❌❌ | ⊥ | degenerate always-false function |
| [`ev`](#ev) | [<code>and</code>] | ❌❌❌✅ | ∼ | **e**qui**v**alent |
| [`gt`](#gt) | [<code>ncon</code>] | ❌❌✅❌ | > | **g**reater **t**han |
| [`lt`](#lt) | [<code>nimp</code>] | ❌✅❌❌ | < | **l**esser **t**han |
| [`ic`](#ic) | [<code>nor</code>] | ✅❌❌❌ | ∦ |  **i**ncomparable |
| [`ge`](#ge) | [<code>snd</code>] | ❌❌✅✅ | ≥ | **g**reater than or **e**quivalent |
| [`le`](#le) | [<code>fst</code>] | ❌✅❌✅ | ≤ | **l**esser than or **e**quivalent |
| [`so`](#so) | [<code>xor</code>] | ❌✅✅❌ | ≶ | **s**trictly **o**rdered |
| [`nso`](#nso) | [<code>nxor</code>] | ✅❌❌✅ | ≸ | **n**ot **s**trictly **o**rdered |
| [`nle`](#nle) | [<code>nfst</code>] | ✅❌✅❌ | ≰ | **n**ot **l**esser than nor **e**quivalent |
| [`nge`](#nge) | [<code>nsnd</code>] | ✅✅❌❌ | ≱ | **n**ot **g**reater than nor **e**quivalent |
| [`nic`](#nic) | [<code>or</code>] | ❌✅✅✅ | ∥ | **n**ot **i**n**c**omparable |
| [`nlt`](#nlt) | [<code>imp</code>] | ✅❌✅✅ | ≮ | **n**ot **l**esser **t**han |
| [`ngt`](#ngt) | [<code>con</code>] | ✅✅❌✅ | ≯ | **n**ot **g**reater **t**han |
| [`nev`](#nev) | [<code>nand</code>] | ✅✅✅❌ | ≁ | **n**ot **e**qui**v**alent |
| [<code>true</code>] | [<code>true</code>] | ✅✅✅✅ | ⊤ | degenerate always-true function |

# ev
# gt
# lt
# ic
# ge
# le
# so
# nso
# nle
# nge
# nic
# nlt
# ngt
# nev

# FAQ


<!--
# deprecated. why did i exclude this? because it adds bloat to the vocabulary the user has to learn, for not much benefit

## w.r.t. one element

when `rel(a, b)` is a total order, cp is always true; so the 16 functions are reduced down to 8. we may present these visually using the one-dimensional nature of a totally ordered set. we have three partitions of the carrier set:

| name | < = > |
| - | - |
| [<code>false</code>] | ❌❌❌ |
| [gt](#gt) | ❌❌✅ |
| [ev](#ev) | ❌✅❌ |
| [lt](#lt) | ✅❌❌ |
| [ge](#ge) | ❌✅✅ |
| [so](#so) | ✅❌✅ |
| [le](#le) | ✅✅❌ |
| [<code>true</code>] | ✅✅✅ |

## w.r.t. two elements

with respect to two elements A and B, we have five partitions of the carrier set:

| name | <A⋯B\> | description |
| - | - | - |
| <del>false</del> | ❌❌❌❌❌ | degenerate always-false|
| <del>gt_B</del> | ❌❌❌❌✅ | > B |
| <del>eq_B</del> | ❌❌❌✅❌ | ∼ B |
| [oo](#oo) | ❌❌✅❌❌ | in open-open interval |
| <del>eq_A</del> | ❌✅❌❌❌ | ∼ A |
| <del>lt_A</del> | ✅❌❌❌❌ | < A |
| <del>ge_B</del> | ❌❌❌✅✅ | ≥ B |
| [bg](#bg) | ❌❌✅❌✅ | between or greater than|
| [oc](#oc) | ❌❌✅✅❌ | in open-closed interval |
| [fg](#fg) | ❌✅❌❌✅ | first or greater than |
| [ei](#ei) | ❌✅❌✅❌ | either A or B |
| [co](#co) | ❌✅✅❌❌ | in closed-open interval |
| [ncc](#ncc) | ✅❌❌❌✅ | not in closed-closed interval |
| [sl](#sl) | ✅❌❌✅❌ | second or lesser than |
| [bl](#bl) | ✅❌✅❌❌ | between or lesser than |
| <del>le_A</del> | ✅✅❌❌❌ | ≤ A |
| <del>gt_A</del> | ❌❌✅✅✅ | > A |
| [nbl](#nbl) | ❌✅❌✅✅ | not between nor lesser than |
| [nsl](#nsl) | ❌✅✅❌✅ | not second nor lesser than |
| [cc](#cc) | ❌✅✅✅❌ | in closed-closed interval |
| [nco](#nco) | ✅❌❌✅✅ | not in closed-open interval |
| [nei](#nei) | ✅❌✅❌✅ | neither A nor B |
| [nfg](#nfg) | ✅❌✅✅❌ | not first nor greater than |
| [noc](#noc) | ✅✅❌❌✅ | not in open-closed interval |
| [nbg](#nbg) | ✅✅❌✅❌ | not between nor greater than|
| <del>lt_B</del> | ✅✅✅❌❌ | < B |
| <del>ge_A</del> | ❌✅✅✅✅ | ≥ A |
| <del>so_A</del> | ✅❌✅✅✅ | ≶ A |
| [noo](#noo) | ✅✅❌✅✅ | not in open-open interval |
| <del>so_B</del> | ✅✅✅❌✅ | ≶ B |
| <del>le_B</del> | ✅✅✅✅❌ | ≤ B|
| <del>true</del> | ✅✅✅✅✅ | degenerate always-true |
-->

{{ yaml_source(page) }}

[boolean functions]: boolean.md
[<code>false</code>]: ../constants/boolean#false
[<code>true</code>]: ../constants/boolean#true
[<code>and</code>]: ./boolean#and
[<code>or</code>]: ./boolean#or
[<code>xor</code>]: ./boolean#xor
[<code>imp</code>]: ./boolean#imp
[<code>con</code>]: ./boolean#con
[<code>fst</code>]: ./boolean#fst
[<code>snd</code>]: ./boolean#snd
[<code>nand</code>]: ./boolean#nand
[<code>nor</code>]: ./boolean#nor
[<code>nxor</code>]: ./boolean#nxor
[<code>nimp</code>]: ./boolean#nimp
[<code>ncon</code>]: ./boolean#ncon
[<code>nfst</code>]: ./boolean#nfst
[<code>nsnd</code>]: ./boolean#nsnd
