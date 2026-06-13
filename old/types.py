from builtins import bool, int

class uint(int):
    def __new__(cls, number):
        if number < 0:
            raise ValueError(f'{number} must be ≥ 0')
        return super().__new__(cls, number)

import inspect
class seq(list):
    def __init__(self, dtype, iterable=()):
        if not inspect.isclass(dtype):
            raise TypeError(f'expected class {type(dtype)}, got object {dtype}')
        self.dtype = dtype
        super().__init__()
        self.extend(iterable)

    def check_dtype(self, v):
        if not isinstance(v, self.dtype):
            raise TypeError(f'expected {self.dtype.__name__}, got {type(v).__name__}')

    def append(self, v): self.check_dtype(v); super().append(v)
    def insert(self, i, v): self.check_dtype(v); super().insert(i, v)
    def extend(self, vs): [self.append(v) for v in vs]
    def __setitem__(self, i, v): self.check_dtype(v); super().__setitem__(i, v)
