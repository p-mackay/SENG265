
#include <stdio.h>
#include <stdlib.h>

typedef int Key;
typedef struct {
    Key k;
} Item;
typedef Item* ItemRef;

typedef struct NodeStruct* NodeRef;
typedef struct NodeStruct{
    NodeRef next;
    ItemRef item;
}Node;

ItemRef createItem(Key val){
    ItemRef ip = (ItemRef)malloc(sizeof(Item));

    ip->k = val;
    return ip;
}

NodeRef createNode(Key val){
    NodeRef np = (NodeRef)malloc(sizeof(Node));

    np->next = NULL;
    np->item = createItem(val);
    return np;
}

void printListFW(NodeRef xp){
    while(xp != NULL){
        printf("Node: %d\n", xp->item->k);
        xp = xp->next;
    }
}

void printListFWPlus(NodeRef xp){
    while(xp != NULL){
        printf("Node: %d\n", xp->item->k += 10);
        xp = xp->next;
    }
}


int main(void){
    printf("malloc example\n");
    NodeRef n5 = createNode(5);
    NodeRef n7 = createNode(7);
    NodeRef n9 = createNode(9);
    NodeRef head = n5;
    n5->next = n7;
    n7->next = n9;
    printListFWPlus(head);
    return EXIT_SUCCESS;
}
