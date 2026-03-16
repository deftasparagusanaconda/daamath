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

#include <errno.h>	// for error codes like EDOM

// incrementation. closed on N, Z, R, C
unsigned int   inc_unsigned_int  (                  unsigned int   b) {return ++b              ;}
int            inc_int           (                  int            b) {return ++b              ;}
double         inc_double        (                  double         b) {return b + 1            ;}
double complex inc_double_complex(                  double complex b) {return b + 1            ;}

// decrementation. closed on Z, R, C but not on N
unsigned int dec_unsigned_int(unsigned int c) 
{	
	if (c == 0)
		errno = EDOM;
	return --c;
}
int            dec_int           (int            c                  ) {return --c              ;}
double         dec_double        (double         c                  ) {return c - 1            ;}
double complex dec_double_complex(double complex c                  ) {return c - 1            ;}

// addition. closed on N, Z, R, C
unsigned int   add_unsigned_int  (unsigned int   a, unsigned int   b) {return a + b            ;}
int            add_int           (int            a, int            b) {return a + b            ;}
double         add_double        (double         a, double         b) {return a + b            ;}
double complex add_double_complex(double complex a, double complex b) {return a + b            ;}

// subtraction. closed on Z, R, C but not on N
int            sub_int           (int            c, int            a) {return c - a            ;}
double         sub_double        (double         c, double         a) {return c - a            ;}
double complex sub_double_complex(double complex c, double complex a) {return c - a            ;}

// multiplication. closed on N, Z, R, C
unsigned int   mul_unsigned_int  (unsigned int   a, unsigned int   b) {return a * b            ;}
int            mul_int           (int            a, int            b) {return a * b            ;}
double         mul_double        (double         a, double         b) {return a * b            ;}
double complex mul_double_complex(double complex a, double complex b) {return a * b            ;}

// division. closed on R, C only
double         div_double        (double         c, double         a) {return c / a            ;}
double complex div_double_complex(double complex c, double complex a) {return c / a            ;}

// exponentiation. closed on N, C only
unsigned int   pow_unsigned_int  (unsigned int   a, unsigned int   b)
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
double complex pow_double_complex(double complex a, double complex b) {return cpow(a, b)       ;}

// logarithm. closed on C only
double complex log_double_complex(double complex c, double complex a) {return clog(c) / clog(a);}

// root. closed on C only
double complex root_double_complex(double complex c, double complex b) {return cpow(c, 1.0 / b) ;}

/*
* daamath supports everything up to complex numbers because complex numbers are algebraically closed. that is very nice
* but the tradeoff is that complex algebra often has branches (multiple outputs for one input) and we want functions to give only one output. so the tradeoff that daamath makes is that it picks conventional principal branches

* in fact, i want to support all geometric algebras by making an algebra generator like ganja.js :( .....
* but i dont have the mathematical expertise yet. one day... GA generator + hyperoperation generator. it would be amazing.. plus, we have a string library too! and constants. etc etc. i love this library
*/
