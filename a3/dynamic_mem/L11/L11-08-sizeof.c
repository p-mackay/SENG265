/*
Paul MacKay - 17/03/2022 - dynamic memory - SENG 265 

 */
#include <stdio.h>
#include <stdlib.h>

int main(){
    int x = 6;
    float f = 18.7;

    printf("Size of an int: %ld\n", sizeof(int));
    printf("Size of an char: %ld\n", sizeof(char));
    printf("Size of an double: %ld\n", sizeof(double));
    printf("Size of the variable x: %ld\n", sizeof(x));
    printf("Size of the variable f: %ld\n", sizeof(f));

    return 0;

}
