#include <stdio.h>

int main() {
    int age, ch;

    printf("Are you an Indian national? (1=Yes, 0=No): ");
    scanf("%d", &ch);
    if (ch != 1) { printf("Not eligible: Must be an Indian national.\n"); return 0; }

    printf("Enter age: ");
    scanf("%d", &age);
    if (age < 18) { printf("Not eligible: Age must be 18 or above.\n"); return 0; }

    printf("Passed driving test? (1=Yes, 0=No): ");
    scanf("%d", &ch);
    if (ch != 1) { printf("Not eligible: Driving test not passed.\n"); return 0; }

    printf("Paid DL processing fee? (1=Yes, 0=No): ");
    scanf("%d", &ch);
    if (ch != 1) { printf("Not eligible: DL processing fee not paid.\n"); return 0; }

    printf("Eligible for a driving licence.\n");
    return 0;
}