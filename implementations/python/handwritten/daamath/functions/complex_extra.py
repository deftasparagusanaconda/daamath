from numbers import Complex, Real

def cis(theta: Real) -> Complex:
	return complex(math.cos(theta), math.sin(theta))
