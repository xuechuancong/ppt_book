#include <stdio.h>
#define SQUARE(x) ((x)*(x))
int Square(int x){
    return (x * x); //未考虑溢出保护
}

int main(void){
    int i = 1;
    while(i <= 5)
        printf("i = %d, Square = %d\n", i, Square(i++));

    int j = 1;
    while(j <= 5)
        printf("j = %d, SQUARE = %d\n", j, SQUARE(j++));
    
    return 0;
}
