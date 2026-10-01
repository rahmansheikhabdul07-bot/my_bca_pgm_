#include<stdio.h>
//declaration
char name[50];
int roll_no;
int marks[5];
int total;
float average;
float cgpa;

void get_student_data();          //collect student data
void get_TOTAL();                 //calculate total of 5 subject marks
void get_average();               //calculate average marks
void get_cgpa();                  //to get cgpa
void display_student_details();   //to display student details

int main(){
    get_student_data();   //collect student data
    get_TOTAL();           //calculate total of 5 subject marks
    get_average();         //calculate average marks
    get_cgpa();             //to get cgpa
    display_student_details(); //to display student details
    return 0;
}

void get_student_data(){
    printf("Enter student name: ");
    scanf("%s", name);

    printf("Enter roll number: ");
    scanf("%d", &roll_no);

    printf("Enter marks of 5 subjects (out of 100 each):\n");
    for(int i = 0; i < 5; i++){
        printf("Subject %d: ", i + 1);
        scanf("%d", &marks[i]);
    }
}

void get_TOTAL(){
    total = 0;
    for(int i = 0; i < 5; i++){
        total += marks[i];
    }
}

void get_average(){
    average = total / 5.0;
}

void get_cgpa(){
    // Simple formula: CGPA = average marks / 9.5 (common percentage-to-CGPA conversion)
    cgpa = average / 9.5;
}

void display_student_details(){
    printf("\n--------- STUDENT DETAILS ---------\n");
    printf("Name        : %s\n", name);
    printf("Roll No     : %d\n", roll_no);
    printf("Total Marks : %d / 500\n", total);
    printf("Average     : %.2f\n", average);
    printf("CGPA        : %.2f\n", cgpa);
    printf("------------------------------------\n");
}
