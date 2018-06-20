#include<stdio.h>
int main(){
int x=30;
int *y,*z;
y = &x;
z=y;

// ++ has more preference so first it increemnt address then print value at that address
*z++;
printf("X = %d Y = %d , Z= %d \n",x, *y,*z);

}
