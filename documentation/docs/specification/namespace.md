# namespace

daamath maintains a cross-language-friendly namespace. daamath's casing conventions do not change according to the implementation. here are the rules:

# everything is lowercase

"why not make constants uppercase?" because then the namespace would be doing something that its not supposed to do: enforcing constantness by convention, not by mechanism. if something is meant to be constant, the language should enforce that, not the namespace. 

# aliases

daamath maintains an internal namespace and a friendly external namespace using [aliases]. each internal name may have only one user-friendly alias. for example, addition is internally `h1r` but its friendly alias is `add`. natural logarithm is `h3d__e` (n3 hyperoperation solving for degree, with second argument bound to e) but its friendly alias is `ln`. 

[aliases.yaml](aliases.yaml):
```yaml
{% include "./aliases.yaml" %}
```

# underscore binding

daamath has a rigorous argument pre-binding convention. it is clearest by example:

`ln(a)` = `LN_A`  
`div(p, q)` = `div_p(q)` = `div__q(p)` = `DIV_P_Q`  
`fma(a, b, c)` = `fma_a(b, c)` = `fma__b(a, c)` = `fma___c(a, b)` = `fma_a_b(c)` = `fma_a__c(b)` = `fma__b_c(a)` = `FMA_A_B_C`  

this allows us to use [prefix notation](https://simple.wikipedia.org/wiki/Prefix_notation) directly in the namespace. the disadvantage is that we cannot have underscores to separate words in names. for this reason, daamath only uses this in the internal namespace. for example, `h3d__10(a)` is very unsightly so instead we give the alias `log10(a)`. the external namespace shall still do its best to conform to this convention though.

# rant

rust has an awesome convention of `FRAC_A_B` for fractions like `FRAC_2_PI` for 2/π for example. in daamath, this becomes `DIV_2_PI`, directly exposing its derivation. `LN_2`, `ZETA_3`, etc etc now makes sense instantly as well. 
