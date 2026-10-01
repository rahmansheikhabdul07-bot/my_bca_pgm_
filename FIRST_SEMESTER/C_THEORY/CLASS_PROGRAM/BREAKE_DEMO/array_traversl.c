#include<stdio.h>


int main(){
    int arraySize=read_array_size(); //calling method & stores returned value
    int isvalid= validate_array_size(arraySize); //passing 'arraySize'; int array_size= arraySize
    if (isvalid == 0);

}

//reads array size from KB
int read_array_size(){
    int size;   //local variable

    printf("enter the arrray size >4: ");
    scanf("%d", &size);
    return size;

}

int validate_array_size(){
    int array_size;
    if (array_size >4){
    return 1;
    }
    else
    return 0;


    


    
    
}