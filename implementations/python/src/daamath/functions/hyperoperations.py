import daamath as dm
from ..exceptions import DomainViolation, CodomainViolation

def succ(a):
    'successor. solves for b in ++a = b'
    if not dm.signatures.succ.domains.a(a):
        raise DomainViolation('succ', ['a'], {}, a, dm.signatures.succ.domains.a)

    image = dm.signatures.succ.mapping(a)

    if not dm.signatures.succ.codomain(image):
        raise CodomainViolation('succ', ['a'], {}, image, dm.signatures.succ.codomain)
    return image

def pred(b):
    'predecessor. solves for a in ++a = b'
    if not dm.signatures.pred.domains.b(b):
        raise DomainViolation('pred', ['b'], {}, b, dm.signatures.pred.domains.b)

    image = dm.signatures.pred.mapping(b)

    if not dm.signatures.pred.codomain(image):
        raise CodomainViolation('pred', ['b'], {}, image, dm.signatures.pred.codomain)
    return image

def add(a, b):
    'addition. solves for c in a + b = c'
    if not dm.signatures.add.domains.a(a):
        raise DomainViolation('add', ['a', 'b'], {}, a, dm.signatures.add.domains.a)
    if not dm.signatures.add.domains.b(b):
        raise DomainViolation('add', ['a', 'b'], {}, b, dm.signatures.add.domains.b)

    image = dm.signatures.add.mapping(a, b)

    if not dm.signatures.add.codomain(image):
        raise CodomainViolation('add', ['a', 'b'], {}, image, dm.signatures.add.codomain)
    return image

def sub(c, b):
    'subtraction. solves for a in a + b = c'
    if not dm.signatures.sub.domains.c(c):
        raise DomainViolation('sub', ['c', 'b'], {}, c, dm.signatures.sub.domains.c)
    if not dm.signatures.sub.domains.b(b):
        raise DomainViolation('sub', ['c', 'b'], {}, b, dm.signatures.sub.domains.b)

    image = dm.signatures.sub.mapping(c, b)

    if not dm.signatures.sub.codomain(image):
        raise CodomainViolation('sub', ['c', 'b'], {}, image, dm.signatures.sub.codomain)
    return image

def bus(c, a):
    'bustraction. solves for b in a + b = c'
    if not dm.signatures.bus.domains.c(c):
        raise DomainViolation('bus', ['c', 'a'], {}, c, dm.signatures.bus.domains.c)
    if not dm.signatures.bus.domains.a(a):
        raise DomainViolation('bus', ['c', 'a'], {}, a, dm.signatures.bus.domains.a)

    image = dm.signatures.bus.mapping(c, a)

    if not dm.signatures.bus.codomain(image):
        raise CodomainViolation('bus', ['c', 'a'], {}, image, dm.signatures.bus.codomain)
    return image

def mul(a, b):
    'multiplication. solves for c in a × b = c'
    if not dm.signatures.mul.domains.a(a):
        raise DomainViolation('mul', ['a', 'b'], {}, a, dm.signatures.mul.domains.a)
    if not dm.signatures.mul.domains.b(b):
        raise DomainViolation('mul', ['a', 'b'], {}, b, dm.signatures.mul.domains.b)

    image = dm.signatures.mul.mapping(a, b)

    if not dm.signatures.mul.codomain(image):
        raise CodomainViolation('mul', ['a', 'b'], {}, image, dm.signatures.mul.codomain)
    return image

def div(c, b):
    'division. solves for a in a × b = c'
    if not dm.signatures.div.domains.c(c):
        raise DomainViolation('div', ['c', 'b'], {}, c, dm.signatures.div.domains.c)
    if not dm.signatures.div.domains.b(b):
        raise DomainViolation('div', ['c', 'b'], {}, b, dm.signatures.div.domains.b)

    image = dm.signatures.div.mapping(c, b)

    if not dm.signatures.div.codomain(image):
        raise CodomainViolation('div', ['c', 'b'], {}, image, dm.signatures.div.codomain)
    return image

def vid(c, a):
    'vidision. solves for b in a × b = c'
    if not dm.signatures.vid.domains.c(c):
        raise DomainViolation('vid', ['c', 'a'], {}, c, dm.signatures.vid.domains.c)
    if not dm.signatures.vid.domains.a(a):
        raise DomainViolation('vid', ['c', 'a'], {}, a, dm.signatures.vid.domains.a)

    image = dm.signatures.vid.mapping(c, a)

    if not dm.signatures.vid.codomain(image):
        raise CodomainViolation('vid', ['c', 'a'], {}, image, dm.signatures.vid.codomain)
    return image

def pow(a, b):
    'exponentiation. solves for c in a ^ b = c'
    if not dm.signatures.pow.domains.a(a):
        raise DomainViolation('pow', ['a', 'b'], {}, a, dm.signatures.pow.domains.a)
    if not dm.signatures.pow.domains.b(b):
        raise DomainViolation('pow', ['a', 'b'], {}, b, dm.signatures.pow.domains.b)

    image = dm.signatures.pow.mapping(a, b)

    if not dm.signatures.pow.codomain(image):
        raise CodomainViolation('pow', ['a', 'b'], {}, image, dm.signatures.pow.codomain)
    return image

def log(c, b):
    'logarithm. solves for a in a ^ b = c'
    if not dm.signatures.log.domains.c(c):
        raise DomainViolation('log', ['c', 'b'], {}, c, dm.signatures.log.domains.c)
    if not dm.signatures.log.domains.b(b):
        raise DomainViolation('log', ['c', 'b'], {}, b, dm.signatures.log.domains.b)

    image = dm.signatures.log.mapping(c, b)

    if not dm.signatures.log.codomain(image):
        raise CodomainViolation('log', ['c', 'b'], {}, image, dm.signatures.log.codomain)
    return image

def root(c, a):
    'root. solves for b in a ^ b = c'
    if not dm.signatures.root.domains.c(c):
        raise DomainViolation('root', ['c', 'a'], {}, c, dm.signatures.root.domains.c)
    if not dm.signatures.root.domains.a(a):
        raise DomainViolation('root', ['c', 'a'], {}, a, dm.signatures.root.domains.a)

    image = dm.signatures.root.mapping(c, a)

    if not dm.signatures.root.codomain(image):
        raise CodomainViolation('root', ['c', 'a'], {}, image, dm.signatures.root.codomain)
    return image
