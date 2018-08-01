/* Quick Sort
*/
#include<stdio.h>

#define SIZE 10

void print(int arr[]);
void quick_sort(int arr[],int base,int end);
int partition(int arr[], int base,int end);
void swap(int *a, int *b);

int main(){
    int arr[SIZE]={66,63,12,88,33,73,99,7,3,44};

    print(arr);
    quick_sort(arr, 0, SIZE-1);
    print(arr);
    return 0;
}
void swap(int *a, int *b){
  int temp;
  temp = *b;
  *b = *a;
  *a = temp;
}
int partition(int arr[], int base,int end){
    int pivot=base;
    int pivot_value = arr[end];
    int temp, i;

    for(i=base;i<=end-1;i++){
        if(arr[i] < pivot_value){
            //swap
            swap(&arr[i],&arr[pivot]);
            pivot++;
      }
    }

    swap(&arr[pivot],&arr[end]);

    //printf("\n Pivote index : %d, pivote value : %d, %d %d\n",pivot,pivot_value,base,end);
    //print(arr);
    return pivot;
}

void quick_sort(int arr[],int base,int end){
    int pivot;
    if(base >= end)
      return;
    pivot = partition(arr, base, end);
    quick_sort(arr,base,pivot-1);
    quick_sort(arr,pivot+1,end);
}

void print(int arr[]){
    int i;
    printf("Printing Current status:\n");
    for(i=0;i<SIZE;i++){
        printf("%d ,",arr[i]);
    }
    printf("\n");
}
