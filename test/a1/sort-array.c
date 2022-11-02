/*
Paul MacKay - 02/02/2022
https://www.tutorialspoint.com/c-program-to-sort-an-array-in-an-ascending-order 
  */
#include <stdio.h>
#include <stdlib.h>

int main(){
    int arr[10];
    int a;

    for(int i = 9; i >= 0; i--){
        arr[i] = i; 
        printf("%d", arr[i]);
    }
    printf("\n");
    
    for (int i = 0; i < 10; ++i){
        for (int j = i + 1; j < 10; ++j){
            if (arr[i] > arr[j]){
                 a = arr[i];
                 arr[i] = arr[j];
                 arr[j] = a;
            }
        }
    }
    for(int i = 0; i < 10; i++){
        printf("%d", arr[i]);
    }
    printf("\n");

}

