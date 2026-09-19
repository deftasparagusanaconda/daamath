# daamath

daamath is a cross-language math library specification, with implementations in various programming languages:

* [python](https://github.com/deftasparagusanaconda/daamath-python): `python -m pip install daamath`

it provides four useful things in math:

* [characters](characters): +, −, ×, ÷, =, %, …
* [constants](constants): π, e, φ, √2, i, γ, …
* [datatypes](datatypes): binary64, int32, uint8, bool, complex128, decimal64, …
* [functions](functions): sin, log, abs, pow, sqrt, round, …

since it must behave the same in different programming languages, it has some rules:

* no implicit assumptions
* no [object-oriented programming](https://en.wikipedia.org/wiki/Object-oriented_programming?wprov=sfla1)
* no [impure functions](https://en.wikipedia.org/wiki/Pure_function?wprov=sfla1)/mutation/side effects
* no keyword arguments 
* no optional arguments
* no stateful behaviour 
* functions are defined mathematically, not algorithmically
* names are [snake_case](https://en.wikipedia.org/wiki/Snake_case?wprov=sfla1) and start with a letter

