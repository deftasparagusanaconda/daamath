# datatypes

in $\text{mathematics}$, we work with various [sets](https://en.wikipedia.org/wiki/Set_(mathematics)), and their [elements](https://en.wikipedia.org/wiki/Element_of_a_set) and [operations](https://en.wikipedia.org/wiki/Operation_(mathematics)). for example, when we write $0.1 + 0.2$, we are working with the set of real numbers, and doing the operation $+$ on its elements $0.1$ and $0.2$

in `programming`, we work with various [datatypes](https://en.wikipedia.org/wiki/Data_type), and their [instances](https://en.wikipedia.org/wiki/Instance_(computer_science)) and [functions](https://en.wikipedia.org/wiki/Function_(computer_programming)). for example, when we write `0.1 + 0.2` in python, we are working the `float` datatype, and doing the operation `op.add` on its instances `0.1` and `0.2`

there are a few differences that we must resolve before we can do math with datatypes:

| sets/elements in math | datatypes/instances in CS | solution |
| - | - | - |
| numbers of same semantic value in different sets are same | instances of same semantic value in different datatypes are different | let datatypes participate in the number tower hierarchy by *explicit* and *exact* conversion |
| number sets follow a subset hierarchy | datatypes are just types values | datatypes shall participate in the number tower |

# finite numeric datatypes

note: $[a:b)$ is python-slice-like integer interval notation for $\{x \mid x \in \mathbb Z, a \le x < b\}$ or more tersely, $\mathbb Z \cap [a, b)$

| name | model | actual |
| - | - | - | 
| [`uint8`](uint) | [$\mathbb N$](https://en.wikipedia.org/wiki/Natural_number "naturals") | $[0:2^{8})$ | 
| [`uint16`](uint) | [$\mathbb N$](https://en.wikipedia.org/wiki/Natural_number "naturals") | $[0:2^{16})$ | 
| [`uint32`](uint) | [$\mathbb N$](https://en.wikipedia.org/wiki/Natural_number "naturals") | $[0:2^{32})$ | 
| [`uint64`](uint) | [$\mathbb N$](https://en.wikipedia.org/wiki/Natural_number "naturals") | $[0:2^{64})$ | 
| [`int8`](int) | [$\mathbb Z$](https://en.wikipedia.org/wiki/Integer "integers") | $[-2^{8-1} : +2^{8-1})$ |
| [`int16`](int) | [$\mathbb Z$](https://en.wikipedia.org/wiki/Integer "integers") | $[-2^{16-1} : +2^{16-1})$ | 
| [`int32`](int) | [$\mathbb Z$](https://en.wikipedia.org/wiki/Integer "integers") | $[-2^{32-1} : +2^{32-1})$ | 
| [`int64`](int) | [$\mathbb Z$](https://en.wikipedia.org/wiki/Integer "integers") | $[-2^{64-1} : +2^{64-1})$ | 
| [`binary32`](binary) | [$\mathbb R$](https://en.wikipedia.org/wiki/Real_numbers) | $\left\{\begin{aligned}&{\pm}\tfrac{n}{2^{23}}2^e, \href{https://en.wikipedia.org/wiki/IEEE_754#Signed_zero}{ {\pm}0},\\&\href{https://en.wikipedia.org/wiki/IEEE_754#Subnormal_numbers}{ {\pm}\tfrac{s}{2^{23}}2^{1-127}},\\&\href{https://en.wikipedia.org/wiki/IEEE_754#Infinities}{ {\pm}\infty}, \href{https://en.wikipedia.org/wiki/IEEE_754#NaNs}{ {\pm}\mathtt{NaN}_s}\\\end{aligned}\;\middle\vert\;\begin{aligned}n &\in [2^{23}:2^{23+1})\\s &\in (0:2^{23})\\e &\in (\mathord{-}127:\mathord{+}127]\\\end{aligned}\right\}$ |
| [`binary64`](binary) | [$\mathbb R$](https://en.wikipedia.org/wiki/Real_numbers) | $\left\{\begin{aligned}&{\pm}\tfrac{n}{2^{52}}2^e, \href{https://en.wikipedia.org/wiki/IEEE_754#Signed_zero}{ {\pm}0},\\&\href{https://en.wikipedia.org/wiki/IEEE_754#Subnormal_numbers}{ {\pm}\tfrac{s}{2^{52}}2^{1-1023}},\\&\href{https://en.wikipedia.org/wiki/IEEE_754#Infinities}{ {\pm}\infty}, \href{https://en.wikipedia.org/wiki/IEEE_754#NaNs}{ {\pm}\mathtt{NaN}_s}\\\end{aligned}\;\middle\vert\;\begin{aligned}n &\in [2^{52}:2^{52+1})\\s &\in (0:2^{52})\\e &\in (\mathord{-}1023:\mathord{+}1023]\\\end{aligned}\right\}$ |
| [`binary128`](binary) | [$\mathbb R$](https://en.wikipedia.org/wiki/Real_numbers) | $\left\{\begin{aligned}&{\pm}\tfrac{n}{2^{112}}2^e, \href{https://en.wikipedia.org/wiki/IEEE_754#Signed_zero}{ {\pm}0},\\&\href{https://en.wikipedia.org/wiki/IEEE_754#Subnormal_numbers}{ {\pm}\tfrac{s}{2^{112}}2^{1-16383}},\\&\href{https://en.wikipedia.org/wiki/IEEE_754#Infinities}{ {\pm}\infty}, \href{https://en.wikipedia.org/wiki/IEEE_754#NaNs}{ {\pm}\mathtt{NaN}_s}\\\end{aligned}\;\middle\vert\;\begin{aligned}n &\in [2^{112}:2^{112+1})\\s &\in (0:2^{112})\\e &\in (\mathord{-}16383:\mathord{+}16383]\\\end{aligned}\right\}$ | 
| [`decimal64`](decimal) | [$\mathbb R$](https://en.wikipedia.org/wiki/Real_numbers) | (im still researching okay) |
| [`decimal128`](decimal) | [$\mathbb R$](https://en.wikipedia.org/wiki/Real_numbers) | (im still researching okay) |
| [`complex64`](complex) | [$ℂ$](https://en.wikipedia.org/wiki/Complex_numbers) | $\{a + b\mathrm i \mid a, b \in$ [`binary32`](binary)$\}$ |
| [`complex128`](complex) | [$ℂ$](https://en.wikipedia.org/wiki/Complex_numbers) | $\{a + b\mathrm i \mid a, b \in$ [`binary64`](binary)$\}$ |
| [`complex256`](complex) | [$ℂ$](https://en.wikipedia.org/wiki/Complex_numbers) | $\{a + b\mathrm i \mid a, b \in$ [`binary128`](binary)$\}$ |

<!--
$\left\{
\begin{aligned}
&{\pm}\tfrac{n}{2^{23}}2^e, \href{https://en.wikipedia.org/wiki/IEEE_754#Signed_zero}{ {\pm}0},\\
&\href{https://en.wikipedia.org/wiki/IEEE_754#Subnormal_numbers}{ {\pm}\tfrac{s}{2^{23}}2^{1-127}},\\
&\href{https://en.wikipedia.org/wiki/IEEE_754#Infinities}{ {\pm}\infty}, \href{https://en.wikipedia.org/wiki/IEEE_754#NaNs}{ {\pm}\mathtt{NaN}_s}\\
\end{aligned}
\;\middle\vert\;
\begin{aligned}
n &\in [2^{23}:2^{23+1})\\
s &\in (0:2^{23})\\
e &\in (\mathord{-}127:\mathord{+}127]\\
\end{aligned}
\right\}$
-->

# infinite numeric datatypes

| name | model | actual | 
| - | - | - |
| [`natural`](natural) | [$ℕ$](https://en.wikipedia.org/wiki/Natural_number "naturals") | [$ℕ$](https://en.wikipedia.org/wiki/Natural_number "naturals") | 
| [`integer`](integer) | [$ℤ$](https://en.wikipedia.org/wiki/Integer "integers") | [$ℤ$](https://en.wikipedia.org/wiki/Integer "integers") | 
| [`rational`](rational) | [$ℚ$](https://en.wikipedia.org/wiki/Rational_number "rationals") | [$\mathbb Q$](https://en.wikipedia.org/wiki/Rational_number "rationals") | 
| [`gaussian`](gaussian) | [$ℚ[\mathrm i]$](https://en.wikipedia.org/wiki/Gaussian_rationals "gaussian rationals") | [$ℚ[\mathrm i]$](https://en.wikipedia.org/wiki/Gaussian_rationals "gaussian rationals") | 

# non-numeric datatypes

| name | model | 
| - | - |
| [`bool`](bool) | [$𝔹$](https://en.wikipedia.org/wiki/Boolean_algebra_(structure) "booleans") 
