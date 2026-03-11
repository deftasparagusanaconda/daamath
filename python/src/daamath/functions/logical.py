'''
AB
00 Neither
01 B
10 A
11 Two

NBAT 
0000 ⊥     
0001 and   
0010 nimp  
0011 A     
0100 ncon  
0101 B     
0110 xor   
0111 or    
1000 nor   
1001 nxor  
1010 not B 
1011 con   
1100 not A 
1101 imp   
1110 nand  
1111 ⊤     
'''

from operator import not_ as bool_not
from operator import and_ as bool_and
from operator import or_ as bool_or
from operator import xor as bool_xor

def bool_nimp(a: bool, b: bool) -> bool:
	'¬(a → b), a ∧ ¬b, only a'
	return a and not b

def bool_ncon(a: bool, b: bool) -> bool:
	'¬(a ← b), ¬a ∧ b, only b'
	return not a and b

def bool_nand(a: bool, b: bool) -> bool:
	'not(and(a, b))'
	return not (a and b)

def bool_nor(a: bool, b: bool) -> bool:
	'not(or(a, b))'
	return not (a or b)

def bool_nxor(a: bool, b: bool) -> bool:
	'not(xor(a, b))'
	return not bool_xor(a, b)

def bool_imp(a: bool, b: bool) -> bool:
	'a → b, ¬a ∨ b, material implication'
	return not a or b

def bool_con(a: bool, b: bool) -> bool:
	'a ← b, a ∨ ¬b, converse implication'
	return a or not b
