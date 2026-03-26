from swissmath import clt, cle, ceq, cne, cge, cgt

import pytest

pos_inf = float('inf')
neg_inf = float('-inf')
pos_zero = 0.0
neg_zero = -0.0
nan = float('nan')

def test_clt():
	assert type(clt(int(), int())) == bool
	assert type(clt(int(), float())) == bool
	assert type(clt(float(), int())) == bool
	assert type(clt(float(), float())) == bool

	assert type(clt(0, complex())) == tuple
	assert type(clt(complex(), 0)) == tuple
	assert type(clt(complex(), complex())) == tuple

	numbers = [-1, 0, 1]
	expects = [[False,  True,  True], 
			   [False, False,  True], 
			   [False, False, False]]

	for i,a in enumerate(numbers):
		for j,b in enumerate(numbers):
			assert clt(a,b) == expects[i][j]

	for i,a in enumerate(numbers):
		for j,b in enumerate(numbers):
			for k,c in enumerate(numbers):
				for l,d in enumerate(numbers):
					assert clt(complex(a,b),complex(c,d)) == (expects[i][j], expects[k][l])

	assert clt( 1,   1.0) == False
	assert clt(-0.0, 0.0) == False
	assert clt( 0.0,-0.0) == False
	assert clt(pos_inf, pos_inf) == False
	assert clt(pos_inf, neg_inf) == False
	assert clt(neg_inf, pos_inf) == True
	assert clt(neg_inf, neg_inf) == False
	assert clt(0,nan) == False
	assert clt(nan,0) == False
	assert clt(nan,nan) == False
	
def test_cle():
	assert type(cle(int(), int())) == bool
	assert type(cle(int(), float())) == bool
	assert type(cle(float(), int())) == bool
	assert type(cle(float(), float())) == bool

	assert type(cle(0, complex())) == tuple
	assert type(cle(complex(), 0)) == tuple
	assert type(cle(complex(), complex())) == tuple

	numbers = [-1, 0, 1]
	expects = [[ True,  True, True], 
			   [False,  True, True], 
			   [False, False, True]]

	for i,a in enumerate(numbers):
		for j,b in enumerate(numbers):
			assert clt(a,b) == expects[i][j]

	for i,a in enumerate(numbers):
		for j,b in enumerate(numbers):
			for k,c in enumerate(numbers):
				for l,d in enumerate(numbers):
					assert clt(complex(a,b),complex(c,d)) == (expects[i][j], expects[k][l])

	assert cle( 1,   1.0) == True
	assert cle(-0.0, 0.0) == True
	assert cle( 0.0,-0.0) == True
	assert cle(pos_inf, pos_inf) == True
	assert cle(pos_inf, neg_inf) == False
	assert cle(neg_inf, pos_inf) == True
	assert cle(neg_inf, neg_inf) == True
	assert cle(0,nan) == False
	assert cle(nan,0) == False
	assert cle(nan,nan) == False

def test_ceq():
	assert type(ceq(int(), int())) == bool
	assert type(ceq(int(), float())) == bool
	assert type(ceq(float(), int())) == bool
	assert type(ceq(float(), float())) == bool

	assert type(ceq(0, complex())) == tuple
	assert type(ceq(complex(), 0)) == tuple
	assert type(ceq(complex(), complex())) == tuple

	numbers = [-1, 0, 1]
	expects = [[ True, False, False], 
			   [False,  True, False], 
			   [False, False, True ]]

	for i,a in enumerate(numbers):
		for j,b in enumerate(numbers):
			assert clt(a,b) == expects[i][j]

	for i,a in enumerate(numbers):
		for j,b in enumerate(numbers):
			for k,c in enumerate(numbers):
				for l,d in enumerate(numbers):
					assert clt(complex(a,b),complex(c,d)) == (expects[i][j], expects[k][l])

	assert ceq( 1,   1.0) == True
	assert ceq(-0.0, 0.0) == True	# by IEEE-754 standards
	assert ceq( 0.0,-0.0) == True
	assert ceq(pos_inf, pos_inf) == True
	assert ceq(pos_inf, neg_inf) == False
	assert ceq(neg_inf, pos_inf) == False
	assert ceq(neg_inf, neg_inf) == True
	assert ceq(0,nan) == False
	assert ceq(nan,0) == False
	assert ceq(nan,nan) == False

	a = complex(2,3)
	b = complex(4,3)
	assert ceq(a,b) == ceq(b,a) == False

	c = complex(4,3)

	assert ceq(b,c) == ceq(c,b) == True

def test_cne():
	assert type(cne(int(), int())) == bool
	assert type(cne(int(), float())) == bool
	assert type(cne(float(), int())) == bool
	assert type(cne(float(), float())) == bool

	assert type(cne(0, complex())) == tuple
	assert type(cne(complex(), 0)) == tuple
	assert type(cne(complex(), complex())) == tuple

	numbers = [-1, 0, 1]
	expects = [[False,  True,  True], 
			   [ True, False,  True], 
			   [ True, True , False]]

	for i,a in enumerate(numbers):
		for j,b in enumerate(numbers):
			assert clt(a,b) == expects[i][j]

	for i,a in enumerate(numbers):
		for j,b in enumerate(numbers):
			for k,c in enumerate(numbers):
				for l,d in enumerate(numbers):
					assert clt(complex(a,b),complex(c,d)) == (expects[i][j], expects[k][l])

	assert cne( 1,   1.0) == False
	assert cne(-0.0, 0.0) == False
	assert cne( 0.0,-0.0) == False
	assert cne(pos_inf, pos_inf) == False
	assert cne(pos_inf, neg_inf) == True
	assert cne(neg_inf, pos_inf) == True
	assert cne(neg_inf, neg_inf) == False
	assert cne(0,nan) == True
	assert cne(nan,0) == True
	assert cne(nan,nan) == True

	a = complex(2,3)
	b = complex(4,3)
	assert cne(a,b) == cne(b,a) == True

	c = complex(4,3)
	assert cne(b,c) == cne(c,b) == False

def test_cge():
	assert type(cge(int(), int())) == bool
	assert type(cge(int(), float())) == bool
	assert type(cge(float(), int())) == bool
	assert type(cge(float(), float())) == bool

	assert type(cge(0, complex())) == tuple
	assert type(cge(complex(), 0)) == tuple
	assert type(cge(complex(), complex())) == tuple

	numbers = [-1, 0, 1]
	expects = [[ True, False, False], 
			   [ True,  True, False], 
			   [ True,  True,  True]]

	for i,a in enumerate(numbers):
		for j,b in enumerate(numbers):
			assert clt(a,b) == expects[i][j]

	for i,a in enumerate(numbers):
		for j,b in enumerate(numbers):
			for k,c in enumerate(numbers):
				for l,d in enumerate(numbers):
					assert clt(complex(a,b),complex(c,d)) == (expects[i][j], expects[k][l])

	assert cge( 1,   1.0) == True
	assert cge(-0.0, 0.0) == True
	assert cge( 0.0,-0.0) == True
	assert cge(pos_inf, pos_inf) == True
	assert cge(pos_inf, neg_inf) == True
	assert cge(neg_inf, pos_inf) == False
	assert cge(neg_inf, neg_inf) == True
	assert cge(0,nan) == False
	assert cge(nan,0) == False
	assert cge(nan,nan) == False

def test_cgt():
	assert type(cgt(int(), int())) == bool
	assert type(cgt(int(), float())) == bool
	assert type(cgt(float(), int())) == bool
	assert type(cgt(float(), float())) == bool

	assert type(cgt(0, complex())) == tuple
	assert type(cgt(complex(), 0)) == tuple
	assert type(cgt(complex(), complex())) == tuple

	numbers = [-1, 0, 1]
	expects = [[False, False, False], 
			   [ True, False, False], 
			   [ True,  True, False]]

	for i,a in enumerate(numbers):
		for j,b in enumerate(numbers):
			assert clt(a,b) == expects[i][j]

	for i,a in enumerate(numbers):
		for j,b in enumerate(numbers):
			for k,c in enumerate(numbers):
				for l,d in enumerate(numbers):
					assert clt(complex(a,b),complex(c,d)) == (expects[i][j], expects[k][l])

	assert cgt( 1,   1.0) == False
	assert cgt(-0.0, 0.0) == False
	assert cgt( 0.0,-0.0) == False
	assert cgt(pos_inf, pos_inf) == False
	assert cgt(pos_inf, neg_inf) == True
	assert cgt(neg_inf, pos_inf) == False
	assert cgt(neg_inf, neg_inf) == False
	assert cgt(0,nan) == False
	assert cgt(nan,0) == False
	assert cgt(nan,nan) == False
