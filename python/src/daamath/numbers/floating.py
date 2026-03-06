# negative versions are not stored separately as they can be easily composed

ZERO           = 0.0
ONE            = 1.0
INF            = float('inf')	
NAN            = float('nan')	# quiet nan

FLT_MAX        = (2 - 2 ** -23) * 2 ** 127
FLT_MIN        = 2 ** -126
FLT_TRUE_MIN   = 2 ** -149

DBL_MAX        = (2 - 2 ** -52) * 2 ** 1023
DBL_MIN        = 2 ** -1022	
DBL_TRUE_MIN   = 2 ** -1074
