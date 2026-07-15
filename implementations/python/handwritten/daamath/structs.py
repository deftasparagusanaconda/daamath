# there are a few patterns in the namespace. this module describes them and gives them concrete shape as structs

from dataclasses import dataclass
from types import SimpleNamespace
from collections.abc import Callable
from typing import Any
from numbers import Number

# ---------
# typehints
# ---------
# you should probably make these more robust some time. ehh, depends on how much complexity it adds to daamath

T = Any
Ordinal = Number
Cardinal = Number

# classes ----------------------------------------------------------------------



# used in dm.sets.yoursethere.wellorders.*
@dataclass
class WellOrder:   
    relation: Callable[[T, T], bool] # the well-order as a binary relation
    ordinality: Ordinal # the order type of the set
    ordinal_of: Callable[[T], Ordinal] # the ordinal bijecting to an element
    element_at: Callable[[Ordinal], T] # the element bijecting to an ordinal
    covers: Callable[[T, T], bool] # is "a covers b" true?
    least: T # the minimal element of the well-order
    greatest: T # the maximal element of the well-order
    successor: Callable[[T], T] # return the covering element
    predecessor: Callable[[T], T] # return the element it covers

# used in dm.sets.*
@dataclass
class Set:
    indicator: Callable[[T], bool] | None # "does x belong in this set?"
    cardinality: Cardinal | None # size/count of the set
    wellorders: SimpleNamespace[WellOrder] # assuming axiom of choice. daamath is ZFC.

