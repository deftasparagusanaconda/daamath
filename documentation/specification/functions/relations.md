# binary relations

when a binary relation `rel(a, b)` is defined on a carrier set, we can compose `rel(a, b)` and `rel(b, a)` using the [boolean functions][boolean] to get many useful functions. we shall use the common partial ordering relation ≤ (less than or equal to) to name these composed functions, although the binary relation can be anything: an equivalence relation, a partial ordering, a pre-order, et cetera.

| name | ∦ | < | > | = | boolean | notation |
| - | - | - | - | - | - | - |
| [`false`] | ❌ | ❌ | ❌ | ❌ | [`false`] | ⊥     |
| [`ev`](#ev)    | ❌ | ❌ | ❌ | ✅ | [and]   | a ∼ b |
| [`gt`](#gt)    | ❌ | ❌ | ✅ | ❌ | [ncon]  | a > b |
| [`lt`](#lt)    | ❌ | ✅ | ❌ | ❌ | [nimp]  | a < b |
| [`cp`](#cp)    | ❌ | ✅ | ✅ | ✅ | [or]    | a ∦ b |
| [`ge`](#ge)    | ❌ | ❌ | ✅ | ✅ | [snd]   | a ≥ b |
| [`le`](#le)    | ❌ | ✅ | ❌ | ✅ | [fst]   | a ≤ b |
| [`so`](#so)    | ❌ | ✅ | ✅ | ❌ | [xor]   | a ≶ b |
| [`nso`](#nso)   | ✅ | ❌ | ❌ | ✅ | [nxor] | a ≸ b |
| [`nle`](#nle)   | ✅ | ❌ | ✅ | ❌ | [nfst] | a ≰ b |
| [`nge`](#nge)   | ✅ | ✅ | ❌ | ❌ | [nsnd] | a ≱ b |
| [`ncp`](#ncp)   | ✅ | ❌ | ❌ | ❌ | [nor]  | a ∥ b |
| [`nlt`](#nlt)   | ✅ | ❌ | ✅ | ✅ | [imp]   | a ≮ b |
| [`ngt`](#ngt)   | ✅ | ✅ | ❌ | ✅ | [con]  | a ≯ b | | 
| [`nev`](#nev)   | ✅ | ✅ | ✅ | ❌ | [nand]   | a ≁ b | | 
| [`true`]  | ✅ | ✅ | ✅ | ✅ | [true]  | ⊤     | | 

you may also notice these are the same degenerates as the [boolean functions][boolean]; but though they are degenerate, daamath still includes them because `ge(a, b)` & `le(a, b)` may be useful aliases for `rel(a, b)` & `rel(b, a)`. similarly with `nb(a, b)` & `na(a, b)` for `not(rel(a, b))` & `not(rel(b, a))`.

the [eq] function is distinct from the [is] function. two objects can be equivalent via eq(a, b) but different via [is](a, b)

# w.r.t. one element

when `rel(a, b)` is a total order, cp is always true; so the 16 functions are reduced down to 8. we may present these visually using the one-dimensional nature of a totally ordered set. we have three partitions of the carrier set:

| x < A | x = A | x > A | name |
| - | - | - | - | 
| ❌ | ❌ | ❌ | [false] |
| ❌ | ❌ | ✅ | [gt](#gt) | 
| ❌ | ✅ | ❌ | [ev](#ev) | 
| ✅ | ❌ | ❌ | [lt](#lt) |
| ❌ | ✅ | ✅ | [ge](#ge) | 
| ✅ | ❌ | ✅ | [so](#so) | 
| ✅ | ✅ | ❌ | [le](#le) | 
| ✅ | ✅ | ✅ | [true] | 

## gt
## ev
## lt
## ge
## so
## le

# w.r.t. two elements

with respect to two elements A and B, we have five partitions of the carrier set:

sl bl ei bg fg

| name | x < A | x = A | A < x < B | x = B | x > B | description |
| - | - | - | - | - | - | - |
| <del>false</del> | ❌ | ❌ | ❌ | ❌ | ❌ |
| <del>gt_B</del> | ❌ | ❌ | ❌ | ❌ | ✅ |
| <del>eq_B</del> | ❌ | ❌ | ❌ | ✅ | ❌ |
| [oo](#oo) | ❌ | ❌ | ✅ | ❌ | ❌ |
| <del>eq_A</del> | ❌ | ✅ | ❌ | ❌ | ❌ |
| <del>lt_a</del> | ✅ | ❌ | ❌ | ❌ | ❌ |
| <del>ge_B</del> | ❌ | ❌ | ❌ | ✅ | ✅ |
| [bg](#bg) | ❌ | ❌ | ✅ | ❌ | ✅ |
| [oc](#oc) |  ❌ | ❌ | ✅ | ✅ | ❌ |
| [fg](#fg) | ❌ | ✅ | ❌ | ❌ | ✅ |
| [ei](#ei) | ❌ | ✅ | ❌ | ✅ | ❌ |
| [co](#co) | ❌ | ✅ | ✅ | ❌ | ❌ |
| [ncc](#ncc) |  ✅ | ❌ | ❌ | ❌ | ✅ |
| [sl](#sl) | ✅ | ❌ | ❌ | ✅ | ❌ |
| [bl](#bl) | ✅ | ❌ | ✅ | ❌ | ❌ |
| <del>le_A</del> | ✅ | ✅ | ❌ | ❌ | ❌ |
| <del>gt_A</del> | ❌ | ❌ | ✅ | ✅ | ✅ |
| [nbl](#nbl) | ❌ | ✅ | ❌ | ✅ | ✅ |
| [nsl](#nsl) | ❌ | ✅ | ✅ | ❌ | ✅ |
| [cc](#cc) |  ❌ | ✅ | ✅ | ✅ | ❌ |
| [nco](#nco) | ✅ | ❌ | ❌ | ✅ | ✅ |
| [nei](#nei) | ✅ | ❌ | ✅ | ❌ | ✅ |
| [nfg](#nfg) | ✅ | ❌ | ✅ | ✅ | ❌ |
| [noc](#noc) |  ✅ | ✅ | ❌ | ❌ | ✅ |
| [nbg](#nbg) | ✅ | ✅ | ❌ | ✅ | ❌ |
| <del>lt_B</del> | ✅ | ✅ | ✅ | ❌ | ❌ |
| <del>ge_A</del> | ❌ | ✅ | ✅ | ✅ | ✅ |
| <del>so_A</del> | ✅ | ❌ | ✅ | ✅ | ✅ |
| [noo](#noo) | ✅ | ✅ | ❌ | ✅ | ✅ |
| <del>so_B</del> | ✅ | ✅ | ✅ | ❌ | ✅ |
| <del>le_B</del> | ✅ | ✅ | ✅ | ✅ | ❌ |
| <del>true</del> | ✅ | ✅ | ✅ | ✅ | ✅ |

## cc
the most intuitive interval
## co
the most used interval in programming
## oc
## oo
## ncc
## nco
## noc
## noo

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
--8<-- "./docs/specification/functions/relations.yaml"
```
</details>

[boolean functions]: boolean.md
