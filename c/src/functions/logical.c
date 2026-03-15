#include <stdbool.h>

bool  not_bool(bool a        ) {return  !a      ;}
bool  and_bool(bool a, bool b) {return   a && b ;}
bool   or_bool(bool a, bool b) {return   a || b ;}
bool  xor_bool(bool a, bool b) {return   a != b ;}
bool  imp_bool(bool a, bool b) {return   a <= b ;}
bool  con_bool(bool a, bool b) {return   a >= b ;}
bool nand_bool(bool a, bool b) {return ~(a && b);}
bool  nor_bool(bool a, bool b) {return ~(a || b);}
bool nxor_bool(bool a, bool b) {return   a == b ;}
bool nimp_bool(bool a, bool b) {return   a >  b ;}
bool ncon_bool(bool a, bool b) {return   a <  b ;}

int   not_int (int  a        ) {return  ~a      ;}
int   and_int (int  a, int  b) {return   a &  b ;}
int    or_int (int  a, int  b) {return   a |  b ;}
int   xor_int (int  a, int  b) {return   a ^  b ;}
int   imp_int (int  a, int  b) {return  ~a |  b ;}
int   con_int (int  a, int  b) {return   a | ~b ;}
int  nand_int (int  a, int  b) {return ~(a &  b);}
int   nor_int (int  a, int  b) {return ~(a |  b);}
int  nxor_int (int  a, int  b) {return ~(a ^  b);}
int  nimp_int (int  a, int  b) {return   a & ~b ;}
int  ncon_int (int  a, int  b) {return  ~a &  b ;}


