#include<stdio.h>
#include<stdio.h>

#define SIZE 10

void selection_sort(int values[], int n)
{
    // Selection SORT
    int min,index;
    int i,j,temp;
    for(i=0;i<n;i++){
    	min=values[i];
		index=i;
		for(j=i;j<n;j++){
     		if(values[j]<min){
     			min=values[j];
     			index=j;
			 }
		}
		temp=values[i];
		values[i]=min;
		values[index]=temp;
	}
}

int main(){
	int i;
	int arr[SIZE]={5,3,6,2,6,3,5,9,6,5};
	selection_sort(arr,SIZE);
	for(i=0;i<SIZE;i++){
		printf("%d, ",arr[i]);
	}
}
