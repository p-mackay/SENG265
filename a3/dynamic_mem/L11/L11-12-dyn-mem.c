/*
Paul MacKay - Friday 18/03/2022 - dynamic memory - SENG 265 

 */
#include <stdio.h>
#include <stdlib.h>

/*
 * is prime accepts an int. If that int is prime --> return 1 
 * else not prime --> return 0
 * */

int is_prime(int n){
    for(int i = 2; i < n; i++){
        if(n % i == 0){
            return 0;
        }
    }
    return 1;
}

int* primes_up_to_k(int k, int* size_ptr){
    int num_primes = 0;
    for(int n = 2; n <= k; n++){
        if(is_prime(n)){
            num_primes++;
        }
    }

    *size_ptr = num_primes;

    int* primes = malloc( num_primes*sizeof(int) );

    int output_idx = 0;
    for(int n = 2; n <= k; n++){
        if (is_prime(n)){
            primes[output_idx] = n;
            output_idx++;
        }
    }
    return primes;
}


int main(){

    int size;
    int* primes = primes_up_to_k(50, &size);

    
    printf("Primes less than 50: ");
    for(int i = 0; i < size; i++){
        printf("%d ", primes[i]);
    }
    printf("\n");

    free(primes);
    return 0;
}
