# functions

a [function in mathematics](https://en.wikipedia.org/wiki/Function_(mathematics)) is a mapping from one domain to another domain. a [function in computer science](https://en.wikipedia.org/wiki/Function_(computer_programming)) is a procedure that performs instructions. unfortunately, they share the same name because the latter can mimic the former very well. daamath takes advantage of this by specifying that a mathematical function (simply called a function) must always be implemented as a programming function (simply called a procedure).

"but daa, a procedure that models a function can take multiple inputs, but the function is supposed to take only 1 input. how is this possible?"  
the procedure is still a function, but it is implied that the input is a tuple (or some other structure) of inputs. thus the function takes one argument, and that one argument is the tuple. when we say `add(a, b)`, `add` doesnt take two inputs. it takes a tuple `(a, b)` as input  
for a consistent interface across languages, daamath will not allow keyword arguments as is allowed in python syntax. only a tuple of arguments is allowed

daamath maintains collections of [functions](https://en.wikipedia.org/wiki/Function_(computer_programming)) that are called typically as `op(a, b, …)`. they may sometimes be called operators. 

functions in daamath are actually thin wrappers that call the corresponding function definition in dm.context. 

functions will always have a fixed arity (take a certain number of arguments) and will never be overloaded to change behaviour depending on different warities. why? have you tried debugging `log(y/8*(49-1)+1,49)` and wondered 'why is this scaled weirdly?', only to realize after painful eye strain that its not log with base e. there is a second argument giving base=49. the problem was that the function changed behaviour depending on arity, and it was hard to read the arity by eye. we should guarantee that log always takes two arguments, and that the one-argument version of log (like `ln`, `log2`, `log10`) should always make their base clear. that way, there is no confusion of 'is this `log` taking base or not?' because you can see from the function name directly.

# context and function behaviour

daamath maintains a .context object that determines idfk

# function sets

daamath maintains mathematically defined functions, as well as some numerically inclined functions such as from [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754#Recommended_operations)
# rant

note to self: the arithmetic, trigonometry, logic, and interval function sets are done. quantize and variadic are not done. i hate that they are hard to define or grasp. this is tough
