// arithmetic primitives are: byte, short, int, long, float, double
// six types. so thats 6^1 for unary operators, 6^2 for binary, 6^3 for ternary, etc
// preserves int, long, float, double, byte to int, short to int, and always promotes to wider type
// type casting is explicitly mentioned even if java implicitly promotes them; only unless the input type already matches the output type

// types are promoted before operation for operand fairness. for example: 
// static float mul(int a, float b)

// make these methods into public

package swissmath;

import java.lang.Math;

public final class SwissMath
{	private SwissMath() {}
		
	// by convention, byte and short are promoted to int, because they hardly support normal arithmetic
	static int    add(byte   a, byte   b) { return (int   )a+(int   )b; }
	static int    add(byte   a, short  b) { return (int   )a+(int   )b; }
	static int    add(byte   a, int    b) { return (int   )a+        b; }
	static long   add(byte   a, long   b) { return (long  )a+        b; }
	static float  add(byte   a, float  b) { return (float )a+        b; }
	static double add(byte   a, double b) { return (double)a+        b; }
	static int    add(short  a, byte   b) { return (int   )a+(int   )b; }
	static int    add(short  a, short  b) { return (int   )a+(int   )b; }
	static int    add(short  a, int    b) { return (int   )a+        b; }
	static long   add(short  a, long   b) { return (long  )a+        b; }
	static float  add(short  a, float  b) { return (float )a+        b; }
	static double add(short  a, double b) { return (double)a+        b; }
	static int    add(int    a, byte   b) { return         a+(int   )b; }
	static int    add(int    a, short  b) { return         a+(int   )b; }
	static int    add(int    a, int    b) { return         a+        b; }
	static long   add(int    a, long   b) { return (long  )a+        b; }
	static float  add(int    a, float  b) { return (float )a+        b; }
	static double add(int    a, double b) { return (double)a+        b; }
	static long   add(long   a, byte   b) { return         a+(long  )b; }
	static long   add(long   a, short  b) { return         a+(long  )b; }
	static long   add(long   a, int    b) { return         a+(long  )b; }
	static long   add(long   a, long   b) { return         a+        b; }
	static float  add(long   a, float  b) { return (float )a+        b; }
	static double add(long   a, double b) { return (double)a+        b; }
	static float  add(float  a, byte   b) { return         a+(float )b; }
	static float  add(float  a, short  b) { return         a+(float )b; }
	static float  add(float  a, int    b) { return         a+(float )b; }
	static float  add(float  a, long   b) { return         a+(float )b; }
	static float  add(float  a, float  b) { return         a+        b; }
	static double add(float  a, double b) { return (double)a+        b; }
	static double add(double a, byte   b) { return         a+(double)b; }
	static double add(double a, short  b) { return         a+(double)b; }
	static double add(double a, int    b) { return         a+(double)b; }
	static double add(double a, long   b) { return         a+(double)b; }
	static double add(double a, float  b) { return         a+(double)b; }
	static double add(double a, double b) { return         a+        b; }
	
	static int    sub(byte   a, byte   b) { return (int   )a-(int   )b; }
	static int    sub(byte   a, short  b) { return (int   )a-(int   )b; }
	static int    sub(byte   a, int    b) { return (int   )a-        b; }
	static long   sub(byte   a, long   b) { return (long  )a-        b; }
	static float  sub(byte   a, float  b) { return (float )a-        b; }
	static double sub(byte   a, double b) { return (double)a-        b; }
	static int    sub(short  a, byte   b) { return (int   )a-(int   )b; }
	static int    sub(short  a, short  b) { return (int   )a-(int   )b; }
	static int    sub(short  a, int    b) { return (int   )a-        b; }
	static long   sub(short  a, long   b) { return (long  )a-        b; }
	static float  sub(short  a, float  b) { return (float )a-        b; }
	static double sub(short  a, double b) { return (double)a-        b; }
	static int    sub(int    a, byte   b) { return         a-(int   )b; }
	static int    sub(int    a, short  b) { return         a-(int   )b; }
	static int    sub(int    a, int    b) { return         a-        b; }
	static long   sub(int    a, long   b) { return (long  )a-        b; }
	static float  sub(int    a, float  b) { return (float )a-        b; }
	static double sub(int    a, double b) { return (double)a-        b; }
	static long   sub(long   a, byte   b) { return         a-(long  )b; }
	static long   sub(long   a, short  b) { return         a-(long  )b; }
	static long   sub(long   a, int    b) { return         a-(long  )b; }
	static long   sub(long   a, long   b) { return         a-        b; }
	static float  sub(long   a, float  b) { return (float )a-        b; }
	static double sub(long   a, double b) { return (double)a-        b; }
	static float  sub(float  a, byte   b) { return         a-(float )b; }
	static float  sub(float  a, short  b) { return         a-(float )b; }
	static float  sub(float  a, int    b) { return         a-(float )b; }
	static float  sub(float  a, long   b) { return         a-(float )b; }
	static float  sub(float  a, float  b) { return         a-        b; }
	static double sub(float  a, double b) { return (double)a-        b; }
	static double sub(double a, byte   b) { return         a-(double)b; }
	static double sub(double a, short  b) { return         a-(double)b; }
	static double sub(double a, int    b) { return         a-(double)b; }
	static double sub(double a, long   b) { return         a-(double)b; }
	static double sub(double a, float  b) { return         a-(double)b; }
	static double sub(double a, double b) { return         a-        b; }
	
	static int    mul(byte   a, byte   b) { return (int   )a*(int   )b; }
	static int    mul(byte   a, short  b) { return (int   )a*(int   )b; }
	static int    mul(byte   a, int    b) { return (int   )a*        b; }
	static long   mul(byte   a, long   b) { return (long  )a*        b; }
	static float  mul(byte   a, float  b) { return (float )a*        b; }
	static double mul(byte   a, double b) { return (double)a*        b; }
	static int    mul(short  a, byte   b) { return (int   )a*(int   )b; }
	static int    mul(short  a, short  b) { return (int   )a*(int   )b; }
	static int    mul(short  a, int    b) { return (int   )a*        b; }
	static long   mul(short  a, long   b) { return (long  )a*        b; }
	static float  mul(short  a, float  b) { return (float )a*        b; }
	static double mul(short  a, double b) { return (double)a*        b; }
	static int    mul(int    a, byte   b) { return         a*(int   )b; }
	static int    mul(int    a, short  b) { return         a*(int   )b; }
	static int    mul(int    a, int    b) { return         a*        b; }
	static long   mul(int    a, long   b) { return (long  )a*        b; }
	static float  mul(int    a, float  b) { return (float )a*        b; }
	static double mul(int    a, double b) { return (double)a*        b; }
	static long   mul(long   a, byte   b) { return         a*(long  )b; }
	static long   mul(long   a, short  b) { return         a*(long  )b; }
	static long   mul(long   a, int    b) { return         a*(long  )b; }
	static long   mul(long   a, long   b) { return         a*        b; }
	static float  mul(long   a, float  b) { return (float )a*        b; }
	static double mul(long   a, double b) { return (double)a*        b; }
	static float  mul(float  a, byte   b) { return         a*(float )b; }
	static float  mul(float  a, short  b) { return         a*(float )b; }
	static float  mul(float  a, int    b) { return         a*(float )b; }
	static float  mul(float  a, long   b) { return         a*(float )b; }
	static float  mul(float  a, float  b) { return         a*        b; }
	static double mul(float  a, double b) { return (double)a*        b; }
	static double mul(double a, byte   b) { return         a*(double)b; }
	static double mul(double a, short  b) { return         a*(double)b; }
	static double mul(double a, int    b) { return         a*(double)b; }
	static double mul(double a, long   b) { return         a*(double)b; }
	static double mul(double a, float  b) { return         a*(double)b; }
	static double mul(double a, double b) { return         a*        b; }

	// a true division always returns at least a float
	static float  div(byte   a, byte   b) { return (float )a/(float )b; }
	static float  div(byte   a, short  b) { return (float )a/(float )b; }
	static float  div(byte   a, int    b) { return (float )a/(float )b; }
	static float  div(byte   a, long   b) { return (float )a/(float )b; }
	static float  div(byte   a, float  b) { return (float )a/        b; }
	static double div(byte   a, double b) { return (double)a/        b; }
	static float  div(short  a, byte   b) { return (float )a/(float )b; }
	static float  div(short  a, short  b) { return (float )a/(float )b; }
	static float  div(short  a, int    b) { return (float )a/(float )b; }
	static float  div(short  a, long   b) { return (float )a/(float )b; }
	static float  div(short  a, float  b) { return (float )a/        b; }
	static double div(short  a, double b) { return (double)a/        b; }
	static float  div(int    a, byte   b) { return (float )a/(float )b; }
	static float  div(int    a, short  b) { return (float )a/(float )b; }
	static float  div(int    a, int    b) { return (float )a/(float )b; }
	static float  div(int    a, long   b) { return (float )a/(float )b; }
	static float  div(int    a, float  b) { return (float )a/        b; }
	static double div(int    a, double b) { return (double)a/        b; }
	static float  div(long   a, byte   b) { return (float )a/(float )b; }
	static float  div(long   a, short  b) { return (float )a/(float )b; }
	static float  div(long   a, int    b) { return (float )a/(float )b; }
	static float  div(long   a, long   b) { return (float )a/(float )b; }
	static float  div(long   a, float  b) { return (float )a/        b; }
	static double div(long   a, double b) { return (double)a/        b; }
	static float  div(float  a, byte   b) { return         a/(float )b; }
	static float  div(float  a, short  b) { return         a/(float )b; }
	static float  div(float  a, int    b) { return         a/(float )b; }
	static float  div(float  a, long   b) { return         a/(float )b; }
	static float  div(float  a, float  b) { return         a/        b; }
	static double div(float  a, double b) { return (double)a/        b; }
	static double div(double a, byte   b) { return         a/(double)b; }
	static double div(double a, short  b) { return         a/(double)b; }
	static double div(double a, int    b) { return         a/(double)b; }
	static double div(double a, long   b) { return         a/(double)b; }
	static double div(double a, float  b) { return         a/(double)b; }
	static double div(double a, double b) { return         a/        b; }

	static float  inv(byte   a) { return 1/(float)a; }
	static float  inv(short  a) { return 1/(float)a; }
	static float  inv(int    a) { return 1/(float)a; }
	static float  inv(long   a) { return 1/(float)a; }
	static float  inv(float  a) { return 1/       a; }
	static double inv(double a) { return 1/       a; }

	static int    neg(byte   a) { return -(int)a; }
	static int    neg(short  a) { return -(int)a; }
	static int    neg(int    a) { return -     a; }
	static long   neg(long   a) { return -     a; }
	static float  neg(float  a) { return -     a; }
	static double neg(double a) { return -     a; }

	static double pow(double a, double b) { return Math.pow(a,b); }
}	
	
