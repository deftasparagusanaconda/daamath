# specification

daamath was originally born in python, where i started implementing the hyperoperations, the trig functions, the boolean gates, etc etc. i faced a bit of friction porting it to C, and i realized that maintaining a language-agnostic specification will be the healthiest direction. so here we are

daamath tries to be simple, regarding separation of concerns. we have a few collections of [functions](), 

# vision

daamath is cross-language and will try to unify things as much as possible. `sum` is presented as variadic addition. `max` is treated as a special case of the generalized mean. stuff like that.

# domains and datatypes

daamath overloads operators to work for datatypes like uint, int, float, double, double complex, etc etc. but javascript has no complex type. python has no uint type. in python, the logic operators are overloaded to support sets, but other languages dont have sets. it is not practical to restrict daamath to only int and float, for example. 

instead, we define operators over domains. daamath maintains the following domains:  
𝔹 : [booleans](https://en.wikipedia.org/wiki/Boolean_algebra)  
ℕ₀: [natural numbers](https://en.wikipedia.org/wiki/Natural_number)  
ℤ : [integers](https://en.wikipedia.org/wiki/Integer)  
ℝ : [real numbers](https://en.wikipedia.org/wiki/Real_number)  
ℂ : [complex numbers](https://en.wikipedia.org/wiki/Complex_number`)  

the following domains are likely useful but would extend daamath beyond practical scope:  
ℚ : [rational numbers](https://en.wikipedia.org/wiki/Rational_number)  
𝕀 : [imaginary numbers](https://en.wikipedia.org/wiki/Imaginary_number)  
ℍ : [quaternions](https://en.wikipedia.org/wiki/Quaternion)  
𝕆 : [octonions](https://en.wikipedia.org/wiki/Octonions)  
[sets](https://en.wikipedia.org/wiki/Set_(mathematics)), [vectors](https://en.wikipedia.org/wiki/Vector_(mathematics_and_physics)), [matrices](https://en.wikipedia.org/wiki/Matrix_(mathematics)), [tensors](https://en.wikipedia.org/wiki/Tensor), [split-complex numbers](https://en.wikipedia.org/wiki/Split-complex_number), [dual numbers](https://en.wikipedia.org/wiki/Dual_number), [clifford algebrae](https://en.wikipedia.org/wiki/Clifford_algebra), …

this way, we are not bound by the datatypes defined by programming languages. instead we define the behaviour of an operator over a domain, and we implement that as accurately as possible in the language. 

thus an operator like `add(a, b)` will not be overloaded with `add_int`, `add_float`, `add_complex` because it would mean you assume the int is ℤ domain, float is ℝ domain, complex is ℂ domain. datatypes only define datatype, not domain type.
instead, it will be overloaded with `addB`, `addN0`, `addZ`, `addR`. each of these then separately implements its own behaviour on appropriate datatypes. finally, `add(a, b)` will be a convenience layer that assumes the domain of a datatype, and then dispatches a function in the correct domain for it.

this allows us to perform integer arithmetic with floats using `addZ(2.0, 3.0) → 5.0` for example. 

this architecture quickly blows up. say we have 9 arithmetic operators, 4 domains, and 4 datatypes. we would have 9 * 4 * 4 = 144 functions just for arithmetic. this is quite ludicrous. im not sure whats the next step to take for this yet.

# mutability

i hate mutating behaviour. daamath will avoid mutation as much as possible. for example, `succ(a)` will be `return 1 + a` instead of `return ++a`. the former leaves the variable intact. the latter mutates the variable.

# etc etc

the specifiation is language-agnostic but still attempts to be as programming-language-friendly as possible. for example, we cant define constants like `2_BY_PI` because languages typically dont allow variable names to start with a digit.
