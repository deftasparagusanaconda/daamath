# orderings

a domain is simply a set of things. we do not have any idea of how these things are related yet. order theory gives us the tools to define how things in a domain are related to each other.

just like a domain can be represented by an indicator function that takes a thing and returns a boolean, an ordering can be represented by a less-than-or-equal-to indicator function that takes a pair of things (that belong in the domain) and returns a boolean

daamath uses this extensively in the [order] function set

the following orderings are recognized for the domains:

a total ordering over the REAL domain, arranging them in a 1D sequence (the real number line) (and similarly, the same total ordering but for subsets of the REAL domain)
a partial ordering over the INTEGER domain, based on their divisibility

[order]: functions/order.md
