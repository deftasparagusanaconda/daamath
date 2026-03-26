#include "logical.h"
#include <stdbool.h>

// boolean
bool  _dm_not_bool(        bool b) {return  !b      ;}
bool  _dm_and_bool(bool a, bool b) {return   a && b ;}
bool   _dm_or_bool(bool a, bool b) {return   a || b ;}
bool  _dm_xor_bool(bool a, bool b) {return   a != b ;}
bool  _dm_imp_bool(bool a, bool b) {return   a <= b ;}
bool  _dm_con_bool(bool a, bool b) {return   a >= b ;}
bool _dm_nand_bool(bool a, bool b) {return ~(a && b);}
bool  _dm_nor_bool(bool a, bool b) {return ~(a || b);}
bool _dm_xnor_bool(bool a, bool b) {return   a == b ;}
bool _dm_nimp_bool(bool a, bool b) {return   a >  b ;}
bool _dm_ncon_bool(bool a, bool b) {return   a <  b ;}
// bitwise
int    _dm_not_int(        int  b) {return  ~b      ;}
int    _dm_and_int(int  a, int  b) {return   a &  b ;}
int     _dm_or_int(int  a, int  b) {return   a |  b ;}
int    _dm_xor_int(int  a, int  b) {return   a ^  b ;}
int    _dm_imp_int(int  a, int  b) {return  ~a |  b ;}
int    _dm_con_int(int  a, int  b) {return   a | ~b ;}
int   _dm_nand_int(int  a, int  b) {return ~(a &  b);}
int    _dm_nor_int(int  a, int  b) {return ~(a |  b);}
int   _dm_xnor_int(int  a, int  b) {return ~(a ^  b);}
int   _dm_nimp_int(int  a, int  b) {return   a & ~b ;}
int   _dm_ncon_int(int  a, int  b) {return  ~a &  b ;}
