#include<stdio.h>
#include<string.h>

int main(){
  char arr[]={"Sudhanshu"};
  char *p;
  p = &arr[2]; // we can share other than base address to pointer
  printf(" Origional Arr : %s\n",arr);
  printf(" \n arr using pointer : %s\n",p);
  return 0;
}
