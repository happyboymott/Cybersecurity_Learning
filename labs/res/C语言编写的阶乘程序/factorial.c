/* 读入一个整数 n（0 到 12），打印 n 的阶乘。 */

#include <stdio.h>

int factorial(int n) {
    int result = 1;

    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

int main(void) {
    int n = 0;

    printf("enter n (0-12): ");
    if (scanf("%d", &n) != 1) {
        puts("bad input");
        return 1;
    }
    if (n < 0 || n > 12) {
        puts("out of range");
        return 2;
    }

    printf("%d! = %d\n", n, factorial(n));
    return 0;
}
