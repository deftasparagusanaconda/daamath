# hyperoperations

to give a pleasant organization to the most common arithmetic operators, daamath uses the [hyperoperation](https://en.wikipedia.org/wiki/Hyperoperation) tower as a semantic guide:

![diagram for little kids i guess lol](diagrams/hyperoperations.svg)

1 + 1 + 1 + … b times is     b
b + b + b + … d times is b × d  
b × b × b × … d times is b ^ d  
b ^ b ^ b ^ … d times is b ⇈ d  
and so on…

this is the basic idea of hyperoperations. repeating the previous operation d times gives you the next operator. this gives us the tower: succ → add → mul → pow → spow → …

the hyperoperation tower starts from the successor function:

| n | b | a |
| - | - | - |
| 0 | [succ](#succ)(a) | [pred](#pred)(b) |

for each binary operation ⊙ involved in a ⊙ b = c, we have three possible functions: solve for c, solve for b, solve for a

| n | c | b | a |
| - | -:| -:| -:|
| 1 |  [add](#add)(a, b) |   [bus](#bus)(c, a) |  [sub](#sub)(c, b) |
| 2 |  [mul](#mul)(a, b) |   [vid](#vid)(c, a) |  [div](#div)(c, b) |
| 3 |  [pow](#pow)(a, b) |  [root](#root)(c, a) |  [log](#log)(c, b) |
| 4 | spow(a, b) | sroot(c, a) | slog(c, b) |
| … | … | … | … |

<!--
c = a + b  add 
b =-a + c bus 
a = c - r  sub 
c = a * b  mul (times)
l = c / r  div (over)
r = r \ c  vid (under)
c = a ^ b  pow
l = c ^ r⁻¹ root
r = log_l(c) log
-->

- since we define the functions as equation solvers, there is no need for inverse elements or identity elements

- it is by construction that an operator in this tower is a repetition of the previous operator, but in domains other than the real numbers, mul is not a repetition of add because they are defined axiomatically with abstract algebra. the tower is simply a nice organizational mnemonic for operators.

- succ(a) returns the cover of a. for succ to be a function, i.e., return only one answer, there should be only one possible answer. a poset can have multiple covers for an element but a toset will have one cover. thus, succ is defined only for tosets. furthermore, succ is degenerate for dense tosets like the rational numbers because elements there have no cover. you can always find another number between two numbers, so a number does not really have a successor. thus succ is only defined for discrete tosets. lastly, the definition of succ is not restricted to integers. though any other definitions would break the construction of the hyperoperation tower, this tower was never meant to be a construction. it is only a framework i make use of to organize functions in a nice way

- any binary operator that is commutative has its left and right inverses same. `add` and `mul` are commutative in many domains, which is why they seem to have only one inverse. but when multiplication is non-commutative like for matrices, it starts having two inverses. daamath anticipates this and thus maintains `vid` and `div` which solve for the left and right respectively. likewise for `bus` and `sub`.

- [tetration](https://en.wikipedia.org/wiki/Tetration), [super-root](https://en.wikipedia.org/wiki/Tetration#Super-root), [super-logarithm](https://en.wikipedia.org/wiki/Tetration#Super-logarithm) are highly debated topics, especially for non-integer numbers. there is no canonical agreed-upon definition for them yet so until this is resolved, daamath shall not maintain hyperoperations of n ≥ 4

# argument order

this works well for sub and div but there is confusion for log and root. in usual math notation, we write logₙ(x) and ⁿ√x. [julia](https://en.wikipedia.org/wiki/Julia_(programming_language)) follows the order of math notation and writes log(n, x). [python](https://en.wikipedia.org/wiki/Python_(programming_language)) and [C](https://en.wikipedia.org/wiki/C_(programming_language)) follow the reverse order log(x, n). daamath follows the orders log(x, n) & root(x, n) because they are consistent with the order of arguments in sub(x, n) & bus(x, n) and div(x, n) & vid(x, n)

# notes

succession and predecession are not the same as incrementation and decrementation. the former two give a new answer, while the latter two imply mutating a variable. if daamath were to implement n=0 hyperoperations, it would use the former two.

# type homomorphism

hyperoperations will return the same output type as its input type. if you pass in an integer, it will give an integer result. this is in contrast to dynamic type promotion in most languages, which eagerly promote integers to fractional numbers.

for example, in C, `pow(2, 3)` gives `8.0`. in python, `2 ** -2` gives `0.25`.   
with daamath, `dm.pow(2, 3)` will give `8`, and `dm.pow(2, -2)` will raise a DomainError because `0.25` cannot be represented as an integer.

the biggest consequence to this is that integer arithmetic stays as integer arithmetic. unsigned integer arithmetic stays as unsigned integer arithmetic.

daamath maintains four number types: [ℕ₀](https://en.wikipedia.org/wiki/Natural_number), [ℤ](https://en.wikipedia.org/wiki/Integer), [ℝ](https://en.wikipedia.org/wiki/Real_number), [ℂ](https://en.wikipedia.org/wiki/Complex_number)

# API implementation

## mul

multiplication. it is overloaded to support the following:

scalar × scalar = scalar
scalar × vector = vector
scalar × matrix = matrix
vector × scalar = vector
vector × vector = (ambiguous. use [inner]/[outer]/[cross]/[hadamard]/…)
vector × matrix = vector (assumes vector is a column vector)
matrix × scalar = matrix
matrix × vector = vector (assumes vector is a row vector)
matrix × matrix = matrix



### inner

### outer

##### [succ](https://en.wikipedia.org/wiki/Successor_function)(degree):
signature: 𝕎 → 𝕎 | ℤ → ℤ  
exceptions: (none)  
returns: 1 + degree  

##### [pred](https://en.wikipedia.org/wiki/Primitive_recursive_function#Predecessor)(result):
signature: 𝕎 → 𝕎 | ℤ → ℤ  
exceptions: if signature is 𝕎 → 𝕎 and result is 0, raise a DomainError  
returns: result − 1  

##### [add](https://en.wikipedia.org/wiki/Addition)(base, degree):
    signature: 𝕎, 𝕎 → 𝕎 | ℤ, ℤ → ℤ | ℝ, ℝ → ℝ | ℂ, ℂ → ℂ  
    exceptions: (none)  
    returns: base + degree  
##### [sub](https://en.wikipedia.org/wiki/Subtraction)(result, degree):
    signature: 𝕎, 𝕎 → 𝕎 | ℤ, ℤ → ℤ | ℝ, ℝ → ℝ | ℂ, ℂ → ℂ 
    returns: result − degree 
##### [mul](https://en.wikipedia.org/wiki/Multiplication)(base, degree):  
    signature: 𝕎, 𝕎 → 𝕎 | ℤ, ℤ → ℤ | ℝ, ℝ → ℝ | ℂ, ℂ → ℂ
    returns: base · degree
##### [div](https://en.wikipedia.org/wiki/Division_(mathematics))(result, degree):  
    signature: 𝕎, 𝕎 → 𝕎 | ℤ, ℤ → ℤ | ℝ, ℝ → ℝ | ℂ, ℂ → ℂ
    returns: result ∕ degree
##### [pow](https://en.wikipedia.org/wiki/Exponentiation)(base, degree):  
    signature: 𝕎, 𝕎 → 𝕎 | ℤ, ℤ → ℤ | ℝ, ℝ → ℝ | ℂ, ℂ → ℂ
    returns: base ^ degree
##### [root](https://en.wikipedia.org/wiki/Nth_root)(result, degree):  
    signature: 𝕎, 𝕎 → 𝕎 | ℤ, ℤ → ℤ | ℝ, ℝ → ℝ | ℂ, ℂ → ℂ
    returns: result ^ (1 / degree)
##### [log](https://en.wikipedia.org/wiki/Logarithm)(result, base):
    signature: 𝕎, 𝕎 → 𝕎 | ℤ, ℤ → ℤ | ℝ, ℝ → ℝ | ℂ, ℂ → ℂ 
    returns: log_base(result)

# rant

the motivation for this hyperoperation table was that i wanted to find a way to unify all the arithmetic operators i knew under one structure. i found the hyperoperation tower a year before i made daamath, and when i applied it, it was surprisingly reliable. it helped me order them, figure out the relationship between pow-log-root, and it also helped me figure out the argument order for log and root. turns out that i should just follow the order that sub and div follow, which is to always put result as first argument. 

