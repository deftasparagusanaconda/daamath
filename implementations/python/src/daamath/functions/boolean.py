import daamath as dm
from ..exceptions import DomainViolation, CodomainViolation

def _not(a):
    'negation'
    if not dm.context._not.domains.a(arg):
        raise DomainViolation('not', ['a'], {}, arg, dm.context._not.domains.a)
    image = dm.context._not.mapping(a)
    if not dm.context._not.codomain(image):
        raise CodomainViolation('not', ['a'], {}, image, dm.context._not.codomain)
    return image

def _and(a, b):
    'conjunction'
    if not dm.context._and.domains.a(arg):
        raise DomainViolation('and', ['a', 'b'], {}, arg, dm.context._and.domains.a)
    if not dm.context._and.domains.b(arg):
        raise DomainViolation('and', ['a', 'b'], {}, arg, dm.context._and.domains.b)
    image = dm.context._and.mapping(a, b)
    if not dm.context._and.codomain(image):
        raise CodomainViolation('and', ['a', 'b'], {}, image, dm.context._and.codomain)
    return image

def _or(a, b):
    'disjunction'
    if not dm.context._or.domains.a(arg):
        raise DomainViolation('or', ['a', 'b'], {}, arg, dm.context._or.domains.a)
    if not dm.context._or.domains.b(arg):
        raise DomainViolation('or', ['a', 'b'], {}, arg, dm.context._or.domains.b)
    image = dm.context._or.mapping(a, b)
    if not dm.context._or.codomain(image):
        raise CodomainViolation('or', ['a', 'b'], {}, image, dm.context._or.codomain)
    return image

def xor(a, b):
    'exclusive disjunction'
    if not dm.context.xor.domains.a(arg):
        raise DomainViolation('xor', ['a', 'b'], {}, arg, dm.context.xor.domains.a)
    if not dm.context.xor.domains.b(arg):
        raise DomainViolation('xor', ['a', 'b'], {}, arg, dm.context.xor.domains.b)
    image = dm.context.xor.mapping(a, b)
    if not dm.context.xor.codomain(image):
        raise CodomainViolation('xor', ['a', 'b'], {}, image, dm.context.xor.codomain)
    return image

def imp(a, b):
    'material implication'
    if not dm.context.imp.domains.a(arg):
        raise DomainViolation('imp', ['a', 'b'], {}, arg, dm.context.imp.domains.a)
    if not dm.context.imp.domains.b(arg):
        raise DomainViolation('imp', ['a', 'b'], {}, arg, dm.context.imp.domains.b)
    image = dm.context.imp.mapping(a, b)
    if not dm.context.imp.codomain(image):
        raise CodomainViolation('imp', ['a', 'b'], {}, image, dm.context.imp.codomain)
    return image

def con(a, b):
    'converse material implication'
    if not dm.context.con.domains.a(arg):
        raise DomainViolation('con', ['a', 'b'], {}, arg, dm.context.con.domains.a)
    if not dm.context.con.domains.b(arg):
        raise DomainViolation('con', ['a', 'b'], {}, arg, dm.context.con.domains.b)
    image = dm.context.con.mapping(a, b)
    if not dm.context.con.codomain(image):
        raise CodomainViolation('con', ['a', 'b'], {}, image, dm.context.con.codomain)
    return image

def nand(a, b):
    'not(and)'
    if not dm.context.nand.domains.a(arg):
        raise DomainViolation('nand', ['a', 'b'], {}, arg, dm.context.nand.domains.a)
    if not dm.context.nand.domains.b(arg):
        raise DomainViolation('nand', ['a', 'b'], {}, arg, dm.context.nand.domains.b)
    image = dm.context.nand.mapping(a, b)
    if not dm.context.nand.codomain(image):
        raise CodomainViolation('nand', ['a', 'b'], {}, image, dm.context.nand.codomain)
    return image

def nor(a, b):
    'not(or)'
    if not dm.context.nor.domains.a(arg):
        raise DomainViolation('nor', ['a', 'b'], {}, arg, dm.context.nor.domains.a)
    if not dm.context.nor.domains.b(arg):
        raise DomainViolation('nor', ['a', 'b'], {}, arg, dm.context.nor.domains.b)
    image = dm.context.nor.mapping(a, b)
    if not dm.context.nor.codomain(image):
        raise CodomainViolation('nor', ['a', 'b'], {}, image, dm.context.nor.codomain)
    return image

def nxor(a, b):
    'not(xor)'
    if not dm.context.nxor.domains.a(arg):
        raise DomainViolation('nxor', ['a', 'b'], {}, arg, dm.context.nxor.domains.a)
    if not dm.context.nxor.domains.b(arg):
        raise DomainViolation('nxor', ['a', 'b'], {}, arg, dm.context.nxor.domains.b)
    image = dm.context.nxor.mapping(a, b)
    if not dm.context.nxor.codomain(image):
        raise CodomainViolation('nxor', ['a', 'b'], {}, image, dm.context.nxor.codomain)
    return image

def nimp(a, b):
    'not(imp)'
    if not dm.context.nimp.domains.a(arg):
        raise DomainViolation('nimp', ['a', 'b'], {}, arg, dm.context.nimp.domains.a)
    if not dm.context.nimp.domains.b(arg):
        raise DomainViolation('nimp', ['a', 'b'], {}, arg, dm.context.nimp.domains.b)
    image = dm.context.nimp.mapping(a, b)
    if not dm.context.nimp.codomain(image):
        raise CodomainViolation('nimp', ['a', 'b'], {}, image, dm.context.nimp.codomain)
    return image

def ncon(a, b):
    'not(ncon)'
    if not dm.context.ncon.domains.a(arg):
        raise DomainViolation('ncon', ['a', 'b'], {}, arg, dm.context.ncon.domains.a)
    if not dm.context.ncon.domains.b(arg):
        raise DomainViolation('ncon', ['a', 'b'], {}, arg, dm.context.ncon.domains.b)
    image = dm.context.ncon.mapping(a, b)
    if not dm.context.ncon.codomain(image):
        raise CodomainViolation('ncon', ['a', 'b'], {}, image, dm.context.ncon.codomain)
    return image
