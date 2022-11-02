/*
Paul MacKay - 17/03/2022 - dynamic memory - SENG 265 

 */
#include <stdio.h>
#include <stdlib.h>

void F(){
    int n = 10000000;
    int* A = malloc(n*sizeof(int));

    printf("In F (before loop)\n");

    for(int i = 0; i<n; i++){
        A[i] = i%11;
    }

    printf("In F (after loop)\n");

    int result = A[n/2] + A[n-1];

    printf("Result = %d\n", result);

    free(A);
}

int main(){
    F();

    return 0;

}
