# TODO: add complex input tests
# TODO: add nan tests

from swissmath import sin, cos, tan, cot, sec, csc, asin, acos, atan, acot, asec, acsc
from swissmath import sinpi, cospi, tanpi, cotpi, secpi, cscpi, asinpi, acospi, atanpi, acotpi, asecpi, acscpi

funcs = [sin, cos, tan, cot, sec, csc, asin, acos, atan, acot, asec, acsc, sinpi, cospi, tanpi, cotpi, secpi, cscpi, asinpi, acospi, atanpi, acotpi, asecpi, acscpi]

pos_inf = float('inf')
neg_inf = float('-inf')

from math import copysign
import pytest

def is_neg_zero(x):
	return x == 0 and copysign(1, x) == -1

def test_io_type():
	for func in funcs:
		assert type(func(int())) in (int, float)
		assert type(func(float())) in (int, float)
		assert type(func(complex())) == complex

def test_sin():
	assert sin(0.0) == 0
	assert is_neg_zero(sin(-0.0))

def test_cos():
	assert cos( 0.0) == 1
	assert cos(-0.0) == 1

def test_tan():
	assert tan(0.0) == 0
	assert is_neg_zero(tan(-0.0))

def test_cot():
	with pytest.raises(ZeroDivisionError):
		cot(0.0)
	with pytest.raises(ZeroDivisionError):
		cot(-0.0)
	
def test_sec():
	assert sec( 0.0) == 1
	assert sec(-0.0) == 1

def test_csc():
	with pytest.raises(ZeroDivisionError):
		csc(0.0)
	with pytest.raises(ZeroDivisionError):
		csc(-0.0)

def test_asin():
	assert asin(0.0) == 0
	assert is_neg_zero(asin(-0.0))

	with pytest.raises(ValueError):
		asin(-1.1)
	with pytest.raises(ValueError):
		asin(1.1)

	asin(-1)
	asin(1)

def test_acos():
	assert acos(1) == 0

	with pytest.raises(ValueError):
		acos(-1.1)
	with pytest.raises(ValueError):
		acos(1.1)

	acos(-1)
	acos(1)

def test_atan():
	assert atan(0.0) == 0
	assert is_neg_zero(atan(-0.0))

	atan(pos_inf)
	atan(neg_inf)
	
def test_acot():
	
