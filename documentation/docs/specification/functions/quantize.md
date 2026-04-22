# quantization

these are [idempotent](https://en.wikipedia.org/wiki/Idempotence#Idempotent_functions) functions that map a domain to a proper subset of that domain, optionally minimizing the metric distance from the input to the output. 

i still dont know what generalizes these (im working on it!) so daamath will blindly ship these for now. they will not be frozen in the API.

![neat thing i made!](diagrams/daamath-quantize.drawio.svg)

## API implementation

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

## type signature

these functions take in a real number, and return an integer. 

## notes

if you need more advanced quantization, the [pyquantize](https://www.github.com/deftasparagusanaconda/pyquantize) project may be useful for you

python has a `round` function that i despise. it has an optional ndigits parameter that, instead of quantizing to any arbitrary scaled lattice, it scales to quantum sizes of 1, 0.1 ,0.01, ... and on top of that, it will return a float if you provide this ndigits parameter, knowing full well that floats do not round decimal digits cleanly.
