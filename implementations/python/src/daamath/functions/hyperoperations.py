import daamath as dm
from ..exceptions import DomainViolation, CodomainViolation

def succ(a):
    'successor. solves for b in ++a = b'
    if not dm.context.succ.domains.a(arg):
        raise DomainViolation('succ', ['a'], {}, arg, dm.context.succ.domains.a)
    image = dm.context.succ.mapping(a)
    if not dm.context.succ.codomain(image):
        raise CodomainViolation('succ', ['a'], {}, image, dm.context.succ.codomain)
    return image

def pred(b):
    'predecessor. solves for a in ++a = b'
    if not dm.context.pred.domains.b(arg):
        raise DomainViolation('pred', ['b'], {}, arg, dm.context.pred.domains.b)
    image = dm.context.pred.mapping(b)
    if not dm.context.pred.codomain(image):
        raise CodomainViolation('pred', ['b'], {}, image, dm.context.pred.codomain)
    return image

def add(a, b):
    'addition. solves for c in a + b = c'
    if not dm.context.add.domains.a(arg):
        raise DomainViolation('add', ['a', 'b'], {}, arg, dm.context.add.domains.a)
    if not dm.context.add.domains.b(arg):
        raise DomainViolation('add', ['a', 'b'], {}, arg, dm.context.add.domains.b)
    image = dm.context.add.mapping(a, b)
    if not dm.context.add.codomain(image):
        raise CodomainViolation('add', ['a', 'b'], {}, image, dm.context.add.codomain)
    return image

def sub(c, b):
    'subtraction. solves for a in a + b = c'
    if not dm.context.sub.domains.c(arg):
        raise DomainViolation('sub', ['c', 'b'], {}, arg, dm.context.sub.domains.c)
    if not dm.context.sub.domains.b(arg):
        raise DomainViolation('sub', ['c', 'b'], {}, arg, dm.context.sub.domains.b)
    image = dm.context.sub.mapping(c, b)
    if not dm.context.sub.codomain(image):
        raise CodomainViolation('sub', ['c', 'b'], {}, image, dm.context.sub.codomain)
    return image

def bus(c, a):
    'bustraction. solves for b in a + b = c'
    if not dm.context.bus.domains.c(arg):
        raise DomainViolation('bus', ['c', 'a'], {}, arg, dm.context.bus.domains.c)
    if not dm.context.bus.domains.a(arg):
        raise DomainViolation('bus', ['c', 'a'], {}, arg, dm.context.bus.domains.a)
    image = dm.context.bus.mapping(c, a)
    if not dm.context.bus.codomain(image):
        raise CodomainViolation('bus', ['c', 'a'], {}, image, dm.context.bus.codomain)
    return image

def mul(a, b):
    'multiplication. solves for c in a × b = c'
    if not dm.context.mul.domains.a(arg):
        raise DomainViolation('mul', ['a', 'b'], {}, arg, dm.context.mul.domains.a)
    if not dm.context.mul.domains.b(arg):
        raise DomainViolation('mul', ['a', 'b'], {}, arg, dm.context.mul.domains.b)
    image = dm.context.mul.mapping(a, b)
    if not dm.context.mul.codomain(image):
        raise CodomainViolation('mul', ['a', 'b'], {}, image, dm.context.mul.codomain)
    return image

def div(c, b):
    'division. solves for a in a × b = c'
    if not dm.context.div.domains.c(arg):
        raise DomainViolation('div', ['c', 'b'], {}, arg, dm.context.div.domains.c)
    if not dm.context.div.domains.b(arg):
        raise DomainViolation('div', ['c', 'b'], {}, arg, dm.context.div.domains.b)
    image = dm.context.div.mapping(c, b)
    if not dm.context.div.codomain(image):
        raise CodomainViolation('div', ['c', 'b'], {}, image, dm.context.div.codomain)
    return image

def vid(c, a):
    'vidision. solves for b in a × b = c'
    if not dm.context.vid.domains.c(arg):
        raise DomainViolation('vid', ['c', 'a'], {}, arg, dm.context.vid.domains.c)
    if not dm.context.vid.domains.a(arg):
        raise DomainViolation('vid', ['c', 'a'], {}, arg, dm.context.vid.domains.a)
    image = dm.context.vid.mapping(c, a)
    if not dm.context.vid.codomain(image):
        raise CodomainViolation('vid', ['c', 'a'], {}, image, dm.context.vid.codomain)
    return image

def pow(a, b):
    'exponentiation. solves for c in a ^ b = c'
    if not dm.context.pow.domains.a(arg):
        raise DomainViolation('pow', ['a', 'b'], {}, arg, dm.context.pow.domains.a)
    if not dm.context.pow.domains.b(arg):
        raise DomainViolation('pow', ['a', 'b'], {}, arg, dm.context.pow.domains.b)
    image = dm.context.pow.mapping(a, b)
    if not dm.context.pow.codomain(image):
        raise CodomainViolation('pow', ['a', 'b'], {}, image, dm.context.pow.codomain)
    return image

def log(c, b):
    'logarithm. solves for a in a ^ b = c'
    if not dm.context.log.domains.c(arg):
        raise DomainViolation('log', ['c', 'b'], {}, arg, dm.context.log.domains.c)
    if not dm.context.log.domains.b(arg):
        raise DomainViolation('log', ['c', 'b'], {}, arg, dm.context.log.domains.b)
    image = dm.context.log.mapping(c, b)
    if not dm.context.log.codomain(image):
        raise CodomainViolation('log', ['c', 'b'], {}, image, dm.context.log.codomain)
    return image

def root(c, a):
    'root. solves for b in a ^ b = c'
    if not dm.context.root.domains.c(arg):
        raise DomainViolation('root', ['c', 'a'], {}, arg, dm.context.root.domains.c)
    if not dm.context.root.domains.a(arg):
        raise DomainViolation('root', ['c', 'a'], {}, arg, dm.context.root.domains.a)
    image = dm.context.root.mapping(c, a)
    if not dm.context.root.codomain(image):
        raise CodomainViolation('root', ['c', 'a'], {}, image, dm.context.root.codomain)
    return image
