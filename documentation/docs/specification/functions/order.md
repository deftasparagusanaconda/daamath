# order

once an ordering is defined on a domain, we can start to define some useful functions

with respect to one element A, we have three partitions of the domain:

| < A | A | A < | name |
| - | - | - | - |
| F | F | F | <del>false</del> |
| F | F | T | [gt](#gt) |
| F | T | F | [eq](#eq) |
| F | T | T | [ge](#ge) |
| T | F | F | [lt](#lt) |
| T | F | T | [ne](#ne) |
| T | T | F | [le](#le) |
| T | T | T | <del>false</del> |

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
| T | F | T | T | T | <del>ne_A</del> |
| T | T | F | F | F | <del>le_A</del> |
| T | T | F | F | T | [noc](#noc) |
| T | T | F | T | F | ? |
| T | T | F | T | T | [noo](#noo) |
| T | T | T | F | F | <del>lt_B</del> |
| T | T | T | F | T | <del>ne_B</del> |
| T | T | T | T | F | <del>le_B</del> |
| T | T | T | T | T | <del>true</del> |

## API implementation

##### lt(a, b):
	less than
	a < b
##### le(a, b):
	less than or equal to
	a ≤ b
##### eq(a, b):
	equal
	a = b
##### ne(a, b):
	not equal
	a ≠ b
##### ge(a, b):
	greater than or equal to
	a > b
##### gt(a, b):
	greater than
	a ≥ b
##### oo(x, a, b):
	in open interval
	x ∈ (a, b)
##### oc(x, a, b):
	in left-open interval
	x ∈ (a, b]
##### co(x, a, b):
	in right-open interval
	x ∈ [a, b)
##### cc(x, a, b):
	in closed interval
	x ∈ [a, b]
