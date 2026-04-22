# datatypes

first, a few definitions:

## datatype

a datatype is a specification for a domain about how its values should be represented. it may not be able to represent all the possible values of the domain (especially with [infinite-domain datatypes](#infinite-domain-datatypes)) but is acceptable enough for approximate computation.

datatypes are parameterized as much as possible, which is how daamath generalizes a lot of existing datatypes.

when daamath works in a certain domain and the value cannot be accurately represented by the datatype, a [FidelityError] occurs. but if a rounding mode is specified for that datatype (through the [context] tree), the value is rounded and an error is not raised.

## value

a value in daamath is a triple: (actual, domain, datatype).  
the actual is the thing we are actually refering to  
the domain is the set of things that the actual belongs to  
the datatype is the representation of the actual (with respect to the domain)  

for example, a value `2` in C would be (2, integers, i32)

# classification

a datatype can be classified based on the following:

## composition

a datatype can either be an atom or a molecule. an element or a compound. a base unit or a derived unit. a leaf node or a branch node. 
a datatype is decomposable if it can be broken down into a composition of multiple datatypes. a datatype is NOT decomposable based on whether its domain is decomposable.

a good example is how int is a primitive datatype, but its domain is decomposable. an integer is just a composition of two natural numbers, related by the inverse of addition (subtraction) and with the equivalence class defined by `a - b = c - d`.

### primitive datatypes

a datatype that cannot be decomposed into other datatypes. it is the foundation for other datatypes.

the uint and the int datatypes are examples of this.

### composed datatypes

these datatypes are composed from other datatypes and can be broken down or decomposed into other composed or primitive datatypes.

the float and complex datatypes are examples of this. a complex is usually two floats. a float is a sequence of bits: the first bit is like a boolean. the second sequence (the exponent) is a shifted integer. the third sequence (the mantissa) is an unsigned integer

in general, any datatype that stores direction (like angle for complex, or sign for real numbers) is a composed datatype.

## domain finiteness

a datatype tries to model a domain. datatypes usually behave starkly differently based on whether the domain they try to model is finite or infinite.

### finite-domain datatypes

a datatype that tries to model a finite domain.

the most famous example is a bool, which has two possible values in the domain: YES/NO or TRUE/FALSE or ON/OFF or etc

some other examples are a ternary, quaternary, integers modulo 2, etc

### infinite-domain datatypes

a datatype that tries to model a domain with an infinite number of elements

# what datatypes does daamath actually recognize?

daamath recognizes datatypes that work with sequences of binary bits, because these are the most common with modern computers. 1s and 0s.

| name  | format                                 | alias | composition | domain                     | example           |
| ----- | -------------------------------------- | ----- | ----------- | -------------------------- | ----------------- |
| truth | truth_states                           | tS    | primitive   | truth (finite)             | t2 is bool        |
| unint | uint_bits                              | uB    | primitive   | NATURALSTART_0 (infinite)  | u8 is [0, 256)    |
| int   | int_sign_bits                          | iX    | primitive   | INTEGERS (infinite)        | i8 is [-128, 128) |
| float | float_radix_sign_exponent_mantissa     | (see below)    | composed    | extended reals (probably)  | f
| cmplx | complex_geometry_component1_component2 | cr8   | composed    | complex (infinite)         | cr128 or something idk lol | 
| posit | idk…                                   | idk…  | idk…        | wheel (infinite) (i think) | i dont really know |

daamath recognizes IEEE 754's impact and provides aliases for the binary formats

| alias | actual |
| - | - |
| b16 | float_2_1_5_10 |
| b32 | float_2_1_8_23 |
| b64 | float_2_1_11_52 |
| b128 | float_2_1_15_112 |
| b256 | float_2_1_19_236 |

(you may notice that datatypes are parameterized. in fact, the naming convention follows daamath's [underscore binding convention])

daamath also creates a new specification for complex numbers: since complex numbers form a vector space with >1 dimensions, we can start representing them in either cartesian or polar coordinates. the lattice formed by the datatype from quantizing these vector spaces are significantly different for cartesian and polar forms. the cost of operations are different in the two as well. hyperoperations of n=1 (addition and subtraction) are cheap with cartesian form but hyperoperatioins of n=2 (multiplication and division) are cheap with polar form. sometimes we may perform n2 hyperops more often than n1 hyperops.

most languages define complex as rectangular (float, float) but daamath also defines polar (int, float). this allows uniform *radial* angular precision, and exponential magnitudinal precision. this is much more suited for certain applications and daamath formalizes that.

# notes

see [here](https://deftasparagusanaconda.github.io/daamath/specification/#scope) why daamath only works with arithmetic up to complex numbers, and no other hypercomplex numbers

# rant

i say whatever i want to say here

datatypes bow down to mathematical domains. the domains do not yield to datatypes. the datatypes yield to the domains. 
i love that realization i made with complex numbers. ive always felt it but it just wasnt convenient enough to work with in programming languages. i dont always want rectangular complex numbers. i want the radial complex plane. 

when daamath might work with vector spaces larger than 2 dimensions, perhaps i shall specify that rectangular is a sequence of scalars, polar is a decomposition of that to scalar and vector, and a recursive polar definition that recursively decomposes a vector until its a sequence of scalars. 


[FidelityError]: https://deftasparagusanaconda.github.io/daamath/specification/errors/#fidelityerror
[context]: context.md
[underscore binding convention]: https://deftasparagusanaconda.github.io/daamath/specification/namespace/#underscore-binding
