//(comments: to understand description of program)
    //(two types of comments (/*1.multi line*/) and (//2.single line comment//)
//pgm to store and display 5 subjects marks

#include<stdio.h>

int main(){
    int my_marks[5];

    int sub_marks[5];    //declares an array sub_marks with size 5 of int type
    // with size 5 of int type  
    //storing data/array initialization - array_name[index]= data/value;
    sub_marks[0]=80;   //stores 80 in position whose index is zero
    sub_marks[1]=78;   //stores 78 in a position whose index is one
    sub_marks[2]=68;   //stores 68 in a position whose index is two
    sub_marks[3]=58;   //stores 58 in a position whose index is three
    sub_marks[4]=88;   //stores 88 in a position whose index is four   //static array initialization
     //fetch the first array element from sub_marks
     printf("first subject marks: %d\n", sub_marks[0] );
     printf("second subject marks: %d\n", sub_marks[1] );
     printf("third subject marks: %d\n", sub_marks[2] );
     printf("fourth subject marks: %d\n", sub_marks[3] );
     printf("fifth subject marks: %d\n", sub_marks[4] );

    //dynamic initialization of 'my_marks'
    //get datafrom key board

    for(int i=0; i<=5;i++){
        printf("enter %d subject marks: [int data] ",i+1);
    scanf("%d", &my_marks[i]);  //stored in first location 
    }

    printf("enter second subject marks:[int data] ");
    scanf("%d", &my_marks[1]);  

     printf("enter third subject marks:[int data] ");
    scanf("%d", &my_marks[2]);  

     printf("enter fourth subject marks:[int data] ");
    scanf("%d", &my_marks[3]);  

     printf("enter  fifth marks:[int data] ");
    scanf("%d", &my_marks[4]);  
    





}