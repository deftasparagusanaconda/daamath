import daamath as dm
from ..exceptions import DomainViolation as _DomainViolation, CodomainViolation as CodomainViolation

def not_(a):
    'negation'
    if not dm.context.not_.domains.a(a):
        raise _DomainViolation('not', (a), {}, a, dm.context.not_.domains.a)

    image = dm.context.not_.mapping(a)

    if not dm.context.not_.codomain(image):
        raise _CodomainViolation('not', ['a'], {}, image, dm.context.not_.codomain)
    return image

def and_(a, b):
    'conjunction'
    if not dm.context.and_.domains.a(a):
        raise _DomainViolation('and', (a, b), {}, a, dm.context.and_.domains.a)
    if not dm.context.and_.domains.b(b):
        raise _DomainViolation('and', (a, b), {}, b, dm.context.and_.domains.b)

    image = dm.context.and_.mapping(a, b)

    if not dm.context.and_.codomain(image):
        raise _CodomainViolation('and', ['a', 'b'], {}, image, dm.context.and_.codomain)
    return image

def or_(a, b):
    'disjunction'
    if not dm.context.or_.domains.a(a):
        raise _DomainViolation('or', (a, b), {}, a, dm.context.or_.domains.a)
    if not dm.context.or_.domains.b(b):
        raise _DomainViolation('or', (a, b), {}, b, dm.context.or_.domains.b)

    image = dm.context.or_.mapping(a, b)

    if not dm.context.or_.codomain(image):
        raise _CodomainViolation('or', ['a', 'b'], {}, image, dm.context.or_.codomain)
    return image

def xor(a, b):
    'exclusive disjunction'
    if not dm.context.xor.domains.a(a):
        raise _DomainViolation('xor', (a, b), {}, a, dm.context.xor.domains.a)
    if not dm.context.xor.domains.b(b):
        raise _DomainViolation('xor', (a, b), {}, b, dm.context.xor.domains.b)

    image = dm.context.xor.mapping(a, b)

    if not dm.context.xor.codomain(image):
        raise _CodomainViolation('xor', ['a', 'b'], {}, image, dm.context.xor.codomain)
    return image

def imp(a, b):
    'material implication'
    if not dm.context.imp.domains.a(a):
        raise _DomainViolation('imp', (a, b), {}, a, dm.context.imp.domains.a)
    if not dm.context.imp.domains.b(b):
        raise _DomainViolation('imp', (a, b), {}, b, dm.context.imp.domains.b)

    image = dm.context.imp.mapping(a, b)

    if not dm.context.imp.codomain(image):
        raise _CodomainViolation('imp', ['a', 'b'], {}, image, dm.context.imp.codomain)
    return image

def con(a, b):
    'converse material implication'
    if not dm.context.con.domains.a(a):
        raise _DomainViolation('con', (a, b), {}, a, dm.context.con.domains.a)
    if not dm.context.con.domains.b(b):
        raise _DomainViolation('con', (a, b), {}, b, dm.context.con.domains.b)

    image = dm.context.con.mapping(a, b)

    if not dm.context.con.codomain(image):
        raise _CodomainViolation('con', ['a', 'b'], {}, image, dm.context.con.codomain)
    return image

def nand(a, b):
    'not(and)'
    if not dm.context.nand.domains.a(a):
        raise _DomainViolation('nand', (a, b), {}, a, dm.context.nand.domains.a)
    if not dm.context.nand.domains.b(b):
        raise _DomainViolation('nand', (a, b), {}, b, dm.context.nand.domains.b)

    image = dm.context.nand.mapping(a, b)

    if not dm.context.nand.codomain(image):
        raise _CodomainViolation('nand', ['a', 'b'], {}, image, dm.context.nand.codomain)
    return image

def nor(a, b):
    'not(or)'
    if not dm.context.nor.domains.a(a):
        raise _DomainViolation('nor', (a, b), {}, a, dm.context.nor.domains.a)
    if not dm.context.nor.domains.b(b):
        raise _DomainViolation('nor', (a, b), {}, b, dm.context.nor.domains.b)

    image = dm.context.nor.mapping(a, b)

    if not dm.context.nor.codomain(image):
        raise _CodomainViolation('nor', ['a', 'b'], {}, image, dm.context.nor.codomain)
    return image

def nxor(a, b):
    'not(xor)'
    if not dm.context.nxor.domains.a(a):
        raise _DomainViolation('nxor', (a, b), {}, a, dm.context.nxor.domains.a)
    if not dm.context.nxor.domains.b(b):
        raise _DomainViolation('nxor', (a, b), {}, b, dm.context.nxor.domains.b)

    image = dm.context.nxor.mapping(a, b)

    if not dm.context.nxor.codomain(image):
        raise _CodomainViolation('nxor', ['a', 'b'], {}, image, dm.context.nxor.codomain)
    return image

def nimp(a, b):
    'not(imp)'
    if not dm.context.nimp.domains.a(a):
        raise _DomainViolation('nimp', (a, b), {}, a, dm.context.nimp.domains.a)
    if not dm.context.nimp.domains.b(b):
        raise _DomainViolation('nimp', (a, b), {}, b, dm.context.nimp.domains.b)

    image = dm.context.nimp.mapping(a, b)

    if not dm.context.nimp.codomain(image):
        raise _CodomainViolation('nimp', ['a', 'b'], {}, image, dm.context.nimp.codomain)
    return image

def ncon(a, b):
    'not(ncon)'
    if not dm.context.ncon.domains.a(a):
        raise _DomainViolation('ncon', (a, b), {}, a, dm.context.ncon.domains.a)
    if not dm.context.ncon.domains.b(b):
        raise _DomainViolation('ncon', (a, b), {}, b, dm.context.ncon.domains.b)

    image = dm.context.ncon.mapping(a, b)

    if not dm.context.ncon.codomain(image):
        raise _CodomainViolation('ncon', ['a', 'b'], {}, image, dm.context.ncon.codomain)
    return image
