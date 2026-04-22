# trigonometry

daamath maintains the full lattice of trigonometric functions. we also expose their relationship directly from [hypercomplex] algebra, believe it or not

## introduction

the trigonometric functions are derived from the exponential series 

ι⁰/0! + ι¹/1! + ι²/2! + ι³/3! + …

where if you set ι = i or ε or j, the even and odd terms will give you the cos and sin for the elliptic, parabolic, hyperbolic geometries respectively

ι² = -1 will give you cos(x) & sin(x)
ι² =  0 will give you cosp(x) & sinp(x)
ι² = +1 will give you cosh(x) & sinh(x)

totally we have 2 ⋅ 3 ⋅ 3P2 = 36 functions. 
2 from the normal trig function and its inverse
3 from the three geometries
3P2 from a triangle of three sides, from which we take two sides

![the lattice](diagrams/daamath-trigonometry.drawio.svg)

unfortunately, parabolic trigonometry is trivial, because . thus daamath excludes parabolic trigonometry and maintains 24 instead.

lastly, you may notice that the word 'angle' is never mentioned. that is because, while angles are convenient in circular geometry, in hyperbolic functions, we dont take the angle of anything anymore. we take the semiarea of the hyperbola with the x = y line. in fact, in circular geometry, what we are really describing when we say 'the angle' is the semiarea subtended by the section. this idea of semiarea extends to parabolic geometry as well.

## API implementation

##### sin(semiarea):
	given the semiarea, return the ratio of opposite to hypotenuse in circular geometry
##### cos(semiarea):
	given the semiarea, return the ratio of adjacent to hypotenuse in circular geometry
##### tan(semiarea):
	given the semiarea, return the ratio of opposite to adjacent in circular geometry
##### cot(semiarea):
	given the semiarea, return the ratio of adjacent to opposite in circular geometry
##### sec(semiarea):
	given the semiarea, return the ratio of hypotenuse to adjacent in circular geometry
##### csc(semiarea):
	given the semiarea, return the ratio of hypotenuse to opposite in circular geometry
##### asin(ratio):
	given the ratio of opposite to hypotenuse, return the semiarea in circular geometry
##### acos(ratio):
	given the ratio of adjacent to hypotenuse, return the semiarea in circular geometry
##### atan(ratio):
	given the ratio of opposite to adjacent, return the semiarea in circular geometry
##### acot(ratio):
	given the ratio of adjacent to opposite, return the semiarea in circular geometry
##### asec(ratio):
	given the ratio of hypotenuse to adjacent, return the semiarea in circular geometry
##### acsc(ratio):
	given the ratio of hypotenuse to opposite, return the semiarea in circular geometry
##### sinh(semiarea):
	given the semiarea, return the ratio of opposite to hypotenuse in hyperbolic geometry
##### cosh(semiarea):
	given the semiarea, return the ratio of adjacent to hypotenuse in hyperbolic geometry
##### tanh(semiarea):
	given the semiarea, return the ratio of opposite to adjacent in hyperbolic geometry
##### coth(semiarea):
	given the semiarea, return the ratio of adjacent to opposite in hyperbolic geometry
##### sech(semiarea):
	given the semiarea, return the ratio of hypotenuse to adjacent in hyperbolic geometry
##### csch(semiarea):
	given the semiarea, return the ratio of hypotenuse to opposite in hyperbolic geometry
##### asinh(ratio):
	given the ratio of opposite to hypotenuse, return the semiarea in hyperbolic geometry
##### acosh(ratio):
	given the ratio of adjacent to hypotenuse, return the semiarea in hyperbolic geometry
##### atanh(ratio):
	given the ratio of opposite to adjacent, return the semiarea in hyperbolic geometry
##### acoth(ratio):
	given the ratio of adjacent to opposite, return the semiarea in hyperbolic geometry
##### asech(ratio):
	given the ratio of hypotenuse to adjacent, return the semiarea in hyperbolic geometry
##### acsch(ratio):
	given the ratio of hypotenuse to opposite, return the semiarea in hyperbolic geometry

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

