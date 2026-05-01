# order

once an order is defined on a domain, we can start to define some useful functions

# partially ordered domains (posets)

for posets, we can derive a very general set of operations. first, let `A` & `B` be the predicates `a ≤ b` & `b ≤ a` respectively. then we can combine these two predicates with any of the 16 possible binary boolean gates (ordered by hamming weight):

| definition | ∥ | < | > | = | name | description |
| -:| - | - | - | - | - | - |
| false(A, B) | ❌ | ❌ | ❌ | ❌ | -- | degenerate always-false function |
|   [nor]\(A, B) | ✅ | ❌ | ❌ | ❌ | nc | not comparable |
|  [nimp]\(A, B) | ❌ | ✅ | ❌ | ❌ | lt | a < b strictly |
|  [ncon]\(A, B) | ❌ | ❌ | ✅ | ❌ | gt | a > b strictly |
|   [and]\(A, B) | ❌ | ❌ | ❌ | ✅ | eq | a = b |
|   fst(A, B) | ❌ | ✅ | ❌ | ✅ | le | a ≤ b. this function is degenerate because it loses information |
|   snd(A, B) | ❌ | ❌ | ✅ | ✅ | ge | a ≥ b. this function is degenerate because it loses information |
|   [xor]\(A, B) | ❌ | ✅ | ✅ | ❌ | so | strictly ordered. either < or >. not equal, but comparable |
|  [nxor]\(A, B) | ✅ | ❌ | ❌ | ✅ | ns | not strictly ordered. either = or incomparable. neither < nor > |
|  nsnd(A, B) | ✅ | ✅ | ❌ | ❌ | na | a is not above b. this function is degenerate because it loses information |
|  nfst(A, B) | ✅ | ❌ | ✅ | ❌ | nb | a is not below b. this function is degenerate because it loses information |
|  [nand]\(A, B) | ✅ | ✅ | ✅ | ❌ | ne | not (a = b) (note: doesnt guarantee comparability) |
|   [con]\(A, B) | ✅ | ✅ | ❌ | ✅ | ng | not (a > b strictly) (note: doesnt guarantee comparability) |
|   [imp]\(A, B) | ✅ | ❌ | ✅ | ✅ | nl | not (a < b strictly) (note: doesnt guarantee comparability) |
|    [or]\(A, B) | ❌ | ✅ | ✅ | ✅ | cp | comparable |
|  true(A, B) | ✅ | ✅ | ✅ | ✅ | -- | degenerate always-true function |

(this is derived from the boolean gates defined in the [logic] function set)

now notice that in a total ordering like the real number line, two elements will always be comparable. so all the functions with the `∥` column as ✅ will be left out. this leaves us with `lt`, `gt`, `eq`, `le`, `ge`, `so`, `cp`. `cp` will be degenerate for a total order because we know two elements are always comparable so `cp` will always return `true`. furthermore, notice that `ne` did not get included. this points to a deeper realization: what we think of as "not equal" on the number line is actually "strictly ordered" in order theory. thus we have three inverse pairs: `lt` & `ge`, `gt` & `le`, `eq` & `so`. these are exactly the same six operators we shall derive in the next section.

# totally ordered domains

on a totally ordered domain, we need not worry about incomparability. this allows us to simplify things greatly.

with respect to one element A, we have three partitions of the domain:

| < A | A | A < | name | description | 
| - | - | - | - | - |
| ❌ | ❌ | ❌ | <del>false</del> | degenerate always-false function | 
| ❌ | ❌ | ✅ | [gt](#gt) | greater than | 
| ❌ | ✅ | ❌ | [eq](#eq) | equal to | 
| ❌ | ✅ | ✅ | [ge](#ge) | greater than or equal to | 
| ✅ | ❌ | ❌ | [lt](#lt) | less than | 
| ✅ | ❌ | ✅ | [so](#so) | strictly ordered (either less than or greater than) | 
| ✅ | ✅ | ❌ | [le](#le) | less than or equal to | 
| ✅ | ✅ | ✅ | <del>false</del> | degenerate always-true function |

functions that involve more than one element can be composed of any of these, but for convenience, daamath provides the following:

with respect to two elements A and B, we have five partitions of the domain:

| < A | A | A < & < B | B | B < | name |
| - | - | - | - | - | - | 
| ❌ | ❌ | ❌ | ❌ | ❌ | <del>false</del> |
| ❌ | ❌ | ❌ | ❌ | ✅ | <del>gt_B</del> |
| ❌ | ❌ | ❌ | ✅ | ❌ | <del>eq_B</del> |
| ❌ | ❌ | ❌ | ✅ | ✅ | <del>ge_B</del> |
| ❌ | ❌ | ✅ | ❌ | ❌ | [oo](#oo) |
| ❌ | ❌ | ✅ | ❌ | ✅ | ? |
| ❌ | ❌ | ✅ | ✅ | ❌ | [oc](#oc) |
| ❌ | ❌ | ✅ | ✅ | ✅ | <del>gt_A</del> |
| ❌ | ✅ | ❌ | ❌ | ❌ | <del>eq_A</del> |
| ❌ | ✅ | ❌ | ❌ | ✅ | ? |
| ❌ | ✅ | ❌ | ✅ | ❌ | ? |
| ❌ | ✅ | ❌ | ✅ | ✅ | ? |
| ❌ | ✅ | ✅ | ❌ | ❌ | [co](#co) |
| ❌ | ✅ | ✅ | ❌ | ✅ | ? |
| ❌ | ✅ | ✅ | ✅ | ❌ | [cc](#cc) |
| ❌ | ✅ | ✅ | ✅ | ✅ | <del>ge_A</del> |
| ✅ | ❌ | ❌ | ❌ | ❌ | <del>lt_a</del> |
| ✅ | ❌ | ❌ | ❌ | ✅ | [ncc](#ncc) |
| ✅ | ❌ | ❌ | ✅ | ❌ | ? |
| ✅ | ❌ | ❌ | ✅ | ✅ | [nco](#nco) |
| ✅ | ❌ | ✅ | ❌ | ❌ | ? |
| ✅ | ❌ | ✅ | ❌ | ✅ | ? |
| ✅ | ❌ | ✅ | ✅ | ❌ | ? |
| ✅ | ❌ | ✅ | ✅ | ✅ | <del>so_A</del> |
| ✅ | ✅ | ❌ | ❌ | ❌ | <del>le_A</del> |
| ✅ | ✅ | ❌ | ❌ | ✅ | [noc](#noc) |
| ✅ | ✅ | ❌ | ✅ | ❌ | ? |
| ✅ | ✅ | ❌ | ✅ | ✅ | [noo](#noo) |
| ✅ | ✅ | ✅ | ❌ | ❌ | <del>lt_B</del> |
| ✅ | ✅ | ✅ | ❌ | ✅ | <del>so_B</del> |
| ✅ | ✅ | ✅ | ✅ | ❌ | <del>le_B</del> |
| ✅ | ✅ | ✅ | ✅ | ✅ | <del>true</del> |
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

[logic]: logic.md
