// 9. Write both recursive and iterative program to
//    a. find factorial of a number.
//    b. find sum of first N natural numbers.
//    c. find Fibonacci number.
//    d. find greatest common divisor.
#include<stdio.h>
#include<stdlib.h>

int factorial_recursive(int n){
    if(n == 0 || n == 1){
        return 1;
    }
    return n * factorial_recursive(n - 1);
}

int factorial_iterative(int n){
    int fact = 1;
    for (int i = 1; i <= n; ++i)
    {
        fact *= i;
    }
    return fact;
}

int sum_recursive(int n){
    if(n == 0){
        return 0;
    }
    return n + sum_recursive(n - 1);
}

int sum_iterative(int n){
    int sum = 0;
    for (int i = 1; i <= n; ++i)
    {
        sum += i;
    }
    return sum;
}

int fibonacci_recursive(int n){
    if(n == 0 || n == 1){
        return n;
    }
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

int fibonacci_iterative(int n){
    int a = 0, b = 1, c;
    if(n == 0){
        return a;
    }
    for (int i = 2; i <= n; ++i)
    {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int gcd_recursive(int a, int b){
    if(b == 0){
        return a;
    }
    return gcd_recursive(b, a % b);
}

int gcd_iterative(int a, int b){
    while(b != 0){
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int lcm(int a, int b){
    return (a * b) / gcd_iterative(a, b);
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);

    printf("Factorial of %d (recursive): %d\n", n, factorial_recursive(n));
    printf("Factorial of %d (iterative): %d\n", n, factorial_iterative(n));

    printf("Sum of first %d natural numbers (recursive): %d\n", n, sum_recursive(n));
    printf("Sum of first %d natural numbers (iterative): %d\n", n, sum_iterative(n));

    printf("Fibonacci number at position %d (recursive): %d\n", n, fibonacci_recursive(n));
    printf("Fibonacci number at position %d (iterative): %d\n", n, fibonacci_iterative(n));

    int a, b;
    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);
    printf("GCD of %d and %d (recursive): %d\n", a, b, gcd_recursive(a, b));
    printf("GCD of %d and %d (iterative): %d\n", a, b, gcd_iterative(a, b));
    printf("LCM of %d and %d: %d\n", a, b, lcm(a, b));

    return 0;
}