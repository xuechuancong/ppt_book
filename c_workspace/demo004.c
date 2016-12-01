#include<stdio.h>

int inner()
{
int b=6;
printf("b=%d\n",b);
return 0;
}

int main()
{
int a=4;
inner();
printf("a=%d\n",a);
return 0;
}
