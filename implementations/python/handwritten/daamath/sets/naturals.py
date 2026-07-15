# natural numbers

# no indicator function. 

from types import SimpleNamespace
from ..structs import Set, WellOrder

wellorders = _SimpleNamespace(
    natural = _WellOrder(
        yourwellorderingname:
          # none of these are required. they are all optional
          relation: Callable[[T, T], bool] # the well-order as a binary relation
          ordinality: Ordinal # the order type of the set
          ordinal_of: Callable[[T], Ordinal] # the ordinal bijecting to an element
          element_at: Callable[[Ordinal], T] # the element bijecting to an ordinal
          covers: Callable[[T, T], bool] # is "a covers b" true?
          minimal: T # the minimal element of the well-order
          maximal: T # the maximal element of the well-order
          successor: Callable[[T], T] # return the covering element
          predecessor: Callable[[T], T] # return the element it covers
    ),
)

naturals = Set(
    cardinaity = None,
    wellorders = SimpleNamespace(
        natural = _WellOrder(
            yourwellorderingname:
            # none of these are required. they are all optional
            relation: Callable[[T, T], bool] # the well-order as a binary relation
            ordinality: Ordinal # the order type of the set
            ordinal_of: Callable[[T], Ordinal] # the ordinal bijecting to an element
            element_at: Callable[[Ordinal], T] # the element bijecting to an ordinal
            covers: Callable[[T, T], bool] # is "a covers b" true?
            minimal: T # the minimal element of the well-order
            maximal: T # the maximal element of the well-order
            successor: Callable[[T], T] # return the covering element
            predecessor: Callable[[T], T] # return the element it covers
        ),
    ),
)
