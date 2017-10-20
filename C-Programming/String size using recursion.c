#include<stdio.h>

// size of string using recursion

int stringSize(char arr[],int top){
	if(arr[top+1]!='\0'){
		return 1+stringSize(arr,top+1);
	}
	else{
		return 0;
	}
}

int main(){
	char arr[10]={"Sudhanshu"};
	printf("\n Size of String = %d \n",stringSize(arr,0));
}
