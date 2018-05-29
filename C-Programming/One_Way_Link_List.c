#include<stdio.h>
#include<stdlib.h>


struct Node{
    int data;
    struct Node *next;
};
typedef struct Node Node;
// You can reassign name using typedef  also

Node *createNode(int data);
void insertAtBeginning(Node **head ,int data);
void print(Node *head);

int main(){
    Node *head = NULL;

    //insert function
    insertAtBeginning(&head,3);
    insertAtBeginning(&head,2);
    insertAtBeginning(&head,1);
    print(head);

    return 0;
}


Node * createNode(int data){
    Node *node = (Node *) calloc(1,sizeof(Node));
    //check error inn memory allocation
    if(node == NULL){
        printf("Memory Allocation Error\n");
        return;
    }

    node->data = data;
    node->next = NULL;
    return node;
}

void insertAtBeginning(Node **head ,int data){
    //insert at beginning of link list
    Node *node;

    node = createNode(data);
    if(node != NULL){
        node->next = *head;
        *head = node;
    }
}

void print(Node *head){
    Node *ptr =head;
    printf("_________Link List Traversal________\n  head");
    while(ptr != NULL){
    printf("-> %d",ptr->data);
    ptr = ptr->next;
    }
    printf("->NULL\n");
}