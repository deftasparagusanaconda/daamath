from swissmath import fact

from math import pi, isclose

def test_fact(x):
	assert fact(0) == 1
	assert fact(1) == 1
	assert fact(2) == 2
	assert fact(3) == 6
	assert fact(4) == 24
	assert fact(5) == 120
	assert fact(6) == 720
	assert isclosefact(-1)
