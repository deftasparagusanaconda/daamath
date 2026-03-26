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

# 
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
'''
def tf(a: bool | int | set, *, universe: set = None) -> bool | int | set:
    'not, negation, complement'
    match a:
        case bool(): return not a
        case  int(): return ~a
        case  set(): return universe.difference(a)
        case      _: raise TypeError

def ffft(a: bool | int | set, b: bool | int | set, *, universe: set = None) -> bool | int | set:
    'and, conjunction, intersection'
    match a:
        case bool(): return a and b
        case  int(): return a & b
        case  set(): return a.intersection(b)
        case      _: raise TypeError

def fttt(a: bool | int | set, b: bool | int | set, *, universe: set = None) -> bool | int | set:
    'or, disjunction, union'
    match a:
        case bool(): return a or b
        case  int(): return a | b
        case  set(): return a.union(b)
        case      _: raise TypeError

def fttf(a: bool | int | set, b: bool | int | set, *, universe: set = None) -> bool | int | set:
    'xor, exclusive disjunction, symmetric difference'
    match a:
        case bool(): return a != b
        case  int(): return a ^ b
        case  set(): return a.symmetric_difference(b)
        case      _: raise TypeError()

def ttft(a: bool | int | set, b: bool | int | set, *, universe: set = None) -> bool | int | set:
    'implication'
    match a:
        case bool(): return a <= b
        case  int(): return a | b
        case  set(): raise NotImplementedError
        case      _: raise TypeError()

def tftt(a: bool | int | set, b: bool | int | set, *, universe: set = None) -> bool | int | set:
    'converse implication'
    match a:
        case bool(): return a >= b
        case  int(): return a | b
        case  set(): raise NotImplementedError
        case      _: raise TypeError()

def tttf(a: bool | int | set, b: bool | int | set, *, universe: set = None) -> bool | int | set:
    'nand, not(and)'
    match a:
        case bool(): return not (a and b)
        case  int(): return ~(a & b)
        case  set(): raise NotImplementedError
        case      _: raise TypeError()
    
def tfff(a: bool | int | set, b: bool | int | set, *, universe: set = None) -> bool | int | set:
    'nor, not(or)'
    match a:
        case bool(): return not(a or b)
        case  int(): return ~(a | b)
        case  set(): raise NotImplementedError
        case      _: raise TypeError()

def tfft(a: bool | int | set, b: bool | int | set, *, universe: set = None) -> bool | int | set:
    'nxor, xnor, not(xor)'
    match a:
        case bool(): return a == b
        case  int(): return ~(a ^ b)
        case  set(): raise NotImplementedError
        case      _: raise TypeError()

def fftf(a: bool | int | set, b: bool | int | set, *, universe: set = None) -> bool | int | set:
    'not(imp)'
    match a:
        case bool(): return a > b
        case  int(): return a & ~b
        case  set(): return a.difference(b)
        case      _: raise TypeError()

def ftff(a: bool | int | set, b: bool | int | set, *, universe: set = None) -> bool | int | set:
    'not(con)'
    match a:
        case bool(): return a < b
        case  int(): return ~a & b
        case  set(): return b.difference(a)
        case      _: raise TypeError()

