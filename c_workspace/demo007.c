#include<stdio.h>

int a=1;
int inner()
{
a=4;
return 0;
}


int main()
{
printf("a=%d\n",a);
inner();
printf("a=%d\n",a);
return 0;
}
