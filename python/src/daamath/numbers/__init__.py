# numbers are intentionally overdefined beyond the precision that a double can store. this is for clarity and novelty

from . import floating, conversion_angle, constants, derived
from .floating import ZERO, NAN, INF, NAN, FLT_MAX, FLT_MIN, FLT_TRUE_MIN, DBL_MAX, DBL_MIN, DBL_TRUE_MIN

from .conversion_angle import TURN_TO_TURN, RAD_TO_TURN, DEG_TO_TURN, GRAD_TO_TURN, MIN_TO_TURN, SEC_TO_TURN
from .conversion_angle import TURN_TO_RAD, RAD_TO_RAD, DEG_TO_RAD, GRAD_TO_RAD, MIN_TO_RAD, SEC_TO_RAD
from .conversion_angle import TURN_TO_DEG, RAD_TO_DEG, DEG_TO_DEG, GRAD_TO_DEG, MIN_TO_DEG, SEC_TO_DEG
from .conversion_angle import TURN_TO_GRAD, RAD_TO_GRAD, DEG_TO_GRAD, GRAD_TO_GRAD, MIN_TO_GRAD, SEC_TO_GRAD
from .conversion_angle import TURN_TO_MIN, RAD_TO_MIN, DEG_TO_MIN, GRAD_TO_MIN, MIN_TO_MIN, SEC_TO_MIN
from .conversion_angle import TURN_TO_SEC, RAD_TO_SEC, DEG_TO_SEC, GRAD_TO_SEC, MIN_TO_SEC, SEC_TO_SEC

from .constants import E, PI, TAU, GAMMA, PHI

from .derived import FRAC_1_E, FRAC_1_PI, FRAC_1_TAU
from .derived import SQRT_E, SQRT_PI, SQRT_2, SQRT_3, SQRT_5
from .derived import CBRT_E, CBRT_PI, CBRT_2, CBRT_3, CBRT_5
from .derived import LN_2, LN_10, LOG_2_E, LOG_2_10, LOG_10_E, LOG_10_2
from .derived import ZETA_2, ZETA_3, ZETA_4, ZETA_5, ZETA_6, ZETA_7, ZETA_8, ZETA_9


