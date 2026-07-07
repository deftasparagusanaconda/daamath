from types import SimpleNamespace as _SimpleNamespace

f32 = _SimpleNamespace(
  epsilon = _SimpleNamespace(
    significand = 1,
    radix = 2,
    exponent = -23,
  ),
  min = _SimpleNamespace(
    normal = _SimpleNamespace(
      significand = 1,
      radix = 2,
      exponent = -126,
    ),
    subnormal = _SimpleNamespace(
      significand = 1,
      radix = 2,
      exponent = -149,
    ),
  ),
  max = _SimpleNamespace(
    normal = _SimpleNamespace(
      significand = 16777215,
      radix = 2,
      exponent = 104,
    ),
    subnormal = _SimpleNamespace(
      significand = 8388607,
      radix = 2,
      exponent = -149,
    ),
  ),
)
f64 = _SimpleNamespace(
  epsilon = _SimpleNamespace(
    significand = 1,
    radix = 2,
    exponent = -52,
  ),
  min = _SimpleNamespace(
    normal = _SimpleNamespace(
      significand = 1,
      radix = 2,
      exponent = -1022,
    ),
    subnormal = _SimpleNamespace(
      significand = 1,
      radix = 2,
      exponent = -1074,
    ),
  ),
  max = _SimpleNamespace(
    normal = _SimpleNamespace(
      significand = 9007199254740991,
      radix = 2,
      exponent = 971,
    ),
    subnormal = _SimpleNamespace(
      significand = 4503599627370495,
      radix = 2,
      exponent = -1074,
    ),
  ),
)
f128 = _SimpleNamespace(
  epsilon = _SimpleNamespace(
    significand = 1,
    radix = 2,
    exponent = -112,
  ),
  min = _SimpleNamespace(
    normal = _SimpleNamespace(
      significand = 1,
      radix = 2,
      exponent = -16382,
    ),
    subnormal = _SimpleNamespace(
      significand = 1,
      radix = 2,
      exponent = -16494,
    ),
  ),
  max = _SimpleNamespace(
    normal = _SimpleNamespace(
      significand = 10384593717069655257060992658440191,
      radix = 2,
      exponent = 16271,
    ),
    subnormal = _SimpleNamespace(
      significand = 5192296858534827628530496329220095,
      radix = 2,
      exponent = -16494,
    ),
  ),
)
d64 = _SimpleNamespace(
  epsilon = _SimpleNamespace(
    significand = 1,
    radix = 10,
    exponent = -15,
  ),
  min = _SimpleNamespace(
    normal = _SimpleNamespace(
      significand = 1,
      radix = 10,
      exponent = -383,
    ),
    subnormal = _SimpleNamespace(
      significand = 1,
      radix = 10,
      exponent = -398,
    ),
  ),
  max = _SimpleNamespace(
    normal = _SimpleNamespace(
      significand = 9999999999999999,
      radix = 10,
      exponent = 369,
    ),
    subnormal = _SimpleNamespace(
      significand = 999999999999999,
      radix = 10,
      exponent = -398,
    ),
  ),
)
d128 = _SimpleNamespace(
  epsilon = _SimpleNamespace(
    significand = 1,
    radix = 10,
    exponent = -33,
  ),
  min = _SimpleNamespace(
    normal = _SimpleNamespace(
      significand = 1,
      radix = 10,
      exponent = -6143,
    ),
    subnormal = _SimpleNamespace(
      significand = 1,
      radix = 10,
      exponent = -6176,
    ),
  ),
  max = _SimpleNamespace(
    normal = _SimpleNamespace(
      significand = 9999999999999999999999999999999999,
      radix = 10,
      exponent = 6111,
    ),
    subnormal = _SimpleNamespace(
      significand = 999999999999999999999999999999999,
      radix = 10,
      exponent = -6176,
    ),
  ),
)