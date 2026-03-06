from numbers import Number, Integral

def lt(a: Number, b: Number) -> bool:
	'a < b'
	return a < b

def le(a: Number, b: Number) -> bool:
	'a ≤ b'
	return a <= b

def eq(a: Number, b: Number) -> bool:
	'a = b'
	return a == b

def ne(a: Number, b: Number) -> bool:
	'a ≠ b'
	return a != b

def ge(a: Number, b: Number) -> bool:
	'a ≥ b'
	return a >= b

def gt(a: Number, b: Number) -> bool:
	'a > b'
	return a > b

def cmp(a: Number, b: Number) -> Integral:
	'comparison. -1 if a < b, 0 if a == b, 1 if a > b'
	return (a > b) - (a < b)
