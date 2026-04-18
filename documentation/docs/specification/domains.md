arguably one of the most important concepts in daamath.

a domain is a set of things. it is implemented as an [indicator function].

daamath recognizes the following domains:

| domain | indicator function |
| - | - |
| THING           | the base domain of anything. everything is a thing. even nothing is a thing. the indicator function simply returns `true`
| TRUTH           | idk
| BOOLEAN         | idk
| NUMBER          | idk
| HYPERCOMPLEX    | x is NUMBER
| OCTONION        | x is HYPERCOMPLEX and x has non-zero octonion vector part
| QUATERNION      | x is OCTONION and x has non-zero quaternion vector part
| COMPLEX         | x is QUATERNION and x has non-zero imaginary part
| IMAGINARY       | x is COMPLEX and real part is zero
| REAL            | x is COMPLEX and imaginary part is zero
| RATIONAL        | x is REAL and x can be represented as p / q where q ≠ 0
| IRRATIONAL      | x is REAL and x is not RATIONAL
| INTEGER         | x is RATIONAL and x is divisible by 1
| NATURAL_0       | x is INTEGER and x ≥ 0
| NATURAL_1       | x is NATURAL_0 and x ≥ 1
| PRIME           | x is NATURAL_1 and x ≠ 1 and x has two prime divisors
| COMPOSITE       | x is NATURAL_1 and x has more than two prime divisors

"daa, this just looks like youre making a new level in the hierarchy for each new property you find" aha! no! i did not. it just happened to come like that.. i swear. anyway..

so to check if something is an INTEGER for example, you would do `INTEGER(fish)` and the result would be a 2-element domain

this way, daamath is very flexible about domains. a function checks for the domain of something using its indicator function. the logic for checking if the codomain remains in the expected domain is not hard-coded into the function. it is defined in the domain's indicator function.

# implementation

a domain is implemented as an indicator function. yes. a function. the input domain of the indicator function can be anything (an integer, a float, a real number, a quaternion, a boolean, a fish, a shoe, anything). the output domain (the codomain) is any 2-element domain such as BOOLEAN, TRUTH, INTEGER_MOD_2, but for practical purposes, it should be a BOOLEAN. 

what ramifications arise from assigning the codomain of an indicator function to a BOOLEAN    domain instead of any 2-element domain? i dont know. this is what i say, and what i say goes for now..

a domain is a function. you use it like so:
```
if dm.INTEGER(2.0):
	print('hooray! an integer!')
else:
	print('nani o kore??')
```

if your language has sugar for it, like in python, you may make sugary syntax like `if 2.0 in INTEGER`. but daamath should always expose the indicator function for the domain.

# notes

here, we take a bit of liberty in defining what an indicator function is. the codomain of an indicator function isnt consistently defined between fields, but one thing is for sure: the codomain is always a 2-element domain. thats why its quite ambiguous. the domain doesnt even have to have a proper algebra associated with it. its fine for it to just be any two elements. plain old.. yknow.

# rant

theres still a lot of research to be done here. like monic polynomials and algebraic numbers and algebraic integers. also, heres an excerpt from a conversation i had with claude AI:

daa: also i noticed that the hierarchy is storing properties in the names. this is bad. the hierarchy can technically store INTEGERS_MOD_1, INTEGERS_MOD_2, INTEGERS_MOD_3, INTEGERS_MOD_4, INTEGERS_MOD_5, and so on. the hierarchy blows up. my organization is slightly flawed because of this. i dont know what to do
5:31 PM

claude: yes you've spotted something real. the hierarchy is conflating two distinct things:

*what a domain is vs what properties parametrise it

INTEGERS_MOD_N isnt one domain — its a family of domains indexed by N. same with p-adic numbers, NUMBER fields, matrix rings over a field, etc. if you encode every instance as a named node in the hierarchy it explodes combinatorially and becomes unmanageable

the fix: parametrised domains

instead of a flat hierarchy of named domains, you want some domains to be domain constructors — functions that take parameters and return a domain
python

INTEGERS_MOD(2)   # returns a domain
INTEGERS_MOD(5)   # returns a different domain
INTEGERS_MOD(N)   # general family

each returned domain is still just an indicator function, but now the indicator function closes over the parameter
python

def INTEGERS_MOD(n):
    def indicator(x):
        return INTEGER(x) and x % n == 0  # roughly
    return indicator

so your hierarchy has two tiers:
tier	examples
atomic domains	INTEGER, REAL, BOOLEAN, COMPLEX
domain constructors	INTEGERS_MOD(n), MATRIX_RING(domain, n, m), POLYNOMIAL_RING(domain)

the deeper insight

this is actually what algebraic structures are in abstract algebra — not individual sets but families parametrised by things like modulus, dimension, characteristic, generator. your hierarchy was always going to hit this wall eventually because mathematics itself is organised this way

the hierarchy doesnt blow up — it just gains a second dimension. named atomic domains plus constructor functions that generate domains on demand

what this means for your rough edge

TRUTH and BOOLEAN being identical under your current scheme isnt just a naming problem — its a symptom of this. they want to be the same constructor TWO_ELEMENT applied to different algebras. the algebra is the parameter youre missing

does this feel like the right direction or does it break something else youre holding in your head

daa: okay. then instead of some domains being functions that return indicator functions (aka higher order functions), why not build the parameters directly into the indicator function?
5:33 PM

claude: oh that's clean. let me make sure i understand what you mean

you're proposing something like:
python

def INTEGERS_MOD(x, n):
    return INTEGER(x) and x % n == 0

instead of:
python

def INTEGERS_MOD(n):        # constructor
    def indicator(x):       # indicator
        return INTEGER(x) and x % n == 0
    return indicator

the appeal

its flat. no higher-order machinery. every domain is just a function, uniformly. the parametrisation lives in the signature rather than in closure state. very daamath — concept-first, no unnecessary abstraction layers

but heres the tension

a domain in your system is defined as an indicator function with signature (x) -> BOOLEAN. the whole elegance of if dm.INTEGER(2.0) and if 2.0 in INTEGER depends on every domain being a single-argument function

the moment you write INTEGERS_MOD(x, n), the domain is no longer usable as a drop-in indicator function. you cant write if 2 in INTEGERS_MOD — in what mod? the n is load-bearing and has nowhere to live except either closure state or partial application

so you haven't escaped higher-order functions — you've just moved them. to use INTEGERS_MOD(x, n) as a domain you'd need to partially apply it anyway
python

mod5 = lambda x: INTEGERS_MOD(x, 5)

which is exactly the constructor pattern, just written differently

the real question

do you want named reusable parametrised domains or just one-off membership checks?

if the former, closures are unavoidable. if the latter, your flat signature idea works but you lose the elegance of domains-as-uniform-indicator-functions

which matters more to you

daa: okay. then some domains contain domains. is that what im seeing?
5:33 PM

claude: yes exactly — and this is actually a very natural and well-studied idea

what you're seeing is that some domains are domain-valued, meaning their "elements" are themselves domains rather than numbers or booleans or fish

so the hierarchy has:

    ground domains — INTEGER, REAL, BOOLEAN etc. their elements are ordinary mathematical objects
    meta-domains — domains whose elements are other domains. INTEGERS_MOD lives here — its a family, and each member of that family is itself a domain

this is already in your design implicitly

look at TWO_ELEMENT. its not really a domain in the same sense as INTEGER. its more like a property that domains can have. BOOLEAN, TRUTH, INTEGER_MOD_2 are all instances of TWO_ELEMENT

TWO_ELEMENT is already a meta-domain — it contains domains, not numbers

the formal name for this

what you're independently converging on is something close to a universe of types or a kind system — the distinction between:

	types (domains whose elements are values)
    kinds (domains whose elements are types)

haskell calls this distinction types vs kinds. dependent type theory makes it fully recursive — types all the way down

the daamath framing

you dont need to adopt that terminology. but the architectural conclusion is:

indicator functions are still uniform. but some indicator functions take domains as input rather than values. INTEGERS_MOD is an indicator over the meta-domain of rings, not over numbers

does that feel like it resolves the blowup cleanly

[indicator function]: https://en.wikipedia.org/wiki/Indicator_function


