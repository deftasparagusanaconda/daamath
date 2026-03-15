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

daamath shall only define operators on number types where they achieve closure

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
float        is R
double       is R
complex      is C
*/

// incrementation. closed on N, Z, R, C
unsigned int   h0c_unsigned_int  (                  unsigned int   b) {return ++b              ;}
int            h0c_int           (                  int            b) {return ++b              ;}
double         h0c_double        (                  double         b) {return b + 1            ;}
double complex h0c_double_complex(                  double complex b) {return b + 1            ;}

// decrementation. closed on Z, R, C but not on N
int            h0b_int           (int            c                  ) {return --c              ;}
double         h0b_double        (double         c                  ) {return c - 1            ;}
double complex h0b_double_complex(double complex c                  ) {return c - 1            ;}

// h0a doesnt exist mathematically

// addition. closed on N, Z, R, C
unsigned int   h1c_unsigned_int  (unsigned int   a, unsigned int   b) {return a + b            ;}
int            h1c_int           (int            a, int            b) {return a + b            ;}
double         h1c_double        (double         a, double         b) {return a + b            ;}
double complex h1c_double_complex(double complex a, double complex b) {return a + b            ;}

// subtraction. closed on Z, R, C but not on N
int            h1b_int           (int            c, int            a) {return c - a            ;}
double         h1b_double        (double         c, double         a) {return c - a            ;}
double complex h1b_double_complex(double complex c, double complex a) {return c - a            ;}

// subtraction. closed on Z, R, C but not on N
int            h1a_int           (int            c, int            b) {return c - b            ;}
double         h1a_double        (double         c, double         b) {return c - b            ;}
double complex h1a_double_complex(double complex c, double complex b) {return c - b            ;}

// multiplication. closed on N, Z, R, C
unsigned int   h2c_unsigned_int  (unsigned int   a, unsigned int   b) {return a * b            ;}
int            h2c_int           (int            a, int            b) {return a * b            ;}
double         h2c_double        (double         a, double         b) {return a * b            ;}
double complex h2c_double_complex(double complex a, double complex b) {return a * b            ;}
#define mul h2c

// division. closed on R, C only
double         h2b_double        (double         c, double         a) {return c / a            ;}
double complex h2b_double_complex(double complex c, double complex a) {return c / a            ;}
#define div h2b

// division. closed on R, C only
double         h2a_double        (double         c, double         b) {return c / b            ;}
double complex h2a_double_complex(double complex c, double complex b) {return c / b            ;}
//#define div h2a

// exponentiation. closed on N, C only
unsigned int   h3c_unsigned_int  (unsigned int   a, unsigned int   b)
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
double complex h3c_double_complex(double complex a, double complex b) {return cpow(a, b)       ;}
#define pow h3c

// logarithm. closed on C only
double complex h3b_double_complex(double complex c, double complex a) {return clog(c) / clog(a);}
#define log h3b

// root. closed on C only
double complex h3a_double_complex(double complex c, double complex b) {return cpow(c, 1.0 / b) ;}
#define root h3a

/*
* daamath supports everything up to complex numbers because complex numbers are algebraically closed. that is very nice
* but the tradeoff is that complex algebra often has branches (multiple outputs for one input) and we want functions to give only one output. so the tradeoff that daamath makes is that it picks conventional principal branches

* in fact, i want to support all geometric algebras by making an algebra generator like ganja.js :( .....
* but i dont have the mathematical expertise yet. one day... GA generator + hyperoperation generator. it would be amazing.. plus, we have a string library too! and constants. etc etc. i love this library
*/
