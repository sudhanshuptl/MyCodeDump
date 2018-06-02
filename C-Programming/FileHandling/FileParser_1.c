#include<stdio.h>
#include<string.h>

int main(){
    FILE *fp; //file pointer
    char line[30];
    char *token;

    //open file
    fp = fopen("data.txt","r");

    //check if any error in opening file
    if(fp == NULL){
        printf("Error in opening File ! ");
        return -1;
    }

    while(fgets(line, sizeof line, fp) != NULL){
        token =strtok(line,"|"); //string and delimiter is input
        printf("\n______________________________________________\n");
        while(token !=NULL){
           printf("User1 : %s\n",token);
           token = strtok(NULL,"|");
        }
    }

    return 0;
}
