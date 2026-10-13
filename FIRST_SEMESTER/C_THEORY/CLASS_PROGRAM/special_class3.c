#include<stdio.h>
int main(){
    int student_adm;
    int second_pu_pass =1;  //one is cleared and 0 means fail
    int interview_clear=1;
    int paid_fees= 1;


    if (second_pu_pass == 1){
        if (interview_clear ==1){
            if(paid_fees==1){
                printf("you tuff? admission completed");
            }else{
                printf("not eligible you poor mf");
            }
        }
        else{
            printf("not elligible nga");
        }



    }else{
        printf("not elligible, ths some real thing ");
    }
    


}