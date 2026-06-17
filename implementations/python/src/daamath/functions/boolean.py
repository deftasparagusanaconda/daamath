import daamath as dm
from ..exceptions import DomainViolation, CodomainViolation

def not_(a):
    'negation'
    if not dm.signatures.not_.domains.a(a):
        raise DomainViolation('not', ['a'], {}, a, dm.signatures.not_.domains.a)

    image = dm.signatures.not_.mapping(a)

    if not dm.signatures.not_.codomain(image):
        raise CodomainViolation('not', ['a'], {}, image, dm.signatures.not_.codomain)
    return image

def and_(a, b):
    'conjunction'
    if not dm.signatures.and_.domains.a(a):
        raise DomainViolation('and', ['a', 'b'], {}, a, dm.signatures.and_.domains.a)
    if not dm.signatures.and_.domains.b(b):
        raise DomainViolation('and', ['a', 'b'], {}, b, dm.signatures.and_.domains.b)

    image = dm.signatures.and_.mapping(a, b)

    if not dm.signatures.and_.codomain(image):
        raise CodomainViolation('and', ['a', 'b'], {}, image, dm.signatures.and_.codomain)
    return image

def or_(a, b):
    'disjunction'
    if not dm.signatures.or_.domains.a(a):
        raise DomainViolation('or', ['a', 'b'], {}, a, dm.signatures.or_.domains.a)
    if not dm.signatures.or_.domains.b(b):
        raise DomainViolation('or', ['a', 'b'], {}, b, dm.signatures.or_.domains.b)

    image = dm.signatures.or_.mapping(a, b)

    if not dm.signatures.or_.codomain(image):
        raise CodomainViolation('or', ['a', 'b'], {}, image, dm.signatures.or_.codomain)
    return image

def xor(a, b):
    'exclusive disjunction'
    if not dm.signatures.xor.domains.a(a):
        raise DomainViolation('xor', ['a', 'b'], {}, a, dm.signatures.xor.domains.a)
    if not dm.signatures.xor.domains.b(b):
        raise DomainViolation('xor', ['a', 'b'], {}, b, dm.signatures.xor.domains.b)

    image = dm.signatures.xor.mapping(a, b)

    if not dm.signatures.xor.codomain(image):
        raise CodomainViolation('xor', ['a', 'b'], {}, image, dm.signatures.xor.codomain)
    return image

def imp(a, b):
    'material implication'
    if not dm.signatures.imp.domains.a(a):
        raise DomainViolation('imp', ['a', 'b'], {}, a, dm.signatures.imp.domains.a)
    if not dm.signatures.imp.domains.b(b):
        raise DomainViolation('imp', ['a', 'b'], {}, b, dm.signatures.imp.domains.b)

    image = dm.signatures.imp.mapping(a, b)

    if not dm.signatures.imp.codomain(image):
        raise CodomainViolation('imp', ['a', 'b'], {}, image, dm.signatures.imp.codomain)
    return image

def con(a, b):
    'converse material implication'
    if not dm.signatures.con.domains.a(a):
        raise DomainViolation('con', ['a', 'b'], {}, a, dm.signatures.con.domains.a)
    if not dm.signatures.con.domains.b(b):
        raise DomainViolation('con', ['a', 'b'], {}, b, dm.signatures.con.domains.b)

    image = dm.signatures.con.mapping(a, b)

    if not dm.signatures.con.codomain(image):
        raise CodomainViolation('con', ['a', 'b'], {}, image, dm.signatures.con.codomain)
    return image

def nand(a, b):
    'not(and)'
    if not dm.signatures.nand.domains.a(a):
        raise DomainViolation('nand', ['a', 'b'], {}, a, dm.signatures.nand.domains.a)
    if not dm.signatures.nand.domains.b(b):
        raise DomainViolation('nand', ['a', 'b'], {}, b, dm.signatures.nand.domains.b)

    image = dm.signatures.nand.mapping(a, b)

    if not dm.signatures.nand.codomain(image):
        raise CodomainViolation('nand', ['a', 'b'], {}, image, dm.signatures.nand.codomain)
    return image

def nor(a, b):
    'not(or)'
    if not dm.signatures.nor.domains.a(a):
        raise DomainViolation('nor', ['a', 'b'], {}, a, dm.signatures.nor.domains.a)
    if not dm.signatures.nor.domains.b(b):
        raise DomainViolation('nor', ['a', 'b'], {}, b, dm.signatures.nor.domains.b)

    image = dm.signatures.nor.mapping(a, b)

    if not dm.signatures.nor.codomain(image):
        raise CodomainViolation('nor', ['a', 'b'], {}, image, dm.signatures.nor.codomain)
    return image

def nxor(a, b):
    'not(xor)'
    if not dm.signatures.nxor.domains.a(a):
        raise DomainViolation('nxor', ['a', 'b'], {}, a, dm.signatures.nxor.domains.a)
    if not dm.signatures.nxor.domains.b(b):
        raise DomainViolation('nxor', ['a', 'b'], {}, b, dm.signatures.nxor.domains.b)

    image = dm.signatures.nxor.mapping(a, b)

    if not dm.signatures.nxor.codomain(image):
        raise CodomainViolation('nxor', ['a', 'b'], {}, image, dm.signatures.nxor.codomain)
    return image

def nimp(a, b):
    'not(imp)'
    if not dm.signatures.nimp.domains.a(a):
        raise DomainViolation('nimp', ['a', 'b'], {}, a, dm.signatures.nimp.domains.a)
    if not dm.signatures.nimp.domains.b(b):
        raise DomainViolation('nimp', ['a', 'b'], {}, b, dm.signatures.nimp.domains.b)

    image = dm.signatures.nimp.mapping(a, b)

    if not dm.signatures.nimp.codomain(image):
        raise CodomainViolation('nimp', ['a', 'b'], {}, image, dm.signatures.nimp.codomain)
    return image

def ncon(a, b):
    'not(ncon)'
    if not dm.signatures.ncon.domains.a(a):
        raise DomainViolation('ncon', ['a', 'b'], {}, a, dm.signatures.ncon.domains.a)
    if not dm.signatures.ncon.domains.b(b):
        raise DomainViolation('ncon', ['a', 'b'], {}, b, dm.signatures.ncon.domains.b)

    image = dm.signatures.ncon.mapping(a, b)

    if not dm.signatures.ncon.codomain(image):
        raise CodomainViolation('ncon', ['a', 'b'], {}, image, dm.signatures.ncon.codomain)
    return image
