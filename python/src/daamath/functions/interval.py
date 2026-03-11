# …|… 
# ABC 
# 000 ⊥     {       } same as ⋁(                   )
# 001 x > B {      >} same as ⋁(              x > B)
# 010 x = B {   =,  } same as ⋁(       x = B,      )
# 100 x < B {<,     } same as ⋁(x < B,             )
# 011 x ≥ B {   =, >} same as ⋁(       x = B, x > B)
# 101 x ≠ B {<,    >} same as ⋁(x < B,        x > B)
# 110 x ≤ B {<, =,  } same as ⋁(x < B, x = B,      )
# 111 ⊤     {<, =, >} same as ⋁(x < B, x = B, x > B)
#
# …|…|… 
# ABCDE <|, |+
# 00000         ⊥         {         } (trivial)
# 
# 00001           (x > D) (simple)
# 00010           (x = D) (simple)
# 00100 (B < x) ∧ (x < D) (shorthand: B < x < D) (x ∈ (B, D))
# 01000 (B = x)           (simple)
# 10000 (B > x)           (simple)
# 
# 00011           (x ≥ D) (simple)
# 00101 (B > x) ∧ (x ≠ D) (shorthand: B > x ≠ D)
# 00110 (B < x) ∧ (x ≤ D) (shorthand: B < x ≤ D) (x ∈ (B, D])
# 01001 (B = x) ∨ (x > D) 
# 01010 (B = x) ∨ (x = D) 
# 01100 (B ≤ x) ∧ (x < D) (shorthand: B ≤ x < D) (x ∈ [B, D))
# 10001 (B < x) ∨ (x > D) 
# 10010 (B > x) ∨ (x = D) 
# 10100 (B ≠ x) ∨ (x < D) 
# 11000 (B ≥ x)           (simple)
# 
# 00111 (B < x)           (simple)
# 01011 (B = x) ∨ (x ≥ D) 
# 01101 (B ≤ x) ∧ (x ≠ D) (shorthand: B ≤ x ≠ D)
# 01110 (B ≤ x) ∧ (x ≤ D) (shorthand: B ≤ x ≤ D) (x ∈ [B, D])
# 10011 (B > x) ∨ (x ≥ D) 
# 10101 (B ≠ x) ∧ (x ≠ D) (shorthand: B ≠ x ≠ D)
# 10110 (B ≠ x) ∨ (x ≤ D) 
# 11001 (B ≤ x) ∨ (x > D) 
# 11010 (B ≤ x) ∨ (x = D) 
# 11100           (x < D) (simple)
# 
# 01111 (B ≤ x)           (simple)
# 10111 (B ≠ x)           (simple)
# 11011 (B ≥ x) ∨ (x ≤ D) B > x 
# 11101           (x ≠ D) (simple)
# 11110           (x ≤ D) (simple)
# 
# 11111         ⊤         (trivial)
# ABCDE 
# …|…|… 
# 
# [], [), (], () are just 01110, 01100, 00110, 00100. this is pretty lame.
# 
# out of these, <, ≤, =, ≠, ≥, >, [], [), (], () are useful

from numbers import Real

def lt(a: Real, b: Real) -> bool:
	'a < b'
	return a < b

def le(a: Real, b: Real) -> bool:
	'a ≤ b'
	return a <= b

def eq(a: Real, b: Real) -> bool:
	'a = b'
	return a == b

def ne(a: Real, b: Real) -> bool:
	'a ≠ b'
	return a != b

def ge(a: Real, b: Real) -> bool:
	'a ≥ b'
	return a >= b

def gt(a: Real, b: Real) -> bool:
	'a > b'
	return a > b

def oo(x: Real, a: Real, b: Real) -> bool:
	'a < x < b, x ∈ (a, b)'
	return a < x < b

def oc(x: Real, a: Real, b: Real) -> bool:
	'a < x ≤ b, x ∈ (a, b]'
	return a < x <= b

def co(x: Real, a: Real, b: Real) -> bool:
	'a ≤ x < b, x ∈ [a, b)'
	return a <= x < b

def cc(x: Real, a: Real, b: Real) -> bool:
	'a ≤ x ≤ b, x ∈ [a, b]'
	return a <= x <= b

# yeah.. i might work on extending this one day
