# binary relations

when a binary relation `rel(a, b)` is defined on a carrier set, we can compose `rel(a, b)` and `rel(b, a)` using the [boolean functions][boolean] to get many useful functions. we shall use the common partial ordering relation ≤ (less than or equal to) to name these composed functions, although the binary relation can be anything: an equivalence relation, a partial ordering, a pre-order, et cetera.

| definition | ∥ | < | > | = | name | description |
| -:| - | - | - | - | - | - |
| [false]\(rel(a, b), rel(b, a)) | ❌ | ❌ | ❌ | ❌ | -- | degenerate always-false function |
|   [and]\(rel(a, b), rel(b, a)) | ❌ | ❌ | ❌ | ✅ | [eq](#eq) | a is equal to b |
|  [ncon]\(rel(a, b), rel(b, a)) | ❌ | ❌ | ✅ | ❌ | [gt](#gt) | a is strictly greater than b |
|  [nimp]\(rel(a, b), rel(b, a)) | ❌ | ✅ | ❌ | ❌ | [lt](#lt) | a is strictly lesser than b |
|   [nor]\(rel(a, b), rel(b, a)) | ✅ | ❌ | ❌ | ❌ | [nc](#nc) | a is not comparable to b |
|   [snd]\(rel(a, b), rel(b, a)) | ❌ | ❌ | ✅ | ✅ | [ge](#ge) | a ≥ b. this function is degenerate because it is the same as rel(b, a) |
|   [fst]\(rel(a, b), rel(b, a)) | ❌ | ✅ | ❌ | ✅ | [le](#le) | a ≤ b. this function is degenerate because it is the same as rel(a, b) |
|   [xor]\(rel(a, b), rel(b, a)) | ❌ | ✅ | ✅ | ❌ | [so](#so) | a is strictly ordered with b |
|  [nxor]\(rel(a, b), rel(b, a)) | ✅ | ❌ | ❌ | ✅ | [ns](#ns) | a is not strictly ordered with b |
|  [nfst]\(rel(a, b), rel(b, a)) | ✅ | ❌ | ✅ | ❌ | [nb](#nb) | a is not below b. this function is degenerate because it is the same as not(rel(a, b)) |
|  [nsnd]\(rel(a, b), rel(b, a)) | ✅ | ✅ | ❌ | ❌ | [na](#na) | a is not above b. this function is degenerate because it is the same as not(rel(b, a)) |
|    [or]\(rel(a, b), rel(b, a)) | ❌ | ✅ | ✅ | ✅ | [cp](#cp) | a is comparable to b |
|   [imp]\(rel(a, b), rel(b, a)) | ✅ | ❌ | ✅ | ✅ | [nl](#nl) | a is not strictly lesser than b |
|   [con]\(rel(a, b), rel(b, a)) | ✅ | ✅ | ❌ | ✅ | [ng](#ng) | a is not strictly greater than b |
|  [nand]\(rel(a, b), rel(b, a)) | ✅ | ✅ | ✅ | ❌ | [ne](#ne) | a is not equal to b |
|  [true]\(rel(a, b), rel(b, a)) | ✅ | ✅ | ✅ | ✅ | -- | degenerate always-true function |

you may also notice these are the same degenerates as the [boolean functions][boolean]; but though they are degenerate, daamath still includes them because `ge(a, b)` & `le(a, b)` may be useful aliases for `rel(a, b)` & `rel(b, a)`. similarly with `nb(a, b)` & `na(a, b)` for `not(rel(a, b))` & `not(rel(b, a))`.

# total order

when `rel(a, b)` is a total order, cp is always true; so the 16 functions are reduced down to 8. we may present these visually using the one-dimensional nature of a totally ordered set. we have three partitions of the carrier set:

| x < A | x = A | x > A | general function | toset equivalent |
| - | - | - | - | - | 
| ❌ | ❌ | ❌ | [nc](#nc) | [false] |
| ❌ | ❌ | ✅ | [nb](#nb) | [gt](#gt) | 
| ❌ | ✅ | ❌ | [ns](#ns) | [eq](#eq) | 
| ✅ | ❌ | ❌ | [na](#na) | [lt](#lt) |
| ❌ | ✅ | ✅ | [nl](#nl) | [ge](#ge) | 
| ✅ | ❌ | ✅ | [ne](#ne) | [so](#so) | 
| ✅ | ✅ | ❌ | [ng](#ng) | [le](#le) | 
| ✅ | ✅ | ✅ | [cp](#cp) | [true] | 

## w.r.t. two elements

with respect to two elements A and B, we have five partitions of the carrier set:

| x < A | x = A | A < x < B | x = B | x > B | name | description |
| - | - | - | - | - | - | - |
| ❌ | ❌ | ❌ | ❌ | ❌ | <del>false</del> |
| ❌ | ❌ | ❌ | ❌ | ✅ | <del>gt_B</del> |
| ❌ | ❌ | ❌ | ✅ | ❌ | <del>eq_B</del> |
| ❌ | ❌ | ✅ | ❌ | ❌ | [oo](#oo) | in open-open interval (A, B) |
| ❌ | ✅ | ❌ | ❌ | ❌ | <del>eq_A</del> |
| ✅ | ❌ | ❌ | ❌ | ❌ | <del>lt_a</del> |
| ❌ | ❌ | ❌ | ✅ | ✅ | <del>ge_B</del> |
| ❌ | ❌ | ✅ | ❌ | ✅ | ? |
| ❌ | ❌ | ✅ | ✅ | ❌ | [oc](#oc) | in open-closed interval (A, B] |  
| ❌ | ✅ | ❌ | ❌ | ✅ | ? |
| ❌ | ✅ | ❌ | ✅ | ❌ | ? |
| ❌ | ✅ | ✅ | ❌ | ❌ | [co](#co) | in closed-open interval [A, B) | 
| ✅ | ❌ | ❌ | ❌ | ✅ | [ncc](#ncc) | not(cc) |
| ✅ | ❌ | ❌ | ✅ | ❌ | ? |
| ✅ | ❌ | ✅ | ❌ | ❌ | ? |
| ✅ | ✅ | ❌ | ❌ | ❌ | <del>le_A</del> |
| ❌ | ❌ | ✅ | ✅ | ✅ | <del>gt_A</del> |
| ❌ | ✅ | ❌ | ✅ | ✅ | ? |
| ❌ | ✅ | ✅ | ❌ | ✅ | ? |
| ❌ | ✅ | ✅ | ✅ | ❌ | [cc](#cc) | in closed-closed interval \[A, B\] | 
| ✅ | ❌ | ❌ | ✅ | ✅ | [nco](#nco) | not(co) |
| ✅ | ❌ | ✅ | ❌ | ✅ | ? |
| ✅ | ❌ | ✅ | ✅ | ❌ | ? |
| ✅ | ✅ | ❌ | ❌ | ✅ | [noc](#noc) | not(oc) | 
| ✅ | ✅ | ❌ | ✅ | ❌ | ? |
| ✅ | ✅ | ✅ | ❌ | ❌ | <del>lt_B</del> |
| ❌ | ✅ | ✅ | ✅ | ✅ | <del>ge_A</del> |
| ✅ | ❌ | ✅ | ✅ | ✅ | <del>so_A</del> |
| ✅ | ✅ | ❌ | ✅ | ✅ | [noo](#noo) | not(oo) |
| ✅ | ✅ | ✅ | ❌ | ✅ | <del>so_B</del> |
| ✅ | ✅ | ✅ | ✅ | ❌ | <del>le_B</del> |
| ✅ | ✅ | ✅ | ✅ | ✅ | <del>true</del> |

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

[boolean functions]: boolean.md
