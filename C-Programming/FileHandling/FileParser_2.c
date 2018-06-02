#include<stdio.h>
#include<string.h>

#define DATA_SEGMENT 3

int main(){
    FILE *fp; //file pointer
    char line[30];
    char *token;
    int i;

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
        //When we exactly know how much data will be
        for(i =0;i<DATA_SEGMENT;i++){
            if(i==0){
                printf("FIRST NAME : %s\n",token);
                token = strtok(NULL,"|");
             }
            else{ if(i==1){
                    printf("LAST NAME : %s\n",token);
                    token = strtok(NULL,"|");
                    }
                else{
                    printf("Extention (integer) : %d\n",atoi(token));// converting to integer
                    }
                }
        }
    }

    return 0;
}
