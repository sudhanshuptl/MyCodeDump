#include<stdio.h>
#include<stdlib.h>
#define SIZE 10

void push(int stack[],int *top, int data);
int pop(int stack[],int *top);
void print_stack(int stack[],int top);

int main(){
 int stack[SIZE];
 int top=-1;
 int option,data;

 while(1){
    printf("\ntype 1 to insert and 2 to remove :");
    scanf("%d",&option);
    switch(option){
        case 1:
            printf("Input data :");
            scanf("%d",&data);
            push(stack,&top,data);
            print_stack(stack,top);
            break;
        case 2:
            printf("\npoped data : %d\n",pop(stack,&top));
            print_stack(stack,top);
            break;
        default:
        	print_stack(stack,top);
            break;
    }
   
 }
  return 0;
}

void push(int stack[],int *top, int data){
    if((*top+1)<SIZE){
        *top=*top+1;
        stack[*top]=data;
    }
    else{
        printf("\n Stack is full , Insertion  failed");
    }
}
int pop(int stack[],int *top){
 int data;
 if(*top<0){
    printf("\nStack is empty\n");
    return -1;
 }
 data=stack[*top];
 stack[*top]=0;
 *top=*top-1;
 return data;
}
void print_stack(int stack[],int top){
    int i;
    printf("\n");
    for(i=0;i<=top;i++){
        printf(" %d,",stack[i]);
    }
 //   printf("------------------------------------------------------------");
}

