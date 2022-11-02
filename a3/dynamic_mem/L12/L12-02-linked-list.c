/*
Paul MacKay - 18/03/2022 - dynamic memory - SENG 265 
"head pointer" points to first element

 */
#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int element;
    struct Node* next;
} Node;


int main(){
    Node node1;
    Node node2;
    Node node3;

    node1.element = 6;
    node1.next = &node3;

    node2.element = 10;
    node2.next = &node1;

    node3.element = 17;
    node3.next = NULL;
    
    Node* head = &node2; 

    printf("First element: %d\n", head->element);

    printf("Second element: %d\n", head->next->element);

    //initial condition
    Node* current_node = head;
    int i = 1;
    
    while(current_node != NULL){
        printf("Element %d: %d\n", i, current_node->element);
        current_node = current_node->next;
        i++;
    }

    i = 1;
    current_node = head;
    node2.next = &node3;

    while(current_node != NULL){
        printf("Element %d: %d\n", i, current_node->element);
        current_node = current_node->next;
        i++;
    }

    return 0;
}
