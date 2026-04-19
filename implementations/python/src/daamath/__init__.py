from .context import Context

from . import functions, numbers, strings, domains
from .functions import *
from .numbers import *
from .strings import *
from .domains import *

from . import aliases
from .aliases import *

from . import exceptions

context = Context(
        check_input_domain  = True,
        check_output_domain = True,
        domain              = REAL,
        error_behaviour     = Context.ErrorBehaviour.FLAG_AND_RAISE,
        rounding            = roundeven,
    )
