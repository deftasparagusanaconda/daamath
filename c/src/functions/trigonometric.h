#include <complex.h>

double         _dm_sin_double          (double         angle);
double         _dm_cos_double          (double         angle);
double         _dm_tan_double          (double         angle);
double         _dm_cot_double          (double         angle);
double         _dm_sec_double          (double         angle);
double         _dm_csc_double          (double         angle);
double         _dm_asin_double         (double         angle);
double         _dm_acos_double         (double         angle);
double         _dm_atan_double         (double         angle);
double         _dm_acot_double         (double         angle);
double         _dm_asec_double         (double         angle);
double         _dm_acsc_double         (double         angle);

double complex _dm_sin_double_complex  (double complex angle);
double complex _dm_cos_double_complex  (double complex angle);
double complex _dm_tan_double_complex  (double complex angle);
double complex _dm_cot_double_complex  (double complex angle);
double complex _dm_sec_double_complex  (double complex angle);
double complex _dm_csc_double_complex  (double complex angle);
double complex _dm_asin_double_complex (double complex angle);
double complex _dm_acos_double_complex (double complex angle);
double complex _dm_atan_double_complex (double complex angle);
double complex _dm_acot_double_complex (double complex angle);
double complex _dm_asec_double_complex (double complex angle);
double complex _dm_acsc_double_complex (double complex angle);

double         _dm_sinh_double         (double         angle);
double         _dm_cosh_double         (double         angle);
double         _dm_tanh_double         (double         angle);
double         _dm_coth_double         (double         angle);
double         _dm_sech_double         (double         angle);
double         _dm_csch_double         (double         angle);
double         _dm_asinh_double        (double         angle);
double         _dm_acosh_double        (double         angle);
double         _dm_atanh_double        (double         angle);
double         _dm_acoth_double        (double         angle);
double         _dm_asech_double        (double         angle);
double         _dm_acsch_double        (double         angle);

double complex _dm_sinh_double_complex (double complex angle);
double complex _dm_cosh_double_complex (double complex angle);
double complex _dm_tanh_double_complex (double complex angle);
double complex _dm_coth_double_complex (double complex angle);
double complex _dm_sech_double_complex (double complex angle);
double complex _dm_csch_double_complex (double complex angle);
double complex _dm_asinh_double_complex(double complex angle);
double complex _dm_acosh_double_complex(double complex angle);
double complex _dm_atanh_double_complex(double complex angle);
double complex _dm_acoth_double_complex(double complex angle);
double complex _dm_asech_double_complex(double complex angle);
double complex _dm_acsch_double_complex(double complex angle);

#define dm_sin(x)   _Generic((x), double: _dm_sin_double,   double complex: _dm_sin_double_complex)(x)
#define dm_cos(x)   _Generic((x), double: _dm_cos_double,   double complex: _dm_cos_double_complex)(x)
#define dm_tan(x)   _Generic((x), double: _dm_tan_double,   double complex: _dm_tan_double_complex)(x)
#define dm_cot(x)   _Generic((x), double: _dm_cot_double,   double complex: _dm_cot_double_complex)(x)
#define dm_sec(x)   _Generic((x), double: _dm_sec_double,   double complex: _dm_sec_double_complex)(x)
#define dm_csc(x)   _Generic((x), double: _dm_csc_double,   double complex: _dm_csc_double_complex)(x)

#define dm_asin(x)  _Generic((x), double: _dm_asin_double,  double complex: _dm_asin_double_complex)(x)
#define dm_acos(x)  _Generic((x), double: _dm_acos_double,  double complex: _dm_acos_double_complex)(x)
#define dm_atan(x)  _Generic((x), double: _dm_atan_double,  double complex: _dm_atan_double_complex)(x)
#define dm_acot(x)  _Generic((x), double: _dm_acot_double,  double complex: _dm_acot_double_complex)(x)
#define dm_asec(x)  _Generic((x), double: _dm_asec_double,  double complex: _dm_asec_double_complex)(x)
#define dm_acsc(x)  _Generic((x), double: _dm_acsc_double,  double complex: _dm_acsc_double_complex)(x)

#define dm_sinh(x)  _Generic((x), double: _dm_sinh_double,  double complex: _dm_sinh_double_complex)(x)
#define dm_cosh(x)  _Generic((x), double: _dm_cosh_double,  double complex: _dm_cosh_double_complex)(x)
#define dm_tanh(x)  _Generic((x), double: _dm_tanh_double,  double complex: _dm_tanh_double_complex)(x)
#define dm_coth(x)  _Generic((x), double: _dm_coth_double,  double complex: _dm_coth_double_complex)(x)
#define dm_sech(x)  _Generic((x), double: _dm_sech_double,  double complex: _dm_sech_double_complex)(x)
#define dm_csch(x)  _Generic((x), double: _dm_csch_double,  double complex: _dm_csch_double_complex)(x)

#define dm_asinh(x) _Generic((x), double: _dm_asinh_double, double complex: _dm_asinh_double_complex)(x)
#define dm_acosh(x) _Generic((x), double: _dm_acosh_double, double complex: _dm_acosh_double_complex)(x)
#define dm_atanh(x) _Generic((x), double: _dm_atanh_double, double complex: _dm_atanh_double_complex)(x)
#define dm_acoth(x) _Generic((x), double: _dm_acoth_double, double complex: _dm_acoth_double_complex)(x)
#define dm_asech(x) _Generic((x), double: _dm_asech_double, double complex: _dm_asech_double_complex)(x)
#define dm_acsch(x) _Generic((x), double: _dm_acsch_double, double complex: _dm_acsch_double_complex)(x)
