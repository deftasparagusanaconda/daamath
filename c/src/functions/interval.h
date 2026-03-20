#include <stdbool.h>

bool _dm_lt_unsigned_int(unsigned int a, unsigned int b);
bool _dm_le_unsigned_int(unsigned int a, unsigned int b);
bool _dm_eq_unsigned_int(unsigned int a, unsigned int b);
bool _dm_ne_unsigned_int(unsigned int a, unsigned int b);
bool _dm_ge_unsigned_int(unsigned int a, unsigned int b);
bool _dm_gt_unsigned_int(unsigned int a, unsigned int b);
bool _dm_oo_unsigned_int(unsigned int x, unsigned int a, unsigned int b);
bool _dm_oc_unsigned_int(unsigned int x, unsigned int a, unsigned int b);
bool _dm_co_unsigned_int(unsigned int x, unsigned int a, unsigned int b);
bool _dm_cc_unsigned_int(unsigned int x, unsigned int a, unsigned int b);

bool _dm_lt_int(int a, int b);
bool _dm_le_int(int a, int b);
bool _dm_eq_int(int a, int b);
bool _dm_ne_int(int a, int b);
bool _dm_ge_int(int a, int b);
bool _dm_gt_int(int a, int b);
bool _dm_oo_int(int x, int a, int b);
bool _dm_oc_int(int x, int a, int b);
bool _dm_co_int(int x, int a, int b);
bool _dm_cc_int(int x, int a, int b);

bool _dm_lt_double(double a, double b);
bool _dm_le_double(double a, double b);
bool _dm_eq_double(double a, double b);
bool _dm_ne_double(double a, double b);
bool _dm_ge_double(double a, double b);
bool _dm_gt_double(double a, double b);
bool _dm_oo_double(double x, double a, double b);
bool _dm_oc_double(double x, double a, double b);
bool _dm_co_double(double x, double a, double b);
bool _dm_cc_double(double x, double a, double b);

#define _dm_same_type(a, b) _Generic((a), \
    unsigned int:   _Generic((b), unsigned int:   1, default: 0), \
    int:            _Generic((b), int:            1, default: 0), \
    double:         _Generic((b), double:         1, default: 0), \
    double complex: _Generic((b), double complex: 1, default: 0), \
    default: 0 \
)

#define dm_lt(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_lt: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_lt_unsigned_int, \
        int:            _dm_lt_int, \
        double:         _dm_lt_double \
    )(a, b); \
})

#define dm_le(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_le: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_le_unsigned_int, \
        int:            _dm_le_int, \
        double:         _dm_le_double \
    )(a, b); \
})

#define dm_eq(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_eq: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_eq_unsigned_int, \
        int:            _dm_eq_int, \
        double:         _dm_eq_double \
    )(a, b); \
})

#define dm_ne(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_ne: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_ne_unsigned_int, \
        int:            _dm_ne_int, \
        double:         _dm_ne_double \
    )(a, b); \
})

#define dm_ge(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_ge: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_ge_unsigned_int, \
        int:            _dm_ge_int, \
        double:         _dm_ge_double \
    )(a, b); \
})

#define dm_gt(a, b) ({ \
    _Static_assert( \
        _dm_same_type(a, b), \
        "dm_gt: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(a)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_gt_unsigned_int, \
        int:            _dm_gt_int, \
        double:         _dm_gt_double \
    )(a, b); \
})

#define _dm_same_type_3(a, b, c) (_dm_same_type(a, b) && _dm_same_type(b, c))

#define dm_oo(x, a, b) ({ \
    _Static_assert( \
        _dm_same_type_3(x, a, b), \
        "dm_oo: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(x)*)1 - (typeof(a)*)1); \
    (void)sizeof((typeof(x)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_oo_unsigned_int, \
        int:            _dm_oo_int, \
        double:         _dm_oo_double \
    )(x, a, b); \
})

#define dm_oc(x, a, b) ({ \
    _Static_assert( \
        _dm_same_type_3(x, a, b), \
        "dm_oc: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(x)*)1 - (typeof(a)*)1); \
    (void)sizeof((typeof(x)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_oc_unsigned_int, \
        int:            _dm_oc_int, \
        double:         _dm_oc_double \
    )(x, a, b); \
})

#define dm_co(x, a, b) ({ \
    _Static_assert( \
        _dm_same_type_3(x, a, b), \
        "dm_co: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(x)*)1 - (typeof(a)*)1); \
    (void)sizeof((typeof(x)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_co_unsigned_int, \
        int:            _dm_co_int, \
        double:         _dm_co_double \
    )(x, a, b); \
})

#define dm_cc(x, a, b) ({ \
    _Static_assert( \
        _dm_same_type_3(x, a, b), \
        "dm_cc: arguments must be of same type. daamath does not allow implicit type promotion" \
    ); \
    (void)sizeof((typeof(x)*)1 - (typeof(a)*)1); \
    (void)sizeof((typeof(x)*)1 - (typeof(b)*)1); \
    _Generic((a), \
        unsigned int:   _dm_cc_unsigned_int, \
        int:            _dm_cc_int, \
        double:         _dm_cc_double \
    )(x, a, b); \
})
