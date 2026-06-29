# rounding

a special case of quantization:

# quantization

A quantization is an idempotent function R: X → X that maps each element to the representative of the equivalence class it belongs to. it is also understood as a [retraction]. it is decomposed as:

R = Q ∘ P  

where  

P: X → X/~, x ∈ P(x) ∀x ∈ X. "give me the equivalence class this element belong to"  
Q: X/~ → X, Q(x) ∈ x ∀x ∈ X/~. "give me the element that represents this equivalence class"  

thus we can classify quantizations based on their equivalence classes and their representative elements:

| name | equivalence classes | representative element |
| - | - | - |
| floor         | {…, [-1, 0), [0, +1), [+1, 2), …} | {…, -1, 0, +1, …} |
| ceil          | {…, (-2, -1], (-1, 0], (0, +1], …} | {…, -1, 0, +1, …} |
| trunc         | {…, \[-1,  0), {0}, (0, +1\], …} | {…, -1, 0, +1, …} | 
| away          | {…, (-2, -1], (-1, +1), [+1, +2), …} | {…, -1, 0, +1, …} | 
| even          | {…, {-1}, (-1, +1), {+1}, …} | {…, -1, 0, +1, …} | 
| odd           | {…, (-2, 0), {0}, (0, +2), …} | {…, -1, 0, +1, …} | 
| nearest_floor | {…, (-1.5, -0.5], (-0.5, +0.5], (+0.5, +1.5], …} | {…, -1, 0, +1, …} |
| nearest_ceil  | {…, [-1.5, -0.5), [-0.5, +0.5), [+0.5, +1.5), …} | {…, -1, 0, +1, …} |
| nearest_trunc | {…, \[-1.5, -0.5), \[-0.5, +0.5\], (+0.5, +1.5], …} | {…, -1, 0, +1, …} |
| nearest_away  | {…, (-1.5, -0.5], (-0.5, +0.5), [+0.5, +1.5), …} | {…, -1, 0, +1, …} |
| nearest_even  | {…, (-1.5, -0.5), \[-0.5, +0.5], (+0.5, +1.5), …} | {…, -1, 0, +1, …} |
| nearest_odd   | {…, \[-1.5, -0.5], (-0.5, +0.5), \[+0.5, +1.5], …} | {…, -1, 0, +1, …} |

![neat thing i made!](diagrams/daamath-quantize.drawio.svg)

these functions that map real numbers to integers all have one thing in common: how they round ties like …, -1.5, -0.5, +0.5, +1.5, …  
we can take advantage of this and describe them by a sequence of bits. the bits describe how they round ties.

floor is …--------…  
ceil is …++++++++…  
trunc is …++++----…  
away is …----++++…  
even is …-+-+-+-+…  
odd is …+-+-+-+-…  

about mathematical dependencies, we can analyze them:

floor returns the nearest (least metric distance) cocover of x
ceil returns the nearest (least metric distance) cover of x

these functions depend on a metric and an order

trunc returns ceil if x > center else floor
away returns floor if x > center else ceil

these functions depend on a center element

even returns floor if floor % 2 == 0 else ceil
odd returns ceil if floor(x) % 2 == 1 else floor

these functions depend on an additional equivalence class, defined via modulo

the nearestX functions always return the nearest (least metric distance) element. when multiple elements are equally distant, they use the order to determine which way to round.

# API implementation

##### floor(number):
	round towards −∞
##### ceil(number):
	round towards +∞
##### trunc(number):
	round towards 0
##### away(number):
	round away from 0
##### even(number):
	round towards the nearest even integer (if not already an integer)
##### odd(number):
	round towards the nearest odd integer (if not already an integer)
##### roundfloor(number):
	round towards the nearest integer, breaking ties towards −∞
##### roundceil(number):
	round towards the nearest integer, breaking ties towards +∞
##### roundtrunc(number):
	round towards the nearest integer, breaking ties towards 0
##### roundaway(number):
	round towards the nearest integer, breaking ties away from 0
##### roundeven(number):
	round towards the nearest integer, breaking ties towards the nearest even integer
	this is the recommended rounding method specified by IEEE. pretty cool.
##### roundodd(number):
	round towards the nearest integer, breaking ties towards the nearest odd integer

# notes

if you need more advanced quantization, my [pyquantize](https://www.github.com/deftasparagusanaconda/pyquantize) project may be useful for you

python has a `round` function that i despise. it has an optional ndigits parameter that, instead of quantizing to any arbitrary scaled lattice, it scales to quantum sizes of 1, 0.1 ,0.01, ... and on top of that, it will return a float if you provide this ndigits parameter, knowing full well that floats do not round decimal digits cleanly.

[retraction]: https://en.wikipedia.org/wiki/Retraction_(topology)
