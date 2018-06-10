#include<stdio.h>
#include<string.h>

int main(){

FILE *fp;
char str[50];
fp = fopen("data.txt","w");

printf("Input data towrite\n");
scanf("%s",str);
printf("Writting into file ***\n");
fputs(str,fp);

fclose(fp);
printf("\nfile closed\n");
return 0;
}

