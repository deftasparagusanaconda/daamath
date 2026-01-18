from abc import ABC

class Real(ABC):

class Natural(Real):
	'0, 1, 2, 3, ... stored as an int'
	def __init__(self, value: int):
		if not isinstance(value, int) or value < 0:
			raise ValueError("must be int and ≥ 0")
		super().__init__(value)

	def __str__(self) -> str:
		return str(self.value)

class Integer(Real):
	'0, 1, -1, 2, -2, 3, -3, ... stored as an int'
	def __init__(self, positive: int, negative: int = 0):
		if not isinstance(positive, int) or not isinstance(negative, int):
			raise ValueError("only takes int arguments")
		if negative < 0:
			raise ValueError("only natural numbers allowed")
		super().__init__(positive - negative)
	def __str__(self) -> str:
		return str(self.value)

class Rational(Real):
	'0, 0.1, -0.1, 0.1234, ... stored as a pair of int'
	def __init__(self, numerator: int, denominator: int = 1):
		if not isinstance(numerator, (int, Natural, Integer)) or not isinstance(denominator, int, Natural, Integer):
			raise ValueError("only takes int/Natural/Integer")
		if denominator == 0:
			raise ValueError("denominator may not be zero")
		super().__init__(numerator / denominator)
	def __str__(self) -> str:
		return str(self.value)

class RealFloat(Real):
	'any real number stored as a float'

	def __init__(self, value: float):
		if not isinstance(value, float):
			raise ValueError("only takes float input")
		self.value = value

	def __str__(self) -> str:
		return str(self.value)

class Complex:
	def __init__(self, real: Real, imag: Real):
		self.real: Real = real
		self.imag: Real = imag
	
	
