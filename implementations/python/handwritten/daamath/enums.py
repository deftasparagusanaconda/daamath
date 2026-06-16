from enum import Enum

class ErrorPolicy:
    SENTINEL = 0
    FLAG_SENTINEL = 1
    RAISE_HALT = 2
    FLAG_RAISE_HALT = 3

class SentinelPolicy:
    IGNORE = 0
    PROPAGATE = 1
