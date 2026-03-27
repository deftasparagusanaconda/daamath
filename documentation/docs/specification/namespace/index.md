# introduction

daamath maintains a cross-language-friendly namespace. here are the rules:

lowercase for functions. uppercase for constants.

daamath maintains an internal namespace and a friendly external namespace. each internal name may have only one user-friendly alias. for example, addition is internally `h1r` but its friendly alias is `add`. natural logarithm is `h3d__e` (n3 hyperoperation solving for degree, with second argument bound to e) but its friendly alias is `ln`. 

functions are internally lowercase, with [underscore binding](#underscore-binding). externally, they are given friendly aliases.  
constants are internally uppercase, with [underscore binding](#underscore-binding). externally, they are given friendly aliases.  
strings are uppercase with normal underscores.  

the namespace will not change according to the language's conventions.

# underscore binding

daamath has a rigorous argument pre-binding convention. it is clearest by example:

`ln(a)` = `LN_A`  
`div(p, q)` = `div_p(q)` = `div__q(p)` = `DIV_P_Q`  
`fma(a, b, c)` = `fma_a(b, c)` = `fma__b(a, c)` = `fma___c(a, b)` = `fma_a_b(c)` = `fma_a__c(b)` = `fma__b_c(a)` = `FMA_A_B_C`  

this allows us to use [prefix notation](https://simple.wikipedia.org/wiki/Prefix_notation) directly in the namespace. the disadvantage is that we cannot have underscores in function names. daamath only uses this in the internal namespace because names get ugly quickly. `h3d__10(a)` is very unsightly so instead we give the alias `log10(a)`.

rust has an awesome convention of `FRAC_A_B` for fractions like `FRAC_2_PI` for 2/π for example. in daamath, this becomes `DIV_2_PI`, directly exposing its derivation. `LN_2`, `ZETA_3`, etc etc now makes sense instantly as well. 

# aliases

each internal name may have 1 alias, but no more. aliases are listed [here][aliases]

[aliases]: aliases.md
