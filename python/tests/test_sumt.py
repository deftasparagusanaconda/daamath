from swissmath import sumt
from math import copysign, isnan
import pytest

pos_inf = float('inf')
neg_inf = float('-inf')

def is_neg_zero(x):
	return x == 0 and copysign(1, x) == -1

"""
def test_sumt():
	assert is_neg_zero(-0.0)
	assert sumt( 0  ) ==  0
	assert sumt( 1  ) ==  1
	assert sumt( 2  ) ==  3
	assert sumt( 3  ) ==  6
	assert sumt( 4  ) ==  10
	assert sumt( 5  ) ==  15
	assert sumt( 0.5) ==  0.375
	assert sumt(-1  ) ==  0
	assert sumt(-2  ) ==  1
	assert sumt(-3  ) ==  3
	assert sumt(-4  ) ==  6
	assert sumt(-0.5) == -0.125
	assert is_neg_zero(sumt(-0.0))
	assert sumt(pos_inf) == pos_inf
	assert sumt(neg_inf) == pos_inf
	assert isnan(sumt(float('nan')))
"""

def test_sumt():
	assert sumt(0) == 0
	assert sumt(1) == 1
	assert sumt(2) == 3
	assert sumt(3) == 6
	assert sumt(4) == 10
	assert sumt(5) == 15
	assert sumt(6) == 21
	assert sumt(10**10) == 50000000005000000000	# ensure that no float trickery is involved

	with pytest.raises(TypeError):	# sumt must take only int type
		sumt(float())

	with pytest.raises(ValueError):	# sumt must take only integers ≥0 
		sumt(-1)
	
	for i in range(10):
		assert type(sumt(i)) == int

	for i in range(1, 101):	# big inputs test
		assert sumt(10**i) == 5*10**(i*2-1) + 5*10**(i-1)
