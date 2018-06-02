#include<stdio.h>
#include<string.h>


//declaring global variable
char *GlobalPointer=NULL;

void printGlobalPointer(){
    printf(" \n sub arr using GlobalPointer : %s\n",GlobalPointer);
    printf(" \n sub arr using GlobalPointer from xth position : %s\n",GlobalPointer+2);
}

int main(){
  char arr[]={"Sudhanshu"};

  // we can share other than base address to globalpointer
  GlobalPointer = &arr[2];

  printf(" Origional Arr : %s\n",arr);
  printGlobalPointer();
  return 0;
}
