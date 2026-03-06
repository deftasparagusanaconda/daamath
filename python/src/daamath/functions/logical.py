# boolean ----------------------------------------------------------------------

from operator import and_

def nand(a: bool, b: bool) -> bool:
	'not(and(a, b))'
	return not(a and b)

from operator import or_

def nor(a: bool, b: bool) -> bool:
	'not(or(a, b))'
	return not(a or b)

from operator import xor

def xnor(a: bool, b: bool) -> bool:
	'not(xor(a, b))'
	return not(xor(a, b))

def imp(a: bool, b: bool) -> bool:
	'a → b, ¬a ∨ b, material implication'
	return not a or b

def nimp(a: bool, b: bool) -> bool:
	'¬(a → b), a ∧ ¬b, only a'
	return a and not b

def con(a: bool, b: bool) -> bool:
	'a ← b, a ∨ ¬b, converse implication'
	return a or not b

def ncon(a: bool, b: bool) -> bool:
	'¬(a ← b), ¬a ∧ b, only b'
	return not a and b
