// trigonometric functions are typically not closed on the integers. so we define real and complex ones. also note that the complex ones pick the most conventional principal branch, just the arc versions
#include <math.h>
#include <complex.h>

double           sin(double         angle) {return sin(angle)       ;}
double           cos(double         angle) {return cos(angle)       ;}
double           tan(double         angle) {return tan(angle)       ;}
double           cot(double         angle) {return 1 / tan(angle)   ;}
double           sec(double         angle) {return 1 / cos(angle)   ;}
double           csc(double         angle) {return 1 / sin(angle)   ;}
double          asin(double         angle) {return asin(angle)      ;}
double          acos(double         angle) {return acos(angle)      ;}
double          atan(double         angle) {return atan(angle)      ;}
double          acot(double         angle) {return atan(1 / angle)  ;}
double          asec(double         angle) {return acos(1 / angle)  ;}
double          acsc(double         angle) {return asin(1 / angle)  ;}

double complex   sin(double complex angle) {return csin(angle)      ;}
double complex   cos(double complex angle) {return ccos(angle)      ;}
double complex   tan(double complex angle) {return ctan(angle)      ;}
double complex   cot(double complex angle) {return 1 / ctan(angle)  ;}
double complex   sec(double complex angle) {return 1 / ccos(angle)  ;}
double complex   csc(double complex angle) {return 1 / csin(angle)  ;}
double complex  asin(double complex angle) {return casin(angle)     ;}
double complex  acos(double complex angle) {return cacos(angle)     ;}
double complex  atan(double complex angle) {return catan(angle)     ;}
double complex  acot(double complex angle) {return catan(1 / angle) ;}
double complex  asec(double complex angle) {return cacos(1 / angle) ;}
double complex  acsc(double complex angle) {return casin(1 / angle) ;}

