# variadic

these are functions that can take a structured arbitrary count of inputs. they usually but not necessarily collapse the inputs down into one output. they are composed of some primitive function that collapses one or more inputs into one output. the primitive function is applied recursively on an arbitrary count of inputs 

in general, for the primitive operation `op`, its variadic version `OP` can take an unordered set of inputs iff `op` is fully commutative (the output is the same regardless of which permutation of inputs is passed to it) and associative. if it is not, then the primitive has many possible definitions (left-fold? right-fold? reversed? etc etc yknow)

#### sum
variadic extension of add
#### prod
variadic extension of mul
#### all
variadic extension of and
#### any
variadic extension of or
#### parityeven
variadic extension of xor
#### parityodd
variadic extension of nxor
#### vmin
variadic extension of min

min is usually presented as its variadic version but it is primitively a binary function
#### vmax
variadic extension of max

max is usually presented as its variadic version but it is primitively a binary function
#### vgcd
variadic extension of gcd

gcd is usually presented as its variadic version but it is primitively a binary function
#### vlcm
variadic extension of lcm

lcm is usually presented as its variadic version but it is primitively a binary function



# notes

these variadic extensions are only valid in certain domains. this is already made clear but just keep in mind that an operator is not intrinsically varidically extensible. it is only extensible in the context of a certain domain.

some functions such as mean, median, mode were not extended because there is no primitive that they can be composed of. so they are not added here. 
