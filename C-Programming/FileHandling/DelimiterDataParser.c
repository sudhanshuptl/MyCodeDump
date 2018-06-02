#include<stdio.h>
#include<string.h>
#include<stdlib.h>

/*Global Variabls*/
char *GlobalPointer=NULL;

/* Prototypes */
char *ParseLine(char *arr, char *delimiter);

int main(){
  FILE *fp;
  char line[50];
  char *token;
  //open file
  fp = fopen("data1.txt","r");
  if(fp == NULL){
     printf("  Error in opening File !\n");
     exit(1);
  }
  //read line by line and process
  while (fgets(line,sizeof line,fp) != NULL) {
      //printf("%s\n",line );
      printf("______________________________\n" );
      token = ParseLine(line,"|");
      while (token !=NULL) {
        printf("data : %s\n",token );
        token = ParseLine(NULL,"|");
      }
  }
  fclose(fp);
  return 0;
}


char *ParseLine(char *arr, char *delimiter){
  int position;
  char *blockString;
  char *ptr;

  if(arr != NULL){
    GlobalPointer = arr;
  }
  else{
    arr = GlobalPointer;
  }

  if(GlobalPointer == NULL)
    return NULL;

  position = strcspn(arr, delimiter);
  //printf("postion :%d\n",position ); //debug
  if(position  <= 0){
    if(*GlobalPointer == '\n' || *GlobalPointer == '\0'){
      return NULL;
    }
    else{
        GlobalPointer++;
        return "\0";
    }
  }

  //allocate memory
  blockString = (char *) calloc(position+2,sizeof(char));
  ptr = blockString;

  while(position--){
      *ptr++ = *arr++;
  }
  arr++;
  GlobalPointer = arr;
  return blockString;
}
