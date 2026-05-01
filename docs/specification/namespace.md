# namespace

daamath maintains a cross-language-friendly namespace. daamath's casing conventions do not change according to the implementation. here are the rules:

# everything is lowercase

"why not make constants uppercase?" because then the namespace would be doing something that its not supposed to do: enforcing constantness by convention, not by mechanism. if something is meant to be constant, the language should enforce that, not the namespace. 

# aliases

daamath will not have an alias for anything. when something has a name, that name becomes the only way to access it. we never maintain any shortcuts in the namespace. 

# underscore binding

daamath has a rigorous argument pre-binding convention. it is clearest by example:

`ln(a)` = `LN_A`  
`div(p, q)` = `div_p(q)` = `div__q(p)` = `DIV_P_Q`  
`fma(a, b, c)` = `fma_a(b, c)` = `fma__b(a, c)` = `fma___c(a, b)` = `fma_a_b(c)` = `fma_a__c(b)` = `fma__b_c(a)` = `FMA_A_B_C`  

this allows us to use [prefix notation](https://simple.wikipedia.org/wiki/Prefix_notation) directly in a name. it is most useful for constants like `DIV_2_PI` = `2 / π`. 

the disadvantage is that we cannot have underscores to separate words in names. this is not always beautiful. for example, `log10(a)` should technically be `log__10(a)` but `log10` should instead be thought of as its own function 

# rant

rust has an awesome convention of `FRAC_A_B` for fractions like `FRAC_2_PI` for 2/π for example. in daamath, this becomes `DIV_2_PI`, directly exposing its derivation. `LN_2`, `ZETA_3`, etc etc now makes sense instantly as well. 
