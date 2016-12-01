#include <stdio.h>
#define PI 3.14159
#define pt "This is my first C programe.\n"
#include "compare.h"
#define add(x,y) x+y

int main(void)
{
int a,b;
printf("PI=%2.5f\n",PI);
printf(pt);
a=3;
b=4;
/* compare(a,b);*/
add(2,4);
return 0;
}
