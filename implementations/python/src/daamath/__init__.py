from .context import Context

from . import functions, numbers, strings, domains
from .functions import *
from .numbers import *
from .strings import *
from .domains import *
from . import enums

from . import aliases
from .aliases import *

from . import exceptions

context = Context(
        functions = '',
        datatypes = ''
#        check_input_domain  = True,
#        check_output_domain = True,
#        domain              = REAL,
#        error_policy     = enums.ErrorPolicy.FLAG_RAISE_HALT,
#        rounding            = roundeven,
    )
