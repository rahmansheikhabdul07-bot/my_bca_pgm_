#include<stdio.h>
int main(){
    for (int j=0; j<=5; j++){
        printf("loop started");
        for(int i=0; i<5;i++){

        
        break;
        printf("from inside the loop");
     }
      printf("from outer loop");
      break;
     

    }
    printf("program terminated..");
}