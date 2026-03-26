#include <stdbool.h>

// boolean
bool  _dm_not_bool(        bool b);
bool  _dm_and_bool(bool a, bool b);
bool   _dm_or_bool(bool a, bool b);
bool  _dm_xor_bool(bool a, bool b);
bool  _dm_imp_bool(bool a, bool b);
bool  _dm_con_bool(bool a, bool b);
bool _dm_nand_bool(bool a, bool b);
bool  _dm_nor_bool(bool a, bool b);
bool _dm_xnor_bool(bool a, bool b);
bool _dm_nimp_bool(bool a, bool b);
bool _dm_ncon_bool(bool a, bool b);

// bitwise
int    _dm_not_int(        int  b);
int    _dm_and_int(int  a, int  b);
int     _dm_or_int(int  a, int  b);
int    _dm_xor_int(int  a, int  b);
int    _dm_imp_int(int  a, int  b);
int    _dm_con_int(int  a, int  b);
int   _dm_nand_int(int  a, int  b);
int    _dm_nor_int(int  a, int  b);
int   _dm_xnor_int(int  a, int  b);
int   _dm_nimp_int(int  a, int  b);
int   _dm_ncon_int(int  a, int  b);

#define  dm_not(x)    _Generic((x), bool: _dm_not_bool,  int:  _dm_not_int)(x)
#define  dm_and(x, y) _Generic((x), bool: _dm_and_bool,  int:  _dm_and_int)(x, y)
#define   dm_or(x, y) _Generic((x), bool:  _dm_or_bool,  int:   _dm_or_int)(x, y)
#define  dm_xor(x, y) _Generic((x), bool: _dm_xor_bool,  int:  _dm_xor_int)(x, y)
#define  dm_imp(x, y) _Generic((x), bool: _dm_imp_bool,  int:  _dm_imp_int)(x, y)
#define  dm_con(x, y) _Generic((x), bool: _dm_con_bool,  int:  _dm_con_int)(x, y)
#define dm_nand(x, y) _Generic((x), bool: _dm_nand_bool, int: _dm_nand_int)(x, y)
#define  dm_nor(x, y) _Generic((x), bool:  _dm_nor_bool, int:  _dm_nor_int)(x, y)
#define dm_xnor(x, y) _Generic((x), bool: _dm_xnor_bool, int: _dm_xnor_int)(x, y)
#define dm_nimp(x, y) _Generic((x), bool: _dm_nimp_bool, int: _dm_nimp_int)(x, y)
#define dm_ncon(x, y) _Generic((x), bool: _dm_ncon_bool, int: _dm_ncon_int)(x, y)
