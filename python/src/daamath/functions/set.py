# unlike boolean algebra, we have to worry about the universe set
# 
# UAIB (universe, A, intersection, B)
# 0000 ∅
# 0001 ncon
# 0010 and
# 0011 B
# 0100 nimp
# 0101 xor
# 0110 A
# 0111 or
# 1000 nor
# 1001 not A
# 1010 nxor
# 1011 imp
# 1100 not B
# 1101 nand
# 1110 con
# 1111 U

# UBAI (universe, B, A, intersection)
# 0000 none  (empty set)
# 0001 and   (intersection)
# 0010 fst   (A - B)
# 0011 A     (set A)
# 0100 snd   (B - A)
# 0101 B     (set B)
# 0110 xor   (symmetric difference) 
# 0111 or    (union)
# 1000 nor   (complement of union)
# 1001 nxor  (complement of symmetric difference)
# 1010 not B (complement of set B)
# 1011 nsnd  (complement of B - A)
# 1100 not A (complement of set A)
# 1101 nfst  (complement of A - B)
# 1110 nand  (complement of intersection)
# 1111 all

def set_not(a: set, u: set) -> set:
	return u.difference(a)

def set_and(a: set, b: set) -> set:
	return a.intersection(b)

def set_nand(a: set, b: set) -> set:
	raise NotImplementedError

def set_or(a: set, b: set) -> set:
	return a.union(b)

def set_nor(a: set, b: set) -> set:
	raise NotImplementedError

def set_xor(a: set, b: set) -> set:
	return a.symmetric_difference(b)

def set_nxor(a: set, b: set) -> set:
	raise NotImplementedError

def set_imp(a: set, b: set) -> set:
	'a → b, ¬a ∨ b, material implication'
	raise NotImplementedError

def set_nimp(a: set, b: set) -> set:
	'¬(a → b), a ∧ ¬b, only a'
	return a.difference(b)

def set_con(a: set, b: set) -> set:
	'a ← b, a ∨ ¬b, converse implication'
	raise NotImplementedError

def set_ncon(a: set, b: set) -> set:
	'¬(a ← b), ¬a ∧ b, only b'
	return b.difference(a)
