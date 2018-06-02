#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char *ReturnSubstring(char *arr){
  char *subString = (char *)calloc(6,sizeof(char));
  char *p = subString;
  // need to copy "patel" only
  //move pointer to p
  arr = arr+9;

  //now copy to p //that actually change data to subString
  while(*arr){
    *p = *arr;
    *p++;
    *arr++;
    // Shorthand : *p++ = *arr++
  }
  return subString;
}


int main(){
  char arr[]={"Sudhanshu Patel"};
  char *p;

  printf(" Origional Arr : %s\n",arr);
  p = ReturnSubstring(arr);
  printf("\n Print Substring :%s\n",p );
  return 0;
}
