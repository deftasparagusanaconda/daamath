# constants

daamath maintains the following constants:

[E](https://en.wikipedia.org/wiki/E_(mathematical_constant)) = 2.71828182845904523536028747135266249775…
[TAU](https://en.wikipedia.org/wiki/Tau) = 6.28318530717958647692528676655900576839433879875021…
[I](https://en.wikipedia.org/wiki/Imaginary_unit) = i

LN_2    = 0.69314718055994530941723212145817656807550013436025525412068000949339362196969472…
LN_10   = 2.3025850929940456840179914546843642076011014886287729760333279009675726096773525…
LOG2_E  = 1.4426950408889634073599246810018921374227996472570904805533527522495202437308308…
LOG2_10 = 3.3219280948873623478703194294893901758648313930245806120547563958159347766086252…
LOG10_E = 0.43429448190325182765112891891660508229323915205547281675221698586834173604285939…
LOG10_2 = 0.30102999566398119521373889472449302676818988146210854131042746112710818927442451…

TRUE    
FALSE   

# what can become a constant?

if a set of constants has no clear bound to it, that set should not exist. `DIV_X_TAU` can create an infinite amount of constants, but its not clear where to end it. so its not done. same with `DIV_TAU_X` for example.

# underscore binding

constants follow the underscore binding convention:

`ln(2)` = `LN_2`
`LOG2_10` = `3.32192809488736234…`

rust's convention of `FRAC_2_PI` is pretty awesome. but in daamath, its `DIV_2_PI` instead.

# unicode support

daamath will NOT deal with unicode in the namespace. it is very very non-portable. i also would love to type `from daamath import τ` but unicode support is inconsistent, and that harms our cross-language consistency a lot. 

# where is π??

daamath has a strong stance on π & τ. π is inelegant. τ is elegant. daamath is elegant. daamath uses ONLY τ. 

# booleans

daamath very specially stores the two binary values: `FALSE` & `TRUE`

we do NOT treat them as the integers 0 & 1, nor do we treat them as the integers modulo 2. booleans are truth/logic values that are completely incompatible in arithmetic expressions with numbers. 

for example, in python, you can do `True + 1` and it gives you `2`. this is bad behaviour. ideally we should raise an error here because a logical value should not interact with a number. 

unfortunately setting `TRUE = True` in python would still allow `TRUE + 1` to happen. the implementation would have to create its own boolean type to do this kind of stuff. at that point, daamath starts to define its own datatypes. this is a bit too much feature creep. im still not sure what the solution should be, but we should be wary of this bad behaviour

# rant

`DIV_X_Y` seemed like a good idea until i realized the space blows up and i have to start making arbitrary decisions on where to stop. this is bad. daamath shouldnt make assumptions unless they are mathematically sound and clear. if you want `DIV_1_PI`, make it yourself: `div(1, pi)` or `minv(pi)`
