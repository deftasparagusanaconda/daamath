daamath maintains collections of [functions](https://en.wikipedia.org/wiki/Function_(computer_programming)) that are called typically as `op(a, b, …)`. they may sometimes be called operators. it also maintains a 

functions will always have a known arity (take a certain number of arguments) and will never be overloaded to change behaviour depending on different arities. why?

have you tried debugging `log(y/8*(49-1)+1,49)` and wondered 'why is this scaled weirdly?', only to realize after painful eye strain that its not log with base e. there is a second argument giving base=49. the problem was that the function changed behaviour depending on arity, and it was hard to read the arity by eye. we should guarantee that log always takes two arguments, and that the one-argument version of log (like `ln`, `log2`, `log10`) should always make their base clear. that way, there is no confusion of 'is this `log` taking base or not?' because you can see from the function name directly.




