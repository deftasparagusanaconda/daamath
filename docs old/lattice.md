# lattice

on a lattice, every element has a meet & a join.

under the natural order, they are [min](#min) & [max](#max)
under divisibility, they are [gcd](#gcd) & [lcm](#lcm)

as such daamath has a slightly uncommon take on min & max: they are binary functions, not variadic functions. the same goes with gcd & lcm. their variadic versions are available in [variadic].

# min
# max
# lcm
# gcd

# rant

for the orders, most of them want to share the 14 names that were generated.

the problem is how daamath will present them.

| type | meet | join | 
| - | - | - |
| set | intersection | union |
| boolean | and | or |
| logic | conjunction | disjunction |
| standard order | minimum | maximum |
| divisibility | gcd | lcm |

variadic versions of meet and join behave nicely on lattices, but not so much on general posets

sup/inf (a.k.a glb/lub) shall *not* be defined. these are more general concepts.


{{ yaml_source(page) }}
