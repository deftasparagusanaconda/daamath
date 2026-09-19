# trigonometric

we have 24 useful trigonometric functions: [`sin`](#sin) [`cos`](#cos) [`tan`](#tan) [`cot`](#cot) [`sec`](#sec) [`csc`](#csc) [`asin`](#asin) [`acos`](#acos) [`atan`](#atan) [`acot`](#acot) [`asec`](#asec) [`acsc`](#acsc) [`sinh`](#sinh) [`cosh`](#cosh) [`tanh`](#tanh) [`coth`](#coth) [`sech`](#sech) [`csch`](#csch) [`asinh`](#asinh) [`acosh`](#acosh) [`atanh`](#atanh) [`acoth`](#acoth) [`asech`](#asech) [`acsch`](#acsch)


<span id="sin"></span>[sin](https://en.wikipedia.org/wiki/Sine)(x) = Im(e^ix^), i^2^ = −1  
<span id="cos"></span>[cos](https://en.wikipedia.org/wiki/Cosine)(x) = Re(e^ix^), i^2^ = −1  
<span id="tan"></span>[tan](https://en.wikipedia.org/wiki/Tangent_(trigonometry))(x) = sin(x) / cos(x)  
<span id="cot"></span>[cot](https://en.wikipedia.org/wiki/Cotangent)(x) = 1 / tan(x)  
<span id="sec"></span>[sec](https://en.wikipedia.org/wiki/Secant_(trigonometry))(x) = 1 / cos(x)  
<span id="csc"></span>[csc](https://en.wikipedia.org/wiki/Cosecant)(x) = 1 / sin(x)  
<span id="asin"></span>[asin](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)(sin(x)) = x ∀x: −π/2 ≤ x ≤ +π/2  
<span id="acos"></span>[acos](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)(cos(x)) = x ∀x: 0 ≤ x ≤ +π  
<span id="atan"></span>[atan](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)(tan(x)) = x ∀x: -π/2 < x < +π/2  
<span id="acot"></span>[acot](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)(cot(x)) = x ∀x: 0 < x < +π  
<span id="asec"></span>[asec](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)(sec(x)) = x ∀x: 0 ≤ x ≤ +π, x ≠ +π/2  
<span id="acsc"></span>[acsc](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions)(csc(x)) = x ∀x: -π/2 ≤ x ≤ +π/2, x ≠ 0  
<span id="sinp"></span>sinp(x) = Im(e^εx^), ε^2^ = 0, ε ≠ 0  
<span id="cosp"></span>cosp(x) = Re(e^εx^), ε^2^ = 0, ε ≠ 0  
<span id="tanp"></span>tanp(x) = sinp(x) / cosp(x)  
<span id="cotp"></span>cotp(x) = 1 / tanp(x)  
<span id="secp"></span>secp(x) = 1 / cosp(x)  
<span id="cscp"></span>cscp(x) = 1 / sinp(x)  
<span id="asinp"></span>asinp(sinp(x)) = x  
<span id="acosp"></span>acosp(cosp(x)) = x  
<span id="atanp"></span>atanp(tanp(x)) = x  
<span id="acotp"></span>acotp(cotp(x)) = x  
<span id="asecp"></span>asecp(secp(x)) = x  
<span id="acscp"></span>acscp(cscp(x)) = x  
<span id="sinh"></span>[sinh](https://en.wikipedia.org/wiki/Hyperbolic_functions)(x) = Im(e^jx^), j^2^ = +1, j ≠ ±1  
<span id="cosh"></span>[cosh](https://en.wikipedia.org/wiki/Hyperbolic_functions)(x) = Re(e^jx^), j^2^ = +1, j ≠ ±1  
<span id="tanh"></span>[tanh](https://en.wikipedia.org/wiki/Hyperbolic_functions)(x) = sinh(x) / cosh(x)  
<span id="coth"></span>[coth](https://en.wikipedia.org/wiki/Hyperbolic_functions)(x) = 1 / tanh(x)  
<span id="sech"></span>[sech](https://en.wikipedia.org/wiki/Hyperbolic_functions)(x) = 1 / cosh(x)  
<span id="csch"></span>[csch](https://en.wikipedia.org/wiki/Hyperbolic_functions)(x) = 1 / sinh(x)  
<span id="asinh"></span>[asinh](https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions)(sinh(x)) = x ∀x: -∞ < x < +∞  
<span id="acosh"></span>[acosh](https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions)(cosh(x)) = x ∀x: +1 ≤ x < +∞  
<span id="atanh"></span>[atanh](https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions)(tanh(x)) = x ∀x: -1 < x < +1  
<span id="acoth"></span>[acoth](https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions)(coth(x)) = x ∀x: -∞ < x < +∞, x ≠ 0  
<span id="asech"></span>[asech](https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions)(sech(x)) = x ∀x: 0 < x ≤ +1  
<span id="acsch"></span>[acsch](https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions)(csch(x)) = x ∀x: -∞ < x < -1 or +1 < x < +∞  

since sinp(x) = x and cosp(x) = 1, the parabolic trig functions are trivial and are not included
<!--
totally we have 2 ⋅ 3 ⋅ 3P2 = 36 functions  
2 from the forward and inverse functions  
3 from the three geometries  
3P2 from a triangle of three sides, from which we take two sides  
-->
<!--
sin and cos are the most primitive of the six ratios. in math, you are encouraged to use only these two ratios if possible. but since daamath will be used in numerics-adjacent code, you are encouraged to use whatever ratio simplifies the expression the most, as it reduces computation steps.

lastly, you may notice that the word 'angle' is never mentioned. that is because, while angles are convenient in circular geometry, in hyperbolic functions, we dont take the angle of anything anymore. we take the semiarea of the hyperbola with the x = y line. in fact, in circular geometry, what we are really describing when we say 'the angle' is the semiarea subtended by the section. this idea of semiarea extends to parabolic geometry as well.
-->
<!--
## rant

why do trigonometric functions have anything to do with hypercomplex numbers? because the hypercomplex numbers encode geometries, which are beautifully expressed through these trig functions we have. there are three 2-dimensional unital algebrae: complex numbers, split-complex numbers, dual numbers. they correspond to circular, hyperbolic, and parabolic geometry.

okay im gonna solve why i use semiarea. for elliptic geometry, its trivial. 2π radians ∝ π area. 2 semiarea ∝ 1 area. so 2π radians ∝ 2π semiarea. so radian = semiarea already. but lets prove by geometry too.

ELLIPTIC GEOMETRY:

ellipse: x² + y² = r²
line: y = tx
intersection: 
	x² + t²x² = r² 
	x² = r² / (1 + t²)
	y² = r²t² / (1 + t²)
(x = r(1 + t²)⁻⁰·⁵, y = rt(1 + t²)⁻⁰·⁵)



area between ellipse and line:


full area = abπr²

sector area = t


DUAL LINE GEOMETRY:

dual line: x² = r²
line: y = tx
intersection: (x = ±1, y = t/2)

HYPERBOLIC GEOMETRY:
x² - y² = r²
-->

