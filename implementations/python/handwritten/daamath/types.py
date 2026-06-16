from __future__ import annotations
import math, collections, numbers
from daacorations import pretty_repr
from typing import Any, Literal
from numbers import Integral, Rational
from functools import cached_property
from itertools import pairwise, cycle
from fractions import Fraction
from abc import abstractmethod
from frozendefaultdict import frozendefaultdict
from collections import defaultdict
from collections.abc import Hashable, MutableMapping
from frozendict import frozendict
from frozendefaultdict import HashableMapping

# numbers ----------------------------------------------------------------------

class Natural(numbers.Integral):
    'a non-negative integer'

    def __init__(self, value: Integral):
        if value < 0 or not isinstance(value, Integral):
            raise ValueError('must be a non-negative integer')
        self.value: Integral = value

    def __add__(self, other) -> Natural:
        return type(self)(self.value + other.value)
    def __sub__(self, other) -> Natural:
        if other.value > self.value:
            raise OutOfDomainError('')
        return type(self)(self.value - other.value)
    def __mul__(self, other) -> Natural:
        return type(self)(self.value * other.value)
    def __truediv__(self, other) -> Natural | Rational:
        if self.value % other.value == 0:
            return type(self)(self.value // other.value)
        else:
            return Fraction(self.value, other.value)
    def __pow__(self, other) -> Natural:
        if self.value == 0 and other.value == 0:
            raise ArithmeticError('0 ** 0 is not defined')
        return Natural(self.value ** other.value)
    def __radd__(self, other) -> Natural:
        return Natural(self.value + other.value)
    def __rsub__(self, other) -> Natural:
        return Natural(self.value + other.value)
    def __rmul__(self, other) -> Natural:
        return Natural(self.value + other.value)
    def __rdiv__(self, other) -> Natural:
        return Natural(self.value + other.value)
    def __rpow__(self, other) -> Natural:
        return Natural(self.value + other.value)

    __repr__ = pretty_repr

class Cardinal:
    'a number that represents the size/cardinality of a set'

    ALEPH_NULL = object()

    def __init__(self, value: Natural | Literal[ALEPH_NULL]):
        self.value: Natural | Literal[ALEPH_NULL] = value

    __repr__ = pretty_repr

    def __str__(self) -> str:
        return str(self.value)

# collections ------------------------------------------------------------------

class Sized:
    'like collections.abc.Sized but properly allowing cardinal number sizes instead of just non-negative integer sizes. thus, infinite collections of different cardinalities are possible'
    @abstractmethod
    def __len__(self) -> Cardinal:
        ...

    __repr__ = pretty_repr

class IterableContainer(collections.abc.Iterable, collections.abc.Container):
    'an iterable container with rich mixins: count, filter, __contains__. can be applied to Collection, Sequence, Set, and any other ABCs that derive both Iterable and Container.'
    
    def count(self, stuff: Set[Any], complement: bool = False) -> Natural:
        '"how many things of stuff does this sequence have?"'
        return sum(thing not in stuff for thing in self) if complement else sum(thing in stuff for thing in self)
    
    def filter(self, stuff: Set[Any], complement: bool = False) -> Sequence[Any]:
        '"things of this sequence which are in stuff"'
        return type(self)((thing for thing in self if thing not in stuff) if complement else (thing for thing in self if thing in stuff))
    
    def __contains__(self, thing) -> bool:
        return any(thing2 in thing for thing2 in self)

    __repr__ = pretty_repr

class Collection(Sized, IterableContainer):
    'like collections.abc.Collection but allows infinite len and has rich mixins (from IterableContainer)'
    ...

class Set(Collection):
    """an interface for datatypes that represent a set: a collection of unique elements"""

class Mapping(Collection):
    ...

class Function(Collection):
    """an object that maps elements from the domain set to the codomain set. 

    __len__ returns how many pairs are defined on the function."""

    def __init__(self, domain: Set[Any], codomain: Set[Any], pairs: Mapping[Any, Any]):
        self.domain: Set[Any] = domain
        self.codomain: Set[Any] = codomain
        self.pairs: Mapping[Any, Any] = pairs

    @property
    def is_total(self):
        return self.domain == self.pairs.keys()

class Sequence(Collection):
    ...
    
class _CyclicView:
    def __init__(self, sequence: Sequence):
        self.sequence = Sequence

    def __getitem__(self, index: int | slice) -> Any:
        match index:
            case int(): return self.sequence[index % len(self)]
            case slice(): return type(self.sequence)(self[i % len(self)] for i in range(*index))
            case _: raise IndexError('index must be int or slice')

    def __len__(self) -> int:
        return len(self.sequence)

    __repr__ = pretty_repr

# there are two kinds of sequences i recognize: if the domain is dense, a .cover cannot be defined. if the domain is not dense, a .cover can be defined, and you can traverse more easily.
#
# a sequence is a triple: (domain, function, codomain), where:
# domain is a . if it is    not dense, a cover can be defined, and the sequence can be traversed easily

class Wheel(collections.abc.Iterator):
    """a wheel for generating primes. its iterator returns the residues of the given wheel size. you get diminishing returns as you go up in size:

    >>> primes = [2,3,5,7,11,13,17,19,23]
    >>> for i in range(len(primes)):
    >>>     size = math.prod(primes[:i])
    >>>     wheel_count = Wheel(size).cycle_size
    >>>     naïve_count = size
    >>>     efficiency = wheel_count / naïve_count
    >>>     print(size, f'{wheel_count}/{naïve_count}={efficiency:.2%}')
    >>>
    1 1/1=100.00%
    2 1/2=50.00%
    6 2/6=33.33%
    30 8/30=26.67%
    210 48/210=22.86%
    2310 480/2310=20.78%
    30030 5760/30030=19.18%
    510510 92160/510510=18.05%
    9699690 1658880/9699690=17.10%
    223092870 36495360/223092870=16.36%
    """
    
    @staticmethod
    def _generate_steps(size: int) -> Sequence[int]:
        candidates = tuple(filter(lambda candidate: math.gcd(candidate, size) == 1, range(size)))
        return [b - a for a, b in pairwise(candidates)] + [(candidates[0] - candidates[-1]) % size]
    
    def __init__(self, factors: collections.abc.Iterable[int]):
        'if you pass non-primes as factors, you wont be able to track them at the start of your generator. thats on you, idiot. sorry, harsh words, sorry but if you do that youre kinda dumb.. a bit'
        size = math.lcm(*factors)
        
        if math.prod(factors) != size:
            raise ValueError('factors must be coprime!')
        
        self.size: int = size
        self.candidate: int = 1

        steps: Sequence[int] = Wheel._generate_steps(size)
        self.cycle: cycle[int] = cycle(steps)
        self.cycle_size: int = len(steps)
        
        # initialize candidate properly
        #for factor in factors:  # indexitis
        #    next(self)
    
    def __iter__(self):
        return self
    
    def __next__(self) -> int:
        self.candidate += next(self.cycle)
        return self.candidate

    __repr__ = pretty_repr

class PrimesIterableContainer(IterableContainer):
    """a singleton class representing the infinite sequence of prime numbers. you can do things like:
    
    Primes = PrimeSequence()
    
    Primes[0] == 2
    Primes[1] == 3
    Primes[2] == 5
    Primes[3] == 7

    assert 5 in Primes
    assert 13 in Primes

    primes = Primes[:10]

    for prime in Primes[:100]:
        print(prime)

    uses a 2x3 wheel by default, thus only testing 6*1-1, 6*1+1, 6*2-1, 6*2+1, 6*3-1, 6*3+1, … for generation. larger wheels like 2x3x5, 2x3x5x7, … can be used for better efficiency (see Wheel class)
    """
    
    _cache: MutableSequence[Integral] = [2, 3]

    def __init__(self, wheel_factors: Iterable[int] = [2, 3]):
        self.wheel: Wheel = Wheel(wheel_factors)
        self._cache.extend(wheel_factors[len(self._cache):])
    
    def _extend_cache_by(self, count: int = 1) -> None:
        'grow cache by a certain .count of primes'

        while count > 0:
            candidate = next(self.wheel)
            
            # "is candidate prime?"
            if all(candidate % prime != 0 for prime in self._cache):
                count -= 1
                self._cache.append(candidate)
        
    def __getitem__(self, index: slice | int):
        if isinstance(index, slice):
            self._extend_cache_by(index.stop - len(self._cache))
        elif isinstance(index, int):
            if index < 0:
                raise ValueError('cannot use negative indices on an infinite sequence')
            self._extend_cache_by(index + 1 - len(self._cache))
        else:
            raise TypeError('index must be either slice or int')
        
        return self._cache[index]

    def __iter__(self):
        i = 0

        while True:
            yield self[i := i + 1]
        
    @classmethod
    def __contains__(cls, number: Natural) -> bool:
        # number is known (from cache) to be prime
        if number in cls._cache:
            return True

        # number is within cache
        if cls._cache[-1] >= number:
            return number in cls._cache
        
        # number is not within cache. perform divisibility check
        # this way, cache is generated up to ≥⌊√n⌋ instead of ≥n
        limit: int = math.floor(math.sqrt(number))
        
        for prime in Primes:
            if prime > limit:
                return True
            if number % prime == 0:
                return False    

    def index(self, number):
        if number not in self:
            raise numberError(f'{number} is not prime')

        while self._cache[-1] < number:
            self._extend_cache_by(1)

        return self._cache.index(number)

    __repr__ = pretty_repr

Primes = PrimesIterableContainer()

'''
# here we dont subclass Rational because surds are not rational!
class Surd(Real):
    'like how Integral is a sub(Natural, Natural) pair, and Rational is a div(Integral, Integral) pair, Surd is a root(Integral, Integral) pair. its cousin is the log(Integral, Integral) pair, which i have not named yet. the equivalence class is op(a, b) = op(c, d). so, for example, 2√2 = 4√4'

    def __init__(self, base: Rational, degree: Rational):
        self.base = base
        self.degree = degree

    def __float__(self) -> float:
        return self.base ** (1 / self.degree)

    def __mul__(self, other) -> Surd:
        return self.base
'''

class Monzo(Hashable, Sequence):#, Rational):
    """a datatype that represents rational number stored as prime factors — conceptually as a sparse sequence, implemented as a mapping, but has the interface of a sequence :)

    examples:
    Monzo(2) = [1⟩     = {0: 1} = 2¹
    Monzo(3) = [0 1⟩   = {1: 1} = 3¹
    Monzo(4) = [2⟩     = {0: 2} = 2²
    Monzo(5) = [0 0 1⟩ = {2: 1} = 5¹
    """
    
    def __init__(self, factors: HashableMapping, sign: Literal[-1, 0, +1] = 1):
        self.factors: HashableMapping = factors
        self.sign: Literal[-1, 0, +1] = sign
    
    @cached_property
    def numerator(self) -> Integral:
        return self.sign * math.prod(Primes[prime_index] ** exponent for prime_index, exponent in self.factors.items() if exponent > 0)
    
    @cached_property
    def denominator(self) -> Integral:
        return math.prod(Primes[prime_index] ** -exponent for prime_index, exponent in self.factors.items() if exponent < 0)
    
    @cached_property
    def prime_factors(self) -> Mapping[Integral, Integral]:
        return frozendefaultdict.from_items(int, ((Primes[prime_index], exponent) for prime_index, exponent in self.factors.items()))
    
    # to support Sequence interface
    def __getitem__(self, index: int) -> int:
        return self.factors[index] if index in self.factors else 0
    def __len__(self) -> Cardinal:
        keys = self.factors.keys()
        return max(keys) + 1 if len(keys) > 0 else 1
    def __iter__(self):
        yield from (self.factors[index] for index in range(len(self)))
    
    # to support Rational interface
    def __add__(self, other) -> Monzo:
        'a / b + c / d = (a * d + b * c) / (b * d)'
        a, b, c, d = self.numerator, self.denominator, other.numerator, other.denominator
        return cls.from_parts(a * d + b * c, b * d)
    def __eq__(self, other) -> bool:
        'a / b = c / d'
        a, b, c, d = self.numerator, self.denominator, other.numerator, other.denominator
        return a * d == b * c
    def __float__(self) -> float:
        return self.numerator / self.denominator

    @classmethod
    def from_prime_factors(cls, prime_factors: Mapping, *args, **kwargs) -> Monzo:
        return cls(frozendefaultdict.from_items(int, ((Primes.index(factor), exponent) for factor, exponent in prime_factors.items())), *args, **kwargs)

    @staticmethod
    def _prime_factorize(number: Natural) -> HashableMapping[int, int]:
        factors: MutableMapping = defaultdict(int)
    
        prime_index = 0
    
        while number > 1:
            prime = Primes[prime_index]

            if number % prime == 0:
                number /= prime
                if prime_index in factors:
                    factors[prime_index] += 1
                else:
                    factors[prime_index] = 1
            else:
                prime_index += 1
        
        return frozendefaultdict.from_items(int, factors.items())

    @classmethod
    def from_parts(cls, numerator: Integral, denominator: Integral) -> Monzo:
        sign: Integral = int(math.copysign(1.0, numerator * denominator))

        numerator = Monzo._prime_factorize(numerator)
        denominator = Monzo._prime_factorize(denominator)
        
        factors: MutableMapping = defaultdict(int, numerator)
        
        for prime_factor, exponent in denominator.items():
            if prime_factor in factors:
                factors[prime_factor] -= exponent
            else:
                factors[prime_factor] = -exponent
        
        return cls(frozendefaultdict.from_items(int, factors.items()), sign)

    @classmethod
    def from_rational(cls, number: Rational) -> Monzo:
        return cls.from_parts(number.numerator, number.denominator)

    @classmethod
    def from_sequence(cls, exponents: Sequence[Integral]) -> Monzo:
        'construct from a sequence. has to use reversed, len, and indexing'
        # because we dont want [1⟩ from [1 0 0], not [1 0 0⟩
        trailing_zero_count: int = 0
        for exponent in reversed(exponents):
            if exponent != 0: 
                break
            trailing_zero_count += 1

        items = enumerate(exponents if trailing_zero_count == 0 else exponents[:-trailing_zero_count])

        return cls(frozendefaultdict.from_items(int, items))

    def __hash__(self) -> int:
        return hash(Fraction(self))

    __repr__ = pretty_repr
    def __str__(self) -> str:
        return '[' + ' '.join(str(exponent) for exponent in self) + '⟩'

Rational.register(Monzo)
