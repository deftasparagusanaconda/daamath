from operator import inv as bit_not
from operator import and_ as bit_and

def bit_nand(a: int, b: int) -> int:
	'not(and(a, b))'
	return ~(a & b)

from operator import or_ as bit_or

def bit_nor(a: int, b: int) -> int:
	'not(or(a, b))'
	return ~(a | b)

from operator import xor as bit_xor

def bit_nxor(a: int, b: int) -> int:
	'not(xor(a, b))'
	return ~(a ^ b)

def bit_imp(a: int, b: int) -> int:
	'a → b, ¬a ∨ b, material implication'
	return ~(a) | b

def bit_nimp(a: int, b: int) -> int:
	'¬(a → b), a ∧ ¬b, only a'
	return a & (~b)

def bit_con(a: int, b: int) -> int:
	'a ← b, a ∨ ¬b, converse implication'
	return a | (~b)

def bit_ncon(a: int, b: int) -> int:
	'¬(a ← b), ¬a ∧ b, only b'
	return ~(a) & b
