#include<stdio.h>
int a=345;
int inner()
{
static int a=554;
printf("a=%d\n",a);
return 0;
}

int main()
{
inner();
printf("a=%d\n",a);
inner();
return 0;
}
