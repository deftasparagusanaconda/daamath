<details><summary>lingo</summary>  

errors occur.  
flags are set.  
exceptions are raised.  
a representation in a programming language means a datatype (like `bool`, `uint`, `int`, `float`, …).  
the fidelity of a representation in a programming language means the precision of a datatype (like `float32` vs `float64`).  

</details>

# introduction

when doing mathematics, we encounter strange things like `1/0`, `0/0`, `0^0`, `-1!`, etc. daamath recognizes all of these through errors. 

the two most important errors are [ClosureError](#closureerror) and [FidelityError](#fidelityerror)


## ClosureError

occurs when a function tries to return a value that is undefined in its codomain. when working with real numbers, `0/0` is undefined because the domain doesnt represent that. so a `ClosureError` occurs. but in wheel algebra, `0/0` is defined so `ClosureError` doesnt occur.

strangely, if the function was something like div: R, R → W, then `0/0` is indeed defined in wheel algebra, even though you divide two real numbers. so `ClosureError` doesnt occur. note that the output codomain wasnt determined by the input domains. the function defined that itself :) so `ClosureError` only occurs based on the function's codomain. 

## FidelityError

occurs when a datatype/representation cannot accurately store a value. for example, `0.1` as a float will raise a `FidelityError` (given that rounding is disabled). `-1` as a `uint` (unsigned integer) will raise a `FidelityError`. 

## TypeError

occurs when a function receives two arguments of different datatypes/representations. since daamath does not want to assume a precision/fidelity and thus a datatype, it wants to preserve the original datatype as much as possible. so though the domains may be different, daamath requires that the datatypes/representations are homogeneous. 

an example is `div(2, 3.0)`. here, `2` is an `int` but `3.0` is a `float` so `div` doesnt know which datatype to return. so it raises a `TypeError`.

daamath shouldnt have to implement this. the language should handle this. if the language cant, then daamath should handle it itself

# implementation

if the programming language supports exceptions, daamath uses them. otherwise, we take an approach similar to [IEEE 754]. when an error is encountered, its corresponding boolean flag is set to `true`, and a default value for that datatype is returned (e.g. 0 for int, Nan for float). it is up to the programmer to check these flags. the sentinel value allows computation to continue until the program checks the sticky flags and decides what to do with them. it is up to the programmer to reset these sticky flags. thus `[assumptions.condition_handling]` has four options: 

`SENTINEL`: return sentinel
`FLAG_SENTINEL`: set flags, return sentinel
`RAISE_HALT`: raise exception, halt execution
`FLAG_RAISE_HALT`: set flags, raise exception, halt execution

the default value is `FLAG_RAISE_HALT` if exceptions are supported else `FLAG_SENTINEL`. sentinel values are defined in the [assumptions]. sentinel values need not be restricted by the domain, and can be any value of the datatype (i havent decided fully yet. perhaps functions that receive values outside of their defined domain wont be very happy about this and wont allow errors to propagate. so im not sure)

in the case that multiple errors occur, and only one exception can be raised at a time, this hierarchy of errors determines which exception is raised first:
`ClosureError` > `FidelityError` > `TypeError`
additionally, if flagging is enabled, the flags for both should be set before one exception is raised and execution is halted. that way, the programmer still has a full picture of all the errors that occurred. 

# motivation

if daamath is to be rigorous, it has to be equally as rigorous in its error handling. handling edge cases and special cases. i dont particularly enjoy designing edge case handling behaviour but this has taught me a good amount.

# rant

it was pretty surprising to realize that `0/0` is actually a ~~`DomainE`~~ err.. a `ClosureError`. i thought it would want to be its own error like `ZeroDivisionError` or `ZeroPowerError` for `0^0` and i was afraid i was going to have to special case every special value. but im glad i figured it out. this is really nice

[IEEE 754]: https://
[assumptions]: https://
[assumptions.condition_handling]: https://
