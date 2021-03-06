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
int find_mid_node(Node *head);
void print_reverse(Node *head);

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

    printf("\n__Mid data__: : %d\n\n",find_mid_node(head)); // we just have to print mid not modify head

    print(head);
    printf("_________Link List Traversal Reverse________\n NULL");
    print_reverse(head);
    printf(" <- head\n\n\n");

    deleteFromBeginning(&head);
    deleteFromBeginning(&head);
    print(head);

    deleteFromEnd(&head);
    deleteFromEnd(&head);
    print(head);


    return 0;
}


Node *createNode(int data){
    Node *node = (Node *) calloc(1,sizeof(Node));
    //check error inn memory allocation
    if(node == NULL){
        printf("Memory Allocation Error\n");
        return NULL;
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

int find_mid_node(Node *head){
    Node *ptr1 = head;
    Node *ptr2 = head;
    //move ptr1 with speed 1 and ptr2 with speed 2
    //then when ptr2 read to the end ptr1 will be at mid
    while(ptr2->next != NULL && ptr2->next->next !=NULL){
      ptr2 = ptr2->next->next;
      ptr1 = ptr1->next;
    }
  return ptr1->data;
}


void print_reverse(Node *head){
    Node *ptr = head;
    if(ptr == NULL){
        return;
    }
    else{
        print_reverse(ptr->next);
        printf("<- %d",ptr->data);
    }
}