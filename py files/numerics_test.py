'''
import math, cmath, mpmath, numpy
from statistics import mean, median, mode, stdev, variance

N = 1000

def ulp_distance(a: float, b: float) -> int:
    '|a - b| in ulps'
    

numbers = numpy.frombuffer(numpy.random.bytes(16*N), dtype=numpy.complex128)

actual_formula = mpmath.tan
approx_formula = cmath.tan

actuals = numpy.array(numpy.fromiter(actual_formula(z) for z in numbers), dtype=numpy.complex128)
approxs = numpy.array(numpy.fromiter(approx_formula(z) for z in numbers), dtype=numpy.complex128)

real_distances = numpy.array(ulp_distance(a, b) for a, b in zip(actuals.real, approxs.real))
imag_distances = numpy.array(ulp_distance(a, b) for a, b in zip(actuals.imag, approxs.imag))

for stat in [min, max, mean, median, mode, stdev, variance]:
    print(stat.__name__, stat(real_distances), stat(imag_distances))
'''
import math, cmath, mpmath, numpy
from matplotlib import pyplot

N = 100_000
DPS = 100

# ── reference ────────────────────────────────────────────────────────────────

mpmath.mp.dps = DPS


# ── random complex128 inputs ─────────────────────────────────────────────────

numbers = numpy.frombuffer(
    numpy.random.bytes(16 * N),
    dtype=numpy.complex128,
)


# ── scalar evaluation ────────────────────────────────────────────────────────

actuals = numpy.fromiter(
    (complex(mpmath.tan(complex(z))) for z in numbers),
    dtype=numpy.complex128,
    count=N,
)

approxs = numpy.fromiter(
    (cmath.tan(complex(z)) for z in numbers),
    dtype=numpy.complex128,
    count=N,
)


# ── float64 → ordered integer representation ─────────────────────────────────

def ordered_bits(x):
    bits = x.view(numpy.uint64)
    sign = bits >> numpy.uint64(63)

    return bits ^ (
        -sign & numpy.uint64(0xffffffffffffffff)
    )


# ── signed ulp residuals ─────────────────────────────────────────────────────
#
# positive → approx is below actual
# negative → approx is above actual
#
# actual and approx are already binary64 here, so this measures the distance
# between their positions in the binary64 lattice.

real_residuals = (
    ordered_bits(actuals.real).astype(numpy.int64)
    - ordered_bits(approxs.real).astype(numpy.int64)
)

imag_residuals = (
    ordered_bits(actuals.imag).astype(numpy.int64)
    - ordered_bits(approxs.imag).astype(numpy.int64)
)


# ── remove non-finite results ────────────────────────────────────────────────

real_mask = numpy.isfinite(actuals.real) & numpy.isfinite(approxs.real)
imag_mask = numpy.isfinite(actuals.imag) & numpy.isfinite(approxs.imag)

real_residuals = real_residuals[real_mask]
imag_residuals = imag_residuals[imag_mask]


# ── statistics ───────────────────────────────────────────────────────────────

def report(name, x):
    print(name)
    print(f"  n       {x.size}")
    print(f"  min     {x.min()}")
    print(f"  max     {x.max()}")
    print(f"  mean    {x.mean():.6g}")
    print(f"  median  {numpy.median(x):.6g}")
    print(f"  exact   {numpy.count_nonzero(x == 0)}")
    print(f"  ≤1 ulp  {numpy.count_nonzero(numpy.abs(x) <= 1)}")
    print(f"  ≤2 ulp  {numpy.count_nonzero(numpy.abs(x) <= 2)}")
    print()


report("real", real_residuals)
report("imag", imag_residuals)


# ── histograms ───────────────────────────────────────────────────────────────

def histogram(x, title, xlabel):
    values, counts = numpy.unique(x, return_counts=True)

    fig, ax = pyplot.subplots()

    ax.bar(values, counts, width=0.9)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("count")

    ax.set_yscale("log")
    ax.grid(axis="y", alpha=0.25)



histogram(
    real_residuals,
    "cmath.tan real-part ulp residual",
    "signed residual (ulp)",
)

histogram(
    imag_residuals,
    "cmath.tan imaginary-part ulp residual",
    "signed residual (ulp)",
)

pyplot.show()
