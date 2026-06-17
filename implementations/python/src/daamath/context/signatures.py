from .. import domains, mappings
from ..utils import Namespace, Signature

succ = Signature(
    domains=Namespace(
        a=domains.COMPLEX),
    codomain=domains.COMPLEX,
    mapping=mappings.succ)

pred = Signature(
    domains=Namespace(
        b=domains.COMPLEX),
    codomain=domains.COMPLEX,
    mapping=mappings.pred)

add = Signature(
    domains=Namespace(
        a=domains.COMPLEX,
        b=domains.COMPLEX),
    codomain=domains.COMPLEX,
    mapping=mappings.add)

sub = Signature(
    domains=Namespace(
        c=domains.COMPLEX,
        b=domains.COMPLEX),
    codomain=domains.COMPLEX,
    mapping=mappings.sub)

bus = Signature(
    domains=Namespace(
        c=domains.COMPLEX,
        a=domains.COMPLEX),
    codomain=domains.COMPLEX,
    mapping=mappings.bus)

mul = Signature(
    domains=Namespace(
        a=domains.COMPLEX,
        b=domains.COMPLEX),
    codomain=domains.COMPLEX,
    mapping=mappings.mul)

div = Signature(
    domains=Namespace(
        c=domains.COMPLEX,
        b=domains.COMPLEX),
    codomain=domains.COMPLEX,
    mapping=mappings.div)

vid = Signature(
    domains=Namespace(
        c=domains.COMPLEX,
        a=domains.COMPLEX),
    codomain=domains.COMPLEX,
    mapping=mappings.vid)

pow = Signature(
    domains=Namespace(
        a=domains.COMPLEX,
        b=domains.COMPLEX),
    codomain=domains.COMPLEX,
    mapping=mappings.pow)

log = Signature(
    domains=Namespace(
        c=domains.COMPLEX,
        b=domains.COMPLEX),
    codomain=domains.COMPLEX,
    mapping=mappings.log)

root = Signature(
    domains=Namespace(
        c=domains.COMPLEX,
        a=domains.COMPLEX),
    codomain=domains.COMPLEX,
    mapping=mappings.root)

not_ = Signature(
    domains=Namespace(
        a=domains.BOOLEAN),
    codomain=domains.BOOLEAN,
    mapping=mappings.not_)

and_ = Signature(
    domains=Namespace(
        a=domains.BOOLEAN,
        b=domains.BOOLEAN),
    codomain=domains.BOOLEAN,
    mapping=mappings.and_)

or_ = Signature(
    domains=Namespace(
        a=domains.BOOLEAN,
        b=domains.BOOLEAN),
    codomain=domains.BOOLEAN,
    mapping=mappings.or_)

xor = Signature(
    domains=Namespace(
        a=domains.BOOLEAN,
        b=domains.BOOLEAN),
    codomain=domains.BOOLEAN,
    mapping=mappings.xor)

imp = Signature(
    domains=Namespace(
        a=domains.BOOLEAN,
        b=domains.BOOLEAN),
    codomain=domains.BOOLEAN,
    mapping=mappings.imp)

con = Signature(
    domains=Namespace(
        a=domains.BOOLEAN,
        b=domains.BOOLEAN),
    codomain=domains.BOOLEAN,
    mapping=mappings.con)

nand = Signature(
    domains=Namespace(
        a=domains.BOOLEAN,
        b=domains.BOOLEAN),
    codomain=domains.BOOLEAN,
    mapping=mappings.nand)

nor = Signature(
    domains=Namespace(
        a=domains.BOOLEAN,
        b=domains.BOOLEAN),
    codomain=domains.BOOLEAN,
    mapping=mappings.nor)

nxor = Signature(
    domains=Namespace(
        a=domains.BOOLEAN,
        b=domains.BOOLEAN),
    codomain=domains.BOOLEAN,
    mapping=mappings.nxor)

nimp = Signature(
    domains=Namespace(
        a=domains.BOOLEAN,
        b=domains.BOOLEAN),
    codomain=domains.BOOLEAN,
    mapping=mappings.nimp)

ncon = Signature(
    domains=Namespace(
        a=domains.BOOLEAN,
        b=domains.BOOLEAN),
    codomain=domains.BOOLEAN,
    mapping=mappings.ncon)
