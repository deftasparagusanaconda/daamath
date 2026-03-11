from typing import Generic as _Generic, TypeVar as _TypeVar
from abc import ABC as _ABC, abstractmethod as _abstractmethod

class Tern(int):
	"""a ternary truth value. one of {False, True, -True}. due to pragmatic reasons, we subclass from int and use 0, 1, -1, like how bool subclasses int and uses 0, 1

	like bool, only three instances ever exist (bool has two)
	like bool, it is subclassed from int
	like bool, anything zero is False
	like bool, anything non-zero and positive is True
	like bool, arithmetic is inherited from its int superclass
	like bool, the constructor casts values to Tern
	unlike bool, anything non-zero and negative is -True
	
	the constructor acts as both a signum and a cmp function
	"""

	def __repr__(self) -> str:
		return ('False', 'True', '-True')[self]
		# same as:
		# return {0: 'False', 1: 'True', -1: '-True'}[self]

# define 'singleton' instances by bootstrapping with int
Tern.__instances__ = (int.__new__(Tern, 0), int.__new__(Tern, 1), int.__new__(Tern, -1))

# override constructor to return one of the three instances
def _Tern_constructor(cls, value = 0, reference = 0):
	truth: int = (value > reference) - (value < reference)
	return cls.__instances__[truth] 
Tern.__new__ = _Tern_constructor

# ------------------------------------------------------------------------------

class ComplexTruth(complex):
	'a truth value, but with real and imaginary parts. Algebraically, multiplying a truth value with the imaginary unit does not make any sense, but it can still carry structure, like how integers are just a 2-tuple of naturals, but with equivalence classes and special operations'
	
	def __new__(cls, *args, **kwargs):
		if cls is ComplexTruth:
			raise TypeError("ComplexTruth is abstract")
		return super().__new__(cls, *args)

# how do i prevent users from instantiating ComplexTruth?

# ------------------------------------------------------------------------------

class ComplexBool(ComplexTruth):
	def __repr__(self) -> str:
		return ('(False', '(True')[int(self.real)] + ('+False*j)', '+True*j)')[int(self.imag)]

# define 'singleton' instances by bootstrapping with ComplexTruth
ComplexBool.__instances__: tuple[
				tuple[ComplexBool, ComplexBool], 
				tuple[ComplexBool, ComplexBool]] = (
		(ComplexTruth.__new__(ComplexBool, 0, 0), ComplexTruth.__new__(ComplexBool, 0, 1)),
		(ComplexTruth.__new__(ComplexBool, 1, 0),	ComplexTruth.__new__(ComplexBool, 1, 1)))

# override constructor to return one of these instances
def _ComplexBool_constructor(cls, real: any = 0, imag: any = 0):
	return cls.__instances__[bool(real)][bool(imag)]
ComplexBool.__new__ = _ComplexBool_constructor

# ------------------------------------------------------------------------------

class ComplexTern(ComplexTruth):
	def __repr__(self) -> str:
		return ('(False', '(True', '(-True')[int(self.real)] + ('+False*j)', '+True*j)', '-True*j)')[int(self.imag)]

# define 'singleton' instances by bootstrapping with ComplexTruth
ComplexTern.__instances__: tuple[
				tuple[ComplexTern, ComplexTern, ComplexTern], 
				tuple[ComplexTern, ComplexTern, ComplexTern],
				tuple[ComplexTern, ComplexTern, ComplexTern]] = (
		(ComplexTruth.__new__(ComplexTern,  0,  0), 
		 ComplexTruth.__new__(ComplexTern,  0,  1), 
		 ComplexTruth.__new__(ComplexTern,  0, -1)),

		(ComplexTruth.__new__(ComplexTern,  1,  0), 
		 ComplexTruth.__new__(ComplexTern,  1,  1), 
		 ComplexTruth.__new__(ComplexTern,  1, -1)),

		(ComplexTruth.__new__(ComplexTern, -1,  0), 
		 ComplexTruth.__new__(ComplexTern, -1,  1), 
		 ComplexTruth.__new__(ComplexTern, -1, -1)))

# override constructor to return one of these instances
def _ComplexTern_constructor(cls, real: any = 0, imag: any = 0):
	return cls.__instances__[Tern(real)][Tern(imag)]
ComplexTern.__new__ = _ComplexTern_constructor

# allow __doc__ on str and instances of Number --------------------------------

import numbers

class Str(str):
	...

class Float(float):
	...
