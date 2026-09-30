# datatypes

in math, we work with various things, and we represent these things via symbols, definitions, and such. but, to represent them in a computer, we store them compactly using datatypes. for example, we represent the number 2 as a character $2$ but in a computer, we would store it as `0b00000010 : int8` which means "the binary digits `00000010` with datatype `int8`"

| value | representation
| - | - |
| $2$ | `0x02 : int8` |
| $2$ | `0x02 : uint8` |
| $2$ | `0x40000000 : binary32` |
| $-2$ | 

a datatype is a way to represent unique things that have some semantic daamath does not care about the bit layout. 

a datatype is a representation of a number, an object, an idea, et cetera. in a binary computer, they are usually stored as bits, and two datatypes representing two different things can have the same bits. in that case, the only distinction between the two values is the type that the language assigns to the bits. the type is remembered by the PL's typing system. an example is: 2 = `0x00000002 : int` = `0x00000000 : uint`

[abstract structure]: https://en.wikipedia.org/wiki/Abstract_structure
[IEEE 754]: https://en.wikipedia.org/wiki/IEEE_754

<!--if we have bigints, we should also have bigfloats. bigints have dynamic precision. bigfloat should also have dynamic precision. heres what i envision: bigints can represent any integer. bigfloat should be able to represent any rational number. *do not include infinities or NaNs into it*-->
