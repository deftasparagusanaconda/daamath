import math as _math

def sigmoid_tan(x: int | float) -> float:
    '[0, 1] → [-∞, +∞]'
    if x < 0 or x > 1:
        raise ValueError("out of range [0,1]")
    elif x == 0:
        return float('-inf')
    elif x == 0.25:
        return -1.0
    elif x == 0.75:
        return 1.0
    elif x == 1:
        return float('inf')
    else:
        if hasattr(_math, 'fma'):
            return _math.tan(_math.fma(x, _math.pi, -_math.pi/2))
        else:
            return _math.tan(x * _math.pi - _math.pi / 2)

def sigmoid_tanh(x, lower_bound = -1, upper_bound = 1, centre_x = 0, centre_y = 0, centre_slope = 1):
	"""sigmoid function using shifted and scaled version of tanh(x)

	formula: centre_y + temp * tanh(centre_slope * (x - centre_x) / temp)
		where temp = centre_y - lower_bound if x < centre_x else upper_bound - centre_y
	"""
	temp = centre_y - lower_bound if x < centre_x else upper_bound - centre_y
	return centre_y + temp * _math.tanh(centre_slope * (x - centre_x) / temp)

#def unsigmoid_tanh(x, lower_bound = -1, upper_bound = 1, centre_x = 0, centre_y = 0, centre_slope = 1):

# x / √(1 + x²)
