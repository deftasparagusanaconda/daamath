# daamath

a mathematician's spellbook: cross-language math library [specification], with [implementations] across various programming languages

# install
<table>
  <tbody>
    <tr>
      <td><a href="https://deftasparagusanaconda.github.io/daamath/implementations/python/install">python</a></td>
      <td><code>python -m pip install daamath</code></td>
    </tr>
    <tr>
      <td><a href="https://deftasparagusanaconda.github.io/daamath/implementations/c/install">c</a></td>
      <td><code>…<!--curl -sSL https://deftasparagusanaconda.github.io/daamath/install.sh | sh--></code></td>
    </tr>
    <tr>
      <td><a href="https://deftasparagusanaconda.github.io/daamath/implementations/c++/install">c++</a></td>
      <td><code>…<!--curl -sSL https://deftasparagusanaconda.github.io/daamath/install.sh | sh--></code></td>
    </tr>
    <tr>
      <td><a href="https://deftasparagusanaconda.github.io/daamath/implementations/javascript/install">javascript</a></td>
      <td><code>…<!--npm install daamath--></code></td>
    </tr>
    <tr>
      <td><a href="https://deftasparagusanaconda.github.io/daamath/implementations/julia/install">julia</a></td>
      <td><code>…<!--julia -e 'using Pkg; Pkg.add("daamath")'--></code></td>
    </tr>
	<tr>
	  <td>…</td>
	  <td><code>…</code></td>
    </tr>
  </tbody>
</table>

# why?

"does integer division do floor rounding or trunc rounding?"

"why does `pow(2, 3)` return a float? i expected an int"

"why do i have to know `powf`, `pow` and `powl` in C? cant they just make one `pow`?"

"i know my int is even so i divide it by 2. why did you promote it to a float? its still supposed to be an int!"

"i wish i could translate my math code from C to Python but it gives me different results"

"why is there no `log(num, base)` in C?"

"but `log(-1)` is defined in the complex numbers. you mean i have to use `clog` for that? `log` should be able to do that if i pass a complex number"

"why is it `log(num, base)` in python but `log(base, num)` in julia?"

"why were my calculations wrong? is `log` base 10 or base e?"

"where is `acot(x)`??? how do i make `acot` from `atan`??" 

"where is `nand(x, y)`? `not (x and y)` is so unnecessary"

"i wish this math library had the golden ratio constant"

this is very ugly to me. so i made daamath.

# features

- **cross-language consistency:** daamath is designed to behave the same across languages. 
- **true functions:** faithful to the mathematics, you can define the domain, codomain, and mapping of functions. for example, an integer divided by an integer can be set to return either an integer or rational number
- **complete function sets:** hyperoperations to n=4, trigonometry in all 2 non-degenerate geometries, all non-degenerate boolean gates to arity 2, all 16 derived functions per relation, 12 rounding functions, …
- **clean namespace:** no aliases, datatype naming conventions, underscore-binding, …
- **unicode characters:** math-related unicode characters, presented in an elegant tree
- **mathematical constants:** e, π, τ, 
- **[documentation website][documentation]**

# examples

for our python examples, first `import daamath as dm`

```python
# by default, daamath does complex arithmetic in f64:

dm.log(-5, 2)
# 4.532360141827194j
```

```python
# you can do integer arithmetic with floats
dm.context.div.codomain = dm.domains.INTEGER
dm.div(5, 2)
# CodomainViolation: div(float 5, float 2) returned float 2.5 ∉ INTEGER
```

```python
# create your own domains
NONZERO_REAL = lambda x: dm.REAL(x) and x != 0
NONZERO_REAL(1.0)
# True
NONZERO_REAL(0)
# False
```

```python
# you can do matrix arithmetic naturally:
dm.context = dm.contexts.matrix
dm.mul([1,2,3], [2,3,4])
# 20
```

you also have cool tidbits like this:

```python
dm.PI_F64 - dm.PI_F32
# 
```

```python
dm.symbols.lowercase.tau
# τ
dm.symbols.infinity + dm.symbols.not.in.right + dm.symbols.latin.doublestruck.uppercase.r

# ∞ ∉ ℝ
```

- daa
<!--# rant

i originally made daamath because when i designed [gapprox], i wanted a math library that was both very functionally complete and had the same behaviour across languages. but i found that programmers made a lot of bad decisions about how to implement mathematics into code. i discovered a lot of maths along the way too. i hope daamath rewires how programmers think of maths, because its not like the real numbers are the only "real" numbers. ugh. or simply going along with IEEE's rounding without even acknowledging it. and they dont even know complex numbers exist. oh my gosh dont you know `log(-1)` exists??? youre just completely ignoring the complex domain. and `0/0` is not an error! your domain simply didnt define it. go look up what wheel algebra is. see the connection? `NaN` is just the IEEE 754 way to represent `⊥`. they just didnt realize it. most of your "errors" can be represented as either a ClosureError (the result wasnt defined in the codomain) or a RepresentationError (you disabled rounding, and the datatype couldnt represent it accurately)

dont even get me started on how left out the unicode math characters are :( everyone slobbers over latex but they dont know about the fact that you can write things like `eⁱᶿ = cos(θ) + i⋅sin(θ)` or `cosh²(θ) - sinh²(θ) = 1` or `ln(x) = logₑ(x)` or `∥z∥₂ = ²√(ℜ² + ℑ²)` entirely with unicode

ok rant done
-->
[documentation]: https://deftasparagusanaconda.github.io/daamath
[specification]: https://deftasparagusanaconda.github.io/daamath/specification
[implementations]: https://deftasparagusanaconda.github.io/daamath/implementations
[gapprox]: https://github.com/deftasparagusanaconda/gapprox
[daa]: https://github.com/deftasparagusanaconda

