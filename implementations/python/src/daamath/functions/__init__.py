# hey! you! yeah, you! daa!
#
# also, implement vector products like dot product, cross product (just a compositon of wedge product and hodge star. also, in 3D and 7D only! because they tie with quaternions and octonions, but none higher. no more normed algebrae after that), wedge product, 

from . import arithmetic, arithmetic_extra, complex, complex_extra, trigonometry, trigonometry_extra, logic, interval, combinatoric, variadic, quantization, sigmoids, mapping, tensor, miscellaneous

from .arithmetic import h0c, h0b, h1c, h1b, h2c, h2b, h3c, h3b, h3a, h4c, h4b, h4a
from .arithmetic_extra import h1b_0, h2b_1, h3c_e, h3c_2, h3c_10, h3b__e, h3b__2, h3b__10, h3c__2, h3c__3, h3a__2, h3a__3, h2b_1_h3c__2, h2b_1_h3c__3, h2b_1_h3a__2, h2b_1_h3a__3, h1c_h2c, h1b_h3c_e__1, h3b_h1c_1__e

from .complex import real, imag, arg, rect, polar, conj
from .complex_extra import cis

from .trigonometry import croh, crah, croa, crao, crha, crho, csoh, csah, csoa, csao, csha, csho, hroh, hrah, hroa, hrao, hrha, hrho, hsoh, hsah, hsoa, hsao, hsha, hsho
from .trigonometry_extra import csoh2, csah2, csoa2, csao2, csha2, csho2, h2b_croh_S_S

from .logic import tf, ffft, fttt, fttf, ttft, tftt, tttf, tfff, tfft, fftf, ftff
from .interval import iee, iie, eie, iei, eii, eei, eeiee, eeiie, eiiee, eiiie

from .variadic import vffft, vfttt, vh1c, vh2c, mean, mean__h1b_0_inf, mean__h1b_0_1, mean__0, mean__1, mean__2, mean__3, mean__inf, vparallel
from .combinatoric import fact, sumt, comb, perm, gcd, lcm
from .quantization import round, round__true_floor, round__true_ceil, round__true_trunc, round__true_away, round__false_floor, round__false_ceil, round__false_trunc, round__false_away, round__false_even, round__false_odd, quot, rem, quotrem
from .sigmoids import sigmoid_tan, sigmoid_tanh
from .mapping import lerp, unlerp, map, fixed_log, fixed_exp, soft_log, soft_exp
from .tensor import norm, normalize, clamp, norm__2, normalize__2
from .miscellaneous import ifelse

from .solvers import roots, coeffs
