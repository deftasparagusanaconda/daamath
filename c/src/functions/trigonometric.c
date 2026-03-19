// trigonometric functions are typically not closed on the integers. so we define real and complex ones. also note that the complex ones pick the most conventional principal branch

#include "trigonometric.h"
#include <math.h>
#include <complex.h>

double           _dm_sin_double        (double         angle) {return sin(angle)       ;}
double           _dm_cos_double        (double         angle) {return cos(angle)       ;}
double           _dm_tan_double        (double         angle) {return tan(angle)       ;}
double           _dm_cot_double        (double         angle) {return 1 / tan(angle)   ;}
double           _dm_sec_double        (double         angle) {return 1 / cos(angle)   ;}
double           _dm_csc_double        (double         angle) {return 1 / sin(angle)   ;}
double          _dm_asin_double        (double         angle) {return asin(angle)      ;}
double          _dm_acos_double        (double         angle) {return acos(angle)      ;}
double          _dm_atan_double        (double         angle) {return atan(angle)      ;}
double          _dm_acot_double        (double         angle) {return atan(1 / angle)  ;}
double          _dm_asec_double        (double         angle) {return acos(1 / angle)  ;}
double          _dm_acsc_double        (double         angle) {return asin(1 / angle)  ;}

double complex   _dm_sin_double_complex(double complex angle) {return csin(angle)      ;}
double complex   _dm_cos_double_complex(double complex angle) {return ccos(angle)      ;}
double complex   _dm_tan_double_complex(double complex angle) {return ctan(angle)      ;}
double complex   _dm_cot_double_complex(double complex angle) {return 1 / ctan(angle)  ;}
double complex   _dm_sec_double_complex(double complex angle) {return 1 / ccos(angle)  ;}
double complex   _dm_csc_double_complex(double complex angle) {return 1 / csin(angle)  ;}
double complex  _dm_asin_double_complex(double complex angle) {return casin(angle)     ;}
double complex  _dm_acos_double_complex(double complex angle) {return cacos(angle)     ;}
double complex  _dm_atan_double_complex(double complex angle) {return catan(angle)     ;}
double complex  _dm_acot_double_complex(double complex angle) {return catan(1 / angle) ;}
double complex  _dm_asec_double_complex(double complex angle) {return cacos(1 / angle) ;}
double complex  _dm_acsc_double_complex(double complex angle) {return casin(1 / angle) ;}

double          _dm_sinh_double        (double         angle) {return sinh(angle)      ;}
double          _dm_cosh_double        (double         angle) {return cosh(angle)      ;}
double          _dm_tanh_double        (double         angle) {return tanh(angle)      ;}
double          _dm_coth_double        (double         angle) {return 1 / tanh(angle)  ;}
double          _dm_sech_double        (double         angle) {return 1 / cosh(angle)  ;}
double          _dm_csch_double        (double         angle) {return 1 / sinh(angle)  ;}
double         _dm_asinh_double        (double         angle) {return asinh(angle)     ;}
double         _dm_acosh_double        (double         angle) {return acosh(angle)     ;}
double         _dm_atanh_double        (double         angle) {return atanh(angle)     ;}
double         _dm_acoth_double        (double         angle) {return atanh(1 / angle) ;}
double         _dm_asech_double        (double         angle) {return acosh(1 / angle) ;}
double         _dm_acsch_double        (double         angle) {return asinh(1 / angle) ;}

double complex  _dm_sinh_double_complex(double complex angle) {return csinh(angle)     ;}
double complex  _dm_cosh_double_complex(double complex angle) {return ccosh(angle)     ;}
double complex  _dm_tanh_double_complex(double complex angle) {return ctanh(angle)     ;}
double complex  _dm_coth_double_complex(double complex angle) {return 1 / ctanh(angle) ;}
double complex  _dm_sech_double_complex(double complex angle) {return 1 / ccosh(angle) ;}
double complex  _dm_csch_double_complex(double complex angle) {return 1 / csinh(angle) ;}
double complex _dm_asinh_double_complex(double complex angle) {return casinh(angle)    ;}
double complex _dm_acosh_double_complex(double complex angle) {return cacosh(angle)    ;}
double complex _dm_atanh_double_complex(double complex angle) {return catanh(angle)    ;}
double complex _dm_acoth_double_complex(double complex angle) {return catanh(1 / angle);}
double complex _dm_asech_double_complex(double complex angle) {return cacosh(1 / angle);}
double complex _dm_acsch_double_complex(double complex angle) {return casinh(1 / angle);}
