#include<stdio.h>

#define null (void*)0 //NULL constant
//(void*)0 is a null pointer constant.
int main(){
char *p=NULL;

if(p==null){
    printf("Null comparision success");
}
else{
    printf("Null comparision Failure");
}
}
