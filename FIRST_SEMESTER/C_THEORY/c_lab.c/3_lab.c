#include <stdio.h>

int main() {
    int ch, a, b;
    float x, y;

    printf("1.Add 2.Subtract 3.Multiply 4.Divide 5.Modulus\nChoice: ");
    scanf("%d", &ch);

    if (ch == 5) {
        printf("Enter two integers: ");
        scanf("%d %d", &a, &b);
    } else {
        printf("Enter two numbers: ");
        scanf("%f %f", &x, &y);
    }

    switch (ch) {
        case 1: printf("%.2f + %.2f = %.2f\n", x, y, x + y); break;
        case 2: printf("%.2f - %.2f = %.2f\n", x, y, x - y); break;
        case 3: printf("%.2f * %.2f = %.2f\n", x, y, x * y); break;
        case 4:
            if (y != 0) printf("%.2f / %.2f = %.2f\n", x, y, x / y);
            else printf("Error: Division by zero\n");
            break;
        case 5:
            if (b != 0) printf("%d %% %d = %d\n", a, b, a % b);
            else printf("Error: Modulus by zero\n");
            break;
        default: printf("Invalid choice\n");
    }
    return 0;
}