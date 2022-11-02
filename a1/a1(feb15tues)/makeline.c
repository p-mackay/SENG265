#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){

    char arr1[100] = "October 23, 2022 (Sunday)";
    char arr2[100];
    char buffer[100];
    int count = 0;
    int i = 0;


    while(arr1[count] != '\0'){
        buffer[count] = '-';
        count++;
    }
    buffer[count] = '\0';
    printf("%d\n", count);
    printf("%s\n", arr1);
    printf("%s\n", buffer);
    strcpy(arr2, buffer);
    printf("%s\n", arr2);

}
