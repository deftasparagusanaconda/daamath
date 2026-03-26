#include "interval.h"
#include <stdbool.h>

bool _dm_lt_unsigned_int(unsigned int a, unsigned int b) {return a < b;}
bool _dm_le_unsigned_int(unsigned int a, unsigned int b) {return a <= b;}
bool _dm_eq_unsigned_int(unsigned int a, unsigned int b) {return a == b;}
bool _dm_ne_unsigned_int(unsigned int a, unsigned int b) {return a != b;}
bool _dm_ge_unsigned_int(unsigned int a, unsigned int b) {return a >= b;}
bool _dm_gt_unsigned_int(unsigned int a, unsigned int b) {return a > b;}
bool _dm_oo_unsigned_int(unsigned int x, unsigned int a, unsigned int b) {return a <  x && x <  b;}
bool _dm_oc_unsigned_int(unsigned int x, unsigned int a, unsigned int b) {return a <  x && x <= b;}
bool _dm_co_unsigned_int(unsigned int x, unsigned int a, unsigned int b) {return a <= x && x <  b;}
bool _dm_cc_unsigned_int(unsigned int x, unsigned int a, unsigned int b) {return a <= x && x <= b;}

bool _dm_lt_int(int a, int b) {return a <  b;}
bool _dm_le_int(int a, int b) {return a <= b;}
bool _dm_eq_int(int a, int b) {return a == b;}
bool _dm_ne_int(int a, int b) {return a != b;}
bool _dm_ge_int(int a, int b) {return a >= b;}
bool _dm_gt_int(int a, int b) {return a >  b;}
bool _dm_oo_int(int x, int a, int b) {return a <  x && x <  b;}
bool _dm_oc_int(int x, int a, int b) {return a <  x && x <= b;}
bool _dm_co_int(int x, int a, int b) {return a <= x && x <  b;}
bool _dm_cc_int(int x, int a, int b) {return a <= x && x <= b;}

bool _dm_lt_double(double a, double b) {return a <  b;}
bool _dm_le_double(double a, double b) {return a <= b;}
bool _dm_eq_double(double a, double b) {return a == b;}
bool _dm_ne_double(double a, double b) {return a != b;}
bool _dm_ge_double(double a, double b) {return a >= b;}
bool _dm_gt_double(double a, double b) {return a >  b;}
bool _dm_oo_double(double x, double a, double b) {return a <  x && x <  b;}
bool _dm_oc_double(double x, double a, double b) {return a <  x && x <= b;}
bool _dm_co_double(double x, double a, double b) {return a <= x && x <  b;}
bool _dm_cc_double(double x, double a, double b) {return a <= x && x <= b;}
