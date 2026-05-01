# variadic

daamath formalizes the extension of a function into variadic inputs. the variadic extension F(X) of a function f(x) is a function (closed on a certain domain) that takes multiple inputs in a structure and collapses them into a smaller output. for this to be possible, f(x) must produce lesser outputs than there are inputs, and the output must be operable with the remaining inputs (that entails, usually, f(x) being the same kind as x. if \[1,2,3\] was suddenly collapsed to [True, 3], then we cannot collapse it further. that is invalid).

usually, this is a closed associative binary (and often commutative) function, whose variadic extension takes in a sequence of inputs and collapses from the left (left-fold, similar to python's `functools.reduce`)

<!--daamath defines a variadically extensible function as a function that is fully commutative (the output is the same regardless of which permutation of inputs is passed to it) and associative. these are a superset of the more specialized meet/join functions from order theory. daamath does not overload 

these are functions that can take a structured arbitrary count of inputs. they usually but not necessarily collapse the inputs down into one output. they are composed of some primitive function that collapses one or more inputs into one output. the primitive function is applied recursively on an arbitrary count of inputs 

in general, for the primitive operation `op`, its variadic version `OP` can take an unordered set of inputs iff `op` is fully commutative (the output is the same regardless of which permutation of inputs is passed to it) and associative. if it is not, then the primitive has many possible definitions (left-fold? right-fold? reversed? etc etc yknow)

as a specialization of these, certain 
-->
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

DAA! remember again (2026-04-30), the primitive functions take arguments flatly. but the variadic versions take one iterable as input (probably a sequence/1D vector). this should decide if max should be the variadic one (takes a vector as input) or the binary one (takes two arguments as input)

2026-04-30 0901 daa, why not instead make a function that takes in a vector and an operator, and applies the operator on the vector to collapse it?  
because some of them can get specialized routines
but couldnt you implement those special routines in the function? if it detects that dm.max was taken in, it would use a special routine for that.  
ah.. interesting. then i *do* want to let users write variadic(max, \[1,2,3\]) instead of vmax(\[1,2,3\]). because then they can turn any binary primitive into a variadic version. ahh! thank you by the way. i also now realized that only functions that preserve type are valid for this. 
