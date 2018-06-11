/*
Altered algo to Merge two sorted array
array is sorted from begining to mid then mid 2 end
write an algo to sort whole array like merging two sorted array
without creating extra space
*/

#include<stdio.h>

#define SIZE 10

void print(int arr[]);
void merge(int arr[], int l,int m, int r);

int main(){
    int arr[SIZE] = {4,5,8,11,15,5,10,12,18,20};
    print(arr);
    merge(arr,0,4,9);
    print(arr);
    return 0;
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
    printf(" Print Current data :\n");

    for(i=0;i<SIZE;i++)
        printf("%d ,",arr[i]);

    printf("\n");
}