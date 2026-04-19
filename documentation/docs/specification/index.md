# specification

daamath was originally born in python, where i started implementing the hyperoperations, the trig functions, the boolean gates, etc etc. i faced a bit of friction porting it to C, and i realized that maintaining a language-agnostic specification will be the healthiest direction. so here we are

daamath tries to be simple, regarding separation of concerns. we have a few collections of [functions], [strings], [constants]. we also maintain a special [context] struct. it defines its own [exceptions], and under all this, it has a special underground idea of [domains], which are separate from [datatypes]

# vision

daamath is a language-agnostic math library specification that attempts to be portable across multiple languages, and tries to introduce a programmer to as much mathematics as they want to get deep in. the documentation should teach them enough to get code done, while also teaching them new perspectives on math. 

daamath should not be worried about performance, and should be worried about computational correctness first, always. if someone nudges me to improve the performance, i will. but it doesnt seem to be a necessity as of now.

when designing the specification, implementation should always be considered in the most low level implementation (often the C language. if your design works cleanly in C, it has shed all unnecessary weight. the implementation is thus trivial in higher level languages, and the design becomes so much clearer because C forced you to shed all the unnecessary features that the design wouldve required, which would not be available in lower languages.)

# domains and datatypes

daamath overloads operators to work for datatypes like uint, int, float, double, double complex, etc etc. but javascript has no complex type. python has no uint type. in python, the logic operators are overloaded to support sets, but other languages dont have sets. it is not practical to restrict daamath to only int and float, for example. 

instead, we define operators over domains. daamath maintains the following domains:  
𝔹 : [booleans](https://en.wikipedia.org/wiki/Boolean_algebra)  
ℕ₀: [natural numbers](https://en.wikipedia.org/wiki/Natural_number)  
ℤ : [integers](https://en.wikipedia.org/wiki/Integer)  
ℝ : [real numbers](https://en.wikipedia.org/wiki/Real_number)  
ℂ : [complex numbers](https://en.wikipedia.org/wiki/Complex_number`)  

booleans are special in that they do NOT participate in arithmetic. they are not treated as ℤ₂ (integers modulo 2. {0, 1}). this prevent behaviour like `True + 1 = 2` in python.

the following domains are likely useful but would extend daamath beyond practical scope:  
ℤ₂: [integers modulo 2](https://en.wikipedia.org/wiki/Modular_arithmetic)
ℚ : [rational numbers](https://en.wikipedia.org/wiki/Rational_number)  
𝕀 : [imaginary numbers](https://en.wikipedia.org/wiki/Imaginary_number)  
ℍ : [quaternions](https://en.wikipedia.org/wiki/Quaternion)  
𝕆 : [octonions](https://en.wikipedia.org/wiki/Octonions)  
[sets](https://en.wikipedia.org/wiki/Set_(mathematics)), [vectors](https://en.wikipedia.org/wiki/Vector_(mathematics_and_physics)), [matrices](https://en.wikipedia.org/wiki/Matrix_(mathematics)), [tensors](https://en.wikipedia.org/wiki/Tensor), [split-complex numbers](https://en.wikipedia.org/wiki/Split-complex_number), [dual numbers](https://en.wikipedia.org/wiki/Dual_number), [clifford algebrae](https://en.wikipedia.org/wiki/Clifford_algebra), …

this way, we are not bound by the datatypes defined by programming languages. instead we define the behaviour of an operator over a domain, and we implement that as accurately as possible in the language. 

thus an operator like `add(a, b)` will not be overloaded with `add_int`, `add_float`, `add_complex` because it would mean you assume the int is ℤ domain, float is ℝ domain, complex is ℂ domain. datatypes only define datatype, not domain type.
instead, it will be overloaded with `addB`, `addN0`, `addZ`, `addR`. each of these then separately implements its own behaviour on appropriate datatypes. finally, `add(a, b)` will be a convenience layer that assumes the domain of a datatype, and then dispatches a function in the correct domain for it.

this allows us to perform integer arithmetic with floats using `addZ(2.0, 3.0) → 5.0` for example. 

this architecture quickly blows up. say we have 9 arithmetic operators, 4 domains, and 4 datatypes. we would have 9 * 4 * 4 = 144 functions just for arithmetic. this is quite ludicrous. instead, we have one function overloaded for each datatype. inside the function, we special-case/          

also, the architecture also allows us to cleanly implement modular arithmetic as a separate domain. the downside is that for each new domain we support, we have to create a new set of operators for that domain. im not sure how to implement all possible modular arithmetic domains of n = 1, 2, 3, 4, etc etc. it would be foolish to have `add_Z2`, `add_Z3`, `add_Z4`. parameterizing a domain is not trivial work. `add_Zn(a, b, mod)` parameterizes the mod but it breaks the 2-arity of the hyperoperations. im not sure whats the next step to take. how. do. we. parameterize. domains???

# scope

concerning the threshold at which daamath starts pruning functions, daamath should keep a consistent vision: prune degenerate functions that are replaceable by a simple single atomic expression. like the boolean gate `fst(a, b)` can just be written as `a`. `always_true(a, b)` can just be `TRUE`. yknow?

# contributing

when writing the specification, .yaml files are very welcome and encouraged

[functions]: functions/index.md
[constants]: constants.md
[strings]: strings.md
[context]: context.md
