// TODO: finish writing exception for functions

notations:
𝕎 = {x:x ∈ ℤ, x ≥ 0}

argument binding convention
	certain functions have variants with pre-bound arguments. examples will show the convention better than words can:
	ln(a) = LN_A
	log(a, b) = log_a(b) = log__b(a) = LOG_A_B
	fma(a, b, c) = fma_a(b, c) = fma__b(a, c) = fma___c(a, b) = fma_a_b(c) = fma_a__c(b) = fma__b_c(a) = FMA_A_B_C
	
	this is very decodable but not very pleasant. the alias module provides alternative names to cumbersome bindings like log__2(a) → log2(a)

	due to this convention, function names with underscores in them signal pre-bound arguments. so round__true_even is accurate in that it binds the second and third arguments to 'directed' and 'even' (and is aliased to round_even) while floor_div(a, b) actually remains correct. the floor takes the result of div as argument, and the div takes (a, b) as argument.
	
hyperoperations
	// hXY where X is n-th level of hyperoperation tower, and Y is the variable to be solved in the equation a ? b = c
	h0c(b)
		alias
			succ
		signature
			𝕎 → 𝕎
			ℤ → ℤ
		explanation
			successor
			c = b + 1
			succession is only defined on integers (and subsets) because the successor of a real number in the real domain is ambiguous
	h0b(c)
		alias
			pred
		signature
			𝕎 → 𝕎
			ℤ → ℤ
		exception
			𝕎 → 𝕎
				// since result is -1, out of domain
				if c == 0 then raise DomainError
		explanation
			predecessor
			b = c - 1 
			predecession is only defined on integers (and subsets) because the predecessor of a real number in the real domain is ambiguous
	// (h0a is not possible)
	h1c(a, b)
		alias
			add
		signature
			𝕎, 𝕎 → 𝕎
			ℤ, ℤ → ℤ
			ℝ, ℝ → ℝ
			ℂ, ℂ → ℂ
		explanation
			c = a + b
	h1b(c, a)
		alias
			sub
		signature
			𝕎, 𝕎 → 𝕎
			ℤ, ℤ → ℤ
			ℝ, ℝ → ℝ
			ℂ, ℂ → ℂ
		exception
			𝕎, 𝕎 → 𝕎
				if c - a < 0 then raise DomainError 
		explanation
			b = c − a
	// (h1a is same as h1b)
	h2c(a, b)
		alias
			mul
		signature
			𝕎, 𝕎 → 𝕎
			ℤ, ℤ → ℤ
			ℝ, ℝ → ℝ
			ℂ, ℂ → ℂ
		explanation
			c = a * b
	h2b(c, a)
		alias
			div
		signature
			𝕎, 𝕎 → 𝕎
			ℤ, ℤ → ℤ
			ℝ, ℝ → ℝ
			ℂ, ℂ → ℂ
		exception
			𝕎, 𝕎 → 𝕎
				// if quotient will not be a whole number
				if c % a ≠ 0 then raise DomainError
			ℤ, ℤ → ℤ
				// if quotient will not be a whole number
				if c % a ≠ 0 then raise DomainError
		explanation
			b = c / a
	// (h2a is same as h2b)
	h3c(a, b)
		alias
			pow
		signature
			𝕎, 𝕎 → 𝕎
			ℤ, ℤ → ℤ
			ℝ, ℝ → ℝ
			ℂ, ℂ → ℂ
		explanation
			c = a ^ b
	h3b(c, a)
		alias
			log
		signature
			𝕎, 𝕎 → 𝕎
			ℤ, ℤ → ℤ
			ℝ, ℝ → ℝ
			ℂ, ℂ → ℂ
		explanation
			b = log_a(c) = ln(c) / ln(a)
	h3a(c, b)
		alias
			root
		signature
			𝕎, 𝕎 → 𝕎
			ℤ, ℤ → ℤ
			ℝ, ℝ → ℝ
			ℂ, ℂ → ℂ
		explanation
			a = ᵇ√c = c ^ (1 / b)
	/*
	h4c(a, b)
		alias
			spow
		signature
			𝕎, 𝕎 → 𝕎
			ℤ, ℤ → ℤ
			ℝ, ℝ → ℝ
			ℂ, ℂ → ℂ
		explanation
			super-power
			super-exponentiation
			tetration
	h4b(c, a)
		alias
			slog
		signature
			𝕎, 𝕎 → 𝕎
			ℤ, ℤ → ℤ
			ℝ, ℝ → ℝ
			ℂ, ℂ → ℂ
		explanation
			super-logarithm
	h4a(c, b)
		alias
			sroot
		signature
			𝕎, 𝕎 → 𝕎
			ℤ, ℤ → ℤ
			ℝ, ℝ → ℝ
			ℂ, ℂ → ℂ
		explanation
			super-root
	*/
hyperoperations extra (hyperoperations with pre-bound arguments):
	h1b_0(a)
		alias
			ainv
		signature
			ℤ → ℤ
			ℝ → ℝ
			ℂ → ℂ	
		explanation
			additive inverse
	h2b_1(a)
		alias
			minv
		signature
			𝕎 → 𝕎
			ℤ → ℤ
			ℝ → ℝ
			ℂ → ℂ	
		exception
			𝕎 → 𝕎
				raise DomainError if a ≠ 1
			ℤ → ℤ
				raise DomainError if |a| ≠ 1
		explanation
			multiplicative inverse
	h3c_e(b)
		alias
			exp
		explanation
			e ^ b
	h3b__e(c)
		alias
			ln
		explanation
			logarithmus naturalis
	h3c_2(b)
		alias
			exp2
		explanation
			2 ^ something
	h3b__2(c)
		alias
			log2
		explanation
			do i even need to explain this???
	h3c_10(b)
		alias
			exp10
		explanation
			its the same thing as the last thing but with 2
	h3b__10(c)
		alias
			log10
		explanation
			waste of time...
	h3c__2(c)
		alias
			square
		explanation
			c²
	h3c__3(c)
		alias
			cube
		explanation
			c³
	h3a__2(c)
		alias
			sqrt
		explanation
			square root
			√c
	h3a__3(c)
		alias
			cbrt
		explanation
			cube root
			∛c

trigonometry
	/* GQND where
	 * Q is quantity to solve for {(s)emiarea, (r)atio}
	 * G is geometry {(c)ircular, (h)yperbolic}
	 * N is numerator {(o)pposite, (a)djacent, (h)ypotenuse}
	 * D is denominator {(o)pposite, (a)djacent, (h)ypotenuse}
	 * this gives us 2 * 2 * 3P2 = 24 functions
	 */
	croh(semiarea)
		alias
			sin
		signature
			𝕎 → 𝕎
			ℤ → ℤ
			ℝ → ℝ
			ℂ → ℂ
		exception
			𝕎 → 𝕎
				raise DomainError if semiarea ≠ 0
			ℤ → ℤ
				raise DomainError if semiarea ≠ 0
		explanation
			circular sine
			opposite / hypotenuse
	crah(semiarea)
		alias
			cos
		signature
			𝕎 → 𝕎
			ℤ → ℤ
			ℝ → ℝ
			ℂ → ℂ
		exception
			𝕎 → 𝕎
				raise DomainError if semiarea ≠ 0
			ℤ → ℤ
				raise DomainError if semiarea ≠ 0
		explanation
			circular cosine
			adjacent / hypotenuse
	croa(semiarea)
		alias
			tan
		signature
			𝕎 → 𝕎
			ℤ → ℤ
			ℝ → ℝ
			ℂ → ℂ
		exception
			𝕎 → 𝕎
				raise DomainError if semiarea ≠ 0
			ℤ → ℤ
				raise DomainError if semiarea ≠ 0
		explanation
			circular tangent
			opposite / adjacent
	crao(semiarea)
		alias
			cot
		signature
			ℝ → ℝ
			ℂ → ℂ
		explanation
			circular cotangent
			adjacent / opposite
	crha(semiarea)
		alias
			sec
		signature
			𝕎 → 𝕎
			ℤ → ℤ
			ℝ → ℝ
			ℂ → ℂ
		exception
			𝕎 → 𝕎
				raise DomainError if semiarea ≠ 1
			ℤ → ℤ
				raise DomainError if semiarea ≠ 1
		explanation
			circular secant
			hypotenuse / adjacent
	crho(semiarea)
		alias
			csc
		signature
			ℝ → ℝ
			ℂ → ℂ
		explanation
			circular cosecant
			hypotenuse / opposite
	croh(ratio)
		alias
			asin
		signature


/*
asin2(opp, hyp) where sign(hyp) = sign(adj)
acos2(adj, hyp) where sign(hyp) = sign(opp)
atan2(opp, adj)
acot2(adj, opp)
asec2(hyp, adj) where sign(hyp) = sign(opp)
acsc2(hyp, opp) where sign(hyp) = sign(adj)
*/

edge case handling
	daamath will not worry about integer overflow or floating point OOB errors because these are computational details, and are not a mathematical detail. it is up to the computer to do these accurately.

daamath will never perform mutation of any variables. for example, succ is b + 1, not ++b.
