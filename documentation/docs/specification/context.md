in math, even when we write `2 / 3`, we assume many things. we assume we are working with the real numbers. we assume `/` is defined on real numbers. in CS, we assume we want `0 / 0` to raise an error. if the datatype is `int`, programmers assume `2 / 3` to be rounded division. daamath makes all of this explicit by storing variables in a [tree][context.yaml] called the context.

functions look at the context to determine what to do. you can change the context in 3 levels of ascending precedence:

1. global default context
	the function refers daamath's default context (`dm.context`). if no other context is passed to a function, this is what is used.

2. scoped/local/temporary redirection/mutation
	daamath's default context is temporarily changed or replaced for a section of code, and then changed back after the section

3. explicit optional function argument
	a new context instance is passed as the last argument to a function

an example in python:

```python
import daamath as dm

x = 1.0

# level 1: global default context
dm.sin(x)	
# 0.8414709848078965

# level 2: temporary mutation
temp = dm.context.domain
dm.context.domain = dm.INTEGER
dm.sin(x)
# ClosureError: result 0.8414709848078965 is not INTEGER
dm.context.domain = temp

# level 3: optional function argument
my_context = dm.Context(domain = dm.COMPLEX)
dm.sin(x, context = my_context)
# 0.8414709848078965
# note: the result is a float because daamath preserves datatype but the domain was promoted to COMPLEX. 0.8414709848078965 is indeed COMPLEX, just with zero imaginary part.
```

# the yaml

[context.yaml](context.yaml): (click to download)
~~~yaml
{% include-markdown "./context.yaml" %}
~~~

# implementation
the context shall be implemented as a thread-local instance of an instantiable collection of variables (like an [object] in [OOP] languages, a [struct] in [C], ...). it cannot be a loose grouping of variables, because the user has to be able to make a copy of the entire set of variables, to store different contexts. to store a context, we may use any data structure that defines an outline, and each [instance] can store different contexts.

in case a user wants to change multiple related variables at once, we provide helper functions that, say, change the domain of all functions at once

# motivation

`add` could have been overloaded to take an optional mod argument, essentially enabling it to work with modular arithmetic. `div` needed to be able to handle special cases like "what do i do when denominator is zero?" or "both operands are zero!".

# FAQ

"why is there no parameter to change the behaviour when `0/0` happens?"  
`0/0` is considered undefined. but thats only because our domain of discussion is usually the real numbers. in wheel algebra, `0/0` is defined as `BOTTOM`. so it is a fault of the domain, and is thus a `DomainError`. `0^0` is also defined but depends on the domain that you work in.

"why not have a context object for each function?"  
because many functions share a lot of the same parameters, and because different operators working in different domains is unusual in maths. usually we define a domain of discussion, and our operators live in that

"why not make functions take environment parameters directly?"  
because this will congest the function call stack significantly, pollute code by having to overload functions, and it also dissolves the fact that many functions will share many of the same context parameters.

"is the context just a fancy way to pre-store/curry arguments for functions so we dont have to pass them everytime?"
essentially, yes! this is apparent with the trigonometric functions. the geometry of the trig functions could have been passed in the function arguments (e.g. `sin(x, 'elliptic')`), in the function names (e.g. `sin` vs `sinh`) or in the context (e.g. `dm.context.geometry`). but only environment parameters are stored in the context. the context is only concerned with the environment of the math. we do have to assume how much you want to assume. 

# rant

the context is similar to what [IEEE 754] does to define rounding modes for floating point operations. each operation looks at the rounding mode to see what it should be like. most people dont know that you can change the rounding mode of floats. it is also worth noting that floats have their own hardware. so unlike functions in daamath that perform slow lookups on the context in memory, floating point ops can perform fast lookups on variables stored in the same IC. if daamath is significant enough one day, we might have special hardware to speed up the context lookup. for now, the CPU cache is probably the optimal place to store the context. whatever the CPU says.

strangely, since type is always preserved and daamath never assumes a different datatype, even the round function ends up being a float -> float function. which is good because the datatype's precision is preserved, but it breaks the assumption that the int datatype is always for integers. not necessarily. daamath thinks of datatypes and domains completely separately. in lean, the domains are the datatype, essentially. so theres no problem for them. but in practical programming languages, we need to deal with practical datatypes. should daamath allow approximate storage like is done in floats? sometimes a float doesnt represent an integer accurately. should daamath raise an error then? IEEE floats raise the inexacterror flag all the time. what shall daamath do about it? perhaps maintain an inexacterror too? ok so so far we have domain, inexact_error_behaviour, domain_error_behaviour. for each error flag, we should be able to change the behaviour. arithmetic domain should be one of: {NATURAL_X (naturals starting from X), INTEGER, REAL, COMPLEX}. logical domain should be an integer, representing the number of states (default 2). 

ah.. i see i am able to parameterize the domains. this will be a problem. in an enum, some values require an additional parameter to be fully defined. NATURALS_FROM_X, INTEGERS_MODULO_X, ... so how shall i resolve this problem? for integers modulo X, a function will want to use the `mod` (alias for floor remainder) operator on the 

im tired boss. awful tired

[namespace]: https://
[object]: https://en.wikipedia.org/wiki/Object_(computer_science)
[C]: https://en.wikipedia.org/wiki/C_(programming_language)
[OOP]: https://en.wikipedia.org/wiki/Object-oriented_programming
[mutable]: https://
[IEEE 754]: https://en.wikipedia.org/wiki/IEEE_754
[struct]: https://en.wikipedia.org/wiki/Struct_(C_programming_language)
[instance]: https://en.wikipedia.org/wiki/Instance_(computer_science)
[context.yaml]: context.yaml
