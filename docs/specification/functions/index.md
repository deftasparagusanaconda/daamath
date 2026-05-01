# functions

a [function in mathematics](https://en.wikipedia.org/wiki/Function_(mathematics)) is a mapping from a domain to a codomain. it is very well-modelled by a [function in computer science](https://en.wikipedia.org/wiki/Function_(computer_programming)), which is a procedure that performs instructions, and can return a value. in daamath, a mathematical function is implemented as a programming procedure.

"but daa, a procedure that models a function can take multiple inputs, but the function is supposed to take only 1 input. how is this possible?"  
the procedure is still a function, but it is implied that the input is a tuple (or some other structure) of inputs. thus the function takes one argument, and that one argument is the tuple. when we say `add(a, b)`, `add` doesnt take two inputs. it is implied to take a tuple `(a, b)` as input  
for a consistent interface across languages, daamath will not allow keyword arguments as is allowed in python syntax. only a tuple of arguments is allowed

daamath maintains collections of [functions](https://en.wikipedia.org/wiki/Function_(computer_programming)) that are called typically as `op(a, b, …)`. they may sometimes be called operators. 

functions in daamath are actually thin wrappers that call the corresponding function definition in dm.context. 

functions will always have a fixed arity (take a certain number of arguments) and will never be overloaded to change behaviour depending on different arities. 

why? 

have you tried debugging `log(y/8*(49-1)+1,49)` and wondered 'why is this scaled weirdly?', only to realize after painful eye strain that its not log with base e. there is a second argument giving base=49. 

the problem was that the function changed behaviour depending on arity, and it was hard to read the arity by eye. we should guarantee that a function should always have a certain arity, and that arguments do not change its behaviour radically. for example, we should not overload `atan` as `atan(x)` and `atan(y, x)` = `atan2(y, x)`. as another example, we should not overload `sin` as `sin(x, geometry)` because one argument is changing its behaviour too much.

# how they relate to domains

before we continue, its important to note that functions are not independent entities. the existence of functions relies on the existence of domains, but not vice versa (not conversely). in category theory, an object can exist without a morphism. but a morphism cannot exist without an object. in graph theory, a node can exist without an edge, but an edge cannot exist without a node. likewise, in daamath, a domain can exist without a function but a function cannot exist without a domain.

so functions are defined for domains, not the other way around

# mutability

functions never mutate memory, because they are meant to be mathematical functions, and not procedures (in computer science). for example: `succ` should not be pre-incrementation. `pred` should not be pre-decrementation. variadic functions should not mutate the vector they take in as input.

# context and function behaviour

daamath maintains a .context object that determines idfk

# function sets

if at all possible, each function should always have all inverses present. examples are:

`sin(semiarea) = ratio` & `asin(ratio) = semiarea`  
`pow(base, degree) = result` & `log(result, base) = degree` & `root(result, degree) = base`  
`quot(dividend, divisor) = quotient` & `rem(dividend, divisor) = remainder` & `fma(divisor, quotient, remainder) = dividend` & `fsd(dividend, remainder, quotient) = divisor`

in short, a function with n inputs and 1 output is involved in an equation of (n + 1) variables. if possible, it should have n other related functions that each solve for individual variables in the equation.

daamath maintains mathematically defined functions, as well as some numerically inclined functions such as from [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754#Recommended_operations)
# rant

note to self: the arithmetic, trigonometry, logic, and interval function sets are done. quantize and variadic are not done. i hate that they are hard to define or grasp. this is tough
