#from swissmath import lt, le, eq, ne, ge, gt, hadlt, hadle, hadeq, hadne, hadge, hadgt

import pytest

lt = lambda a,b: a<b
le = lambda a,b: a<=b
eq = lambda a,b: a==b
ne = lambda a,b: a!=b
ge = lambda a,b: a>=b
gt = lambda a,b: a>b

pos_inf = float('inf')
neg_inf = float('-inf')
pos_zero = 0.0
neg_zero = -0.0
nan = float('nan')

def test_lt():
	assert type(lt(int(), int())) == bool
	assert type(lt(int(), float())) == bool
	assert type(lt(float(), int())) == bool
	assert type(lt(float(), float())) == bool

	with pytest.raises(TypeError):
		lt(0, complex())
		lt(complex(), 0)
		lt(complex(), complex())
	
	assert lt(-1, -1) == False
	assert lt(-1,  0) == True
	assert lt(-1,  1) == True
	assert lt( 0, -1) == False
	assert lt( 0,  0) == False
	assert lt( 0,  1) == True
	assert lt( 1, -1) == False
	assert lt( 1,  0) == False
	assert lt( 1,  1) == False
	assert lt( 1,   1.0) == False
	assert lt(-0.0, 0.0) == False
	assert lt( 0.0,-0.0) == False
	assert lt(pos_inf, pos_inf) == False
	assert lt(pos_inf, neg_inf) == False
	assert lt(neg_inf, pos_inf) == True
	assert lt(neg_inf, neg_inf) == False
	assert lt(0,nan) == False
	assert lt(nan,0) == False
	assert lt(nan,nan) == False

def test_le():
	assert type(le(int(), int())) == bool
	assert type(le(int(), float())) == bool
	assert type(le(float(), int())) == bool
	assert type(le(float(), float())) == bool

	with pytest.raises(TypeError):
		le(0, complex())
		le(complex(), 0)
		le(complex(), complex())

	assert le(-1, -1) == True
	assert le(-1,  0) == True
	assert le(-1,  1) == True
	assert le( 0, -1) == False
	assert le( 0,  0) == True
	assert le( 0,  1) == True
	assert le( 1, -1) == False
	assert le( 1,  0) == False
	assert le( 1,  1) == True
	assert le( 1,   1.0) == True
	assert le(-0.0, 0.0) == True
	assert le( 0.0,-0.0) == True
	assert le(pos_inf, pos_inf) == True
	assert le(pos_inf, neg_inf) == False
	assert le(neg_inf, pos_inf) == True
	assert le(neg_inf, neg_inf) == True
	assert le(0,nan) == False
	assert le(nan,0) == False
	assert le(nan,nan) == False

def test_eq():
	assert type(eq(int(), int())) == bool
	assert type(eq(int(), float())) == bool
	assert type(eq(float(), int())) == bool
	assert type(eq(float(), float())) == bool

	assert eq(-1, -1) == True
	assert eq(-1,  0) == False
	assert eq(-1,  1) == False
	assert eq( 0, -1) == False
	assert eq( 0,  0) == True
	assert eq( 0,  1) == False
	assert eq( 1, -1) == False
	assert eq( 1,  0) == False
	assert eq( 1,  1) == True
	assert eq( 1,   1.0) == True
	assert eq(-0.0, 0.0) == True	# by IEEE-754 standards
	assert eq( 0.0,-0.0) == True
	assert eq(pos_inf, pos_inf) == True
	assert eq(pos_inf, neg_inf) == False
	assert eq(neg_inf, pos_inf) == False
	assert eq(neg_inf, neg_inf) == True
	assert eq(0,nan) == False
	assert eq(nan,0) == False
	assert eq(nan,nan) == False

	a = complex(2,3)
	b = complex(4,3)
	assert eq(a,b) == eq(b,a) == False

	c = complex(4,3)

	assert eq(b,c) == eq(c,b) == True

def test_ne():
	assert type(ne(int(), int())) == bool
	assert type(ne(int(), float())) == bool
	assert type(ne(float(), int())) == bool
	assert type(ne(float(), float())) == bool

	assert ne(-1, -1) == False
	assert ne(-1,  0) == True
	assert ne(-1,  1) == True
	assert ne( 0, -1) == True
	assert ne( 0,  0) == False
	assert ne( 0,  1) == True
	assert ne( 1, -1) == True
	assert ne( 1,  0) == True
	assert ne( 1,  1) == False
	assert ne( 1,   1.0) == False
	assert ne(-0.0, 0.0) == False
	assert ne( 0.0,-0.0) == False
	assert ne(pos_inf, pos_inf) == False
	assert ne(pos_inf, neg_inf) == True
	assert ne(neg_inf, pos_inf) == True
	assert ne(neg_inf, neg_inf) == False
	assert ne(0,nan) == True
	assert ne(nan,0) == True
	assert ne(nan,nan) == True

	a = complex(2,3)
	b = complex(4,3)
	assert ne(a,b) == ne(b,a) == True

	c = complex(4,3)
	assert ne(b,c) == ne(c,b) == False

def test_ge():
	assert type(ge(int(), int())) == bool
	assert type(ge(int(), float())) == bool
	assert type(ge(float(), int())) == bool
	assert type(ge(float(), float())) == bool

	with pytest.raises(TypeError):
		ge(0, complex())
		ge(complex(), 0)
		ge(complex(), complex())

	assert ge(-1, -1) == True
	assert ge(-1,  0) == False
	assert ge(-1,  1) == False
	assert ge( 0, -1) == True
	assert ge( 0,  0) == True
	assert ge( 0,  1) == False
	assert ge( 1, -1) == True
	assert ge( 1,  0) == True
	assert ge( 1,  1) == True
	assert ge( 1,   1.0) == True
	assert ge(-0.0, 0.0) == True
	assert ge( 0.0,-0.0) == True
	assert ge(pos_inf, pos_inf) == True
	assert ge(pos_inf, neg_inf) == True
	assert ge(neg_inf, pos_inf) == False
	assert ge(neg_inf, neg_inf) == True
	assert ge(0,nan) == False
	assert ge(nan,0) == False
	assert ge(nan,nan) == False

def test_gt():
	assert type(gt(int(), int())) == bool
	assert type(gt(int(), float())) == bool
	assert type(gt(float(), int())) == bool
	assert type(gt(float(), float())) == bool

	with pytest.raises(TypeError):
		gt(0, complex())
		gt(complex(), 0)
		gt(complex(), complex())

	assert gt(-1, -1) == False
	assert gt(-1,  0) == False
	assert gt(-1,  1) == False
	assert gt( 0, -1) == True
	assert gt( 0,  0) == False
	assert gt( 0,  1) == False
	assert gt( 1, -1) == True
	assert gt( 1,  0) == True
	assert gt( 1,  1) == False
	assert gt( 1,   1.0) == False
	assert gt(-0.0, 0.0) == False
	assert gt( 0.0,-0.0) == False
	assert gt(pos_inf, pos_inf) == False
	assert gt(pos_inf, neg_inf) == True
	assert gt(neg_inf, pos_inf) == False
	assert gt(neg_inf, neg_inf) == False
	assert gt(0,nan) == False
	assert gt(nan,0) == False
	assert gt(nan,nan) == False
