from dataclasses import dataclass
from typing import Callable

@dataclass
class Input:
    ...

@dataclass
class Output:
    ...

@dataclass
class Function:
    definition: Callable
    inputs: Input
    output: Output

@dataclass
class Functions:
    add: Function

@dataclass
class Domain:
    ...

@dataclass
class Domains:
    RATIONALS: Domain

@dataclass
class DataType:
    assumed_domain: Domain
    sentinel_value: Any
    rounding: idfk

@dataclass
class DataTypes:
    int
    float

@dataclass
class Context:
    "a collection of variables that define daamath's behaviour"
    functions: Functions
    domains: Domains
    datatypes: DataTypes
