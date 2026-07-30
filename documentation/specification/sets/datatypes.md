# datatypes

a datatype is an [abstract structure] on an abstract carrier set which specifies how elements in the carrier behave. it is analogous to an interface

a realization is a datatype with a concrete carrier set. it is analogous to a class. two realizations are isomorphic if they have the same structure/datatype

a value is an element of the carrier set. it is analogous to an instance of a class.

daamath defines integers up to 128 bits, because we we require them to store bin128 approximations of constants.

# uint

a finite subset of the unsigned integers {0, 1, 2, …}. 

# int

# binary

# decimal

# yaml

here is a yaml file, usable for generating code for an implementation
<details><summary>yaml</summary>
```yaml
--8<-- "./docs/specification/sets/datatypes.yaml"
```
</details>

[abstract structure]: https://en.wikipedia.org/wiki/Abstract_structure
