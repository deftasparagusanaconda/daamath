# hey! you! yeah, you! daa!
#
# also, implement vector products like dot product, cross product (just a compositon of wedge product and hodge star. also, in 3D and 7D only! because they tie with quaternions and octonions, but none higher. no more normed algebrae after that), wedge product, 

from . import hyperoperations, arithmetic, complex, complex_extra, trigonometry, trigonometry_extra, logic, order, combinatoric, variadic, quantization, sigmoids, mapping, tensor, miscellaneous

from .hyperoperations import succ, pred, add, sub, bus, mul, div, vid, pow, log, root
#from .hyperoperations import h0c, h0b, h1c, h1b, h2c, h2b, h3c, h3b, h3a, h4c, h4b, h4a
#from .arithmetic import h1b_0, h2b_1, h3c_e, h3c_2, h3c_10, h3b__e, h3b__2, h3b__10, h3c__2, h3c__3, h3a__2, h3a__3, h2b_1_h3c__2, h2b_1_h3c__3, h2b_1_h3a__2, h2b_1_h3a__3, h1c_h2c, h1b_h3c_e__1, h3b_h1c_1__e
from .arithmetic import ainv, minv, sq, cb, sqrt, cbrt, rsq, rcb, rsqrt, rcbrt, exp, exp2, exp10, ln, log2, log10, expm1, ln1p

from .complex import real, imag, arg, rect, polar, conj
from .complex_extra import cis

from .trigonometry import sin, cos, tan, cot, sec, csc, asin, acos, atan, acot, asec ,acsc, sinh, cosh, tanh, coth, sech, csch, asinh, acosh, atanh, acoth, asech, acsch
#from .trigonometry import croh, crah, croa, crao, crha, crho, csoh, csah, csoa, csao, csha, csho, hroh, hrah, hroa, hrao, hrha, hrho, hsoh, hsah, hsoa, hsao, hsha, hsho
from .trigonometry_extra import csoh2, csah2, csoa2, csao2, csha2, csho2, h2b_croh_S_S

from .logic import not_, and_, or_, xor, imp, con, nand, nor, nxor, nimp, ncon
#from .logic import tf, ffft, fttt, fttf, ttft, tftt, tttf, tfff, tfft, fftf, ftff
#from .order import iee, iie, eie, iei, eii, eei, eeiee, eeiie, eiiee, eiiie
#from .order import cp, nc, so, ns, lt, le, eq, ne, ge, gt, oo, oc, co, cc, ncc, noc, nco, noo
from .order import nc, lt, gt, eq, le, ge, so, ns, na, nb, ne, ng, nl, cp, oo, oc, co, cc, ncc, nco, noc, noo

from .variadic import vand, vor, vadd, vmul, mean, mean__h1b_0_inf, mean__h1b_0_1, mean__0, mean__1, mean__2, mean__3, mean__inf, vparallel
from .combinatoric import fact, sumt, comb, perm, gcd, lcm
from .quantization import floor, ceil, trunc, away, even, odd, nearest_floor, nearest_ceil, nearest_trunc, nearest_away, nearest_even, nearest_odd
from .sigmoids import sigmoid_tan, sigmoid_tanh
from .mapping import lerp, unlerp, map, fixed_log, fixed_exp, soft_log, soft_exp
from .tensor import norm, normalize, clamp, norm__2, normalize__2
from .miscellaneous import ifelse, quot, rem, fma, fsd, ln_div, mul_exp, div_exp

from .solvers import roots, coeffs
