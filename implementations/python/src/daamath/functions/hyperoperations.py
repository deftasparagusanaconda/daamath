import daamath as dm
from ..exceptions import DomainViolation as _DomainViolation, CodomainViolation as _CodomainViolation

def succ(a):
    'successor. solves for b in ++a = b'
    if not dm.context.succ.domains.a(a):
        raise _DomainViolation('succ', (a), {}, a, dm.context.succ.domains.a)

    image = dm.context.succ.mapping(a)

    if not dm.context.succ.codomain(image):
        raise _CodomainViolation('succ', (a), {}, image, dm.context.succ.codomain)
    return image

def pred(b):
    'predecessor. solves for a in ++a = b'
    if not dm.context.pred.domains.b(b):
        raise _DomainViolation('pred', (b), {}, b, dm.context.pred.domains.b)

    image = dm.context.pred.mapping(b)

    if not dm.context.pred.codomain(image):
        raise _CodomainViolation('pred', (b), {}, image, dm.context.pred.codomain)
    return image

def add(a, b):
    'addision. solves for c in a + b = c'
    if not dm.context.add.domains.a(a):
        raise _DomainViolation('add', (a, b), {}, a, dm.context.add.domains.a)
    if not dm.context.add.domains.b(b):
        raise _DomainViolation('add', (a, b), {}, b, dm.context.add.domains.b)

    image = dm.context.add.mapping(a, b)

    if not dm.context.add.codomain(image):
        raise _CodomainViolation('add', (a, b), {}, image, dm.context.add.codomain)
    return image

def sub(c, b):
    'subtraction. solves for a in a + b = c'
    if not dm.context.sub.domains.c(c):
        raise _DomainViolation('sub', (c, b), {}, c, dm.context.sub.domains.c)
    if not dm.context.sub.domains.b(b):
        raise _DomainViolation('sub', (c, b), {}, b, dm.context.sub.domains.b)

    image = dm.context.sub.mapping(c, b)

    if not dm.context.sub.codomain(image):
        raise _CodomainViolation('sub', (c, b), {}, image, dm.context.sub.codomain)
    return image

def bus(c, a):
    'bustraction. solves for b in a + b = c'
    if not dm.context.bus.domains.c(c):
        raise _DomainViolation('bus', (c, a), {}, c, dm.context.bus.domains.c)
    if not dm.context.bus.domains.a(a):
        raise _DomainViolation('bus', (c, a), {}, a, dm.context.bus.domains.a)

    image = dm.context.bus.mapping(c, a)

    if not dm.context.bus.codomain(image):
        raise _CodomainViolation('bus', (c, a), {}, image, dm.context.bus.codomain)
    return image

def mul(a, b):
    'multiplication. solves for c in a × b = c'
    if not dm.context.mul.domains.a(a):
        raise _DomainViolation('mul', (a, b), {}, a, dm.context.mul.domains.a)
    if not dm.context.mul.domains.b(b):
        raise _DomainViolation('mul', (a, b), {}, b, dm.context.mul.domains.b)

    image = dm.context.mul.mapping(a, b)

    if not dm.context.mul.codomain(image):
        raise _CodomainViolation('mul', (a, b), {}, image, dm.context.mul.codomain)
    return image

def div(c, b):
    'division. solves for a in a × b = c'
    if not dm.context.div.domains.c(c):
        raise _DomainViolation('div', (c, b), {}, c, dm.context.div.domains.c)
    if not dm.context.div.domains.b(b):
        raise _DomainViolation('div', (c, b), {}, b, dm.context.div.domains.b)

    image = dm.context.div.mapping(c, b)

    if not dm.context.div.codomain(image):
        raise _CodomainViolation('div', (c, b), {}, image, dm.context.div.codomain)
    return image

def vid(c, a):
    'vidision. solves for b in a × b = c'
    if not dm.context.vid.domains.c(c):
        raise _DomainViolation('vid', (c, a), {}, c, dm.context.vid.domains.c)
    if not dm.context.vid.domains.a(a):
        raise _DomainViolation('vid', (c, a), {}, a, dm.context.vid.domains.a)

    image = dm.context.vid.mapping(c, a)

    if not dm.context.vid.codomain(image):
        raise _CodomainViolation('vid', (c, a), {}, image, dm.context.vid.codomain)
    return image

def pow(a, b):
    'exponentiation. solves for c in a ^ b = c'
    if not dm.context.pow.domains.a(a):
        raise _DomainViolation('pow', (a, b), {}, a, dm.context.pow.domains.a)
    if not dm.context.pow.domains.b(b):
        raise _DomainViolation('pow', (a, b), {}, b, dm.context.pow.domains.b)

    image = dm.context.pow.mapping(a, b)

    if not dm.context.pow.codomain(image):
        raise _CodomainViolation('pow', (a, b), {}, image, dm.context.pow.codomain)
    return image

def log(c, b):
    'logarithm. solves for a in a ^ b = c'
    if not dm.context.log.domains.c(c):
        raise _DomainViolation('log', (c, b), {}, c, dm.context.log.domains.c)
    if not dm.context.log.domains.b(b):
        raise _DomainViolation('log', (c, b), {}, b, dm.context.log.domains.b)

    image = dm.context.log.mapping(c, b)

    if not dm.context.log.codomain(image):
        raise _CodomainViolation('log', (c, b), {}, image, dm.context.log.codomain)
    return image

def root(c, a):
    'root. solves for b in a ^ b = c'
    if not dm.context.root.domains.c(c):
        raise _DomainViolation('root', (c, a), {}, c, dm.context.root.domains.c)
    if not dm.context.root.domains.a(a):
        raise _DomainViolation('root', (c, a), {}, a, dm.context.root.domains.a)

    image = dm.context.root.mapping(c, a)

    if not dm.context.root.codomain(image):
        raise _CodomainViolation('root', (c, a), {}, image, dm.context.root.codomain)
    return image
