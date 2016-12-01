#include<stdio.h>

int main(int argc, char *argv[])
{
FILE *fp;
fp = fopen(argv[1],"w");
fputs("I love you",fp);
fclose(fp);
return 0;

}
