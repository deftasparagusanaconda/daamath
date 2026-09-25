import math, cmath, numpy, seaborn, pandas, matplotlib, oklab, mpmath#, gmpy2

N = 2 ** 18
mpmath.mp.dps = 20
#gmpy2.get_context().precision = 66

actual_formula = mpmath.tan
def approx_formula(z) -> complex:
    try:
        x = z.real
        y = z.imag

        # sin formula 1
        #return complex(math.sin(x) * math.cosh(y), math.cos(x) * math.sinh(y))
        
        # sin formula 2
        #return (cmath.exp(1j * z) - cmath.exp(-1j * z)) / 2j

        # sinh formula 1
        #return complex(math.sinh(x) * math.cos(y), math.cosh(x) * math.sin(y))

        # sinh formula 2
        #return (cmath.exp(z) - cmath.exp(-z)) / 2

        # cos formula 1
        #return complex(math.cos(x) * math.cosh(y), -math.sin(x) * math.sinh(y))
        
        # cos formula 2
        #return (cmath.exp(1j * z) + cmath.exp(-1j * z)) / 2

        # cosh formula 1
        #return complex(math.cosh(x) * math.cos(y), math.sinh(x) * math.sin(y))

        # cosh formula 2
        #return (cmath.exp(z) + cmath.exp(-z)) / 2

        # tan formula 1. my favourite
        tan_x = math.tan(x)
        tanh_y = math.tanh(y)
        return math.nan if math.isclose(abs(y), 1, rel_tol=(2**32-1) / 2**32) or abs(y) > 1 else math.tan(z)#complex(tan_x, tanh_y) / complex(1, -tan_x * tanh_y) 
        # tan formula 2. not good... 
        # return cmath.sin(z) / cmath.cos(z)

        # tan formula 3
        # tx = math.tanh(z.real)
        # ty = math.tan(z.imag)
        # txty = tx * ty
        # return complex(
        #     math.fma(txty, ty, tx)     / math.fma(txty, txty, 1),
        #     ty * math.cosh(z.real) ** -2 / math.fma(txty, txty, 1))
        
        # tan formula 4
        # return -1j * cmath.tanh(1j * z)

        # tanh formula 1. just tan rotated
        # tanh_x = math.tanh(x)
        # tan_y = math.tan(y)
        # return complex(tanh_x, tan_y) / complex(1, tanh_x * tan_y)

    except OverflowError:
        return math.nan

print(f'{N=}')
print(f'{mpmath.mp.dps=}')
#print(f'{gmpy2.get_context().precision=}')
print()

# ------------------------------------------------------------------------------

def ordered_bits(x):
    bits = x.view(numpy.uint64)
    sign = bits >> numpy.uint64(63)

    return numpy.where(
        sign,
        ~bits,
        bits | numpy.uint64(0x8000000000000000),
    )

print('generating numbers')
numbers = numpy.frombuffer(
    numpy.random.bytes(16 * N),
    dtype=numpy.complex128)

print('filtering numbers to finites')
numbers = numbers[numpy.isfinite(numbers)]

print('generating actuals')
actuals = numpy.fromiter(
    map(actual_formula, numbers),
    dtype=numpy.complex128,
)

print('generating approxs')
approxs = numpy.fromiter(
    map(approx_formula, numbers),
    dtype=numpy.complex128,
)

print('filtering to common finites of actuals & approxs')
mask = numpy.isfinite(actuals) & numpy.isfinite(approxs)
actuals = actuals[mask]
approxs = approxs[mask]
numbers = numbers[mask]

print('casting to ulps')
real_residuals = (
    ordered_bits(actuals.real).astype(numpy.int64)
    - ordered_bits(approxs.real).astype(numpy.int64))
imag_residuals = (
    ordered_bits(actuals.imag).astype(numpy.int64)
    - ordered_bits(approxs.imag).astype(numpy.int64))

# statistics ───────────────────────────────────────────────────────────────----

print('calculating statistics')
print('-' * 80)
for stat in [numpy.size, numpy.min, numpy.max, numpy.mean, numpy.median, numpy.var]:
    print(stat.__name__, stat(real_residuals), stat(imag_residuals))
print('-' * 80)

print('generating colormap')
# colour_map = matplotlib.colors.ListedColormap([
#     oklab.lch_to_rgb((0.75, 0.1275, hue))
#     for hue in numpy.linspace(240, 0, 256, endpoint=False)])
colour_map = matplotlib.colors.ListedColormap([
    oklab.lch_to_rgb((0.71, 0.145, hue % 360))
    for hue in numpy.linspace(527, 232.5, 256, endpoint=False)])


# print('plotting relative distance heatmap')
# crosstab = pandas.crosstab(imag_residuals, real_residuals)
# seaborn.heatmap(
#     crosstab,
#     norm=matplotlib.colors.LogNorm(
#         vmin=1,
#         vmax=crosstab.to_numpy().max()),
#     cmap=colour_map,
# )
#
# matplotlib.pyplot.show()

print('plotting argand plane error heatmap')

error = numpy.maximum(
    numpy.abs(real_residuals),
    numpy.abs(imag_residuals),
)

real_coordinates = ordered_bits(numbers.real)
imag_coordinates = ordered_bits(numbers.imag)

bins = 256

real_bins = real_coordinates >> 56
imag_bins = imag_coordinates >> 56

def bin_coordinates(coordinates):
    minimum = int(coordinates.min())
    maximum = int(coordinates.max())
    span = maximum - minimum

    edges = numpy.array(
        [minimum + span * i // bins for i in range(bins + 1)],
        dtype=numpy.uint64,
    )

    return numpy.clip(
        numpy.searchsorted(edges, coordinates, side='right') - 1,
        0,
        bins - 1,
    )
#real_bins = bin_coordinates(real_coordinates >> 56)
#imag_bins = bin_coordinates(imag_coordinates >> 56)

error_sum = numpy.zeros((bins, bins))
count = numpy.zeros((bins, bins), dtype=numpy.int64)

numpy.add.at(error_sum, (real_bins, imag_bins), error)
numpy.add.at(count, (real_bins, imag_bins), 1)

mean_error = numpy.divide(
    error_sum,
    count,
    out=numpy.full_like(error_sum, numpy.nan),
    where=count != 0,
)

seaborn.heatmap(mean_error.T, cmap=colour_map)

matplotlib.pyplot.show()
