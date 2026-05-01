# what is a constant?

a constant is something whose value doesnt depend on anything and doesnt change 

daamath maintains the following constants:

| name | value |
| - | - |
| [E](https://en.wikipedia.org/wiki/E_(mathematical_constant)) | 2.71828182845904523536028747135266249775… |
| [TAU](https://en.wikipedia.org/wiki/Tau) | 6.28318530717958647692528676655900576839433879875021… | 
| [I](https://en.wikipedia.org/wiki/Imaginary_unit) | i |
| TRUE    | boolean top element |
| FALSE   | boolean bottom element |
| PLASTIC     | 1.324717957244746… |
| SUPERGOLDEN | 1.465571231876768… |
| GOLDEN      | 1.618033988749… |
| SILVER      | 2.41421356237309504880… |

# what can become a constant?

if a set of constants has no clear bound to it, that set should not exist. `DIV_X_TAU` can create an infinite amount of constants, but its not clear where to end it. so its not done. same with `DIV_TAU_X` for example.

# unicode support

daamath will NOT deal with unicode in the namespace. it is very very non-portable. i also would love to type `from daamath import τ` but unicode support is inconsistent, and that harms our cross-language consistency a lot. 

# where is π??

daamath has a strong stance on π & τ. π is inelegant. τ is elegant. daamath is elegant. daamath uses ONLY τ. 

# rant

`DIV_X_Y` seemed like a good idea until i realized the space blows up and i have to start making arbitrary decisions on where to stop. this is bad. daamath shouldnt make assumptions unless they are mathematically sound and clear. if you want `DIV_1_PI`, make it yourself: `div(1, pi)` or `minv(pi)`
