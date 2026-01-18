from typing import Generic as _Generic, TypeVar as _TypeVar
from dataclasses import dataclass as _dataclass

class Tern(int):
	"""a ternary truth value. due to pragmatic reasons, we subclass from int and use -1, 0, 1, like how bool subclasses int and uses 0, 1

	like bool, anything zero is 0, anything non-zero is 1, but unlike bool, anything non-zero and negative is -1

	like bool, arithmetic is inherited from its int superclass


	the constructor acts as both a signum and a cmp function
	"""
	def __new__(cls, value, reference = 0):
		truth = (value > reference) - (value < reference)
		return super().__new__(cls, truth)

	def __repr__(self) -> str:
		return {-1: '-True', 0: 'False', 1: 'True'}[self]

_R = _TypeVar('R', bool, Tern)
_I = _TypeVar('I', bool, Tern)

@_dataclass(frozen=True)
class ComplexTruth(_Generic[_R, _I]):
	real: _R
	imag: _I

	def __repr__(self) -> str:
		return f"({self.real}{self.imag:+}j)"
