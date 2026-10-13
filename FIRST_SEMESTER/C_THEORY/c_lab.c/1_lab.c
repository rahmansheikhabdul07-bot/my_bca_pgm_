#include <stdio.h>

int main() {
    int a = 17, b = 5;
    float x = 7.5f, y = 2.5f;
    double p = 12.75, q = 3.25;
    char c1 = 'A', c2 = 2;   /* char used as a small integer */

    printf("===== INTEGER =====\n");
    printf("%d + %d = %d\n", a, b, a + b);
    printf("%d - %d = %d\n", a, b, a - b);
    printf("%d * %d = %d\n", a, b, a * b);
    printf("%d / %d = %d\n", a, b, a / b);
    printf("%d %% %d = %d\n", a, b, a % b);

    printf("\n===== FLOAT =====\n");
    printf("%.2f + %.2f = %.2f\n", x, y, x + y);
    printf("%.2f - %.2f = %.2f\n", x, y, x - y);
    printf("%.2f * %.2f = %.2f\n", x, y, x * y);
    printf("%.2f / %.2f = %.2f\n", x, y, x / y);
    printf("%% not allowed for float\n");

    printf("\n===== DOUBLE =====\n");
    printf("%.3lf + %.3lf = %.3lf\n", p, q, p + q);
    printf("%.3lf - %.3lf = %.3lf\n", p, q, p - q);
    printf("%.3lf * %.3lf = %.3lf\n", p, q, p * q);
    printf("%.3lf / %.3lf = %.3lf\n", p, q, p / q);
    printf("%% not allowed for double\n");

    printf("\n===== CHAR =====\n");
    printf("'%c' (ASCII %d) + %d = %d\n", c1, c1, c2, c1 + c2);
    printf("'%c' (ASCII %d) - %d = %d\n", c1, c1, c2, c1 - c2);
    printf("'%c' (ASCII %d) * %d = %d\n", c1, c1, c2, c1 * c2);
    printf("'%c' (ASCII %d) / %d = %d\n", c1, c1, c2, c1 / c2);
    printf("'%c' (ASCII %d) %% %d = %d\n", c1, c1, c2, c1 % c2);

    return 0;
}