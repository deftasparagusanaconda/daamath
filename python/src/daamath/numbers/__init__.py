# numbers are intentionally overdefined beyond the precision that a double can store. this is for clarity and novelty

from . import floating, conversion, constants, derived
from .floating import ZERO, NAN, INF, NAN, FLT_MAX, FLT_MIN, FLT_TRUE_MIN, DBL_MAX, DBL_MIN, DBL_TRUE_MIN
from .conversion import TURN_PER_RAD, TURN_PER_DEG, TURN_PER_GRAD, RAD_PER_TURN, RAD_PER_DEG, RAD_PER_GRAD, DEG_PER_TURN, DEG_PER_RAD, DEG_PER_GRAD, GRAD_PER_TURN, GRAD_PER_RAD, GRAD_PER_DEG
from .constants import PSI, OMEGA, CATALAN, PHI, E, PI, TAU
from .derived import *
