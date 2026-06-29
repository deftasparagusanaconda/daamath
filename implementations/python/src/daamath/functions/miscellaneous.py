import daamath as dm
from ..exceptions import DomainViolation as _DomainViolation, CodomainViolation as _CodomainViolation

def fold(function, iterable):
    'fold an interable (from left to right) into a single scalar value using a binary function'
    if not dm.context.fold.domains.function(function):
        raise _DomainViolation('fold', (function, iterable), {}, function, dm.context.fold.domains.function)
    if not dm.context.fold.domains.iterable(iterable):
        raise _DomainViolation('fold', (function, iterable), {}, iterable, dm.context.fold.domains.iterable)

    image = dm.context.fold.mapping(function, iterable)

    if not dm.context.fold.codomain(image):
        raise _CodomainViolation('fold', (function, iterable), {}, image, dm.context.fold.codomain)
    return image

def fma(a, b, c):
    'fused multiply-add. solves for d in (a × b) + c = d'
    if not dm.context.fma.domains.a(a):
        raise _DomainViolation('fma', (a, b, c), {}, a, dm.context.fma.domains.a)
    if not dm.context.fma.domains.b(b):
        raise _DomainViolation('fma', (a, b, c), {}, b, dm.context.fma.domains.b)
    if not dm.context.fma.domains.c(c):
        raise _DomainViolation('fma', (a, b, c), {}, c, dm.context.fma.domains.c)

    image = dm.context.fma.mapping(a, b, c)

    if not dm.context.fma.codomain(image):
        raise _CodomainViolation('fma', (a, b, c), {}, image, dm.context.fma.codomain)
    return image

def fsd(d, c, b):
    'fused subtract-divide. solves for a = (d - c) / b in (a × b) + c = d'
    if not dm.context.fsd.domains.d(d):
        raise _DomainViolation('fsd', (d, c, b), {}, d, dm.context.fsd.domains.d)
    if not dm.context.fsd.domains.c(c):
        raise _DomainViolation('fsd', (d, c, b), {}, c, dm.context.fsd.domains.c)
    if not dm.context.fsd.domains.b(b):
        raise _DomainViolation('fsd', (d, c, b), {}, b, dm.context.fsd.domains.b)

    image = dm.context.fsd.mapping(d, c, b)

    if not dm.context.fsd.codomain(image):
        raise _CodomainViolation('fsd', (d, c, b), {}, image, dm.context.fsd.codomain)
    return image

def lerp(parameter, start, end):
    'linear interpolation. solves for result = start + parameter × (end - start). parameter is from an ordered field. start and end are from vector space.'
    if not dm.context.lerp.domains.parameter(parameter):
        raise _DomainViolation('lerp', (parameter, start, end), {}, parameter, dm.context.lerp.domains.parameter)
    if not dm.context.lerp.domains.start(start):
        raise _DomainViolation('lerp', (parameter, start, end), {}, start, dm.context.lerp.domains.start)
    if not dm.context.lerp.domains.end(end):
        raise _DomainViolation('lerp', (parameter, start, end), {}, end, dm.context.lerp.domains.end)

    image = dm.context.lerp.mapping(parameter, start, end)

    if not dm.context.lerp.codomain(image):
        raise _CodomainViolation('lerp', (parameter, start, end), {}, image, dm.context.lerp.codomain)
    return image
