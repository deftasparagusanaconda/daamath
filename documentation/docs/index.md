---
title: home
hide:
  - navigation
---

<!-- {% include "../../readme.md" %} -->
<!-- --8<-- "../../readme.md" -->

# daamath

a mathematician's spellbook: cross-language math library specification, with implementations in various programming languages

# why does daamath exist?

"does integer division do floor rounding or trunc rounding?"

"why is there no `log(num, base)` in C?"

"why does `pow(2, 3)` return a float?"

"why do i have to know `powf`, `pow` and `powl` in C? cant they just make one `pow`?"

"i wish i could translate my math code from C to Python but they gives me different results"

"but `log(-1)` is defined in the complex numbers. you mean i have to use `clog` for that? `log` should be able to do that if i pass a complex number"

"where is `acot(x)`??? how do i make `acot` from `atan`??" 

"where is `nand(x, y)`? `not(and(x, y))` looks so unnecessary"

"i know my int is even so i divide it by 2. why did you promote it to a float? its still supposed to be an int!"

"why does `log(2)` give me `0.69314718056`? is it base 10 or base e?"

"why is it `log(num, base)` in python but `log(base, num)` in julia?"

"i wish this math library had the golden ratio constant"

this is very ugly to me. so i made daamath.

# what does daamath do?

- **cross-language consistency:** daamath is a language-agnostic specification. it has consistent behaviour and interface across languages
- **domain-aware mathematics:** operators respect the domain of discussion. for example, an integer divided by an integer can be set to return either an integer or rational number
- **complete function sets:** hyperoperations
to n=4, trigonometry in all 2 non-degenerate geometries, all non-trivial boolean gates, ordering operators, quantization/rounding, …
- **type preservation:** daamath will never cast an `int` to a `float`. it will _always_ preserve your contract of precision aka your datatype.
- **clean namespace:** everything in daamath has one name only, and no aliases
- **unicode characters:** find math characters from unicode easily
- **mathematical constants:** e, τ, φ, …
- **documentation website:** everything in daamath has a dedicated documentation webpage 

# examples

by default, integer division raises an error if the result isnt an integer

```python
dm.div(5, 2)
# OutOfDomainError: result 2.5 is not in INTEGERS
```

but if you enable rounding, no error is raised

```python
dm.context.datatypes.rounding = dm.roundfloor
dm.div(5, 2)
# 2
```

by default, daamath enables nearest-even rounding for float operations. you can disable that to make sure all your operations are 100% accurate

```python
dm.context.datatypes.rounding = None
dm.add(1.0, 2.0)
# 3.0
dm.add(0.1, 0.2)
# FidelityError: result 0.3000000000000000166533453693773481063544750213623046875 cannot be accurately represented by the float datatype
```

you also have cool tidbits like this:

```python
print(dm.greek.lowercase.tau)
# τ
print(dm.infinity, dm.not.in.right, dm.latin.doublestruck.uppercase.r)
# ∞ ∉ ℝ
```

# install
<table>
  <tbody>
    <tr>
      <td><a href="https://deftasparagusanaconda.github.io/daamath/implementations/python/install">python</a></td>
      <td><code>python -m pip install daamath</code></td>
    </tr>
    <tr>
      <td><a href="https://deftasparagusanaconda.github.io/daamath/implementations/c/install">c</a></td>
      <td><code>curl -sSL https://deftasparagusanaconda.github.io/daamath/install.sh | sh</code></td>
    </tr>
    <tr>
      <td><a href="https://deftasparagusanaconda.github.io/daamath/implementations/c++/install">c++</a></td>
      <td><code>curl -sSL https://deftasparagusanaconda.github.io/daamath/install.sh | sh</code></td>
    </tr>
    <tr>
      <td><a href="https://deftasparagusanaconda.github.io/daamath/implementations/javascript/install">javascript</a></td>
      <td><code>npm install daamath</code></td>
    </tr>
    <tr>
      <td><a href="https://deftasparagusanaconda.github.io/daamath/implementations/julia/install">julia</a></td>
      <td><code>julia -e 'using Pkg; Pkg.add("daamath")'</code></td>
    </tr>
	<tr>
	  <td>…</td>
	  <td><code>…</code></td>
    </tr>
  </tbody>
</table>

click on your language for full instructions

# rant

i originally made daamath because when i designed [gapprox], i wanted a math library that was both very functionally complete and had the same behaviour across languages. but i found that programmers made a lot of bad decisions about how to implement mathematics into code. i discovered a lot of maths along the way too. i hope daamath rewires how programmers think of maths, because its not like the real numbers are the only "real" numbers. ugh. or simply going along with IEEE's rounding without even acknowledging it. and they dont even know complex numbers exist. oh my gosh dont you know `log(-1)` exists??? youre just completely ignoring the complex domain. and `0/0` is not an error! your domain simply didnt define it. go look up what wheel algebra is. see the connection? `NaN` is just the IEEE 754 way to represent `⊥`. they just didnt realize it. most of your "errors" can be represented as either a ClosureError (the result wasnt defined in the codomain) or a RepresentationError (you disabled rounding, and the datatype couldnt represent it accurately)

dont even get me started on how left out the unicode math characters are :( everyone slobbers over latex but they dont know about the fact that you can write things like `eⁱᶿ = cos(θ) + i⋅sin(θ)` or `cosh²(θ) - sinh²(θ) = 1` or `ln(x) = logₑ(x)` or `∥z∥₂ = ²√(ℜ² + ℑ²)` entirely with unicode

ok rant done

made by  
🌸 [daa]

[specification]: https://deftasparagusanaconda.github.io/daamath/specification
[implementations]: https://deftasparagusanaconda.github.io/daamath/implementations
[gapprox]: https://github.com/deftasparagusanaconda/gapprox
[install]: https://deftasparagusanaconda.github.io/daamath/install/
[daa]: https://github.com/deftasparagusanaconda
