#include<stdio.h>

int increment()
{
static int x=0;
x=x+1;
printf("x=%d\n",x); 
return 0;
}

int main()
{
increment();
increment();
increment();
return 0;
}
