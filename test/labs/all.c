#include <stdio.h>

#define MAX_NUMS  5

void rogue(int *numbers, int num)
{
    int i;

    for (i = -2; i <= num; i++) {
        numbers[i] = 111 * i + 11;
    }
}


int main() {
    int innocent = 123;
    int nums[MAX_NUMS] = {1, 2, 3, 4, 5};
    int really_innocent = 456;
    int i;

    printf("%d %d\n", innocent, really_innocent);
    for (i = 0; i < MAX_NUMS; i++) {
        printf("%d: %d\n", i, nums[i]);
    }

    rogue(nums, MAX_NUMS);

    printf("----------------\n");
    printf("%d %d\n", innocent, really_innocent);
    for (i = 0; i < MAX_NUMS; i++) {
        printf("%d: %d\n", i, nums[i]);
    }
}

# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <ctype.h>


long get_number_memory(char *st);
long get_number(char *st);
long get_number_sscanf(char *st);

int main(int argc, char *argv[]){

        char *st = "a b 4 c d";

        long num1 = get_number(st);

        printf("%li\n", num1);

        long num2 = get_number_memory(st);

        printf("%li\n", num2);

        long num3 = get_number_sscanf(st);

        printf("%li\n", num3);

}

long get_number(char *st){
        // Uses indexing

        if (isdigit(st[4])){
                char * temp = &st[4];
                long num = strtol(temp, &temp, 10);
                return num;
        }

        return -1.11111111111111111;
}

long get_number_sscanf(char *st){
        // Uses the sscanf function

        long temp;
        char *discard;
        int success = sscanf(st, "%*[^0123456789]%li", &temp);

        if (success == 1){
                // printf(" works %li", temp);
                return temp;
        } else {
                printf("Failed");
                return -1.1111111111111111111111111;
        }
}
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10

 /*
  * Design a function rotate(int num, .........) that take a number as a parameter (int num) and any other parameters as required
  * When called, the function will modify arr_1 by moving each of its values to an index lowered by num. If the new index becomes negative, then MAX_SIZE is added to get the correct index
  * For example, if num = 2, then a number at index 4 is moved to index 2 (4 - num) and a number at index 1 is moved to index 9(1 - num + MAX_SIZE)
  * Another example, if at the start, arr_1 is {2,4,6,8,1,5},
  * calling arr_1 with num = 2 should change arr_1 to {6,8,1,5,2,4}
  */

void rotate(int num, int arr[MAX_SIZE]){
    int buffer[MAX_SIZE];
    int j = 0;

    //create a buffer array to store all the original values from arr.
    for(int i = 0; i < MAX_SIZE; i++){
        buffer[i] = arr[i];
    }
    //shift each index num times to the left. 
    for(int i = 0; i < MAX_SIZE; i++){
        arr[i] = buffer[i+num];
    }
    //fill back in the values we lost on the right side.
    for(int i = MAX_SIZE - num; i < MAX_SIZE; i++){
        arr[i] = buffer[j]; 
        j++;
    }
}

int main(){

    int i = 0;
    char *sep = "";
    // declare and initialize an int array arr_1 of size MAX_SIZE and initialize it with random values
    // For example, declare and initialize arr_1 to {1,2,3,4,5,6,7,8,9,10}
    int arr_1[MAX_SIZE] = {1,2,3,4,5,6,7,8,9,10};


    // This for statement prints the content of arr_1 to console
    for (i = 0; i < MAX_SIZE; i++) {
        printf("%d, ", arr_1[i]);
    }
    printf("\n");


    // call rotate() with num = 1

    rotate(1, arr_1);


    for (i = 0; i < MAX_SIZE; i++) {
        printf("%d, ", arr_1[i]);
    }
    printf("\n");
    // Outcome on console from the above for loop should be 2, 3, 4, 5, 6, 7, 8, 9, 10, 1


    // call rotate() with num = 2

    rotate(2, arr_1);


    for (i = 0; i < MAX_SIZE; i++) {
        printf("%d, ", arr_1[i]);
    }
    printf("\n");

}




#include <stdio.h>

int main()
{
    int a;
    int b;
    int *pp;

    a = 10;
    b = 20;

    printf("%d %d\n", a, b);

    pp = &a;
    *pp = 333;

    printf("%d %d\n", a, b);

    pp = &b;
    a = 444;
    b = 555;

    printf("%d %d\n", a, b);
    printf("%d\n", *pp);
    printf("%p\n", (void *)pp);
}

# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include <ctype.h>


int get_date(char *st);
int get_date_sscanf(char *st);
int get_date_dtend(char *st);


int main(int argc, char *argv[]){

        char *st1 = "asdrtgkl knbvhgfk2021udfhg (blgfdl) fdgllk";
        char *st2 = "DTEND:20210102T123000";
        char *st3 = "RRULE:FREQ=WEEKLY;WKST=MO;UNTIL=20210301T235959;BYDAY=SA";

        int num1 = get_date(st1);
        printf("number found. %d\n", num1);
        int num2 = get_date_sscanf(st1);
        printf("number found. %d\n", num2);
        int num3 = get_date_dtend(st1);
        printf("number found. %d\n", num3);
        printf("-------\n");

        num1 = get_date(st2);
        printf("number found. %d\n", num1);
        num2 = get_date_sscanf(st2);
        printf("number found. %d\n", num2);
        num3 = get_date_dtend(st2);
        printf("number found. %d\n", num3);
        printf("-------\n");

        num1 = get_date(st3);
        printf("number found. %d\n", num1);
        num2 = get_date_sscanf(st3);
        printf("number found. %d\n", num2);
        num3 = get_date_dtend(st3);
        printf("number found. %d\n", num3);
}

// COMPLETE IMPLEMENTATION OF FUNCTIONS BELOW.

int get_date(char *st){
        // Indexes through st, char by char, until it
        // encounters the first digit, and proceeds from there.

}

int get_date_sscanf(char *st){
        // Uses the sscanf function to find date in st.

}

int get_date_dtend(char *st) {
        // Use direct memory access and pointer arithmetic to find the date in st

}
#include <stdio.h>

void rotate(int *m, int *n, int *p, int *q)
{
    int temp;
    temp = *m;

    *m = *n;
    *n = *p;
    *p = *q;
    *q = temp;
}


int main(){
    int a = 111;
    int b = 222;
    int c = 333;
    int d = 444;

    printf("%d %d %d %d\n", a, b, c, d);

    rotate(&a, &b, &c, &d);
    printf("%d %d %d %d\n", a, b, c, d);

    rotate(&a, &b, &c, &d);
    printf("%d %d %d %d\n", a, b, c, d);
}
#include <stdio.h>

int main(int argc, char *argv[]) {
    printf("Howdy, world!\n");
}
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{

        // variable to store the final answer
        int factorial = 1;

        // WRITE YOUR CODE TO DO COMMAND LINE INPUT CHECKING HERE



        // Takes the command line input and converts it into int.
        num = atoi(argv[1]);


        // WRITE YOUR CODE TO DO THE FACTORIAL CALCULATIONS HERE


        printf("%f\n", factorial);
}
# include <stdio.h>
# include <stdlib.h>
# include <time.h>

int main(int argc, char* argv[]) {

	
	srand(time(NULL));
	for (int i = 1; i <= 10; i++) {
		int
		n = rand() % 10 + 1;
		printf("%d\n", n);
	}
}
#include <math.h>
#include <stdio.h>

int main()
{
    double a = 10.0;
    double b = 13.0;
    double c;

    c = sqrt(a * a + b * b);

    printf("Right triangle with sides %.2f and %.2f has "
        "hypotenuse of length %.2f\n", a, b, c);
}

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int expo(int a, int b){

        double c = pow(a,b);

        printf("Answer is %f\n", c);
        return c;

}

#include <stdio.h>

int expo(int a, int b);

int main() {

        int p = 10;
        int t = 4;

        expo(p,t);

}
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    double a;
    double b;
    double c;

    if (argc < 3) {
        printf("usage: %s <length> <length>\n", argv[0]);
        exit(1);
    }

    a = atof(argv[1]);
    b = atof(argv[2]);

    c = pythag(a, b);

    printf("Right triangle with sides %.2f and %.2f has "
        "hypotenuse of length %.2f\n", a, b, c);
}
#include <math.h>
#include <stdio.h>

double pythag(double a, double b)
{
    return sqrt(a * a + b * b);
}


int main()
{
    printf("Right triangle with sides %.2f and %.2f has "
        "hypotenuse of length %.2f\n",
        10.0, 13.0, pythag(10, 13));

    printf("Right triangle with sides %.2f and %.2f has "
        "hypotenuse of length %.2f\n",
        21.9, 31.2, pythag(21.9, 31.2));

    printf("Right triangle with sides %.2f and %.2f has "
        "hypotenuse of length %.2f\n",
        719.21, 21.2, pythag(719.21, 21.2));
}
#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"

void *emalloc(size_t n) {
    void *p; 

    p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

#define MAX_LINE_LEN 80


void inccounter(node_t *p, void *arg) {
    int *ip = (int *)arg;
    (*ip)++;
}


void print_node(node_t *p, void *arg) {
    char *fmt = (char *)arg;
    printf(fmt, p->op, p->val);

}


void analysis(node_t *l) {
    int len = 0;

    apply(l, inccounter, &len);    
    printf("Number of nodes: %d\n", len);

    apply(l, print_node, "%c:%d\n");
}


int main(int argc, char *argv[]) {
    char *line = NULL;
    char *t;
    int  num = 0;
    node_t *list = NULL;


    list = add_end(list, new_node('v', 100));
    list = add_end(list, new_node('v', 50));
    list = add_end(list, new_node('+', 0));
    list = add_end(list, new_node('v', 2));
    list = add_end(list, new_node('*', 0));
 
    analysis(list);
 
    exit(0); 
}
/*
 * linkedlist.c
 *
 * Based on the implementation approach described in "The Practice 
 * of Programming" by Kernighan and Pike (Addison-Wesley, 1999).
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"


node_t *new_node(char *val) {
    assert( val != NULL);

    node_t *temp = (node_t *)emalloc(sizeof(node_t));

    strncpy(temp->word, val, MAX_WORD_LEN);
    temp->next = NULL;

    return temp;
}


node_t *add_front(node_t *list, node_t *new) {
    new->next = list;
    return new;
}


node_t *add_end(node_t *list, node_t *new) {
    node_t *curr;

    if (list == NULL) {
        new->next = NULL;
        return new;
    }

    for (curr = list; curr->next != NULL; curr = curr->next);
    curr->next = new;
    new->next = NULL;
    return list;
}


node_t *peek_front(node_t *list) {
    return list;
}


node_t *remove_front(node_t *list) {
    if (list == NULL) {
        return NULL;
    }

    return list->next;
}



void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for ( ; list != NULL; list = list->next) {
        (*fn)(list, arg);
    }
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 20

int main(int argc, char *argv[]) {
    char *line = NULL;
    char *t;
    int  num = 0;

    if (argc < 2) {
        fprintf(stderr, "usage: %s <some string>\n", argv[0]);
        exit(1);
    }

    line = (char *)malloc(sizeof(char) * MAX_LEN);
    if (line == NULL) {
        fprintf(stderr,
            "Argh. Something bad happened with malloc. :-(\n");
    }

    strcpy(line, argv[1]);

    t = strtok(line, " ");
    while (t) {
        num++;
        printf("Word: %s\n", t);
        t = strtok(NULL, " ");
    }
  
    printf("Number of words: %d\n", num);
 
    exit(0); 
}
#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"

void *emalloc(size_t n) {
    void *p; 

    p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

#define MAX_LINE_LEN 80

void inccounter(node_t *p, void *arg) {
    int *ip = (int *)arg;
    (*ip)++;
}


void print_node(node_t *p, void *arg) {
    char *fmt = (char *)arg;
    printf(fmt, p->op, p->val);
}


void analysis(node_t *l) {
    int len = 0;

    apply(l, inccounter, &len);    
    printf("Number of nodes: %d\n", len);

    apply(l, print_node, "%c:%d\n");
}


int main(int argc, char *argv[]) {
    node_t *list = NULL;

    list = add_front(list, new_node('v', 100));
    list = add_front(list, new_node('v', 50));
    list = add_front(list, new_node('+', 0));
    list = add_front(list, new_node('v', 2));
    list = add_front(list, new_node('*', 0));
 
    analysis(list);

    exit(0); 
}
#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"

void *emalloc(size_t n) {
    void *p; 

    p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

#define MAX_LINE_LEN 80

void inccounter(node_t *p, void *arg) {
    int *ip = (int *)arg;
    (*ip)++;
}


void print_word(node_t *p, void *arg) {
    char *fmt = (char *)arg;
    printf(fmt, p->word);
}


void analysis(node_t *l) {
    int len = 0;

    apply(l, inccounter, &len);    
    printf("Number of words: %d\n", len);

    apply(l, print_word, "%s\n");
}


int main(int argc, char *argv[]) {
    char *line = NULL;
    char *t;
    int  num = 0;
    node_t *list = NULL;

    if (argc < 2) {
        fprintf(stderr, "usage: %s <some string>\n", argv[0]);
        exit(1);
    }

    line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    if (line == NULL) {
        fprintf(stderr,
            "Argh. Something bad happened with malloc. :-(\n");
    }

    strcpy(line, argv[1]);

    t = strtok(line, " ");
    while (t) {
        num++;
        list = add_end(list, new_node(t)); 
        t = strtok(NULL, " ");
    }
 
    analysis(list);

/*
    node_t  *temp_n = NULL;
    for ( ; list != NULL; list = temp_n ) {
        temp_n = list->next;
        free(list);
    } 

    free(line);
*/
 
    exit(0); 
}
/*
 * linkedlist.c
 *
 * Based on the implementation approach described in "The Practice 
 * of Programming" by Kernighan and Pike (Addison-Wesley, 1999).
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"


node_t *new_node(char *val) {
    assert( val != NULL);

    node_t *temp = (node_t *)emalloc(sizeof(node_t));

    strncpy(temp->word, val, MAX_WORD_LEN);
    temp->next = NULL;

    return temp;
}


node_t *add_front(node_t *list, node_t *new) {
    new->next = list;
    return new;
}


node_t *add_end(node_t *list, node_t *new) {
    node_t *curr;

    if (list == NULL) {
        new->next = NULL;
        return new;
    }

    for (curr = list; curr->next != NULL; curr = curr->next);
    curr->next = new;
    new->next = NULL;
    return list;
}


node_t *peek_front(node_t *list) {
    return list;
}


node_t *remove_front(node_t *list) {
    if (list == NULL) {
        return NULL;
    }

    return list->next;
}



void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for ( ; list != NULL; list = list->next) {
        (*fn)(list, arg);
    }
}
#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"

void *emalloc(size_t n) {
    void *p; 

    p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

#define MAX_LINE_LEN 80

void inccounter(node_t *p, void *arg) {
    int *ip = (int *)arg;
    (*ip)++;
}


void print_node(node_t *p, void *arg) {
    char *fmt = (char *)arg;
    printf(fmt, p->op, p->val);
}


void analysis(node_t *l) {
    int len = 0;

    apply(l, inccounter, &len);    
    printf("Number of nodes: %d\n", len);

    apply(l, print_node, "%c:%d\n");
}


int main(int argc, char *argv[]) {
    node_t *list = NULL;

    list = add_front(list, new_node('v', 100));
    list = add_front(list, new_node('v', 50));
    list = add_front(list, new_node('+', 0));
    list = add_front(list, new_node('v', 2));
    list = add_front(list, new_node('*', 0));
 
    analysis(list);

    node_t *temp_n = NULL;

    for ( ; list != NULL; list = temp_n ) {
        temp_n = list->next;
        free(list);
    } 

    free(list);

    exit(0); 
}
/*
 * linkedlist.c
 *
 * Based on the implementation approach described in "The Practice 
 * of Programming" by Kernighan and Pike (Addison-Wesley, 1999).
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"


node_t *new_node(char op, int val) {
    node_t *temp = (node_t *)malloc(sizeof(node_t));

    assert(temp != NULL);  /* If this goes wrong, stop the train. */

    temp->op = op;
    temp->val = val;
    temp->next = NULL;

    return temp;
}


node_t *add_front(node_t *list, node_t *new) {
    new->next = list;
    return new;
}


node_t *add_end(node_t *list, node_t *new) {
    node_t *curr;

    if (list == NULL) {
        new->next = NULL;
        return new;
    }

    for (curr = list; curr->next != NULL; curr = curr->next);
    curr->next = new;
    new->next = NULL;
    return list;
}


node_t *peek_front(node_t *list) {
    return list;
}


node_t *remove_front(node_t *list) {
    if (list == NULL) {
        return NULL;
    }

    return list->next;
}



void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for ( ; list != NULL; list = list->next) {
        (*fn)(list, arg);
    }
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "list.h"

#define MAX_LINE_LEN 80

void inccounter(node_t *p, void *arg);
void print_node(node_t *p, void *arg);
void analysis(node_t *l);

int main(int argc, char *argv[]) {

/* 
 * Note that the expression in the example above is a postfix expression. 
 * 23 15 - 10 * is the same as (23-15)*10.
 * In part 2, you will use the linkedlist that you created, to evaluate the expression
 * and print the final result. 
 * You will need to use a linked list like a stack, in order to evaluate the expression.
 * If you do not know how to evaluate the expression using a stack, ask your lab instructor,
 * who can give you a demonstration. 
 * Try the following expressions
 *              '31 21 + 2 * 9 -'       : Answer should be 95
 *              '23 18 + 89 * 2 -'      : Answer should be 3647
 *              '100 10 20 3 * + + 5 /' : Answer should be 34 
 *
 * REMEMBER TO FREE DYNAMIC MEMORY WHERE APPROPRIATE.
 * You will need to modify the make file if you want to use it to compile this program.
 * You may use some of your code from q_expression.c 
 */

    if (argc != 2) {
        fprintf(stderr, "usage: %s <some string>\n", argv[0]);
        exit(1);
    }

    // COMPLETE IMPLEMENTATION

    exit(0); 
}

void inccounter(node_t *p, void *arg) {
    int *ip = (int *)arg;
    (*ip)++;
}


void print_node(node_t *p, void *arg) {
    char *fmt = (char *)arg;
    printf(fmt, p->op, p->val);
}


void analysis(node_t *l) {
    int len = 0;

    apply(l, inccounter, &len);    
    printf("Number of nodes: %d\n", len);

    apply(l, print_node, "%c:%d\n");
}
#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"

void *emalloc(size_t n) {
    void *p; 

    p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}
/*
 * linkedlist.c
 *
 * Based on the implementation approach described in "The Practice 
 * of Programming" by Kernighan and Pike (Addison-Wesley, 1999).
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"


node_t *new_node(char op, int val) {
    node_t *temp = (node_t *)malloc(sizeof(node_t));

    assert(temp != NULL);  /* If this goes wrong, stop the train. */

    temp->op = op;
    temp->val = val;
    temp->next = NULL;

    return temp;
}


node_t *add_front(node_t *list, node_t *new) {
    new->next = list;
    return new;
}


node_t *add_end(node_t *list, node_t *new) {
    node_t *curr;

    if (list == NULL) {
        new->next = NULL;
        return new;
    }

    for (curr = list; curr->next != NULL; curr = curr->next);
    curr->next = new;
    new->next = NULL;
    return list;
}


node_t *peek_front(node_t *list) {
    return list;
}


node_t *remove_front(node_t *list) {
    if (list == NULL) {
        return NULL;
    }

    return list->next;
}



void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for ( ; list != NULL; list = list->next) {
        (*fn)(list, arg);
    }
}
#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"

void *emalloc(size_t n) {
    void *p; 

    p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

#define MAX_LINE_LEN 80

void inccounter(node_t *p, void *arg) {
    int *ip = (int *)arg;
    (*ip)++;
}


void print_word(node_t *p, void *arg) {
    char *fmt = (char *)arg;
    printf(fmt, p->word);
}


void analysis(node_t *l) {
    int len = 0;

    apply(l, inccounter, &len);    
    printf("Number of words: %d\n", len);

    apply(l, print_word, "%s\n");
}


int main(int argc, char *argv[]) {
    char *line = NULL;
    char *t;
    int  num = 0;
    node_t *list = NULL;

    if (argc < 2) {
        fprintf(stderr, "usage: %s <some string>\n", argv[0]);
        exit(1);
    }

    line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    if (line == NULL) {
        fprintf(stderr,
            "Argh. Something bad happened with malloc. :-(\n");
    }

    strcpy(line, argv[1]);

    t = strtok(line, " ");
    while (t) {
        num++;
        list = add_end(list, new_node(t)); 
        t = strtok(NULL, " ");
    }
 
    analysis(list);
 
    exit(0); 
}
/*
 * linkedlist.c
 *
 * Based on the implementation approach described in "The Practice 
 * of Programming" by Kernighan and Pike (Addison-Wesley, 1999).
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"


node_t *new_node(char *val) {
    assert( val != NULL);

    node_t *temp = (node_t *)emalloc(sizeof(node_t));

    strncpy(temp->word, val, MAX_WORD_LEN);
    temp->next = NULL;

    return temp;
}


node_t *add_front(node_t *list, node_t *new) {
    new->next = list;
    return new;
}


node_t *add_end(node_t *list, node_t *new) {
    node_t *curr;

    if (list == NULL) {
        new->next = NULL;
        return new;
    }

    for (curr = list; curr->next != NULL; curr = curr->next);
    curr->next = new;
    new->next = NULL;
    return list;
}


node_t *peek_front(node_t *list) {
    return list;
}


node_t *remove_front(node_t *list) {
    if (list == NULL) {
        return NULL;
    }

    return list->next;
}



void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for ( ; list != NULL; list = list->next) {
        (*fn)(list, arg);
    }
}
/*
 * linkedlist.c
 *
 * Based on the implementation approach described in "The Practice 
 * of Programming" by Kernighan and Pike (Addison-Wesley, 1999).
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"


node_t *new_node(char op, int val) {
    node_t *temp = (node_t *)malloc(sizeof(node_t));

    assert(temp != NULL);  /* If this goes wrong, stop the train. */

    temp->op = op;
    temp->val = val;
    temp->next = NULL;

    return temp;
}


node_t *add_front(node_t *list, node_t *new) {
    new->next = list;
    return new;
}


node_t *add_end(node_t *list, node_t *new) {
    node_t *curr;

    if (list == NULL) {
        new->next = NULL;
        return new;
    }

    for (curr = list; curr->next != NULL; curr = curr->next);
    curr->next = new;
    new->next = NULL;
    return list;
}


node_t *peek_front(node_t *list) {
    return list;
}


node_t *remove_front(node_t *list) {
    if (list == NULL) {
        return NULL;
    }

    return list->next;
}



void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for ( ; list != NULL; list = list->next) {
        (*fn)(list, arg);
    }
}
#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"

void *emalloc(size_t n) {
    void *p; 

    p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "list.h"

#define MAX_LINE_LEN 80

void inccounter(node_t *p, void *arg);
void print_node(node_t *p, void *arg);
void analysis(node_t *l);

int main(int argc, char *argv[]) {

    /*
    while(token){
        if(isdigit(token)){
            list = add_front(list, new_node('v', atoi(token)));
            printf("token: %s\n", token);
            token = strtok(NULL, " ");
        }else{
            list = add_front(list, new_node(atoi(token), 0));
            printf("token: %s\n", token);
            token = strtok(NULL, " ");
        }
    }
    */

/* 
 * Program when run will take an expression from the command line 
 * and store it in a linked list. For example:
 *    ./q_expression '23 15 - 10 *' 
 * will store data into 5 nodes.  (Notice the use of strong quotes
 * for the argument provided to q_expression.)
 *
 *      Node 1: op:"v", val:23 (This is the head node; next is node 2)
 *      Node 2: op:"v", val:15 (next is node 3)
 *      Node 3: op:"-", val:0  (next is node 4)
 *      Node 4: op:"v", val:10 (next is node 5)
 *      Node 5: op:"*", val:0  (as this is the tail node, next is null)
 *
 * Note that when the item is a number, it is stored in val 
 * with the op as "v" and when the item is a mathematical operation 
 * (*, -, +, /), it is stores in op with the val as 0 .
 *
 * REMEMBER TO FREE DYNAMIC MEMORY WHERE APPROPRIATE.
 */

    if (argc != 2) {
        fprintf(stderr, "usage: %s <some string>\n", argv[0]);
        exit(1);
    }

    /* COMPLETE IMPLEMENTATION BELOW. */

    /*The user enters a string like "23 19 3 + -" which is argv[1] 
     * then we get a char*  with the elements 23, 19, 3, +, -
     */
    node_t *list = NULL;
    char s[100];
    strcpy(s, argv[1]);
    printf("%s\n", s);
    char* token = strtok(s, " ");

    /*while token != NULL 
     * create a new node with data fields val and op - 
     * add it to a linked list
     *
     * */
    while(token){
        list = add_front(list, new_node("v", atoi(token)));
        token = strtok(NULL, " ");
    }
    analysis(list);


    /*Free the memory we used from emalloc when we created the nodes*/

    node_t *temp_n = NULL;
    for ( ; list != NULL; list = temp_n ) {
        temp_n = list->next;
        free(list);
    } 
    free(list);


    exit(0); 
}


void inccounter(node_t *p, void *arg) {
    int *ip = (int *)arg;
    (*ip)++;
}


void print_node(node_t *p, void *arg) {
    char *fmt = (char *)arg;
    printf(fmt, p->op, p->val);
}


void analysis(node_t *l) {
    int len = 0;

    apply(l, inccounter, &len);    
    printf("Number of nodes: %d\n", len);

    apply(l, print_node, "%c:%d\n");
}
/*
 * linkedlist.c
 *
 * Based on the implementation approach described in "The Practice 
 * of Programming" by Kernighan and Pike (Addison-Wesley, 1999).
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"


node_t *new_node(char* op, int val) {
    node_t *temp = (node_t *)malloc(sizeof(node_t));

    assert(temp != NULL);  /* If this goes wrong, stop the train. */

    temp->op = op;
    temp->val = val;
    temp->next = NULL;

    return temp;
}


node_t *add_front(node_t *list, node_t *new) {
    new->next = list;
    return new;
}


node_t *add_end(node_t *list, node_t *new) {
    node_t *curr;

    if (list == NULL) {
        new->next = NULL;
        return new;
    }

    for (curr = list; curr->next != NULL; curr = curr->next);
    curr->next = new;
    new->next = NULL;
    return list;
}


node_t *peek_front(node_t *list) {
    return list;
}


node_t *remove_front(node_t *list) {
    if (list == NULL) {
        return NULL;
    }

    return list->next;
}



void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for ( ; list != NULL; list = list->next) {
        (*fn)(list, arg);
    }
}
#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"

void *emalloc(size_t n) {
    void *p; 

    p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

#define MAX_LINE_LEN 80

void inccounter(node_t *p, void *arg) {
    int *ip = (int *)arg;
    (*ip)++;
}


void print_word(node_t *p, void *arg) {
    char *fmt = (char *)arg;
    printf(fmt, p->word);
}


void analysis(node_t *l) {
    int len = 0;

    apply(l, inccounter, &len);    
    printf("Number of words: %d\n", len);

    apply(l, print_word, "%s\n");
}


int main(int argc, char *argv[]) {
    char *line = NULL;
    char *t;
    int  num = 0;
    node_t *list = NULL;

    if (argc < 2) {
        fprintf(stderr, "usage: %s <some string>\n", argv[0]);
        exit(1);
    }

    line = (char *)malloc(sizeof(char) * MAX_LINE_LEN);
    if (line == NULL) {
        fprintf(stderr,
            "Argh. Something bad happened with malloc. :-(\n");
    }

    strcpy(line, argv[1]);

    t = strtok(line, " ");
    while (t) {
        num++;
        list = add_inorder(list, new_node(t)); 
        t = strtok(NULL, " ");
    }
 
    analysis(list);

    node_t  *temp_n = NULL;
    for ( ; list != NULL; list = temp_n ) {
        temp_n = list->next;
        free(list->word);
        free(list);
    } 

    free(line);
 
    exit(0); 
}
/*
 * linkedlist.c
 *
 * Based on the implementation approach described in "The Practice 
 * of Programming" by Kernighan and Pike (Addison-Wesley, 1999).
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"


node_t *new_node(char *val) {
    assert( val != NULL);

    node_t *temp = (node_t *)emalloc(sizeof(node_t));

    temp->word = strdup(val);
    temp->next = NULL;

    return temp;
}


node_t *add_front(node_t *list, node_t *new) {
    new->next = list;
    return new;
}


node_t *add_end(node_t *list, node_t *new) {
    node_t *curr;

    if (list == NULL) {
        new->next = NULL;
        return new;
    }

    for (curr = list; curr->next != NULL; curr = curr->next);
    curr->next = new;
    new->next = NULL;
    return list;
}


node_t *add_inorder(node_t * list, node_t *new) {
    node_t *prev = NULL;
    node_t *curr = NULL;

    if (list == NULL) {
        return new;
    }

    for (curr = list; curr != NULL; curr = curr->next) {
        if (strcmp(new->word, curr->word) > 0) {
            prev = curr;
        } else {
            break;
        }
    }

    new->next = curr;

    if (prev == NULL) {
        return (new);
    } else {
        prev->next = new;
        return list;
    }
}


node_t *peek_front(node_t *list) {
    return list;
}


node_t *remove_front(node_t *list) {
    if (list == NULL) {
        return NULL;
    }

    return list->next;
}



void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for ( ; list != NULL; list = list->next) {
        (*fn)(list, arg);
    }
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NUMS 10

int comparator(const void *a, const void *b) {
    long l_a = *(long *)a;
    long l_b = *(long *)b;

    /* if l_a < l_b, then a negative integer is to be returned.
     * if l_a > l_b, then a positive integer is to be returned.
     * if l_a == l_b, then zero is to be returned.
     */
    return (l_a - l_b);  /* There *could* be a subtle bug here... */
}


int main(int argc, char *argv[]) {
    long numbers[MAX_NUMS];
    int i;

    if (argc < 2) {
        fprintf(stderr, "usage: %s <some seed value>\n", argv[0]);
        exit(1);
    }

    srandom(atoi(argv[1]));

    printf("BEFORE qsort:\n------------\n");
    for (i = 0; i <MAX_NUMS; i++) {
        numbers[i] = random();
        printf("%12ld\n", numbers[i]);
    } 

    printf("\n");
    qsort(numbers, MAX_NUMS, sizeof(long), comparator);

    printf("AFTER qsort:\n------------\n");
    for (i = 0; i < MAX_NUMS; i++) {
        printf("%12ld\n", numbers[i]);
    }
    printf("\n");

    printf("Address of 'comparator' function: %lx\n",
        (unsigned long)comparator);
    printf("Address of 'numbers' array %lx\n",
        (unsigned long)numbers);
 
    exit(0); 
}
#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"

void *emalloc(size_t n) {
    void *p; 

    p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"

#define MAX_NUMS 1000
#define MAX_LINE_LEN 50


/* Recall: if item represented by `a` comes before the
 * item represented by `b`, then a negative value is returned;
 * if `a` comes after `b`, then a positive value is returned;
 * otherwise 0 is return. Also: 1 and -1 are suitable negative
 * and positive values.
 */
int compare_two_doubles(const void *a, const void *b) {
    /* ?? */

    return 0;
}

int main(int argc, char *argv[]) {
    double *data;
    int     i;
    int     nums;
    double  temp;
    char    line[MAX_LINE_LEN];

    data = NULL; /* ?? */

    nums = 0;
    while (fgets(line, MAX_LINE_LEN, stdin)) {
        temp = atof(line);
        data[nums] = temp;
        nums++;

        if (nums == MAX_NUMS) {
            break;
        }
    }

    printf("BEFORE qsort:\n------------\n");
    for (i = 0; i <nums; i++) {
        printf("%12.8f\n", data[i]);
    } 

    printf("\n");
    /* 
    qsort(data, ...? );
     */

    printf("AFTER qsort:\n------------\n");
    for (i = 0; i < nums; i++) {
        printf("%12.8f\n", data[i]);
    }

    /* Deallocated memory referred to by `data`? */

    exit(0); 
}
#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"

void *emalloc(size_t n) {
    void *p; 

    p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"

#define MAX_LINE_LEN 80

void inccounter(node_t *p, void *arg) {
    int *ip = (int *)arg;
    (*ip)++;
}


void print_word(node_t *p, void *arg) {
    char *fmt = (char *)arg;
    printf(fmt, p->name, p->birth_year);
}


void analysis(node_t *l) {
    int len = 0;

    apply(l, inccounter, &len);    
    printf("Number of actors: %d\n", len);

    apply(l, print_word, "%s (born %d)\n");
}


int main(int argc, char *argv[]) {
    node_t *list = NULL;
/*
    list = add_end(list, new_node("Bishop, John", 1966));
    list = add_end(list, new_node("Cusack, John", 1966));
    list = add_end(list, new_node("Rhys-Davies, John", 1944));
    list = add_end(list, new_node("Depp, Johnny", 1963));
*/   

    list = add_inorder(list, new_node("Bishop, John", 1966));
    list = add_inorder(list, new_node("Cusack, John", 1966));
    list = add_inorder(list, new_node("Rhys-Davies, John", 1944));
    list = add_inorder(list, new_node("Depp, Johnny", 1963));
    list = add_inorder(list, new_node("Wayne, John", 1907));
    list = add_inorder(list, new_node("Malkovich, John", 1953));
    list = add_inorder(list, new_node("Oliver, John", 1977));
    list = add_inorder(list, new_node("Higgins, John Michael", 1966));
    list = add_inorder(list, new_node("Glover, John", 1944));
    peek_front(list); 

    analysis(list);

    node_t  *temp_n = NULL;
    for ( ; list != NULL; list = temp_n ) {
        temp_n = list->next;
        free(list->name);
        free(list);
    } 
 
    exit(0); 
}
/*
 * linkedlist.c
 *
 * Based on the implementation approach described in "The Practice 
 * of Programming" by Kernighan and Pike (Addison-Wesley, 1999).
 */

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"
#include "list.h"


node_t *new_node(char *name, int birth_year) {
    assert( name != NULL);

    node_t *temp = (node_t *)emalloc(sizeof(node_t));

    temp->name       = strdup(name);
    temp->birth_year = birth_year;
    temp->next       = NULL;

    return temp;
}


node_t *add_front(node_t *list, node_t *new) {
    new->next = list;
    return new;
}


node_t *add_end(node_t *list, node_t *new) {
    node_t *curr;

    if (list == NULL) {
        new->next = NULL;
        return new;
    }

    for (curr = list; curr->next != NULL; curr = curr->next);
    curr->next = new;
    new->next = NULL;
    return list;
}


node_t *add_inorder(node_t * list, node_t *new) {
    node_t *prev = NULL;
    node_t *curr = NULL;

    if (list == NULL) {
        return new;
    }
    
    for (curr = list; curr != NULL; curr = curr->next) {

        if (new->birth_year > curr->birth_year) {
            prev = curr;
        } else {
            break;
        }
    }

    new->next = curr;

    if (prev == NULL) {
        return (new);
    } else {
        prev->next = new;
        return list;
    }
}


node_t *peek_front(node_t *list) {
    return list;
}


node_t *remove_front(node_t *list) {
    if (list == NULL) {
        return NULL;
    }

    return list->next;
}


void apply(node_t *list,
           void (*fn)(node_t *list, void *),
           void *arg)
{
    for ( ; list != NULL; list = list->next) {
        (*fn)(list, arg);
    }
}
#include <stdlib.h>
#include <stdio.h>
#include "emalloc.h"

void *emalloc(size_t n) {
    void *p; 

    p = malloc(n);
    if (p == NULL) {
        fprintf(stderr, "malloc of %zu bytes failed", n); 
        exit(1);
    }   

    return p;
}
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "emalloc.h"

#define MAX_WORDS 10

int comparator(const void *a, const void *b) {
    char *c_a = *(char **)a;
    char *c_b = *(char **)b;

    return (strcmp(c_a, c_b));
}

int main(int argc, char *argv[]) {
    char *line;
    char **words;
    char *t;
    int  num;
    int  i;

    if (argc < 2) {
        fprintf(stderr, "usage: %s <some string>\n", argv[0]);
        exit(1);
    }

    line = strdup(argv[1]);
    words = (char **)emalloc(sizeof(char *) * MAX_WORDS);

    num = 0; 
    t = strtok(line, " ");
    while (t && num < MAX_WORDS) {
        words[num] = strdup(t);
        t = strtok(NULL, " ");
        num++;
    }

    printf("BEFORE qsort:\n------------\n");
    for (i = 0; i < num; i++) {
        printf("%2d:%s\n", i, words[i]);
    }

    printf("\n");
    qsort(words, num, sizeof(char *), comparator);

    printf("AFTER qsort:\n------------\n");
    for (i = 0; i < num; i++) {
        printf("%2d:%s\n", i, words[i]);
    }

    for (i = 0; i < num; i++) {
        free(words[i]);
    }
    free(words);
    free(line);
 
    exit(0); 
}
