#define add(a, b) \
_Generic((a), \
    double: _Generic((b), \
        double: add_double, \
        default: add_type_mismatch \
    ), \
    double complex: _Generic((b), \
        double complex: add_double_complex, \
        default: add_type_mismatch \
    ), \
    default: add_type_mismatch \
)(a, b)

#include <complex.h>

// incrementation ++b = c
unsigned int   _inc_unsigned_int    (                  unsigned int   b); 
int            _inc_int             (                  int            b);
double         _inc_double          (                  double         b);
double complex _inc_double_complex  (                  double complex b);

// decrementation --c = b
unsigned int   _dec_unsigned_int    (unsigned int   c                  ); 
int            _dec_int             (int            c                  ); 
double         _dec_double          (double         c                  ); 
double complex _dec_double_complex  (double complex c                  ); 

// addition a + b = c
unsigned int   _add_unsigned_int    (unsigned int   a, unsigned int   b);
int            _add_int             (int            a, int            b);
double         _add_double          (double         a, double         b);
double complex _add_double_complex  (double complex a, double complex b);

// subtraction c - a = b
unsigned int   _sub_unsigned_int    (unsigned int   c, unsigned int   a);
int            _sub_int             (int            c, int            a);
double         _sub_double          (double         c, double         a); 
double complex _sub_double_complex  (double complex c, double complex a);

// multiplication a * b = c
unsigned int   _mul_unsigned_int    (unsigned int   a, unsigned int   b);
int            _mul_int             (int            a, int            b);
double         _mul_double          (double         a, double         b);
double complex _mul_double_complex  (double complex a, double complex b);

// division c / a = b
unsigned int   _div_unsigned_int    (unsigned int   c, unsigned int   a);
int            _div_int             (int            c, int            a);
double         _div_double          (double         c, double         a);
double complex _div_double_complex  (double complex c, double complex a);

// exponentiation a ^ b = c
unsigned int   _pow_unsigned_int    (unsigned int   a, unsigned int   b);
int            _pow_int             (int            a, int            b);
float          _pow_float           (float          a, float          b);
double complex _pow_double_complex  (double complex a, double complex b);

// logarithm log_a(c) = b
unsigned int   _log_unsigned_int    (unsigned int   a, unsigned int   c);
int            _log_int             (int            a, int            c);
double         _log_double          (double         a, double         c);
double complex _log_double_complex  (double complex a, double complex c);

// root a √ c = b
unsigned int   _root_unsigned_int   (unsigned int   a, unsigned int   c);
int            _root_int            (int            a, int            c);
double         _root_double         (double         a, double         c);
double complex _root_double_complex (double complex a, double complex c);

// superexponentiation
unsigned int   _spow_unsigned_int   (unsigned int   a, unsigned int   b);
int            _spow_int            (int            a, int            b);
float          _spow_float          (float          a, float          b);
double complex _spow_double_complex (double complex a, double complex b);

// superlogarithm log_a(c) = b
unsigned int   _slog_unsigned_int   (unsigned int   a, unsigned int   c);
int            _slog_int            (int            a, int            c);
double         _slog_double         (double         a, double         c);
double complex _slog_double_complex (double complex a, double complex c);

// superroot a √ c = b
unsigned int   _sroot_unsigned_int  (unsigned int   a, unsigned int   c);
int            _sroot_int           (int            a, int            c);
double         _sroot_double        (double         a, double         c);
double complex _sroot_double_complex(double complex a, double complex c);





/*
* daamath supports everything up to complex numbers because complex numbers are algebraically closed. that is very nice
* but the tradeoff is that complex algebra often has branches (multiple outputs for one input) and we want functions to give only one output. so the tradeoff that daamath makes is that it picks conventional principal branches

* in fact, i want to support all geometric algebras by making an algebra generator like ganja.js :( .....
* but i dont have the mathematical expertise yet. one day... GA generator + hyperoperation generator. it would be amazing.. plus, we have a string library too! and constants. etc etc. i love this library
*/
