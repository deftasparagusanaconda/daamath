#include <complex.h>

#define _dm_same_type(a, b) _Generic((a), \
    unsigned int:   _Generic((b), unsigned int:   1, default: 0), \
    int:            _Generic((b), int:            1, default: 0), \
    double:         _Generic((b), double:         1, default: 0), \
    double complex: _Generic((b), double complex: 1, default: 0), \
    default: 0 \
)
/*
#define _dm_check_types(a, b, fname) _Static_assert( \
    _dm_same_type(a, b), \
    fname ": arguments must be of same type" \
)
*/
/*
#define _dm_check_types(a, b, fname) _Generic((a), \
    unsigned int:   _Static_assert(_Generic((b), unsigned int:   1, default: 0), \
        fname ": 'a' is uint — 'b' must also be uint"), \
    int:            _Static_assert(_Generic((b), int:            1, default: 0), \
        fname ": 'a' is int — 'b' must also be int"), \
    double:         _Static_assert(_Generic((b), double:         1, default: 0), \
        fname ": 'a' is double — 'b' must also be double"), \
    double complex: _Static_assert(_Generic((b), double complex: 1, default: 0), \
        fname ": 'a' is double complex — 'b' must also be double complex"), \
    default:        _Static_assert(0, \
        fname ": 'a' is an unsupported type") \
)
*/
/*
// produces an int expression (always 0), but triggers static assert if cond is false
#define _dm_sassert(cond, msg) (sizeof(struct{ _Static_assert(cond, msg); int _; }) * 0)

#define _dm_check_types(a, b, fname) \
  _Generic((a), \
    unsigned int:   _dm_sassert(_Generic((b), unsigned int:   1, default: 0), \
                      fname ": 'a' is uint — 'b' must also be uint"), \
    int:            _dm_sassert(_Generic((b), int:            1, default: 0), \
                      fname ": 'a' is int — 'b' must also be int"), \
    double:         _dm_sassert(_Generic((b), double:         1, default: 0), \
                      fname ": 'a' is double — 'b' must also be double"), \
    double complex: _dm_sassert(_Generic((b), double complex: 1, default: 0), \
                      fname ": 'a' is double complex — 'b' must also be double complex"), \
    default:        _dm_sassert(0, fname ": 'a' is an unsupported type") \
  )
*/

// successor b + 1 = c
unsigned int   _dm_succ_unsigned_int   (                  unsigned int   b); 
int            _dm_succ_int            (                  int            b);
double         _dm_succ_double         (                  double         b);
double complex _dm_succ_double_complex (                  double complex b);

// predecessor c - 1 = b
unsigned int   _dm_pred_unsigned_int   (unsigned int   c                  ); 
int            _dm_pred_int            (int            c                  ); 
double         _dm_pred_double         (double         c                  ); 
double complex _dm_pred_double_complex (double complex c                  ); 

// addition a + b = c
unsigned int   _dm_add_unsigned_int    (unsigned int   a, unsigned int   b);
int            _dm_add_int             (int            a, int            b);
double         _dm_add_double          (double         a, double         b);
double complex _dm_add_double_complex  (double complex a, double complex b);

// subtraction c - a = b
unsigned int   _dm_sub_unsigned_int    (unsigned int   c, unsigned int   a);
int            _dm_sub_int             (int            c, int            a);
double         _dm_sub_double          (double         c, double         a); 
double complex _dm_sub_double_complex  (double complex c, double complex a);

// multiplication a * b = c
unsigned int   _dm_mul_unsigned_int    (unsigned int   a, unsigned int   b);
int            _dm_mul_int             (int            a, int            b);
double         _dm_mul_double          (double         a, double         b);
double complex _dm_mul_double_complex  (double complex a, double complex b);

// division c / a = b
unsigned int   _dm_div_unsigned_int    (unsigned int   c, unsigned int   a);
int            _dm_div_int             (int            c, int            a);
double         _dm_div_double          (double         c, double         a);
double complex _dm_div_double_complex  (double complex c, double complex a);

// exponentiation a ^ b = c
unsigned int   _dm_pow_unsigned_int    (unsigned int   a, unsigned int   b);
int            _dm_pow_int             (int            a, int            b);
double         _dm_pow_double          (double         a, double         b);
double complex _dm_pow_double_complex  (double complex a, double complex b);

// logarithm log_a(c) = b
unsigned int   _dm_log_unsigned_int    (unsigned int   a, unsigned int   c);
int            _dm_log_int             (int            a, int            c);
double         _dm_log_double          (double         a, double         c);
double complex _dm_log_double_complex  (double complex a, double complex c);

// root a √ c = b
unsigned int   _dm_root_unsigned_int   (unsigned int   a, unsigned int   c);
int            _dm_root_int            (int            a, int            c);
double         _dm_root_double         (double         a, double         c);
double complex _dm_root_double_complex (double complex a, double complex c);

// superexponentiation
unsigned int   _dm_spow_unsigned_int   (unsigned int   a, unsigned int   b);
int            _dm_spow_int            (int            a, int            b);
double         _dm_spow_double         (double         a, double         b);
double complex _dm_spow_double_complex (double complex a, double complex b);
// superlogarithm log_a(c) = b
unsigned int   _dm_slog_unsigned_int   (unsigned int   a, unsigned int   c);
int            _dm_slog_int            (int            a, int            c);
double         _dm_slog_double         (double         a, double         c);
double complex _dm_slog_double_complex (double complex a, double complex c);
// superroot a √ c = b
unsigned int   _dm_sroot_unsigned_int  (unsigned int   a, unsigned int   c);
int            _dm_sroot_int           (int            a, int            c);
double         _dm_sroot_double        (double         a, double         c);
double complex _dm_sroot_double_complex(double complex a, double complex c);

#define succ(b) 
#define pred(c) 

#define dm_add(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_add: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_add_unsigned_int, \
        int:            _dm_add_int, \
        double:         _dm_add_double, \
        double complex: _dm_add_double_complex \
    )(a, b); \
})

#define dm_sub(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_sub: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_sub_unsigned_int, \
        int:            _dm_sub_int, \
        double:         _dm_sub_double, \
        double complex: _dm_sub_double_complex \
    )(a, b); \
})

#define dm_mul(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_mul: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_mul_unsigned_int, \
        int:            _dm_mul_int, \
        double:         _dm_mul_double, \
        double complex: _dm_mul_double_complex \
    )(a, b); \
})

#define dm_div(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_div: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_div_unsigned_int, \
        int:            _dm_div_int, \
        double:         _dm_div_double, \
        double complex: _dm_div_double_complex \
    )(a, b); \
})

#define dm_pow(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_pow: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_pow_unsigned_int, \
        int:            _dm_pow_int, \
        double:         _dm_pow_double, \
        double complex: _dm_pow_double_complex \
    )(a, b); \
})

#define dm_log(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_log: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_log_unsigned_int, \
        int:            _dm_log_int, \
        double:         _dm_log_double, \
        double complex: _dm_log_double_complex \
    )(a, b); \
})

#define dm_root(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_root: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_root_unsigned_int, \
        int:            _dm_root_int, \
        double:         _dm_root_double, \
        double complex: _dm_root_double_complex \
    )(a, b); \
})

#define dm_spow(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_spow: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_spow_unsigned_int, \
        int:            _dm_spow_int, \
        double:         _dm_spow_double, \
        double complex: _dm_spow_double_complex \
    )(a, b); \
})

#define dm_slog(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_slog: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_slog_unsigned_int, \
        int:            _dm_slog_int, \
        double:         _dm_slog_double, \
        double complex: _dm_slog_double_complex \
    )(a, b); \
})

#define dm_sroot(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_sroot: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_sroot_unsigned_int, \
        int:            _dm_sroot_int, \
        double:         _dm_sroot_double, \
        double complex: _dm_sroot_double_complex \
    )(a, b); \
})





/*
* daamath supports everything up to complex numbers because complex numbers are algebraically closed. that is very nice
* but the tradeoff is that complex algebra often has branches (multiple outputs for one input) and we want functions to give only one output. so the tradeoff that daamath makes is that it picks conventional principal branches

* in fact, i want to support all geometric algebras by making an algebra generator like ganja.js :( .....
* but i dont have the mathematical expertise yet. one day... GA generator + hyperoperation generator. it would be amazing.. plus, we have a string library too! and constants. etc etc. i love this library
*/
