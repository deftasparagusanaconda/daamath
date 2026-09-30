# datatypes

in math, we work with various sets, and elements of those sets. for example, when we do complex analysis, we work with the set of complex numbers, and operations on that set such as addition, multiplication, absolute value, …

in CS, we work with various datatypes, and instances of those datatypes. for example, when we write `0.1 + 0.2` in python, we are using the `float` datatype, and methods on that datatype such as `add`, `mul`, `abs`, …

there are a few differences that we must resolve before we can do math with datatypes:

| sets/elements in math | datatypes/instances in CS | solution |
| - | - | - |
| sets can have infinite unique elements | datatypes can only have finite unique instances | datatypes are finite subsets of sets |
| numbers of same semantic value in different sets are same | instances of same semantic value in different datatypes are different | let datatypes participate in the number tower hierarchy by *explicit* and *exact* conversion |

daamath maintains the following datatypes:

|

<!--
| value | representation
| - | - |
| $2$ | `0x02 : int8` |
| $2$ | `0x02 : uint8` |
| $2$ | `0x40000000 : binary32` |
| $-2$ | 
-->

a datatype is a way to represent unique things that have some semantic daamath does not care about the bit layout. 

a datatype is a representation of a number, an object, an idea, et cetera. in a binary computer, they are usually stored as bits, and two datatypes representing two different things can have the same bits. in that case, the only distinction between the two values is the type that the language assigns to the bits. the type is remembered by the PL's typing system. an example is: 2 = `0x00000002 : int` = `0x00000000 : uint`

[abstract structure]: https://en.wikipedia.org/wiki/Abstract_structure
[IEEE 754]: https://en.wikipedia.org/wiki/IEEE_754

<!--if we have bigints, we should also have bigfloats. bigints have dynamic precision. bigfloat should also have dynamic precision. heres what i envision: bigints can represent any integer. bigfloat should be able to represent any rational number. *do not include infinities or NaNs into it*-->
