# these are numbers that can be derived algebraically from other numbers. they are simply for performance, and less cluttering up of expressions
# why dont we store neg versions? because negating a float doesnt involve rounding, but other operations involve rounding

ONE_BY_E   =	0.36787944117144232159552377016146086744679191851029413502330656097927063236733467	# 1 / e
ONE_BY_TAU = 0.15915494309189533576888376337251436203482285175580162802194945132510166927876223	# 1 / τ
ONE_BY_PI  = 0.31830988618379067153776752674502872406964570351160325604389890265020333855752447	# p / π

# heres the lattice to make:
# (pow, root, exp, log) * (e, pi, tau, 2, 3, 10) * (normal, reciproal)
POWE_E          = 15.154262241479264189760430272629911905308899820020620483863635630803466044870802	# e ^ e
POWE_TAU        = 535.49165552476473650304932958904718146115729373573175166515877877423341520638973
POWE_PI         = 23.140692632779269005729086367948547379906382699926726622137050436520922599040514	# e ^ π
ROOT2_2         = 1.4142135623730951
ROOT2_3         = 1.7320508075688772
LOGE_2           = 0.6931471805599453
LOGE_10          = 2.302585092994046

ONE_BY_ROOT2_5        = 0.44721359549995793928183473374625524708812367192230514485417944908210418512756098   # 1 / √5

ZETA_1         = ...
ZETA_2         = ...
ZETA_3         = 1.20205690315959428539
ZETA_4         = ...

'''
we group these based on the complexity of their expression tree. simpler ones appear first
            ONE_BY   TWO_BY
     E      1 /  E   2 /  E     E      
    √E      1 / √E   2 / √E     ROOT2_E
     E²     1 /  E²  2 /  E²    POW2_E
     2ᴱ     1 /  2ᴱ  2 /  2ᴱ    EXP2_E
log₂(E)                         LOG2_E
'''
