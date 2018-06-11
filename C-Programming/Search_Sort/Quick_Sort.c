#include<stdio.h>

#define SIZE 10

void print(int arr[]);
void quick_sort(int arr[],int base,int end);

int main(){
    int arr[SIZE]={5,63,12,66,66,73,99,7,3,44};
    print(arr);
    quick_sort(arr,0,SIZE-1);
    print(arr);
    return 0;
}

void quick_sort(int arr[],int base,int end){
    int pivot=base;
    int i,temp;
    if(base == end)
        return;

    for(i=base+1;i<=end;i++){
        if(arr[i] < arr[pivot]){
            temp = arr[pivot];
            arr[pivot] = arr[i];
            arr[i] = temp;
            pivot = i;
        }
    quick_sort(arr,base,pivot-1);
    quick_sort(arr,pivot+1,end);
    }


}
void print(int arr[]){
    int i;
    printf("Printing Current status:\n");

    for(i=0;i<SIZE;i++){
        printf("%d ,",arr[i]);
    }
    printf("\n");
}