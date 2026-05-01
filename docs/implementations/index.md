# implementations

an implementation is a realization of the specification onto a programming language

an implementation shall NOT have interfaces that other implementations dont. this causes portability issues. for example, the python implementation should not have methods for the Context class because non-OOP languages will lack those features. thus those methods should live as separate functions.

an implementation must have a corresponding install page. say for language X, it must have the install link `https://deftasparagusanaconda.github.io/daamath/implementations/X/install`. this is the link pointed to by the [install table in the front page](https://deftasparagusanaconda.github.io/daamath#install)
