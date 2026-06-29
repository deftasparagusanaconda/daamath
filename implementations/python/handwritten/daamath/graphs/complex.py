from numbers import Complex, Real
import math, cmath

def real(z: Complex) -> Real:
	return z.real

def imag(z: Complex) -> Real:
	return z.imag

# mag(z) is not defined because abs(z) should do this.

from cmath import phase as arg
from cmath import rect, polar

def conj(z: Complex) -> Complex:
	return z.conjugate()
