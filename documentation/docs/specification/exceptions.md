<details><summary>lingo</summary>  

errors occur.  
flags are set and unset.  
exceptions are raised.  
a representation in a programming language means a datatype (like `bool`, `uint`, `int`, `float`, …).  
the fidelity of a representation in a programming language means the precision of a datatype (like `float32` vs `float64`).  

</details>

# introduction

when doing mathematics, we encounter strange things like `1/0`, `0/0`, `0^0`, `-1!`, etc. daamath recognizes all of these through errors. 

# Error

the base class of all errors in daamath.

## DomainError

an [Error](#error) that occurs when something related to a domain goes wrong

### OutOfDomainError

a [DomainError](#domainerror) that occurs when a function checks its inputs or output and they dont adhere to the function's desired domain for that input or output. 

when working with real numbers, `0/0` is undefined because the domain doesnt represent that. so a `ClosureError` occurs. but in wheel algebra, `0/0` is defined so `ClosureError` doesnt occur.

strangely, if the function was something like div: R, R → W, then `0/0` is indeed defined in wheel algebra, even though you divide two real numbers. so `OutOfDomainError` doesnt occur. note that the output codomain wasnt determined by the input domains. the function defined the domain of the output :)

## DataTypeError

an [Error](#error) that ocurs when something related to a datatype goes wrong.

### FidelityError

a [DataTypeError](#datatypeerror) that occurs when a datatype cannot accurately store a value. for example, `0.1` as a float will raise a `FidelityError` (given that rounding is disabled). `-1` as a `uint` (unsigned integer) will raise a `FidelityError`. 

### TypeInferenceError

a [DataTypeError](#datatypeerror) that occurs when a function receives two arguments of different datatypes/representations. since daamath does not want to assume a precision/fidelity and thus a datatype, it tries to infer your precision contract from your inputs. when it cannot reliably do this, it will raise a [TypeInferenceError](#typeinferenceerror)

an example is `div(2, 3.0)`. here, `2` is an `int` but `3.0` is a `float` so `div` doesnt know which datatype to return. so it raises a `TypeInferenceError`.

this error will rarely occur, if even implemented at all: if your language only has definitions for certain types, it will never be defined for type combinations where the output type cannot be inferred. but in languages with duck typing like python, this error is indeed useful.

# implementation

if the programming language supports exceptions, daamath uses them. otherwise, we take an approach similar to [IEEE 754]: when an error is encountered, its corresponding flag is set, and the sentinel value for that datatype is returned. it is up to the programmer to check these flags. it is up to the programmer to unset these sticky flags. thus `[assumptions.condition_handling]` has four options: 

`SENTINEL`: return sentinel
`FLAG_SENTINEL`: set flags, return sentinel
`RAISE_HALT`: raise exception, halt execution
`FLAG_RAISE_HALT`: set flags, raise exception, halt execution

the default value `FLAG_RAISE_HALT` if exceptions are supported else `FLAG_SENTINEL`. sentinel values are defined in the [assumptions]. sentinel values need not be restricted by the domain, and can be any value of the datatype.

in the case that multiple errors occur, and only one exception can be raised at a time, the precedence of exceptions should be the same as the order in which they appear in this document. and yes that does mean an [Error](#error) should be raised before a DomainError because if an error doesnt even have a name, it is probably very very serious, as it cannot even be classified as a [DomainError](#domainerror) or a [DataTypeError](#datatypeerror). a [DomainError](#domainerror) is more serious than a [DataTypeError](#datatypeerror) because it is a violation of mathematics, which is more serious than a violation of computation. additionally, if flagging is also enabled, the corresponding flag for each error should be set before the exception is raised and execution is halted. that way, the programmer still has a full picture of all the errors that occurred. 

# motivation

if daamath is to be rigorous, it has to be equally as rigorous in its error handling. handling edge cases and special cases. i dont particularly enjoy designing edge case handling behaviour but this has taught me a good amount.

# rant

it was pretty surprising to realize that `0/0` is actually a `OutOfDomainError`. i thought it would want to be its own error like `ZeroDivisionError` or `ZeroPowerError` for `0^0` and i was afraid i was going to have to special case every special value. but im glad i figured it out. this is really nice and very true to the mathematics

[IEEE 754]: https://
[assumptions]: https://
[assumptions.condition_handling]: https://
