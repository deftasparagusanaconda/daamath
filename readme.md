[📖 docs][docs] | [💾 install](#install) | [🌸 daa (me)][contact]

# daamath

a mathematician's spellbook. the most coherent math library ever. 

see how to install [here][install] or choose your language:

[python](https://deftasparagusanaconda.github.io/daamath/install/python/) | [c](https://deftasparagusanaconda.github.io/daamath/install/c/) | [c++](https://deftasparagusanaconda.github.io/daamath/install/cpp/) | [javascript](https://deftasparagusanaconda.github.io/daamath/install/javascript)| [julia](https://deftasparagusanaconda.github.io/daamath/install/julia) | (and hopefully more)

## why does daamath exist?

"does this round to the nearest integer? or is it like floor/ceil?"

"why is there no log(num, base) in C?"

"why does pow(2,3) return a float?"

"why do i have to know `powf`, `pow` and `powl` in C? cant they just make one `pow`?"

"but `log(-1)` is defined in the complex numbers. you mean i have to use `clog` for that? cant `log` do that naturally?"

"if we have `sqrt` and `cbrt`, where are the other n-th roots?"

"where is `acot(x)`??? how do i make `acot` from `atan`??" 

"where is `nand(x, y)`? `not(and(x, y))` looks so unnecessary"

"i know my int is even so i divide it by 2. why did you promote it to a float? its still supposed to be an int!"

"why does `log(2)` give me `0.69314718056`? is it base 10 or base e?"

"why is it `log(num, base)` in python but `log(base, num)` in julia?"

"i wish this math library had the golden ratio constant"

this is very ugly to me. so i made daamath.

## what daamath does

- **cross-language consistency:** daamath is a language-agnostic specification. it has consistent behaviour across languages, up to the limitations of the language.
- **domain-aware arithmetic:** arithmetic operators respect the number domain. for example, an integer divided by an integer shall not return a rational number. instead, it raises a `DomainError`. [learn more][type homomorphism]
- **complete function sets:** hyperoperations, trigonometry, boolean gates, ordering operators, quantization, and more
- **no implicit type promotion:** daamath will not cast an integer to a float. it will preserve the precision of your datatype.
- **no aliases:** one name per function/constant/string
- **unicode lookup table:**  to find math characters easily
- **mathematical constants:** e, tau, phi, and so much more
- **[documentation pages][docs]:** you will probably learn a lot of new mathematics reading this

[docs]: https://deftasparagusanaconda.github.io/daamath/
[install]: https://deftasparagusanaconda.github.io/daamath/install/
[type homomorphism]: https://deftasparagusanaconda.github.io/daamath/functions/
[contact]: https://discordapp.com/users/608255432859058177
