// trigonometric functions are typically not closed on the integers. so we define real and complex ones. also note that the complex ones pick the most conventional principal branch, just the arc versions
#include <math.h>
#include <complex.h>

double          sinh(double         angle) {return sinh(angle)      ;}
double          cosh(double         angle) {return cosh(angle)      ;}
double          tanh(double         angle) {return tanh(angle)      ;}
double          coth(double         angle) {return 1 / coth(angle)  ;}
double          sech(double         angle) {return 1 / cosh(angle)  ;}
double          csch(double         angle) {return 1 / sinh(angle)  ;}
double         asinh(double         angle) {return asinh(angle)     ;}
double         acosh(double         angle) {return acosh(angle)     ;}
double         atanh(double         angle) {return atanh(angle)     ;}
double         acoth(double         angle) {return acoth(1 / angle) ;}
double         asech(double         angle) {return acosh(1 / angle) ;}
double         acsch(double         angle) {return asinh(1 / angle) ;}

double complex  sinh(double complex angle) {return csinh(angle)     ;}
double complex  cosh(double complex angle) {return ccosh(angle)     ;}
double complex  tanh(double complex angle) {return ctanh(angle)     ;}
double complex  coth(double complex angle) {return 1 / ccoth(angle) ;}
double complex  sech(double complex angle) {return 1 / ccosh(angle) ;}
double complex  csch(double complex angle) {return 1 / csinh(angle) ;}
double complex asinh(double complex angle) {return casinh(angle)    ;}
double complex acosh(double complex angle) {return cacosh(angle)    ;}
double complex atanh(double complex angle) {return catanh(angle)    ;}
double complex acoth(double complex angle) {return cacoth(1 / angle);}
double complex asech(double complex angle) {return cacosh(1 / angle);}
double complex acsch(double complex angle) {return casinh(1 / angle);}


