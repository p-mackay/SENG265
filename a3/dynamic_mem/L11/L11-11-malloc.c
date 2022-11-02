/*
Paul MacKay - 17/03/2022 - dynamic memory - SENG 265 

 */
#include <stdio.h>
#include <stdlib.h>

typedef struct{
    char customer_name[101];
    float order_prices[10000000];
}CustomerData;

void F(){
    CustomerData* c_ptr = malloc(sizeof(CustomerData));
    printf("In F\n");
}

int main(){
    printf("In main (before calling F)\n");
    F();
    printf("In main (after calling F)\n");

    return 0;

}
