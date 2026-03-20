# hey! you! yeah, you! daa!
#
# also, implement vector products like dot product, cross product (just a compositon of wedge product and hodge star. also, in 3D and 7D only! because they tie with quaternions and octonions, but none higher. no more normed algebrae after that), wedge product, 

from . import hyperoperations, hyperoperations_extra, complex, complex_extra, trigonometric, trigonometric_extra, logical, interval, combinatorial, variadic, rounding, sigmoids, mapping, tensor, floating, miscellaneous

from .hyperoperations import succ, pred, add, sub, mul, div, pow, log, root, spow, slog, sroot#, hyper
from .hyperoperations_extra import ainv, minv, square, cube, sqrt, cbrt, rsquare, rcube, rsqrt, rcbrt, pow_2, pow_10, log_2, log_10, exp, ln, expm1, ln1p
 
from .complex import real, imag, arg, rect, polar, conj
from .complex_extra import cis

from .trigonometric import sin, cos, tan, cot, sec, csc, asin, acos, atan, acot, asec, acsc, sinh, cosh, tanh, coth, sech, csch, asinh, acosh, atanh, acoth, asech, acsch
from .trigonometric_extra import atan2, sinc

from .logical import not_, and_, or_, xor, imp, con, nand, nor, nxor, nimp, ncon
from .interval import lt, le, eq, ne, ge, gt, oo, oc, co, cc

from .variadic import any, all, sum, prod, vparallel, amean, hmean, gmean, pmean, min, max, median, mode, var, stdev
from .combinatorial import fact, sumt, comb, perm, gcd, lcm
from .rounding import round, floor, ceil, trunc, away, round_floor, round_ceil, round_trunc, round_away, round_even, round_odd, quot, rem, quotrem
from .sigmoids import sigmoid_tan, sigmoid_tanh
from .mapping import lerp, unlerp, map, fixed_log, fixed_exp, soft_log, soft_exp
from .tensor import norm, normalize, clamp, abs, sgn
from .floating import copysign, fma
from .miscellaneous import ifelse

from .solvers import roots, coeffs
