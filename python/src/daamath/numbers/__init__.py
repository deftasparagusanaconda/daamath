# numbers are intentionally overdefined beyond the precision that a double can store. this is for clarity and novelty

from . import floating, conversion_angle, constants, derived
from .floating import ZERO, NAN, INF, NAN, FLT_MAX, FLT_MIN, FLT_TRUE_MIN, DBL_MAX, DBL_MIN, DBL_TRUE_MIN

from .conversion_angle import TURN_TO_TURN, RAD_TO_TURN, DEG_TO_TURN, GRAD_TO_TURN, MIN_TO_TURN, SEC_TO_TURN
from .conversion_angle import TURN_TO_RAD, RAD_TO_RAD, DEG_TO_RAD, GRAD_TO_RAD, MIN_TO_RAD, SEC_TO_RAD
from .conversion_angle import TURN_TO_DEG, RAD_TO_DEG, DEG_TO_DEG, GRAD_TO_DEG, MIN_TO_DEG, SEC_TO_DEG
from .conversion_angle import TURN_TO_GRAD, RAD_TO_GRAD, DEG_TO_GRAD, GRAD_TO_GRAD, MIN_TO_GRAD, SEC_TO_GRAD
from .conversion_angle import TURN_TO_MIN, RAD_TO_MIN, DEG_TO_MIN, GRAD_TO_MIN, MIN_TO_MIN, SEC_TO_MIN
from .conversion_angle import TURN_TO_SEC, RAD_TO_SEC, DEG_TO_SEC, GRAD_TO_SEC, MIN_TO_SEC, SEC_TO_SEC

from .constants import *
from .derived import *
#from .fractions import *
