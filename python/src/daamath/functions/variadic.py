from collections.abc import Iterable

def vand(iterable: Iterable[bool]) -> bool:
	'variadic AND gate'
	return all(iterable)

def vor(iterable: Iterable[bool]) -> bool:
	'variadic OR gate'
	return any(iterable)

def vadd(iterable: Iterable[int | float | complex]) -> int | float | complex:
	'variadic addition'
	return sum(iterable)

def vmul(iterable: Iterable[int | float | complex]) -> int | float | complex:
	'variadic multiplication'
	return _math.prod(iterable)

def vparallel(iterable: Iterable[int | float | complex]) -> int | float | complex: 
	'variadic parallel'

	n = len(iterable)

	if n == 0:
		return 0
	if n == 1:
		return iterable[0]

	numerator = _math.prod(iterable)

	# sum of products of n-1 elements
	#denominator = sum(prod(xs[j] for j in range(n) if j != i) for i in range(n))
	denominator = sum(_math.prod(i) for i in _combinations(iterable, n - 1))

	return numerator / denominator

