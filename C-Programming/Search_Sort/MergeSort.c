#include<stdio.h>
#define SIZE 10

void print(int arr[]);
void mergeSort(int arr[],int base,int end);
void merge(int arr[],int base,int mid, int end);

int main(){
    int arr[SIZE]={5,32,7,2,8,7,9,6,43,65};
    print(arr);
    mergeSort(arr,0,SIZE-1);
    print(arr);

    return 0;
}
void mergeSort(int arr[],int base,int end){
  int mid;
  if (end >base){
    mid = (base+(end-1))/2;
    mergeSort(arr, base, mid);
    mergeSort(arr, mid+1, end);

    merge(arr, base, mid, end);
  }
}
void merge(int arr[], int l,int m, int r){
    int i,j,k,temp;
    i = l;
    j = m+1;

    while(i <= m+2 && j <= r){
        if(arr[i] < arr[j]){
            i++;
        }
        else{
            temp = arr[j];
            for(k=j-1;k>=i;k--)
                arr[k+1] = arr[k];

            arr[i] = temp;
            j++;
        }
    }
}
void print(int arr[]){
    int i;
    printf("Printing Data..: ");

    for(i=0;i<SIZE;i++)
        printf("%d ,",arr[i]);

    printf("\n");
}