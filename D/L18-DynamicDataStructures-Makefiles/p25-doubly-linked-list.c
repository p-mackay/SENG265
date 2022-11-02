#include <stdio.h>
#include <stdlib.h>

typedef int Info;
typedef struct{
        Info info;
}Item;
typedef Item* ItemRef;

typedef struct NodeStruct* NodeRef;
typedef struct NodeStruct{
    ItemRef item;
    NodeRef next;
    NodeRef prev;
}Node;
