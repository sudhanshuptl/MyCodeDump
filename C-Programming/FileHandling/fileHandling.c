#include<stdio.h>
#include<string.h>

int main(){

FILE *fp;
char ch[50];
fp = fopen("data.txt","w");

printf("Input data towrite\n");

gets(ch);
fputs(ch,fp);

fclose(fp);
printf("\nfile closed\n");
return 0;
}

