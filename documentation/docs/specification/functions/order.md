# order

once an order is defined on a domain, we can start to define some useful functions

# partially ordered domains (posets)

for posets, we can derive a very general set of operations. first, let `A` & `B` be the predicates `a ≤ b` & `b ≤ a` respectively. then we can combine these two predicates with any of the 16 possible binary boolean gates (ordered by hamming weight):

| definition | ∥ | < | > | = | name | description |
| -:| - | - | - | - | - | - |
| false(A, B) | F | F | F | F | -- | degenerate always-false function |
|   [nor]\(A, B) | T | F | F | F | nc | not comparable |
|  [nimp]\(A, B) | F | T | F | F | lt | a < b strictly |
|  [ncon]\(A, B) | F | F | T | F | gt | a > b strictly |
|   [and]\(A, B) | F | F | F | T | eq | a = b |
|   fst(A, B) | F | T | F | T | le | a ≤ b. this function is degenerate because it loses information |
|   snd(A, B) | F | F | T | T | ge | a ≥ b. this function is degenerate because it loses information |
|   [xor]\(A, B) | F | T | T | F | so | strictly ordered. either < or >. not equal, but comparable |
|  [nxor]\(A, B) | T | F | F | T | ns | not strictly ordered. either = or incomparable. neither < nor > |
|  nsnd(A, B) | T | T | F | F | na | a is not above b. this function is degenerate because it loses information |
|  nfst(A, B) | T | F | T | F | nb | a is not below b. this function is degenerate because it loses information |
|  [nand]\(A, B) | T | T | T | F | ne | not (a = b) (note: doesnt guarantee comparability) |
|   [con]\(A, B) | T | T | F | T | ng | not (a > b strictly) (note: doesnt guarantee comparability) |
|   [imp]\(A, B) | T | F | T | T | nl | not (a < b strictly) (note: doesnt guarantee comparability) |
|    [or]\(A, B) | F | T | T | T | cp | comparable |
|  true(A, B) | T | T | T | T | -- | degenerate always-true function |

(this is derived from the boolean gates defined in the [logic] function set)

now notice that in a total ordering like the real number line, two elements will always be comparable. so all the functions with the `∥` column as T will be left out. this leaves us with `lt`, `gt`, `eq`, `le`, `ge`, `so`, `cp`. `cp` will be degenerate for a total order because we know two elements are always comparable so `cp` will always return `true`. furthermore, notice that `ne` did not get included. this points to a deeper realization: what we think of as "not equal" on the number line is actually "strictly ordered" in order theory. thus we have three inverse pairs: `lt` & `ge`, `gt` & `le`, `eq` & `so`. these are exactly the same six operators we shall derive in the next section.

# totally ordered domains

on a totally ordered domain, we need not worry about incomparability. this allows us to simplify things greatly.

with respect to one element A, we have three partitions of the domain:

| < A | A | A < | name | description | 
| - | - | - | - | - |
| F | F | F | <del>false</del> | degenerate always-false function | 
| F | F | T | [gt](#gt) | greater than | 
| F | T | F | [eq](#eq) | equal to | 
| F | T | T | [ge](#ge) | greater than or equal to | 
| T | F | F | [lt](#lt) | less than | 
| T | F | T | [so](#so) | strictly ordered (either less than or greater than) | 
| T | T | F | [le](#le) | less than or equal to | 
| T | T | T | <del>false</del> | degenerate always-true function |

functions that involve more than one element can be composed of any of these, but for convenience, daamath provides the following:

with respect to two elements A and B, we have five partitions of the domain:

| < A | A | A < & < B | B | B < | name |
| - | - | - | - | - | - | 
| F | F | F | F | F | <del>false</del> |
| F | F | F | F | T | <del>gt_B</del> |
| F | F | F | T | F | <del>eq_B</del> |
| F | F | F | T | T | <del>ge_B</del> |
| F | F | T | F | F | [oo](#oo) |
| F | F | T | F | T | ? |
| F | F | T | T | F | [oc](#oc) |
| F | F | T | T | T | <del>gt_A</del> |
| F | T | F | F | F | <del>eq_A</del> |
| F | T | F | F | T | ? |
| F | T | F | T | F | ? |
| F | T | F | T | T | ? |
| F | T | T | F | F | [co](#co) |
| F | T | T | F | T | ? |
| F | T | T | T | F | [cc](#cc) |
| F | T | T | T | T | <del>ge_A</del> |
| T | F | F | F | F | <del>lt_a</del> |
| T | F | F | F | T | [ncc](#ncc) |
| T | F | F | T | F | ? |
| T | F | F | T | T | [nco](#nco) |
| T | F | T | F | F | ? |
| T | F | T | F | T | ? |
| T | F | T | T | F | ? |
| T | F | T | T | T | <del>so_A</del> |
| T | T | F | F | F | <del>le_A</del> |
| T | T | F | F | T | [noc](#noc) |
| T | T | F | T | F | ? |
| T | T | F | T | T | [noo](#noo) |
| T | T | T | F | F | <del>lt_B</del> |
| T | T | T | F | T | <del>so_B</del> |
| T | T | T | T | F | <del>le_B</del> |
| T | T | T | T | T | <del>true</del> |
<!--
## API implementation

#### lt(a, b):
less than
a < b

=== "python"
	```python
	dm.lt(1, 2)
	# True
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
