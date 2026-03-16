from math import copysign

try:
    from math import fma
except ImportError:
    def fma(a: float, b: float, c: float) -> float:
        'a * b + c, fused multiply-add'
        return a * b + c

