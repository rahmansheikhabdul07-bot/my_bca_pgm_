#include <stdio.h>

int main() {
    int roll, i;
    float marks[5], total = 0, average, percentage;

    printf("Enter roll number: ");
    scanf("%d", &roll);

    printf("Enter marks in 5 subjects (out of 100 each):\n");
    for (i = 0; i < 5; i++) {
        printf("Subject %d: ", i + 1);
        scanf("%f", &marks[i]);
        total += marks[i];
    }

    average = total / 5;
    percentage = (total / 500) * 100;

    printf("\n----- Result -----\n");
    printf("Roll Number : %d\n", roll);
    printf("Total Marks : %.2f / 500\n", total);
    printf("Average     : %.2f\n", average);
    printf("Percentage  : %.2f%%\n", percentage);

    return 0;
}