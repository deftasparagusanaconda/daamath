import daamath as dm
from ..exceptions import DomainViolation as _DomainViolation, CodomainViolation as _CodomainViolation

def sin(semiarea):
    'circular sin; real(exp(semiarea * i)) where i² = −1'
    if not dm.context.sin.domains.semiarea(semiarea):
        raise _DomainViolation('sin', (semiarea), {}, semiarea, dm.context.sin.domains.semiarea)

    image = dm.context.sin.mapping(semiarea)

    if not dm.context.sin.codomain(image):
        raise _CodomainViolation('sin', (semiarea), {}, image, dm.context.sin.codomain)
    return image

def cos(semiarea):
    'circular sin; real(exp(semiarea * i)) where i² = −1'
    if not dm.context.cos.domains.semiarea(semiarea):
        raise _DomainViolation('cos', (semiarea), {}, semiarea, dm.context.cos.domains.semiarea)

    image = dm.context.cos.mapping(semiarea)

    if not dm.context.cos.codomain(image):
        raise _CodomainViolation('cos', (semiarea), {}, image, dm.context.cos.codomain)
    return image

def tan(semiarea):
    'sin(semiarea) / cos(semiarea)'
    if not dm.context.tan.domains.semiarea(semiarea):
        raise _DomainViolation('tan', (semiarea), {}, semiarea, dm.context.tan.domains.semiarea)

    image = dm.context.tan.mapping(semiarea)

    if not dm.context.tan.codomain(image):
        raise _CodomainViolation('tan', (semiarea), {}, image, dm.context.tan.codomain)
    return image

def cot(semiarea):
    'multiplicative inverse of tan'
    if not dm.context.cot.domains.semiarea(semiarea):
        raise _DomainViolation('cot', (semiarea), {}, semiarea, dm.context.cot.domains.semiarea)

    image = dm.context.cot.mapping(semiarea)

    if not dm.context.cot.codomain(image):
        raise _CodomainViolation('cot', (semiarea), {}, image, dm.context.cot.codomain)
    return image

def sec(semiarea):
    'multiplicative inverse of cos'
    if not dm.context.sec.domains.semiarea(semiarea):
        raise _DomainViolation('sec', (semiarea), {}, semiarea, dm.context.sec.domains.semiarea)

    image = dm.context.sec.mapping(semiarea)

    if not dm.context.sec.codomain(image):
        raise _CodomainViolation('sec', (semiarea), {}, image, dm.context.sec.codomain)
    return image

def csc(semiarea):
    'multiplicative inverse of sin'
    if not dm.context.csc.domains.semiarea(semiarea):
        raise _DomainViolation('csc', (semiarea), {}, semiarea, dm.context.csc.domains.semiarea)

    image = dm.context.csc.mapping(semiarea)

    if not dm.context.csc.codomain(image):
        raise _CodomainViolation('csc', (semiarea), {}, image, dm.context.csc.codomain)
    return image

def asin(ratio):
    'haha'
    if not dm.context.asin.domains.ratio(ratio):
        raise _DomainViolation('asin', (ratio), {}, ratio, dm.context.asin.domains.ratio)

    image = dm.context.asin.mapping(ratio)

    if not dm.context.asin.codomain(image):
        raise _CodomainViolation('asin', (ratio), {}, image, dm.context.asin.codomain)
    return image

def acos(ratio):
    'haha'
    if not dm.context.acos.domains.ratio(ratio):
        raise _DomainViolation('acos', (ratio), {}, ratio, dm.context.acos.domains.ratio)

    image = dm.context.acos.mapping(ratio)

    if not dm.context.acos.codomain(image):
        raise _CodomainViolation('acos', (ratio), {}, image, dm.context.acos.codomain)
    return image

def atan(ratio):
    'haha'
    if not dm.context.atan.domains.ratio(ratio):
        raise _DomainViolation('atan', (ratio), {}, ratio, dm.context.atan.domains.ratio)

    image = dm.context.atan.mapping(ratio)

    if not dm.context.atan.codomain(image):
        raise _CodomainViolation('atan', (ratio), {}, image, dm.context.atan.codomain)
    return image

def acot(ratio):
    'haha'
    if not dm.context.acot.domains.ratio(ratio):
        raise _DomainViolation('acot', (ratio), {}, ratio, dm.context.acot.domains.ratio)

    image = dm.context.acot.mapping(ratio)

    if not dm.context.acot.codomain(image):
        raise _CodomainViolation('acot', (ratio), {}, image, dm.context.acot.codomain)
    return image

def asec(ratio):
    'haha'
    if not dm.context.asec.domains.ratio(ratio):
        raise _DomainViolation('asec', (ratio), {}, ratio, dm.context.asec.domains.ratio)

    image = dm.context.asec.mapping(ratio)

    if not dm.context.asec.codomain(image):
        raise _CodomainViolation('asec', (ratio), {}, image, dm.context.asec.codomain)
    return image

def acsc(ratio):
    'haha'
    if not dm.context.acsc.domains.ratio(ratio):
        raise _DomainViolation('acsc', (ratio), {}, ratio, dm.context.acsc.domains.ratio)

    image = dm.context.acsc.mapping(ratio)

    if not dm.context.acsc.codomain(image):
        raise _CodomainViolation('acsc', (ratio), {}, image, dm.context.acsc.codomain)
    return image

def sinh(semiarea):
    'haha'
    if not dm.context.sinh.domains.semiarea(semiarea):
        raise _DomainViolation('sinh', (semiarea), {}, semiarea, dm.context.sinh.domains.semiarea)

    image = dm.context.sinh.mapping(semiarea)

    if not dm.context.sinh.codomain(image):
        raise _CodomainViolation('sinh', (semiarea), {}, image, dm.context.sinh.codomain)
    return image

def cosh(semiarea):
    'haha'
    if not dm.context.cosh.domains.semiarea(semiarea):
        raise _DomainViolation('cosh', (semiarea), {}, semiarea, dm.context.cosh.domains.semiarea)

    image = dm.context.cosh.mapping(semiarea)

    if not dm.context.cosh.codomain(image):
        raise _CodomainViolation('cosh', (semiarea), {}, image, dm.context.cosh.codomain)
    return image

def tanh(semiarea):
    'haha'
    if not dm.context.tanh.domains.semiarea(semiarea):
        raise _DomainViolation('tanh', (semiarea), {}, semiarea, dm.context.tanh.domains.semiarea)

    image = dm.context.tanh.mapping(semiarea)

    if not dm.context.tanh.codomain(image):
        raise _CodomainViolation('tanh', (semiarea), {}, image, dm.context.tanh.codomain)
    return image

def coth(semiarea):
    'haha'
    if not dm.context.coth.domains.semiarea(semiarea):
        raise _DomainViolation('coth', (semiarea), {}, semiarea, dm.context.coth.domains.semiarea)

    image = dm.context.coth.mapping(semiarea)

    if not dm.context.coth.codomain(image):
        raise _CodomainViolation('coth', (semiarea), {}, image, dm.context.coth.codomain)
    return image

def sech(semiarea):
    'haha'
    if not dm.context.sech.domains.semiarea(semiarea):
        raise _DomainViolation('sech', (semiarea), {}, semiarea, dm.context.sech.domains.semiarea)

    image = dm.context.sech.mapping(semiarea)

    if not dm.context.sech.codomain(image):
        raise _CodomainViolation('sech', (semiarea), {}, image, dm.context.sech.codomain)
    return image

def csch(semiarea):
    'haha'
    if not dm.context.csch.domains.semiarea(semiarea):
        raise _DomainViolation('csch', (semiarea), {}, semiarea, dm.context.csch.domains.semiarea)

    image = dm.context.csch.mapping(semiarea)

    if not dm.context.csch.codomain(image):
        raise _CodomainViolation('csch', (semiarea), {}, image, dm.context.csch.codomain)
    return image

def asinh(semiarea):
    'haha'
    if not dm.context.asinh.domains.semiarea(semiarea):
        raise _DomainViolation('asinh', (semiarea), {}, semiarea, dm.context.asinh.domains.semiarea)

    image = dm.context.asinh.mapping(semiarea)

    if not dm.context.asinh.codomain(image):
        raise _CodomainViolation('asinh', (semiarea), {}, image, dm.context.asinh.codomain)
    return image

def acosh(ratio):
    'haha'
    if not dm.context.acosh.domains.ratio(ratio):
        raise _DomainViolation('acosh', (ratio), {}, ratio, dm.context.acosh.domains.ratio)

    image = dm.context.acosh.mapping(ratio)

    if not dm.context.acosh.codomain(image):
        raise _CodomainViolation('acosh', (ratio), {}, image, dm.context.acosh.codomain)
    return image

def atanh(ratio):
    'haha'
    if not dm.context.atanh.domains.ratio(ratio):
        raise _DomainViolation('atanh', (ratio), {}, ratio, dm.context.atanh.domains.ratio)

    image = dm.context.atanh.mapping(ratio)

    if not dm.context.atanh.codomain(image):
        raise _CodomainViolation('atanh', (ratio), {}, image, dm.context.atanh.codomain)
    return image

def acoth(ratio):
    'haha'
    if not dm.context.acoth.domains.ratio(ratio):
        raise _DomainViolation('acoth', (ratio), {}, ratio, dm.context.acoth.domains.ratio)

    image = dm.context.acoth.mapping(ratio)

    if not dm.context.acoth.codomain(image):
        raise _CodomainViolation('acoth', (ratio), {}, image, dm.context.acoth.codomain)
    return image

def asech(ratio):
    'haha'
    if not dm.context.asech.domains.ratio(ratio):
        raise _DomainViolation('asech', (ratio), {}, ratio, dm.context.asech.domains.ratio)

    image = dm.context.asech.mapping(ratio)

    if not dm.context.asech.codomain(image):
        raise _CodomainViolation('asech', (ratio), {}, image, dm.context.asech.codomain)
    return image

def acsch(ratio):
    'haha'
    if not dm.context.acsch.domains.ratio(ratio):
        raise _DomainViolation('acsch', (ratio), {}, ratio, dm.context.acsch.domains.ratio)

    image = dm.context.acsch.mapping(ratio)

    if not dm.context.acsch.codomain(image):
        raise _CodomainViolation('acsch', (ratio), {}, image, dm.context.acsch.codomain)
    return image
