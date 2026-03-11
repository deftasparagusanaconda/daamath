from numbers import Complex, Real

def real(z: Complex) -> Real:
	return z.real

def imag(z: Complex) -> Real:
	return z.imag

# mag(z) is not defined because abs(z) should do this.

def arg(z: Complex) -> Real:
	return math.atan2(z.imag, z.real)

from cmath import rect, polar

def conj(z: Complex) -> Complex:
	return z.conjugate()
