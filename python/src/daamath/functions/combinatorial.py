from math import factorial as fact

def sumt(x):
	"sum of all numbers from 1 to x, using x * (x + 1) / 2 (gauss' formula). like factorial but with addition."
	return (x * (x + 1)) // 2 if isinstance(x, int) else (x * (x + 1)) / 2

from math import comb, perm
