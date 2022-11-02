#include <stdio.h>                                                  
#include <string.h>                                                 
#include <stdlib.h>                                                 
#include <time.h> 
#define MAX_LINE_LEN 100


int main(int argc, char *argv[]){
    char line[MAX_LINE_LEN];
    int from_y = 0, from_m = 0, from_d = 0;
    int to_y = 0, to_m = 0, to_d = 0;
    char *filename = NULL;
    int i;
    

    for (i = 0; i < argc; i++) {
        if (strncmp(argv[i], "--start=", 8) == 0) {
            sscanf(argv[i], "--start=%d/%d/%d", &from_y, &from_m, &from_d);
        } else if (strncmp(argv[i], "--end=", 6) == 0) {
            sscanf(argv[i], "--end=%d/%d/%d", &to_y, &to_m, &to_d);
        }     
    }

    if(from_y < 2022){
    printf("%d\n", from_y);
    }
}
