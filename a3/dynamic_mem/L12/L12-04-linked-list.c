/*
Paul MacKay - 18/03/2022 - dynamic memory - SENG 265 
"head pointer" points to first element

 */
#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int value;
    struct Node* next;
} Node;

typedef struct{
    Node* head;
} LinkedList;

int sum_elements(LinkedList* L){
    int sum = 0;

    for(Node* current_node = L->head; current_node != NULL; current_node = current_node->next){
        sum = sum + current_node->value;
    }

    return sum;
}

int count_elements(LinkedList* L){
    int count = 0;
    Node* current_node = L->head;
    while(current_node != NULL){
        count++;
        current_node = current_node->next;
    }

    return count;
}

void print_list(LinkedList* L){
    Node* current_node = L->head;
    while(current_node != NULL){
        printf("%d ", current_node->value);
        current_node = current_node->next;
    }
    printf("\n");
}

void add_to_front(LinkedList* L, int new_element){
    if (L->head == NULL){
        //adding the first element to an empty list
        
        //Create a new node
        Node* new_node = malloc(sizeof(Node));
        //set the value of the new node to new_element
        new_node->value = new_element;
        //set the next pointer of the new node to NULL
        new_node->next = NULL;
        //set the head pointer of the list to point to the new node
        L->head = new_node;
    }else{
        //adding an element before an existin node
        Node* new_node = malloc(sizeof(Node));
        //set the value of the new node to new_element
        new_node->value = new_element;
        //set the next pointer of the new node to the first node in the list
        new_node->next = L->head;
        //set the head pointer of the list to point to the new node
        L->head = new_node;
    }
}

void add_to_end(LinkedList* L, int new_element){
    if(L->head == NULL){
        //Adding to the end of an empty list is the same
        //as adding to the front
        add_to_front(L, new_element);
    }else{
        //Adding an element after the existing contents
        //of a non-empty list
        Node* old_last_node = L->head; 
        while(old_last_node->next != NULL){
            old_last_node = old_last_node->next;
        }

        //Create 
        //adding an element before an existin node
        Node* new_node = malloc(sizeof(Node));
        //set the value of the new node to new_element
        new_node->value = new_element;
        //Set the next pointer of the new node to NULL
        new_node->next = NULL;
        //Set the next pointer of the old last node
        //to point at the new node
        old_last_node->next = new_node;
    }

}

int delete_first(LinkedList* L){
    //TO DO: Check if the list is already empty and print an error
    //       message and exit the program if so.
    Node* delete_node = L->head;
    L->head = delete_node->next;
    delete_node->next = NULL; //Optional

    int return_value = delete_node->value;
    free(delete_node);
    return return_value;
}

int main(){

    LinkedList L1;
    L1.head = NULL;

    LinkedList L2;
    L2.head = NULL;

    add_to_front(&L1, 6);
    add_to_front(&L1, 10);
    add_to_front(&L1, 17);

    add_to_end(&L1, 100);
    add_to_end(&L1, 200);

    for(int i = 0; i < 10; i++){
        add_to_end(&L2, i*i);
    }

    printf("Number of elements in L2: %d \n", count_elements(&L2));
    printf("Sum of elements in L2: %d \n", sum_elements(&L2));

    print_list(&L1);
    print_list(&L2);

    delete_first(&L1);
    print_list(&L1);
    delete_first(&L1);
    print_list(&L1);

    //Now delete every node in the list
    //(to ensure that free() is called for each
    //allocated node)

    while(L1.head != NULL){
        delete_first(&L1);
    }
    while(L2.head != NULL){
        delete_first(&L2);
    }



    return 0;
}
