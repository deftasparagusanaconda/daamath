from . import domains as _domains, mappings as _mappings
from .utils import Signature as _Signature
from types import SimpleNamespace as _SimpleNamespace
context = _SimpleNamespace(
    not_ = _Signature(
        domains = _SimpleNamespace(
            a = _domains.BOOLEAN),
        codomain = _domains.BOOLEAN,
        mapping = _mappings.not_),

    and_ = _Signature(
        domains = _SimpleNamespace(
            a = _domains.BOOLEAN,
            b = _domains.BOOLEAN),
        codomain = _domains.BOOLEAN,
        mapping = _mappings.and_),

    or_ = _Signature(
        domains = _SimpleNamespace(
            a = _domains.BOOLEAN,
            b = _domains.BOOLEAN),
        codomain = _domains.BOOLEAN,
        mapping = _mappings.or_),

    xor = _Signature(
        domains = _SimpleNamespace(
            a = _domains.BOOLEAN,
            b = _domains.BOOLEAN),
        codomain = _domains.BOOLEAN,
        mapping = _mappings.xor),

    imp = _Signature(
        domains = _SimpleNamespace(
            a = _domains.BOOLEAN,
            b = _domains.BOOLEAN),
        codomain = _domains.BOOLEAN,
        mapping = _mappings.imp),

    con = _Signature(
        domains = _SimpleNamespace(
            a = _domains.BOOLEAN,
            b = _domains.BOOLEAN),
        codomain = _domains.BOOLEAN,
        mapping = _mappings.con),

    nand = _Signature(
        domains = _SimpleNamespace(
            a = _domains.BOOLEAN,
            b = _domains.BOOLEAN),
        codomain = _domains.BOOLEAN,
        mapping = _mappings.nand),

    nor = _Signature(
        domains = _SimpleNamespace(
            a = _domains.BOOLEAN,
            b = _domains.BOOLEAN),
        codomain = _domains.BOOLEAN,
        mapping = _mappings.nor),

    nxor = _Signature(
        domains = _SimpleNamespace(
            a = _domains.BOOLEAN,
            b = _domains.BOOLEAN),
        codomain = _domains.BOOLEAN,
        mapping = _mappings.nxor),

    nimp = _Signature(
        domains = _SimpleNamespace(
            a = _domains.BOOLEAN,
            b = _domains.BOOLEAN),
        codomain = _domains.BOOLEAN,
        mapping = _mappings.nimp),

    ncon = _Signature(
        domains = _SimpleNamespace(
            a = _domains.BOOLEAN,
            b = _domains.BOOLEAN),
        codomain = _domains.BOOLEAN,
        mapping = _mappings.ncon),

    succ = _Signature(
        domains = _SimpleNamespace(
            a = _domains.COMPLEX),
        codomain = _domains.COMPLEX,
        mapping = _mappings.succ),

    pred = _Signature(
        domains = _SimpleNamespace(
            b = _domains.COMPLEX),
        codomain = _domains.COMPLEX,
        mapping = _mappings.pred),

    add = _Signature(
        domains = _SimpleNamespace(
            a = _domains.COMPLEX,
            b = _domains.COMPLEX),
        codomain = _domains.COMPLEX,
        mapping = _mappings.add),

    sub = _Signature(
        domains = _SimpleNamespace(
            c = _domains.COMPLEX,
            b = _domains.COMPLEX),
        codomain = _domains.COMPLEX,
        mapping = _mappings.sub),

    bus = _Signature(
        domains = _SimpleNamespace(
            c = _domains.COMPLEX,
            a = _domains.COMPLEX),
        codomain = _domains.COMPLEX,
        mapping = _mappings.bus),

    mul = _Signature(
        domains = _SimpleNamespace(
            a = _domains.COMPLEX,
            b = _domains.COMPLEX),
        codomain = _domains.COMPLEX,
        mapping = _mappings.mul),

    div = _Signature(
        domains = _SimpleNamespace(
            c = _domains.COMPLEX,
            b = _domains.COMPLEX),
        codomain = _domains.COMPLEX,
        mapping = _mappings.div),

    vid = _Signature(
        domains = _SimpleNamespace(
            c = _domains.COMPLEX,
            a = _domains.COMPLEX),
        codomain = _domains.COMPLEX,
        mapping = _mappings.vid),

    pow = _Signature(
        domains = _SimpleNamespace(
            a = _domains.COMPLEX,
            b = _domains.COMPLEX),
        codomain = _domains.COMPLEX,
        mapping = _mappings.pow),

    log = _Signature(
        domains = _SimpleNamespace(
            c = _domains.COMPLEX,
            b = _domains.COMPLEX),
        codomain = _domains.COMPLEX,
        mapping = _mappings.log),

    root = _Signature(
        domains = _SimpleNamespace(
            c = _domains.COMPLEX,
            a = _domains.COMPLEX),
        codomain = _domains.COMPLEX,
        mapping = _mappings.root),

)