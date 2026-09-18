# datatypes

a datatype is an [abstract structure] on an abstract carrier set which specifies how elements in the carrier behave. it is analogous to an interface

a realization is a datatype with a concrete carrier set. it is analogous to a class. two realizations are isomorphic if they have the same structure/datatype

a value is an element of the carrier set. it is analogous to an instance of a class.

daamath defines integers up to 128 bits, because we we require them to store binary128 approximations of constants.

# uint

a finite subset of the unsigned integers {0, 1, 2, …}. 

# int

a finite subset of the unsigned integers {0, 1, 2, …}. 

# [IEEE 754]

## binary32

it is the second-most common floating point format

## binary64

it is the most common floating point format

## binary128



## decimal64

## decimal128

# yaml

here is a yaml file, usable for generating code for an implementation
<details><summary>yaml</summary>
```yaml
--8<-- "./docs/specification/sets/datatypes.yaml"
```
</details>

[abstract structure]: https://en.wikipedia.org/wiki/Abstract_structure
[IEEE 754]: https://en.wikipedia.org/wiki/IEEE_754

if we have bigints, we should also have bigfloats. bigints have dynamic precision. bigfloat should also have dynamic precision. heres what i envision: bigints can represent any integer. bigfloat should be able to represent any rational number. *do not include infinities or NaNs into it*
