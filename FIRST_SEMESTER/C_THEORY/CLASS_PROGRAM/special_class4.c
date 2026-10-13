#include<stdio.h>
int main(){
    int mark;
    printf("enter your marks: ");
    scanf("%d", &mark);


     if (mark>70){
        printf("distinction ", mark);
    }
     
      else if (mark>35){
        printf("second class", mark);
     }
     else
     { printf("fail", mark);
     }

     return 0;



     
    

     
     

     
}