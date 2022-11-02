#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char a[] = "20220223";
    char b[] = "20220210";



    if (strcmp(a, b) < 0){
        printf("%s <  %s\n", a, b);
    }
    if (strcmp(a, b) > 0){
        printf("%s > %s\n", a, b);
    }

}
