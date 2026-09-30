# datatypes

in math, we work with various sets, and elements of those sets. for example, when we do complex analysis, we work with the set of complex numbers, and operations on that set such as addition, multiplication, absolute value, …

in CS, we work with various datatypes, and instances of those datatypes. for example, when we write `0.1 + 0.2` in python, we are using the `float` datatype, and methods on that datatype such as `add`, `mul`, `abs`, …

there are a few differences that we must resolve before we can do math with datatypes:

| sets/elements in math | datatypes/instances in CS | solution |
| - | - | - |
| sets can have infinite unique elements | datatypes can only have finite unique instances | datatypes are finite subsets of sets |
| numbers of same semantic value in different sets are same | instances of same semantic value in different datatypes are different | let datatypes participate in the number tower hierarchy by *explicit* and *exact* conversion |

daamath maintains the following numeric datatypes:

| name | number set | size | precision |
| - | - | - | - |
| [`uint8`<br>`uint16`<br>`uint32`<br>`uint64`](uint) | [$\mathbb N$](https://en.wikipedia.org/wiki/Natural_number) (naturals) | fixed | finite |
| [`int8`<br>`int16`<br>`int32`<br>`int64`](int) | [$\mathbb Z$](https://en.wikipedia.org/wiki/Integer) (integers) | fixed | finite |
| [`bigint`](bigint) | [$\mathbb Z$](https://en.wikipedia.org/wiki/Integer) (integers) | dynamic | exact |
| [`binary32`<br>`binary64`<br>`binary128`](binary) | [$\mathbb Z\left[\dfrac{1}{2}\right]$](https://en.wikipedia.org/wiki/Dyadic_rational) (dyadic rationals) | fixed | finite |
| [`decimal64`<br>`decimal128`](decimal) | $\mathbb Z\left[\dfrac{1}{10}\right]$ (decadic rationals) | fixed | finite |
| [`fraction`](fraction) | [$\mathbb Q$](https://en.wikipedia.org/wiki/Rational_number) (rationals) | dynamic | exact |
| [`complex64`<br>`complex128`<br>`complex256`](complex) | $\mathbb Z\left[\dfrac{1}{2}\right](\mathrm i)$ (dyadic gaussian rationals) | fixed | finite |

daamath also maintains one non-numeric datatype:

| name | model | 
| - | - |
| [`bool`](bool) | [$\mathbb B$](https://en.wikipedia.org/wiki/Boolean_algebra_(structure)) (booleans) 


<!--| `biguint` | [$\mathbb N$](https://en.wikipedia.org/wiki/Natural_number) (naturals) | dynamic | exact |-->
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
