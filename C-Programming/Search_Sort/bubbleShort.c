#include<stdio.h>


#define SIZE 10

void bubble_sort(int values[], int n)
{
    // BUBBLE SHORT
    int i,j,temp;
    for(i=0;i<n;i++){
    	for(j=0;j<n-1-i;j++){
    		if(values[j]>values[j+1]){
    			temp=values[j];
				values[j]=values[j+1];
				values[j+1]=temp;
			}
		}
	}
}

int main(){
	int i;
	int arr[SIZE]={5,3,6,2,6,3,5,9,6,7};
	bubble_sort(arr,SIZE);
	for(i=0;i<SIZE;i++){
		printf("%d, ",arr[i]);
	}
}
