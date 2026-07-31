# relational

when a binary relation `rel(a, b)` is defined on a carrier set, we can compose `rel(a, b)` and `rel(b, a)` using the [boolean functions][boolean] to get many useful functions. we shall use the common partial ordering relation ≤ (less than or equal to) to name these composed functions, although the binary relation can be anything: an equivalence relation, a partial ordering, a pre-order, et cetera.

| name | boolean | ∥ < > ∼ | notation | description |
| - | - | - | - | - |
| [<code>false</code>] | [<code>false</code>] | ❌❌❌❌ | `⊥` | degenerate always-false |
| [`ev`](#ev) | [<code>and</code>] | ❌❌❌✅ | `a ∼ b` | equivalent |
| [`gt`](#gt) | [<code>ncon</code>] | ❌❌✅❌ | `a > b` | greater than |
| [`lt`](#lt) | [<code>nimp</code>] | ❌✅❌❌ | `a < b` | lesser than |
| [`ncp`](#ncp) | [<code>nor</code>] | ✅❌❌❌ | `a ∥ b` | incomparable |
| [`ge`](#ge) | [<code>snd</code>] | ❌❌✅✅ | `a ≥ b` | greater than or equivalent |
| [`le`](#le) | [<code>fst</code>] | ❌✅❌✅ | `a ≤ b` | lesser than or equivalent |
| [`so`](#so) | [<code>xor</code>] | ❌✅✅❌ | `a ≶ b` | strictly ordered |
| [`nso`](#nso) | [<code>nxor</code>] | ✅❌❌✅ | `a ≸ b` | not strictly ordered |
| [`nle`](#nle) | [<code>nfst</code>] | ✅❌✅❌ | `a ≰ b` | not lesser than nor equivalent |
| [`nge`](#nge) | [<code>nsnd</code>] | ✅✅❌❌ | `a ≱ b` | not greater than nor equivalent |
| [`cp`](#cp) | [<code>or</code>] | ❌✅✅✅ | `a ∦ b` | comparable |
| [`nlt`](#nlt) | [<code>imp</code>] | ✅❌✅✅ | `a ≮ b` | not lesser than |
| [`ngt`](#ngt) | [<code>con</code>] | ✅✅❌✅ | `a ≯ b` | not greater than |
| [`nev`](#nev) | [<code>nand</code>] | ✅✅✅❌ | `a ≁ b` | not equivalent |
| [<code>true</code>] | [<code>true</code>] | ✅✅✅✅ | `⊤` | degenerate always-true |

the [eq] function is distinct from the [is] function. two objects can be equivalent via eq(a, b) but different via [is](a, b)

# FAQ

"where is the binary relation for these functions stored?"
	in dm.context — both the carrier set and the binary relation for these functions are stored in dm.context

<!--
## API implementation

#### lt(a, b):
less than
a < b

=== "python"
	```python
	dm.lt(1, 2)
	# true
	```
=== "c"
	```c
	dm_lt(1, 2)
	# true
	```
#### le(a, b):
	less than or equal to
	a ≤ b
#### eq(a, b):
	equal
	a = b
#### ne(a, b):
	not equal
	a ≠ b
#### ge(a, b):
	greater than or equal to
	a ≥ b
#### gt(a, b):
	greater than
	a > b
#### oo(x, a, b):
	in open interval
	x ∈ (a, b)
#### oc(x, a, b):
	in left-open interval
	x ∈ (a, b]
#### co(x, a, b):
	in right-open interval
	x ∈ [a, b)
#### cc(x, a, b):
	in closed interval
	x ∈ [a, b]
-->

# yaml

here is a yaml file, usable for generating code for an implementation
<details><summary>yaml</summary>
```yaml
--8<-- "./docs/specification/functions/relational.yaml"
```
</details>

# deprecated

why did i exclude this? it adds bloat to the vocabulary the user has to learn, for not much benefit

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
