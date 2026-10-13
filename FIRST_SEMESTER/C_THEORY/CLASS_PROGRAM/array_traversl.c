#include<stdio.h>

int main(){
    int isValid=1; 
    int arraysize=0; 

    //calling method & stores returned value
    //passing 'arraySize'; int array_size= arraySize
 
    while (isValid ==1)
    {
        int arraySize = read_array_size();
        int isValid=validate_array_size(arraySize);
        int validated;
        if (validated ==1){

            break;

        }
        printf("array size is nit valid .....try again"); 

    }
    int myarray[arraysize];
    for (int i=0;i<=arraysize;i++){

    }

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