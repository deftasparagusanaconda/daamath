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
| re    | scalar part | re(2+3i) = 2 |
| im    | vector part | im(2+3ε) = 3ε |
| conj  | conjugate   | conj(2+3j) = 2−3j |
| rei   | imaginary part as real number | reify(2+3i) = 3 |
<!--| angle | angle       | angle(2+3i) ≈ 0.98279372 |-->

daamath's goal is to not promote the complex numbers as the only extension of the real numbers, and to not have functions specialized specifically to complex numbers only. the functions provided should generalize to more algebrae to introduce the user to more maths.

the `rei` function only works for the three 2D HYPERCOMPLEX domains (complex, split-complex, dual). it extracts the coefficient of the imaginary part, and casts it onto the REAL domain. this is possible only with the 2D domains because their imaginary part has the same shape as the real number axis: a 1D line.

getting the angle of a complex number is not supported yet because daamath has not formalized yet what angles are. the domains page will elaborate on this in the future. specifically, about how angles have equivalence classes but those equivalence classes are based on the lie group. you cant assume everything obeys 360° = 0° because, for example, quaternions dont °

# vectorial

norm(V) returns the norm of a vector V. it generalizes abs
unit(V) = V / norm(V) returns the unit vector associated with a vector V. it generalizes signum. if V is 0, it returns 0, because the vector is a zero vector.

norm is overloaded for scalars, scalars that behave like vectors (like complex numbers), and vectors. it is not overloaded for tensors of rank > 1 because there is no canonical norm for them, yet.
