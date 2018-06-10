#include<stdio.h>
#include<stdlib.h>
#define SIZE 5

struct queue{
	//add at end and remove from begining
	int arr[SIZE];
	int front;
	int rear;
};
typedef struct queue Queue;


void insert(Queue *queue,int data);
void print_queue(Queue queue);
int delQueue(Queue *queue);

int main(){
	Queue queue;
	int data,option;
	queue.front=-1;
	queue.rear=-1;
	
	while(1){
    printf("\ntype 1 to insert and 2 to remove :");
    scanf("%d",&option);
    	switch(option){
        	case 1:
            	printf("Input data :");
            	scanf("%d",&data);
            	insert(&queue,data);
            	print_queue(queue);
            	break;
        	case 2:
            	printf("\n Deleted data : %d\n",delQueue(&queue));
            	print_queue(queue);
            	break;
        	default:
        		print_queue(queue);
            	break;
    }
   
 }
	return 0;
}

int delQueue(Queue *queue){
	int data;
	if((queue->rear+1)%SIZE >= queue->front || queue->front==-1){
		printf("\nQueue is empty");
		return -1;
	}
	else{
		if(queue->front==queue->rear){
			data=queue->arr[queue->rear];
			queue->rear=-1;
			queue->front=-1;
		}
		else{
		
			data=queue->arr[queue->rear];
			queue->rear=queue->rear+1;
		}
	}
}
void insert(Queue *queue,int data){
	if(queue->front==-1){
		//insert when no element
		queue->front=queue->front+1;
		queue->rear=queue->rear+1;
		queue->arr[queue->front]=data;
	
	}
	else{
		//check is full
		if((queue->front+1)%SIZE ==queue->rear){
			printf("\nQueue IS full, Insertion failed ");
		}
		else{
			queue->front=(queue->front+1)%SIZE;
			queue->arr[queue->front]=data;
		}
	}
}
void print_queue(Queue queue){
	//print queue 
	int i=queue.front;
	printf("\n");
	while(i%SIZE >= queue.rear){
		printf(" %d,",queue.arr[i]);
		i--;
	}
}
