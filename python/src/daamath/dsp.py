from .functions import soft_log as _soft_log, soft_exp as _soft_exp	# for frequency conversions
from .functions import plerp as _plerp, unplerp as _unplerp	# for frequency lerping
import math as _math

# for the frequency lerpers at the end
_DEFAULT_LOW_HZ = 20
_DEFAULT_HIGH_HZ = 20000	

# decibel conversions -------------------------

def rpow_to_pow(rpow):
	'convert a root-power quantity to power. returns rpow²'
	return rpow ** 2

def pow_to_rpow(pow):
	'convert a root-power quantity to power. returns √pow'
	return _math.sqrt(pow)

def db_to_bel(db):
	'convert db to bel. returns db / 10'
	return db / factor

def bel_to_db(bel):
	'convert bel to decibel. returns 10 * bel'
	return factor * bel

_np_to_db_factor = 8.6858896380650365530225783783321016458647830411094563350443397173668347208571878 # 20 * _math.log10(_math.e)

def db_to_np(db):
	'convert decibels to nepers. by default uses db * 20 * log⏨(e) which assumes decibels describe power ratios and nepers describe root-power ratios'
	# db / (20 * _math.log10(_math.e))
	return db * 0.11512925464970228420089957273421821038036201556142658733102210701271816669945107

def np_to_db(np):
	'convert nepers to decibels. by default uses np / (20 * log⏨(e)) which assumes decibels describe power ratios and nepers describe root-power ratios'
	# np * 20 * _math.log10(_math.e)
	return np * 8.6858896380650365530225783783321016458647830411094563350443397173668347208571878

def rpow_to_db(rpow, *, reference_rpow = 1, factor = 20, base = 10):
	'convert a ratio of root-power quantities like amplitude or voltage to decibels. by default uses 20 * log⏨(rpow)'
	return factor * _math.log(rpow / reference_rpow, base)

def db_to_rpow(db, *, reference_rpow = 1, factor = 20, base = 10):
	'convert decibels to a ratio of root-power quantities like amplitude or voltage. by default uses 10 ^ (db / 20)'
	return reference_rpow * base ** (db / factor)

def pow_to_db(pow, *, reference_pow = 1, factor = 10, base = 10):
	'convert a power ratio to decibel. by default uses 10 * log⏨(pow)'
	return factor * _math.log(pow / reference_pow, base)

def db_to_pow(db, *, reference_pow = 1, factor = 10, base = 10):
	'convert decibels to a power ratio. by default uses 10 ^ (db / 10)'
	return reference_pow * base ** (db / factor)

def rpow_to_np(rpow, *, reference_rpow = 1, factor = 1, base = _math.e):
	'convert a ratio of root-power quantities into nepers'
	return factor * _math.log(rpow / reference_rpow, base)

def np_to_rpow(np, *, reference_rpow = 1, factor = 1, base = _math.e):
	'convert nepers to a ratio of root-power quantities'
	return reference_rpow * base ** (np / factor)

# frequency hz conversions -------------------------------

def hz_to_midi(hz, *, reference_hz = 440, offset_midi = 69) -> float:
	'convert a midi note to Hz. by default uses 69 (nice) + 12 * log₂(hz / 440)'
	return offset_midi + 12 * log2(hz / reference_hz)

def midi_to_hz(midi, *, reference_hz = 440, offset_midi = 69) -> float:
	'convert a midi note to Hz. by default uses 440 * 2 ^ ((midi - 69nice) / 12)'
	return reference_hz * 2 ** ((midi - offset_midi) / 12)

def hz_to_str(
	hz, 
	char_double_flat : str = '𝄫',
	char_flat        : str = '♭',
	char_natural     : str = '♮',
	char_sharp       : str = '♯',
	char_double_sharp: str = '𝄪',
	notes            : str = 'CDEFGABC',
	) -> str:
	'convert frequency in hertz to a 12-TET '
	return notes[(midi + offset) % 7] + str((midi + offset) // 7)
	"""if isinstance(midi, int):
	elif isinstance(midi, float):
		temp = round(midi)
	else:
		raise ValueError("expected int or float")"""

def hz_to_oct(hz, base = 2) -> float:
	'convert frequency in hz to log2 frequency. by default uses log₂(hz)'
	return _math.log(base, hz)

def oct_to_hz(oct, base = 2) -> int | float:
	'convert log2 frequency to frequency in hz. by default uses 2ʰᶻ'
	return base ** hz

def hz_to_mel(hz, softness = 700, low_x = 0, high_x = 1000, low_y = 0, high_y = 1000):
	"""convert frequency in hz to mel scale. it is based on O'Shaughnessy's formula from 1987:
	
	2595 * log⏨(1 + hz / 700) where 2595 should actually be 1000 / log⏨(1 + 1000 / 700)
	"""
	return _soft_log(hz, softness = softness, low_x = low_x, high_x = high_x, low_y = low_y, high_y = high_y)
	
def mel_to_hz(mel, softness = 700, low_x = 0, high_x = 1000, low_y = 0, high_y = 1000):
	'inverse of hz_to_mel'
	return _soft_exp(mel, softness = softness, low_x = low_x, high_x = high_x, low_y = low_y, high_y = high_y)
	#return break_hz * ((1 + norm_hz / break_hz) ** (mel / norm_hz) - 1)

def hz_to_mel2(hz, break_hz = 1000, norm_hz = 1000, base = _math.e):
	"""convert frequency in hz to mel scale. uses a two-piece fit. the derivative w.r.t. hz is continuous as well, as long as you dont change the base of the logarithm (though the actual function will still be continuous)
	
	default formula: hz if hz ≤ 1000 else (1 + ln(hz / 1000)) * 1000 
	
	this is based on a 1000Hz normalized version of slanley's formula, except its mathematically elegant so it avoids wierd constants:
	
	3 * hz / 200 if hz < 1000 else 15 + 27 * log₆.₄(hz / 1000)
	"""
	return hz if hz <= break_hz else (1 + log(hz / break_hz, base)) / (1 + log(norm_hz / break_hz, base)) * norm_hz
	
def mel_to_hz2(mel, break_hz = 1000, norm_hz = 1000, base = _math.e):
	"""inverse of hz_to_mel2. converts mel scale to frequency in hz. by default uses:
	
	mel if mel ≤ 1000 else 1000 * e ** (mel / 1000 - 1)
	"""
	return mel if mel <= break_hz else break_hz * base ** (mel / norm_hz * (1 + log(norm_hz / break_hz, base)) - 1)
	
_beranek_1949_hz = [20, 160, 394, 670, 1000, 1420, 1900, 2450, 3120, 4000, 5100, 6600, 9000, 14000]
_beranek_1949_mel = [0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 3250]
_umesh_1999_hz = [40, 161, 200, 404, 693, 867, 1000, 2022, 3000, 3393, 4109, 5526, 6500, 7743, 12000]
_umesh_1999_mel = [43, 257, 300, 514, 771, 928, 1000, 1542, 2000, 2142, 2314, 2600, 2771, 2914, 3228]
"""
def hz_to_mel3(hz, = _beranek_1949_hz, = _beranek_1949_mel):
	'convert frequency in hz to mel scale. uses a linear interpolation of the data from beranek 1949'
def hz_to_mel4(hz, = _umesh_1999_hz, = _umesh_1999_mel):
	'convert frequency in hz to mel scale. uses a linear interpolation of the data from umesh 1999'
"""

def hz_to_bark(hz: float, norm_hz: float = 0, formula: _Literal['zt1', 'zt2', 'zt3', 'tjomov', 'schroeder'] = 'ht2') -> float:
	'convert frequency in Hertz to the bark scale'
	match formula:
		case 'zt2':
			result = 14.2 * _math.log10(hz / 1000) + 8.7
		case 'zt3':
			result = 6.578 * _math.log(hz) - 36.99
		case 'zt1':
			result = 13 * arctan(0.00076 * hz) + 3.5 * arctan((hz / 7500) ** 2)
		case 'ht1':
			result = 26.81 * hz / (1960 + hz) - 0.53
		case 'ht2':
			bark = 26.81 * hz / (1960 + hz) - 0.53
			if bark < 2:
				result = bark + 0.15 * (2 - bark)
			elif bark > 20.1:
				result = bark + 0.22 * (bark - 20.1)
			else:
				result = bark
		case 'tjomov':
			result = 600 * _math.sinh(hz / 6.7) + 20
		case 'schroeder':
			result = 650 * _math.sinh(hz / 7)
		case 'wsg':
			result = 6 * _math.asinh(hz / 600)
		case _:
			raise ValueError('unrecognized formula')
	
	if norm_hz > 0:
		return result / hz_to_bark(norm_hz, formula = formula) * norm_hz

	return result
		
def bark_to_hz(bark: float, norm_hz: float = 0, formula: str = 'ht2') -> float:
	'inverse of hz_to_bark. converts bark scale values to frequency in Hertz'
	if norm_hz > 0:
		bark = bark * hz_to_bark(norm_hz, formula = formula) / norm_hz

	match formula:
		case 'zt2':
			result = 10 ** ((bark - 33.9) / 14.2)
		case 'zt3':
			result = _math.exp((bark + 36.99) / 6.578)
		case 'ht1':
			if hasattr(_math, 'fma'):
				result = _math.fma(bark, 1960, 0.53) / (26.28 - bark)
			else:
				result = 1960 * (bark + 0.53) / (26.28 - bark)
		case 'ht2':
			if bark < 2:
				bark = (bark - 0.3) / 0.85
			elif bark > 20.1:
				bark = (bark + 4.422) / 1.22
			result = 1960 * (bark + 0.53) / (26.28 - bark)
		case 'tjomov':
			result = 6.7 * _math.asinh((bark - 20) / 600)
		case 'schroeder':
			result = 7 * _math.asinh(bark / 650)
		case 'wsg':
			result = 600 * _math.sinh(bark / 6)
		case _:
			raise ValueError('unrecognized formula')
	
	return result
"""

	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24
	60	150	250	350	450	570	700	840	1000	1170	1370	1600	1850	2150	2500	2900	3400	4000	4800	5800	7000	8500	10500	13500
20	100	200	300	400	510	630	770	920	1080	1270	1480	1720	2000	2320	2700	3150	3700	4400	5300	6400	7700	9500	12000	15500
	80	100	100	100	110	120	140	150	160	190	210	240	280	320	380	450	550	700	900	1100	1300	1800	2500	3500
no. center  cutoff  bandwidth
 			20 	
1 	60 		100 	80
2 	150 	200 	100
3 	250 	300 	100
4 	350 	400 	100
5 	450 	510 	110
6 	570 	630 	120
7 	700 	770 	140
8 	840 	920 	150
9 	1000 	1080 	160
10 	1170 	1270 	190
11 	1370 	1480 	210
12 	1600 	1720 	240
13 	1850 	2000 	280
14 	2150 	2320 	320
15 	2500 	2700 	380
16 	2900 	3150 	450
17 	3400 	3700 	550
18 	4000 	4400 	700
19 	4800 	5300 	900
20 	5800 	6400 	1100
21 	7000 	7700 	1300
22 	8500 	9500 	1800
23 	10500 	12000 	2500
24 	13500 	15500 	3500
"""

def hz_to_erbs(hz, norm_hz = 0):
	"""convert hz to erbs (also known as caws)
	
	formula: A * log1p(B * (hz / (hz + C))) which is mathematically equivalent to A * ln(1 + (hz * B) / (hz + C))
	where: A = 100000 / √80109737
	         ≈ 11.1726796613307508659409591598553369046875791603224092625910488…
	       B = (9339 + √80109737) / (9339 - √80109737) - 1
	         ≈ 46.0653791116351008187372868311781991418099625357253121238190101…
	       C = (9339 + √80109737) / 1.246
	         ≈ 14678.4946168094343650325240435293097711148959365979858846912749…
	the constants are precomputed using an arbitrary precision calculator so they are as precise as a double can be
	this is a numerically stable version of the integral of reciprocal of 6.23khz² + 93.39khz + 28.52. with the integration constant set so that hz_to_erbs(0) = 0, the formula is ln(abs(1.246 * hz + 9339 - √80109737) / abs(1.246 * hz + 9339 + √80109737)) * 100000 / √80109737 + ln(abs(9339 - √80109737) / abs(9339 + √80109737)) * 10000/ √80109737. derive the rest yourself
	
	an alternate formula is: log((hz + A) / (hz + B), base = C) + D
	where: A = (9339 - √80109737) / 1.246
	         ≈ 311.87456457098324…
	       B = (9339 + √80109737) / 1.246
	         ≈ 14678.494616809434…
	       C = e ^ (100000 / √80109737)
	         ≈ 1.0936317547750625…
	       D = log(B / A, base = C) = ln(B / A) * 10000 / √80109737
	         ≈ 43.031996702539864…
	"""
	if norm_hz > 0:
		return _math.log1p(46.0653791116351008187372868311781991418099625357253121238190101 * (hz / (hz + 14678.4946168094343650325240435293097711148959365979858846912749))) / _math.log1p(46.0653791116351008187372868311781991418099625357253121238190101 * (norm_hz / (norm_hz + 14678.4946168094343650325240435293097711148959365979858846912749)))
	else:
		return 11.1726796613307508659409591598553369046875791603224092625910488 * _math.log1p(46.0653791116351008187372868311781991418099625357253121238190101 * (hz / (hz + 14678.4946168094343650325240435293097711148959365979858846912749)))

def erbs_to_hz(erbs):
	"""inverse of hz_to_erbs. there are many ways to perform this but they are less numerically stable than hz_to_erbs

	default formula: A * (T / (B - T))
		where A = (9339 + √80109737) / 1.246
		        ≈ 14678.4946168094343650325240435293097711148959365979858846912…
		      B = (9339 + √80109737) / (9339 - √80109737) - 1
		        ≈ 46.0653791116351008187372868311781991418099625357253121238190… 
		      T = expm1 (erbs * C) which is mathematically equivalent to e ^ (erbs * C) - 1
		where C = √80109737 / 100000
		        ≈ 0.089504042925445552188305249582375199748091603370010904123253286141232001286708029
	
	the constants are precomputed using an arbitrary precision calculator so they are as precise as a double can be

	there may be other forms. i havent explored them yet
	"""
	temp = _math.expm1(erbs / 11.1726796613307508659409591598553369046875791603224092625910488)

	return 14678.4946168094343650325240435293097711148959365979858846912749 * (temp / (46.0653791116351008187372868311781991418099625357253121238190101 - temp))

def hz_to_gw(hz, softness = 165.4, low_x = 20, low_y = 0, high_x = 20000, high_y = 1):
	"""convert frequency in hertz to cochlear frequency–place map according to the greenwood function

	this is the "actual" form of greenwood's original function which is hz = 165.4 * (10 ^ (2.1 * gw) - 0.88). the inverse is gw = log10(hz / 165.4 + 0.88) / 2.1. in my formula, 165.4 stays as it is, but 0.88 is supposed to be 1 - 20 / 165.4 and 2.1 is supposed to be log10(1 + (20000 - 20) / 165.4). derive the rest yourself
	"""
	return _soft_log(hz, softness = softness, low_x = low_x, high_x = high_x, low_y = low_y, high_y = high_y)

def gw_to_hz(gw, softness = 165.4, low_x = 0, low_y = 20, high_x = 1, high_y = 20000):
	"""inverse of hz_to_gw. derived from greenwood's formula hz = 165.4 * (10 ^ (2.1 * gw) - 0.88) where 0.88 is supposed to be 1 - 20 / 165.4 and 2.1 is supposed to be log10(1 + (20000 - 20) / 165.4). derive the rest yourself
	"""
	return _soft_exp(gw, softness = softness, low_x = low_x, high_x = high_x, low_y = low_y, high_y = high_y)

# lerping converters --------------------------

def lerp_freq(
		value: float                   , 
		low  : float = _DEFAULT_LOW_HZ , 
		high : float = _DEFAULT_HIGH_HZ, 
		power: float = 0               ,
		) -> float:
	'lerp a fractional value to a frequency in an interval. by default, maps [0, 1] → [20, 20000] in oct space'
	return _plerp(value, low, high, power)

def unlerp_freq(
		value: float                   , 
		low  : float = _DEFAULT_LOW_HZ , 
		high : float = _DEFAULT_HIGH_HZ, 
		power: float = 0               ,
		) -> float:
	'unlerp a frequency in an interval to a fractional value. by default, maps [20, 20000] in hz space to [0, 1]'
	return _unplerp(value, low, high, power)

# finished up to this ----------------------------------------------------------

# string helpers

# factories --------------------------------------------------------------------
"""
def multilerp(value: float, x_values: _Iterable[float], y_values: _Iterable[float], is_sorted: bool = False) -> float:
	'a slow inefficient ass function that linearly interpolates a bunch of points and lets you sample on them'
	
	if x_value
	
	#x_values, y_values = (x_values, y_values) if is_sorted else zip(*sorted(zip(x_values, y_values)))

	index_low: int = 0
	index_high: int = 0

	if is_sorted:
		for index, x_value in enumerate(x_values):
			if x_value > value:
				break
			index_low = 
	else:
		for index, x_value in enumerate(x_values):
			if x_value == value:
				return y_values[index]
			index_low = index if x_value < value and index_low < index else index_low
			index_high = index if x_value > value and index_high > index else index_high
	
	value_intermediate = (value - x_values[index_low]) / (x_values[index_high] - x_values[index_low])
	return y_values[index_low] * (1 - value_intermediate) + y_values[index_high] * value_intermediate
"""	
def factory_ascii_converter(from_str: str, to_str: str) -> _Callable[[str], str]:
	# create a dictionary mapping for all non-space characters
    mapping = {a: b for a, b in zip(from_str, to_str) if b.strip()}
    def converter(s: str) -> str:
        return ''.join(mapping.get(ch, ch) for ch in s)
    return converter

def factory_interpolation(x_values: _Sequence[int|float], y_values: _Sequence[int|float]) -> _Callable[[int|float], int|float]:
	'a factory that turns a bunch of points into a sample-able ℝ ⟼ ℝ function by a polynomial interpolation'
	raise NotImplementedError



# specific converters
to_superscript = factory_ascii_converter(ASCII, ASCII_SUPERSCRIPT)
to_subscript = factory_ascii_converter(ASCII, ASCII_SUBSCRIPT)

# add slerp and unslerp

# DSP --------------------------------------------------------------------------

"""
def square_wave(length: int, amplitude: float = 1, period_samples: int = 2, offset: float = 0) -> _Sequence[float]:
	if not isinstance(period_samples, int) or period_samples % 2 != 0:
		raise ValueError("only even integer period samples supported for now")

	if length % period_samples != 0:
		raise ValueError("length should be a multiple of period_samples")

	one_shot = [offset + amplitude] * (period_samples // 2) + [offset - amplitude] * (period_samples // 2)
	return one_shot * (length // period_samples)
"""
def coeffs_from_roots(roots: _Sequence[float]) -> _Sequence[float]:
    """
    given an iterable of roots r1, r2, ..., rn
    returns coefficients [c0, c1, ..., cn] such that
	
    (x - r1)(x - r2)...(x - rn)
    = c0*x^n + c1*x^(n-1) + ... + cn
    """
    coeffs = [1]
	
    for r in roots:
        new = [0] * (len(coeffs) + 1)
        for i, c in enumerate(coeffs):
            new[i]     += c        # multiply by x
            new[i + 1] -= r * c    # multiply by -r
        coeffs = new
	
    return coeffs

"""
Fs = 48000
f0 = 200
dBgain = 10
Q = 2

A = 10 ** (dBgain / 40)
w0 = 2 * _math.pi * f0 * Fs
cos_w0 = cos(w0)
sin_w0 = sin(w0)

alpha = sin_w0 / (2 * Q)
"""               
