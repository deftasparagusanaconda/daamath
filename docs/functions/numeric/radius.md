# radius

`radius(x, y)` = $\sqrt{x^2 + y^2}$

commonly known as hypot in most other libraries, this calculates the euclidean norm of a vector (x, y). it is needed specially because the usual algorithm to compute it would overflow when $x^2$ or $y^2$ are calculated. 
