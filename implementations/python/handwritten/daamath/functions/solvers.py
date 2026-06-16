from numbers import Number
from collections.abc import Iterable, Sequence

def coeffs(roots: Iterable[float]) -> Sequence[float]:
	"""
    get coefficients of a polynomial, given its roots

	(x - r1)(x - r2)...(x - rn)
	= c0*x^n + c1*x^(n-1) + ... + cn

	i dont like this. why? because as it iterates through the things, it starts running into a lot of 
	"""
	coefficients = [1]

	for r in roots:
		new = [0] * (len(coefficients) + 1)
		for i, c in enumerate(coefficients):
			new[i]	 += c		# multiply by x
			new[i + 1] -= r * c	# multiply by -r
		coefficients = new

	return coefficients

def roots(coeffs: Iterable[Number]) -> Iterable[Number]:
    'get roots of a polynomial given its coefficients'
    raise NotImplementedError
