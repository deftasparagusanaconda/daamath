#include <stdio.h>
#include "daamath.h"

int main(void)
{
	printf("%lf\n", dm_add(1.0, 1.0));
	printf("%d\n", dm_add(1, 1));
	printf("%d\n", dm_pow(1, 2));
	printf("%lf\n", dm_root(2.0, 2.0));
	printf("%lf\n", dm_sin(1.0));
	printf("%d\n", dm_not(2));

	return 0;
}



