from . import domains as _domains, mappings as _mappings
from .utils import Signature as _Signature
from types import SimpleNamespace as _SimpleNamespace
context = _SimpleNamespace(
    succ = _Signature(
        domains = _SimpleNamespace(
            a = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.succ),

    pred = _Signature(
        domains = _SimpleNamespace(
            b = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.pred),

    add = _Signature(
        domains = _SimpleNamespace(
            a = _domains.complex,
            b = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.add),

    sub = _Signature(
        domains = _SimpleNamespace(
            c = _domains.complex,
            b = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.sub),

    bus = _Signature(
        domains = _SimpleNamespace(
            c = _domains.complex,
            a = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.bus),

    mul = _Signature(
        domains = _SimpleNamespace(
            a = _domains.complex,
            b = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.mul),

    div = _Signature(
        domains = _SimpleNamespace(
            c = _domains.complex,
            b = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.div),

    vid = _Signature(
        domains = _SimpleNamespace(
            c = _domains.complex,
            a = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.vid),

    pow = _Signature(
        domains = _SimpleNamespace(
            a = _domains.complex,
            b = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.pow),

    log = _Signature(
        domains = _SimpleNamespace(
            c = _domains.complex,
            b = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.log),

    root = _Signature(
        domains = _SimpleNamespace(
            c = _domains.complex,
            a = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.root),

    sin = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.sin),

    cos = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.cos),

    tan = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.tan),

    cot = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.cot),

    sec = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.sec),

    csc = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.csc),

    asin = _Signature(
        domains = _SimpleNamespace(
            ratio = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.asin),

    acos = _Signature(
        domains = _SimpleNamespace(
            ratio = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.acos),

    atan = _Signature(
        domains = _SimpleNamespace(
            ratio = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.atan),

    acot = _Signature(
        domains = _SimpleNamespace(
            ratio = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.acot),

    asec = _Signature(
        domains = _SimpleNamespace(
            ratio = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.asec),

    acsc = _Signature(
        domains = _SimpleNamespace(
            ratio = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.acsc),

    sinh = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.sinh),

    cosh = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.cosh),

    tanh = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.tanh),

    coth = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.coth),

    sech = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.sech),

    csch = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.csch),

    asinh = _Signature(
        domains = _SimpleNamespace(
            semiarea = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.asinh),

    acosh = _Signature(
        domains = _SimpleNamespace(
            ratio = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.acosh),

    atanh = _Signature(
        domains = _SimpleNamespace(
            ratio = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.atanh),

    acoth = _Signature(
        domains = _SimpleNamespace(
            ratio = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.acoth),

    asech = _Signature(
        domains = _SimpleNamespace(
            ratio = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.asech),

    acsch = _Signature(
        domains = _SimpleNamespace(
            ratio = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.acsch),

    not_ = _Signature(
        domains = _SimpleNamespace(
            a = _domains.boolean),
        codomain = _domains.boolean,
        mapping = _mappings.not_),

    and_ = _Signature(
        domains = _SimpleNamespace(
            a = _domains.boolean,
            b = _domains.boolean),
        codomain = _domains.boolean,
        mapping = _mappings.and_),

    or_ = _Signature(
        domains = _SimpleNamespace(
            a = _domains.boolean,
            b = _domains.boolean),
        codomain = _domains.boolean,
        mapping = _mappings.or_),

    xor = _Signature(
        domains = _SimpleNamespace(
            a = _domains.boolean,
            b = _domains.boolean),
        codomain = _domains.boolean,
        mapping = _mappings.xor),

    imp = _Signature(
        domains = _SimpleNamespace(
            a = _domains.boolean,
            b = _domains.boolean),
        codomain = _domains.boolean,
        mapping = _mappings.imp),

    con = _Signature(
        domains = _SimpleNamespace(
            a = _domains.boolean,
            b = _domains.boolean),
        codomain = _domains.boolean,
        mapping = _mappings.con),

    nand = _Signature(
        domains = _SimpleNamespace(
            a = _domains.boolean,
            b = _domains.boolean),
        codomain = _domains.boolean,
        mapping = _mappings.nand),

    nor = _Signature(
        domains = _SimpleNamespace(
            a = _domains.boolean,
            b = _domains.boolean),
        codomain = _domains.boolean,
        mapping = _mappings.nor),

    nxor = _Signature(
        domains = _SimpleNamespace(
            a = _domains.boolean,
            b = _domains.boolean),
        codomain = _domains.boolean,
        mapping = _mappings.nxor),

    nimp = _Signature(
        domains = _SimpleNamespace(
            a = _domains.boolean,
            b = _domains.boolean),
        codomain = _domains.boolean,
        mapping = _mappings.nimp),

    ncon = _Signature(
        domains = _SimpleNamespace(
            a = _domains.boolean,
            b = _domains.boolean),
        codomain = _domains.boolean,
        mapping = _mappings.ncon),

    fold = _Signature(
        domains = _SimpleNamespace(
            function = _domains.function,
            iterable = _domains.iterable),
        codomain = _domains.anything,
        mapping = _mappings.fold),

    fma = _Signature(
        domains = _SimpleNamespace(
            a = _domains.float,
            b = _domains.float,
            c = _domains.float),
        codomain = _domains.float,
        mapping = _mappings.fma),

    fsd = _Signature(
        domains = _SimpleNamespace(
            d = _domains.float,
            c = _domains.float,
            b = _domains.float),
        codomain = _domains.float,
        mapping = _mappings.fsd),

    lerp = _Signature(
        domains = _SimpleNamespace(
            parameter = _domains.real,
            start = _domains.complex,
            end = _domains.complex),
        codomain = _domains.complex,
        mapping = _mappings.lerp),

)