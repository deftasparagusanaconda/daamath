# hey! you! yeah, you! daa!
#
# also, implement vector products like dot product, cross product (just a compositon of wedge product and hodge star. also, in 3D and 7D only! because they tie with quaternions and octonions, but none higher. no more normed algebrae after that), wedge product, 

from . import hyperoperations, arithmetic_numeric, complex, complex_numeric, trigonometric, trigonometric_numeric, logical, interval, combinatorial, variadic, rounding, sigmoids, mapping, tensor, floating, miscellaneous

from .hyperoperations import inc, dec, add, sub, mul, div, pow, log, root, spow, slog, sroot, hyper
from .arithmetic_numeric import fma, ainv, minv
#from .arithmetic_numeric import h3c_e, h3c_2, h3c_3, h3c_10, h3a_e, h3a_2, h3a_3, h3a_10, h3b_e, h3b_2, h3b_3, h3b_10
#from .arithmetic_numeric import pow_e_m1, pow_2_m1, pow_3_m1, pow_10_m1, root_e_1p, root_2_1p, root_3_1p, root_10_1p, exp_e_m1, exp_2_m1, exp_3_m1, exp_10_m1, log_e_1p, log_2_1p, log_3_1p, log_10_1p

from .complex import real, imag, arg, rect, polar, conj
from .complex_numeric import cis

from .trigonometric import sin, cos, tan, cot, sec, csc, asin, acos, atan, acot, asec, acsc, sinh, cosh, tanh, coth, sech, csch, asinh, acosh, atanh, acoth, asech, acsc
from .trigonometric_numeric import atan2

from .logical import not_, and_, or_, xor, imp, con, nand, nor, nxor, nimp, ncon
from .interval import lt, le, eq, ne, ge, gt, oo, oc, co, cc

from .statistics import mean, hmean, gmean, min, max, median, mode, var, stdev
from .combinatorial import fact, sumt, comb, perm
from .variadic import vand, vor, vadd, vmul, vparallel
from .rounding import round, floor, ceil, trunc, away, round_floor, round_ceil, round_trunc, round_away, round_even, round_odd, quot, rem, quotrem, quot_1, rem_1, quotrem_1
#from .hyperoperation import
from .sigmoids import *
from .mapping import lerp, unlerp, map, fixed_log, fixed_exp, soft_log, soft_exp
from .tensor import norm, normalize, clamp, abs, sgn, clamp_2
from .floating import copysign
from .miscellaneous import ifelse

# sinc (sin(x) / x), cosc, … perhaps?

