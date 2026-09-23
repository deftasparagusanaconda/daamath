# functions

a [function in mathematics](https://en.wikipedia.org/wiki/Function_(mathematics)) is a mapping from a domain to a codomain. it is very well-modelled by a [function in programming](https://en.wikipedia.org/wiki/Function_(computer_programming)), which is a procedure that can take parameters, perform instructions, and return a value. but there are a few differences:

| function in programming | function in mathematics | solution |
| - | - | - |
| can take multiple inputs | can take only one input | consider a tuple of multiple inputs as one single input: the tuple itself |
| can take keyword arguments | can take only one input | disallow keyword arguments, allow only positional arguments | 
| can take optional arguments | always have the same arguments | disallow optional arguments |
| can be non-deterministic or have [side effects](https://en.wikipedia.org/wiki/Side_effect_(computer_science)) | are deterministic, and do not have side effects | functions must always be [pure functions](https://en.wikipedia.org/wiki/Pure_function) |

<!--functions never mutate memory, because they are meant to be mathematical functions, and not procedures (in computer science). for example: `succ` should not be pre-incrementation. `pred` should not be pre-decrementation. variadic functions should not mutate the vector they take in as input.-->

# function families

in an equation, you can always solve for each variable

`sin(semiarea) = ratio` & `asin(ratio) = semiarea`  
`pow(base, degree) = result` & `log(result, base) = degree` & `root(result, degree) = base`  
`quot(dividend, divisor) = quotient` & `rem(dividend, divisor) = remainder` & `fma(divisor, quotient, remainder) = dividend` & `fsd(dividend, remainder, quotient) = divisor`

in short, a function with n inputs and 1 output is involved in an equation of (n + 1) variables. if possible, it should have n other related functions that each solve for individual variables in the equation.

# naming

functions follow common namespace convention. each section is named as if it would be followed by the word "functions". like: "trigonometric ^^functions^^" instead of "trigonometry ^^functions^^" or "relational ^^functions^^" instead of "relation ^^functions^^"

# numerics

daamath gives slight importance to the numeric behaviour of IEEE 754 floats, and gives formulae that are numerically usable. this is most apparent in the [trigonometric](trigonometric) functions

```python
--8<-- "numerics_test.py"
```

# rant

note to self: the arithmetic, trigonometry, logic, and interval function sets are done. quantize and variadic are not done. i hate that they are hard to define or grasp. this is tough

have you tried debugging `log(y/8*(49-1)+1,49)` and wondered 'why is this scaled weirdly?', only to realize after painful eye strain that its not log with base e. there is a second argument giving base=49. 

the problem was that the function changed behaviour depending on arity, and it was hard to read the arity by eye. we should guarantee that a function should always have a certain arity, and that arguments do not change its behaviour radically. for example, we should not overload `atan` as `atan(x)` and `atan(y, x)` = `atan2(y, x)`. as another example, we should not overload `sin` as `sin(x, geometry)` because one argument is changing its behaviour too much.
