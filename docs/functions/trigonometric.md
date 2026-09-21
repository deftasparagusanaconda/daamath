# trigonometric

we have 24 useful trigonometric functions: [`sin`](#sin) [`cos`](#cos) [`tan`](#tan) [`cot`](#cot) [`sec`](#sec) [`csc`](#csc) [`asin`](#asin) [`acos`](#acos) [`atan`](#atan) [`acot`](#acot) [`asec`](#asec) [`acsc`](#acsc) [`sinh`](#sinh) [`cosh`](#cosh) [`tanh`](#tanh) [`coth`](#coth) [`sech`](#sech) [`csch`](#csch) [`asinh`](#asinh) [`acosh`](#acosh) [`atanh`](#atanh) [`acoth`](#acoth) [`asech`](#asech) [`acsch`](#acsch)

we derive 36 trigonometric functions from the [three 2-dimensional unital ℝ algebras](https://en.wikipedia.org/wiki/Hypercomplex_number#Two-dimensional_real_algebras):

$\href{https://en.wikipedia.org/wiki/Complex_number}{\mathrm i^2 = -1}$  
$\href{https://en.wikipedia.org/wiki/Dual_number}{\mathrm ε^2 = \phantom{+}0,\quad \mathrm ε \ne \phantom{\pm}0}$  
$\href{https://en.wikipedia.org/wiki/Split-complex_number}{\mathrm j^2 = +1,\quad \mathrm j \ne \pm1}$  

<!--we use the familiar variable $z = x + \mathrm iy\quad x, y\in\href{https://en.wikipedia.org/wiki/Real_number}{\mathbb R}$  -->

<span id="sin">
	$\href{https://en.wikipedia.org/wiki/Sine}{\sin}(z) = \dfrac{\mathrm e^{+\mathrm iz} - \mathrm e^{-\mathrm iz}}{2\mathrm i}$
</span>

<span id="cos">
	$\href{https://en.wikipedia.org/wiki/Cosine}{\cos}(z) = \dfrac{\mathrm e^{+\mathrm iz} + \mathrm e^{−\mathrm iz}}{2}$
</span>

<span id="tan">
	$\href{https://en.wikipedia.org/wiki/Tangent_(trigonometry)}{\tan}(z) = \dfrac{\mathrm e^{+\mathrm iz} - \mathrm e^{-\mathrm iz}}{\mathrm e^{+\mathrm iz} + \mathrm e^{-\mathrm iz}}\dfrac{1}{\mathrm i}$
</span>

<span id="cot">
	$\href{https://en.wikipedia.org/wiki/Cotangent}{\cot}(z) = \dfrac{\mathrm e^{+\mathrm iz} + \mathrm e^{-\mathrm iz}}{\mathrm e^{+\mathrm iz} - \mathrm e^{-\mathrm iz}}\dfrac{\mathrm i}{1}$
</span>

<span id="sec">
	$\href{https://en.wikipedia.org/wiki/Secant_(trigonometry)}{\sec}(z) = \dfrac{2}{\mathrm e^{+\mathrm iz} + \mathrm e^{−\mathrm iz}}$
</span>

<span id="csc">
	$\href{https://en.wikipedia.org/wiki/Cosecant}{\csc}(z) = \dfrac{2\mathrm i}{\mathrm e^{+\mathrm iz} - \mathrm e^{-\mathrm iz}}$
</span>

<span id="asin" title="real principal interval: [−π/2, +π/2]">
	<!--$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{asin}}(z) = \displaystyle\int_0^z\dfrac{\mathrm d t}{\sqrt{1 - t^2}}$-->
	$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{asin}}(z) = -\mathrm i \ln\left(\sqrt{1 - z^2} + \mathrm iz\right)$<!--, z \notin (-\infty, -1) \cup (+1, +\infty)-->
	<!--	
	$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{asin}}(z) =
	\begin{cases}
	-\mathrm i \ln\left(\sqrt{1-z^2}+\mathrm iz\right),
	& z\notin(-\infty,-1)\cup\left(+1,+\infty\right)\\[8pt]
	-\dfrac{\pi}{2}\pm\mathrm i\ln\left(\sqrt{x^2-1}-x\right),
	& z\in (-\infty, -1], z = x \pm\mathrm i0\\[8pt]
	+\dfrac{\pi}{2}\pm\mathrm i\ln\left(\sqrt{x^2-1}+x\right),
	& z\in [+1, +\infty), z = x \pm\mathrm i0
	\end{cases}$
	-->
	<!--
	$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{asin}}(z) =
	\begin{cases} 
	-\mathrm{i}\ln\left(\sqrt{1-z^2}+\mathrm{i}z\right), 
	& z\notin(-\infty,-1)\cup(1,+\infty),\\[6pt]
	-\dfrac{\pi}{2} +\mathrm{i}\ln\left(\sqrt{x^2-1}-x\right), 
	& z=x+\mathrm{i}0,\quad x\le-1,\\[6pt]
	-\dfrac{\pi}{2} -\mathrm{i}\ln\left(\sqrt{x^2-1}-x\right), 
	& z=x-\mathrm{i}0,\quad x\le-1,\\[6pt]
	+\dfrac{\pi}{2} +\mathrm{i}\ln\left(\sqrt{x^2-1}+x\right), 
	& z=x+\mathrm{i}0,\quad x\ge1,\\[6pt] +\dfrac{\pi}{2}
	-\mathrm{i}\ln\left(\sqrt{x^2-1}+x\right), 
	& z=x-\mathrm{i}0,\quad x\ge1
	\end{cases}$
	-->
	<!--
	$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{asin}}(z) =
	\begin{cases} 
	-\mathrm{i}\ln\left(\sqrt{1-z^2}+\mathrm{i}z\right), 
	& z\notin(-\infty,-1)\cup(1,+\infty)\\[6pt] 
	\operatorname{sgn}(x)\dfrac{\pi}{2} \pm\mathrm{i}\ln\left(|x|+\sqrt{x^2-1}\right), 
	& z=x\pm\mathrm{i}0,\quad |x|\geq1
	\end{cases}$
	-->
	<!--
	$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{asin}}(z) =
	\begin{cases} 
	-\mathrm{i}\ln(\sqrt{1-z^2}+\mathrm{i}z), 
	& z\notin(-\infty,-1]\cup[1,+\infty)\\
	\operatorname{sgn}(x)\dfrac{\pi}{2} \pm\mathrm{i}\ln(\sqrt{x^2-1} + |x|), 
	&|x|\ge1,\ y=\pm0
	\end{cases}$
	-->
</span>

<span id="acos" title="real principal interval: [0, +π]">
	<!--$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{acos}}(z) = \displaystyle\int_z^1\dfrac{\mathrm d t}{\sqrt{1 - t^2}}$-->
	<!--$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{acos}}(z) =
	\begin{cases}
	-2\mathrm i\ln\left(\sqrt{\dfrac{1+z}{2}}+\mathrm i\sqrt{\dfrac{1-z}{2}}\right),
	& z\notin(-\infty,-1]\cup[1,+\infty)\\
	\pi \textbf{1}_{x < 0} \mp \mathrm{i}\ln(\sqrt{x^2-1} + |x|), 
	&|x|\ge1,\ y=\pm0
	\end{cases}$
	-->
	$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{acos}}(z) =	-2\mathrm i\ln\left(\sqrt{\dfrac{1+z}{2}}+\mathrm i\sqrt{\dfrac{1-z}{2}}\right)$
</span>

<span id="atan" title="real principal interval: [−π/2, +π/2]">
	<!--$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{atan}}(z) = \displaystyle\int_0^z\dfrac{\mathrm d t}{1 + t^2}, \mathrm{z} \ne \pm i$-->
	<!--$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{atan}}(z) = 
	\begin{cases}
	\dfrac{\mathrm i}{2}\ln\left(\dfrac{\mathrm i + \mathrm z}{\mathrm i - \mathrm z}\right)
	& x = \pm0, |y| \ge 0 
	\end{cases}$-->
	$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{atan}}(z) = \dfrac{\mathrm i}{2}\ln\left(\dfrac{\mathrm i + \mathrm z}{\mathrm i - \mathrm z}\right)$
</span>

<span id="acot" title="real principal interval: [−π/2, +π/2]">
	$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{acot}}(z) = \operatorname{atan}\left(\dfrac{1}{z}\right)$
</span>

<span id="asec" title="real principal interval: [0, +π] ∖ {+π/2}">
	$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{asec}}(z) = \operatorname{acos}\left(\dfrac{1}{z}\right)$
</span>

<span id="acsc" title="real principal inverval: [−π/2, +π/2] ∖ {0}">
	$\href{https://en.wikipedia.org/wiki/Inverse_trigonometric_functions}{\operatorname{acsc}}(z) = \operatorname{asin}\left(\dfrac{1}{z}\right)$  
</span>

<span id="sinp">
	$\operatorname{sinp}(z) = \dfrac{\mathrm e^{+\mathrm εz} − \mathrm e^{−\mathrm εz}}{2\mathrm ε}$
</span>

<span id="cosp">
	$\operatorname{cosp}(z) = \dfrac{\mathrm e^{+\mathrm εz} + \mathrm e^{−\mathrm εz}}{2}$
</span>

<span id="tanp">
	$\operatorname{tanp}(z) = \dfrac{\mathrm e^{+\mathrm εz} − \mathrm e^{−\mathrm εz}}{\mathrm e^{+\mathrm εz} - \mathrm e^{-\mathrm εz}}\dfrac{1}{\mathrm ε}$
</span>

<span id="cotp">
	$\operatorname{cotp}(z) = \dfrac{\mathrm e^{+\mathrm εz} + \mathrm e^{−\mathrm εz}}{\mathrm e^{+\mathrm εz} - \mathrm e^{-\mathrm εz}}\dfrac{\mathrm ε}{1}$
</span>

<span id="secp">
	$\operatorname{secp}(z) = \dfrac{2}{\mathrm e^{+\mathrm εz} + \mathrm e^{−\mathrm εz}}$
</span>

<span id="cscp">
	$\operatorname{cscp}(z) = \dfrac{2\mathrm ε}{\mathrm e^{+\mathrm εz} - \mathrm e^{−\mathrm εz}}$
</span>

<span id="asinp">
	$\operatorname{asinp}(z) =\ ?$
</span>

<span id="acosp">
	$\operatorname{acosp}(z) =\ ?$
</span>

<span id="atanp">
	$\operatorname{atanp}(z) =\ ?$
</span>

<span id="acotp">
	$\operatorname{acotp}(z) = \operatorname{atan}\left(\dfrac{1}{z}\right)$
</span>

<span id="asecp">
	$\operatorname{asecp}(z) = \operatorname{acos}\left(\dfrac{1}{z}\right)$
</span>

<span id="acscp">
	$\operatorname{acscp}(z) = \operatorname{asin}\left(\dfrac{1}{z}\right)$
</span>

<span id="sinh">
	$\href{https://en.wikipedia.org/wiki/Hyperbolic_functions}{\operatorname{sinh}}(z) = \dfrac{\mathrm e^{+\mathrm jz} - \mathrm e^{−\mathrm jz}}{2\mathrm j}$
</span>

<span id="cosh">
	$\href{https://en.wikipedia.org/wiki/Hyperbolic_functions}{\operatorname{cosh}}(z) = \dfrac{\mathrm e^{+\mathrm jz} + \mathrm e^{−\mathrm jz}}{2}$
</span>

<span id="tanh">
	$\href{https://en.wikipedia.org/wiki/Hyperbolic_functions}{\tanh}(z) = \dfrac{\mathrm e^{+\mathrm jz} - \mathrm e^{−\mathrm jz}}{\mathrm e^{+\mathrm jz} + \mathrm e^{−\mathrm jz}}\dfrac{1}{\mathrm j}$
</span>

<span id="coth">
	$\href{https://en.wikipedia.org/wiki/Hyperbolic_functions}{\coth}(z) = \dfrac{\mathrm e^{+\mathrm jz} + \mathrm e^{−\mathrm jz}}{\mathrm e^{+\mathrm jz} - \mathrm e^{−\mathrm jz}}\dfrac{\mathrm j}{1}$
</span>

<span id="sech">
	$\href{https://en.wikipedia.org/wiki/Hyperbolic_functions}{\operatorname{sech}}(z) = \dfrac{2}{\mathrm e^{+\mathrm jz} + \mathrm e^{−\mathrm jz}}$
</span>

<span id="csch">
	$\href{https://en.wikipedia.org/wiki/Hyperbolic_functions}{\operatorname{csch}}(z) = \dfrac{2\mathrm j}{\mathrm e^{+\mathrm jz} - \mathrm e^{−\mathrm jz}}$
</span>

<span id="asinh" title="real principal interval: (−∞, +∞)">
	$\href{https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions}{\operatorname{asinh}}(z) = \ln\left(\sqrt{z^2 + 1} + z\right)$
</span>

<span id="acosh" title="real principal interval: [+1, +∞)">
	<!--$\href{https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions}{\operatorname{acosh}}(z) = \ln\left(\pm\sqrt{z^2 - 1} + z\right)$-->
	$\href{https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions}{\operatorname{acosh}}(z) = 2\ln\left(\sqrt{\dfrac{z + 1}{2}} + \sqrt{\dfrac{z - 1}{2}}\right)$
</span>

<span id="atanh" title="real principal interval: (−1, +1)">
	$\href{https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions}{\operatorname{atanh}}(z) = \dfrac{1}{2}\ln\left(\dfrac{1+z}{1-z}\right)$
</span>

<span id="acoth" title="real principal interval: (−∞, +∞) ∖ {0}">
	$\href{https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions}{\operatorname{acoth}}(z) = \operatorname{atanh}\left(\dfrac{1}{z}\right)$
</span>

<span id="asech" title="real principal interval: (0, +1]">
	$\href{https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions}{\operatorname{asech}}(z) = \operatorname{acosh}\left(\dfrac{1}{z}\right)$
</span>

<span id="acsch" title="real principal interval: (−∞, −1) ∪ (+1, +∞)">
	$\href{https://en.wikipedia.org/wiki/Inverse_hyperbolic_functions}{\operatorname{acsch}}(z) = \operatorname{asinh}\left(\dfrac{1}{z}\right)$
</span>

the 12 parabolic trig functions are not included because they are trivial: $\operatorname{sinp}(z) = z,\quad \operatorname{cosp}(z) = 1$

when branch values differ by approach direction, the input datatype must encode that direction; otherwise, evaluation raises DatatypeError.
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
# source

* [Digital Library of Mathematical Functions](https://dlmf.nist.gov/4)
* [Branch Cuts for Complex Elementary Functions](https://grouper.ieee.org/groups/msc/ANSI_IEEE-Std-754-2019/background/kahan86branch.pdf) ([Kahan](https://en.wikipedia.org/wiki/William_Kahan))

<!--
# rant

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
<!--
# rant 2

also daa, im just gonna write a note here so you read it later: the wikipedia definition for acot's range does NOT agree with the DLMF nor with Kahan. so keep that in mind.  
- okay, then ill just decide that the DLMF and Kahan are the true sources. because the two of them agree. the wikipedia definition... i really wish they changed it. not much people know about this discrepancy, i bet
-->
