from swissmath import fact

from math import pi, isclose
import pytest

def test_fact(x):
	assert fact(0) == 1
	assert fact(1) == 1
	assert fact(2) == 2
	assert fact(3) == 6
	assert fact(4) == 24
	assert fact(5) == 120
	assert fact(6) == 720

	with pytest.raises(TypeError):	# fact must take only int type
		fact(float())

	with pytest.raises(ValueError):	# fact must take only integers ≥0 
		fact(-1)
	
	for i in range(10):
		assert type(fact(i)) == int
