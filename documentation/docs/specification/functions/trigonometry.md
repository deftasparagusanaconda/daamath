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

=== "input semiarea, output ratio"

	| numerator  | denominator | elliptic | parabolic | hyperbolic |
	| -          | -           | - | - | - |
	| opposite   | hypotenuse  | [sin](#sin) | <del>sinp</del> | [sinh](#sinh) |
	| adjacent   | hypotenuse  | [cos](#cos) | <del>cosp</del> | [cosh](#cosh) |
	| opposite   | adjacent    | [tan](#tan) | <del>tanp</del> | [tanh](#tanh) |
	| adjacent   | opposite    | [cot](#cot) | <del>cotp</del> | [coth](#coth) |
	| hypotenuse | adjacent    | [sec](#sec) | <del>secp</del> | [sech](#sech) |
	| hypotenuse | opposite    | [csc](#csc) | <del>cscp</del> | [csch](#csch) |

=== "input ratio, output semiarea"

	| numerator  | denominator | elliptic | parabolic | hyperbolic |
	| -          | -           | - | - | - |
	| opposite   | hypotenuse  | [asin](#asin) | <del>asinp</del> | [asinh](#asinh) |
	| adjacent   | hypotenuse  | [acos](#acos) | <del>acosp</del> | [acosh](#acosh) |
	| opposite   | adjacent    | [atan](#atan) | <del>atanp</del> | [atanh](#atanh) |
	| adjacent   | opposite    | [acot](#acot) | <del>acotp</del> | [acoth](#acoth) |
	| hypotenuse | adjacent    | [asec](#asec) | <del>asecp</del> | [asech](#asech) |
	| hypotenuse | opposite    | [acsc](#acsc) | <del>acscp</del> | [acsch](#acsch) |

unfortunately, parabolic trigonometry is trivial, because . thus daamath excludes parabolic trigonometry and maintains 24 instead.

lastly, you may notice that the word 'angle' is never mentioned. that is because, while angles are convenient in circular geometry, in hyperbolic functions, we dont take the angle of anything anymore. we take the semiarea of the hyperbola with the x = y line. in fact, in circular geometry, what we are really describing when we say 'the angle' is the semiarea subtended by the section. this idea of semiarea extends to parabolic geometry as well.

## API implementation

#### sin
	given the semiarea, return the ratio of opposite to hypotenuse in circular geometry
#### cos
	given the semiarea, return the ratio of adjacent to hypotenuse in circular geometry
#### tan
	given the semiarea, return the ratio of opposite to adjacent in circular geometry
#### cot
	given the semiarea, return the ratio of adjacent to opposite in circular geometry
#### sec
	given the semiarea, return the ratio of hypotenuse to adjacent in circular geometry
#### csc
	given the semiarea, return the ratio of hypotenuse to opposite in circular geometry
#### asin
	given the ratio of opposite to hypotenuse, return the semiarea in circular geometry
#### acos
	given the ratio of adjacent to hypotenuse, return the semiarea in circular geometry
#### atan
	given the ratio of opposite to adjacent, return the semiarea in circular geometry
#### acot
	given the ratio of adjacent to opposite, return the semiarea in circular geometry
#### asec
	given the ratio of hypotenuse to adjacent, return the semiarea in circular geometry
#### acsc
	given the ratio of hypotenuse to opposite, return the semiarea in circular geometry
#### sinh
	given the semiarea, return the ratio of opposite to hypotenuse in hyperbolic geometry
#### cosh
	given the semiarea, return the ratio of adjacent to hypotenuse in hyperbolic geometry
#### tanh
	given the semiarea, return the ratio of opposite to adjacent in hyperbolic geometry
#### coth
	given the semiarea, return the ratio of adjacent to opposite in hyperbolic geometry
#### sech
	given the semiarea, return the ratio of hypotenuse to adjacent in hyperbolic geometry
#### csch
	given the semiarea, return the ratio of hypotenuse to opposite in hyperbolic geometry
#### asinh
	given the ratio of opposite to hypotenuse, return the semiarea in hyperbolic geometry
#### acosh
	given the ratio of adjacent to hypotenuse, return the semiarea in hyperbolic geometry
#### atanh
	given the ratio of opposite to adjacent, return the semiarea in hyperbolic geometry
#### acoth
	given the ratio of adjacent to opposite, return the semiarea in hyperbolic geometry
#### asech
	given the ratio of hypotenuse to adjacent, return the semiarea in hyperbolic geometry
#### acsch
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

