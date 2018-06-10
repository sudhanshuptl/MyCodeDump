#include<stdio.h>
#include<stdio.h>

#define SIZE 10

void inserstion_sort(int values[], int n)
{
    // inserstion_sort
    int ent,index;
	int i,j,temp;
    for(i=1;i<n;i++){
    	for(j=0;j<i;j++){
    		if(values[j]>values[i])	{
    			temp=values[j];
    			values[j]=values[i];
    			values[i]=temp;
			}
			
		}
	}
}

int main(){
	int i;
	int arr[SIZE]={5,3,6,2,6,3,5,9,6,1};
	inserstion_sort(arr,SIZE);
	for(i=0;i<SIZE;i++){
		printf("%d, ",arr[i]);
	}
}
