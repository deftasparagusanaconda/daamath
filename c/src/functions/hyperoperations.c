/*
1. we must not have add_i(), add_f(), add_d(), add_cd(). we must have add(), which will dispatch the correct function
2. add(a, b) must never allow implicit type casting anywhere. add(2, 3.0) is strictly forbidden. there is absolutely no implicit type casting done anywhere

---------------

if i define a canonical data type for each number type, then the number type is restricted to that only. user wont be able to add two real floats. only two real doubles. this is bad..
if i define a canonical number type for each data type, then the operator knows that float is real, double is real, etc etc. this relation fits better. because many data types <-> one number type, but not many number type <-> one data type. 
so instead of defining add_integer, add_real, add_complex, i should have add_int, add_float, add_double, add_complex_float, … 

do not have typedefs like:

#define integer int
#define real double

do NOT do this!!! you will want to expand later. just make the operators for int, double, and double complex for now. oh and bool of course. but just do that for now!!! and later youll expand to more datatypes

----------------

operators are fully closed in these domains:
inc : NZRC
dec :  ZRC
add : NZRC
sub :  ZRC
mul : NZRC
div :   RC
pow : N  C
root:    C
log :    C

unsigned int is N
int          is Z
double       is R
complex      is C

later, we shall support float, uint* types, int*, float*, complex* etc etc. but lets keep these four for now, just to get a feel for the domains first
*/

#include "hyperoperations.h"
#include <errno.h>	// for error codes like EDOM
#include <math.h>


// incrementation. closed on N, Z, R, C
unsigned int _dm_inc_unsigned_int(unsigned int b)
{
	return ++b;
}
int _dm_inc_int (int b) 
{	
	return ++b;
}
double _dm_inc_double(double b)
{	
	return b + 1;
}
double complex _dm_inc_double_complex(double complex b) 
{	
	return b + 1;
}

// decrementation. closed on ℤ, ℝ, ℂ but not on ℕ
unsigned int _dm_dec_unsigned_int(unsigned int c) 
{	
	// since -1 doesnt exist for natural numbers ℕ
	if (c == 0)
		errno = EDOM;

	return --c;
}
int _dm_dec_int(int c)
{
	return --c;
}
double _dm_dec_double(double c)
{	
	return c - 1;
}
double complex _dm_dec_double_complex(double complex c)
{	
	return c - 1;
}

// addition. closed on N, Z, R, C
unsigned int _dm_add_unsigned_int(unsigned int a, unsigned int b)
{	
	return a + b;
}
int _dm_add_int(int a, int b)
{	
	return a + b;
}
double _dm_add_double(double a, double b) 
{	
	return a + b;
}
double complex _dm_add_double_complex(double complex a, double complex b)
{	
	return a + b;
}

// subtraction. closed on Z, R, C but not on N
unsigned int   _dm_sub_unsigned_int  (unsigned int   c, unsigned int   a)
{	
	// since c - a cannot be < 0
	if (c < a)
		errno = EDOM;
	
	return c - a;
}
int            _dm_sub_int           (int            c, int            a) {return c - a            ;}
double         _dm_sub_double        (double         c, double         a) {return c - a            ;}
double complex _sub_double_complex(double complex c, double complex a) {return c - a            ;}

// multiplication. closed on N, Z, R, C
unsigned int   _dm_mul_unsigned_int  (unsigned int   a, unsigned int   b) {return a * b            ;}
int            _dm_mul_int           (int            a, int            b) {return a * b            ;}
double         _dm_mul_double        (double         a, double         b) {return a * b            ;}
double complex _dm_mul_double_complex(double complex a, double complex b) {return a * b            ;}

// division. closed on R, C only
unsigned int _dm_div_unsigned_int(unsigned int c, unsigned int a)
{	
	if (c % a != 0)
		errno = EDOM;

	return c / a;
}
int _dm_div_int (int c, int a)
{	
	if (c % a != 0)
		errno = EDOM;

	return c / a;
}
double _dm_div_double(double c, double a)
{	
	return c / a;
}
double complex _dm_div_double_complex(double complex c, double complex a)
{	
	return c / a;
}

// exponentiation. closed on N, C only
unsigned int _dm_pow_unsigned_int(unsigned int a, unsigned int b)
{
	unsigned int result = 1;
	
	while (b > 0)
	{	
		if (b & 1)	// if current bit of exponent is 1
			result *= a;	// multiply result by a

		a *= a;	// square the base
		b >>= 1;	// shift exponent right by 1 (divide by 2)
	}
	
	return result;
}
int _dm_pow_int(int a, int b)
{
	/*              b
	 *   -27 -8 -1  0  1  8 27 
	 *     9  4  1  0  1  4  9
	 *    -3 -2 -1  0  1  2  3   
	 * -a  1  1  1  ?  1  1  1  a
	 *     X  X -1  0  1  X  X
	 *     X  X  1  0  1  X  X
	 *     X  X -1  0  1  X  X
	 *             -b
	 */
	
	if ((b < 0) && ((a == -1) || (a == 1)))
		errno = EDOM;

	if ((a == 0) && (b == 0))
		errno = EDOM;
	
	return pow(a, b);
}
int dm_dm_pow_i(int a, int b)
{
    if (a == 0 && b == 0) { errno = EDOM; return 0; }
    if (a == 0)           { return 0; }
    if (b < 0)            { errno = EDOM; return 0; } // not closed on ℤ unless |a|==1
    
    int result = 1;
    while (b > 0)
    {
        if (b % 2 == 1)
            result *= a;
        a *= a;
        b /= 2;
    }
    return result;
}
double _dm_pow_double(double a, double b)
{
	return pow(a, b);
}
double complex _dm_pow_double_complex(double complex a, double complex b)
{	
	return cpow(a, b);
}

// logarithm. closed on C only
double complex _dm_log_double_complex(double complex a, double complex c) {return clog(c) / clog(a);}

// root. closed on C only
double _dm_root_double(double b, double c)
{	
	return cpow(c, 1.0 / b) ;
}
double complex _dm_root_double_complex(double complex b, double complex c) {return cpow(c, 1.0 / b) ;}

/*
* daamath supports everything up to complex numbers because complex numbers are algebraically closed. that is very nice
* but the tradeoff is that complex algebra often has branches (multiple outputs for one input) and we want functions to give only one output. so the tradeoff that daamath makes is that it picks conventional principal branches

* in fact, i want to support all geometric algebras by making an algebra generator like ganja.js :( .....
* but i dont have the mathematical expertise yet. one day... GA generator + hyperoperation generator. it would be amazing.. plus, we have a string library too! and constants. etc etc. i love this library
*/
