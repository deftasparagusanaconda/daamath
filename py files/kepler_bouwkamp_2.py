
from itertools import count
from flint import arb, ctx


def kepler_bouwkamp(precision, guard=20):
    # Arb's precision is set in decimal digits.
    ctx.dps = precision + guard

    total = arb(0)
    target = arb(10) ** (-precision)

    for two_k in count(2, 2):
        z = arb(two_k).zeta(3)
        p = arb(2) ** two_k

        # Original summand, expressed using Hurwitz zeta.
        term = z / two_k * (p - 1 / p + p * z - z)
        total += term

        # For n >= two_k + 2, the terms are bounded by
        # 2 * (4/9)**n / n, with n = two_k/2.
        n = two_k // 2 + 1
        ratio = arb(4) / 9
        tail_bound = 2 * ratio**n / n / (1 - ratio)

        if tail_bound < target:
            break

    # Your original code returns exp(-2 * total).
    # Keep this factor if it matches your derivation.
    result = (-2 * total).exp()

    return two_k, result


for precision in range(30000, 100000, 100000000000):
    iterations, value = kepler_bouwkamp(precision)
    print(precision, iterations, value)

