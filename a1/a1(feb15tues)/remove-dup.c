/*
 Paul MacKay - 02/02/2022
 https://www.tutorialspoint.com/c-program-to-delete-the-duplicate-elements-in-an-array
 
  */
#include <stdio.h>
#include <stdlib.h>

int main(){
    int number = 100;
    int a[number];
    for (int i = 0; i < number; i++){
        a[i] = i;
    }
    a[0] = 1;
    a[1] = 1;
    a[2] = 1;
    a[3] = 1;
    a[4] = 1;
    

    for(int i=0;i<number;i++){
       for(int j = i+1; j < number; j++){
          if(a[i] == a[j]){
             for(int k = j; k <number; k++){
                a[k] = a[k+1];
             }
             j--;
             number--;
          }
       }
    }

    for(int i=0;i<number;i++){
    printf("%d ",a[i]);
    }
    printf("\n");
}

