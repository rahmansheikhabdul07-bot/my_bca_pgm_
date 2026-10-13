#include <stdio.h>

int main() {
    float a, b, c, max, min;

    printf("Enter three numbers: ");
    scanf("%f %f %f", &a, &b, &c);

    max = min = a;
    if (b > max) max = b;
    if (c > max) max = c;
    if (b < min) min = b;
    if (c < min) min = c;

    printf("\nLargest  : %2f\n", max);
    printf("Smallest : %.2f\n", min);

    return 0;
}