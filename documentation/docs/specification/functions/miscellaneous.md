# miscellaneous

here, daamath keeps functions that dont really have a home yet

# rounded division

rounded division with quotient and remainder is special. we have the following family of operators:

quot(dividend, divisor) = quotient ≈ quantize(div(dividend, divisor))
rem(dividend, divisor) = remainder ≈ dividend - quot(dividend, divisor)

these two functions are involved in two equations, with a total of 4 variables. the 2 functions already solve for quotient and remainder. we can solve for dividend and divisor using fma and fsd:

fma(divisor, quotient, remainder) = (divisor * quotient) + remainder = dividend  
fsd(dividend, remainder, quotient) = (dividend - remainder) / quotient = divisor  

thus the four functions `quot` `rem` `fma` `fsd` are all part of the same family. this result was quite surprising to me, because quot and rem came from number theory, and fma is found in the depths of numerical computation. somehow, fma now naturally finds its way into daamath's roster, and fsd emerges as a new operation to complete the family.

# meet & join: gcd & lcm, …

gcd and lcm are just the meet and join of the integer divisibility lattice

# idfk

fact(n) = prod(\[1, n\]) = n!
sumt(n) = sum(\[1, n\]) = (n * (n + 1)) / 2
comb(n, k) = how many k-combinations are possible with n elements?
perm(n, k) = how many k-permutations are possible with n elements?

we should also have inverses for each one. inverse factorial, inverse sumtorial, inverse comb, inverse perm

# hypercomplex

| name | explanation | example |
| - | - | - |
| scalar  | scalar part |  scalar(2+3𝑖) = 2 |
| vector  | vector part |  vector(2+3ε) = 3ε |
| reify | coefficient of imaginary component | reify(2+3j) = 3 |
| angle   | angle       |   angle(2+3𝑖) ≈ 0.98279372 |
| conj  | conjugate      |  conj(2+3𝑖) = 2−3𝑖 |

the `reify` function works for any of the 3 canonical 2D HYPERCOMPLEX domains (complex/hyperbolic/dual). it extracts the coefficient of the imaginary part, and casts it onto the REAL domain. this is possible only with the 2D domains because their imaginary part has the same shape as the real number axis: a 1D line.

similarly, the `angle` function 

# vectorial

norm(V) returns the norm of a vector V. it generalizes abs
unit(V) = V / norm(V) returns the unit vector associated with a vector V. it generalizes signum. if V is 0, it returns 0, because the vector is a zero vector.

norm is overloaded for scalars, scalars that behave like vectors (like complex numbers), and vectors. it is not overloaded for tensors of rank > 1 because there is no canonical norm for them, yet.
