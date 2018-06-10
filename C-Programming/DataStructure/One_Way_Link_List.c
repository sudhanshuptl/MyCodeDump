/* Sudhanshu Patel -sudhanshuptl13@gmail.com */
#include<stdio.h>
#include<stdlib.h>


struct Node{
    int data;
    struct Node *next;
};
typedef struct Node Node;
// You can reassign name using typedef  also

//declaring prototype of function i gonna declare
Node *createNode(int data);
void insertAtBeginning(Node **head ,int data);
void print(Node *head);
void insertAtEnd(Node **head, int data);
void insertAtPosition(Node **head,int data,int position);
void deleteFromBeginning(Node **head);
void deleteFromEnd(Node **head);

int main(){
    Node *head = NULL;

    //insert function
    insertAtBeginning(&head,3);
    insertAtBeginning(&head,2);
    insertAtBeginning(&head,1);
    print(head);

    insertAtEnd(&head,6);
    insertAtEnd(&head,7);
    print(head);

    insertAtPosition(&head,4,4);
    insertAtPosition(&head,5,5);
    print(head);

    deleteFromBeginning(&head);
    deleteFromBeginning(&head);
    print(head);

    deleteFromEnd(&head);
    deleteFromEnd(&head);
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

void insertAtEnd(Node **head, int data){

    Node *ptr=*head;
    Node *node = createNode(data); // create a new node

    if(node == NULL){
        printf("Memory Allocation Error\n");
        return;
    }
    //if list is empty insert as first node
    if(*head == NULL){
        //Since head is already double pointer so just passing value of head means
        // sending address of single pointer of head
        insertAtBeginning(head, data);
        return;
    }

    //go to last node
    while(ptr->next != NULL){
        ptr = ptr->next;
    }

    //now insert new node after ptr
    ptr->next = node;
    node->next = NULL;
}

void insertAtPosition(Node **head,int data,int position){
    Node *ptr = *head ;
    int count = 1;
    // *node because it receive address of a new node
    Node *node = createNode(data);
    if(node == NULL){
        printf("Memory Allocation Error\n");
        return;
    }

    //if list is empty insert at beginning
    if(*head == NULL){
        //Since head is already double pointer so just passing value of head means
        // sending address of single pointer of head
        insertAtBeginning(head, data);
        return;
    }

    // move pointer to position -1
    //if position not available insert at end
    while(ptr->next != NULL && count < position-1){
        ptr = ptr->next;
        count++;
    }
    // now insert after ptr
    node->next = ptr->next;
    ptr->next = node;

}

void deleteFromBeginning(Node **head){

    Node *node = *head;
    // move head to next and free node
    //check if list is empty
    if(*head == NULL ){
        printf("List is Empty!\n");
        return;
    }

    *head = node->next;
    free(node);
}

void deleteFromEnd(Node **head){
    Node *ptr = *head;
    Node *last_node;

    //check if list is empty
    if(*head == NULL ){
        printf("List is Empty!\n");
        return;
    }


    // If only one node
    if(ptr->next == NULL){
        *head = NULL;
        free(ptr);
        return;
    }

    //find second last node
    while(ptr->next->next != NULL){
        ptr = ptr->next;
    }

    last_node = ptr->next;
    ptr->next = NULL;
    free(last_node);

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