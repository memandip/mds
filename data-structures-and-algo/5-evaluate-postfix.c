#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>

#define MAX 100  // Maximum size of the operand stack

int stack[MAX];  // Global stack array
int top = -1;    // Initially, the stack is empty

// Push a value onto the stack
void push(int value) {
    if (top >= MAX - 1) {
        printf("Stack overflow error!\n");
        exit(1);
    }
    stack[++top] = value;
}

// Pop a value from the stack
int pop() {
    if (top < 0) {
        printf("Stack underflow error!\n");
        exit(1);
    }
    return stack[top--];
}

// Function to evaluate a postfix expression (assumes single-digit operands)
int evaluatePostfix(const char *expr) {
    int i = 0;
    char symb;
    while (expr[i] != '\0' && expr[i] != '\n') {  // Read until end-of-string or newline
        symb = expr[i];

        // 2.1. If symb is an operand (a digit), push its integer value onto the stack.
        if (isdigit(symb)) {
            push(symb - '0');  // Convert char digit to integer
        }
        // Ignore spaces (optional)
        else if (symb == ' ' || symb == '\t') {
            // do nothing
        }
        // 2.2. Otherwise, symb is assumed to be an operator.
        else {
            // 2.2.1. Remove the topmost element and place it in opnd2.
            int opnd2 = pop();
            // 2.2.2. Remove the next topmost element and place it in opnd1.
            int opnd1 = pop();
            int value;
            // 2.2.3. Apply the operator to opnd1 and opnd2.
            switch (symb) {
                case '+':
                    value = opnd1 + opnd2;
                    break;
                case '-':
                    value = opnd1 - opnd2;
                    break;
                case '*':
                    value = opnd1 * opnd2;
                    break;
                case '/':
                    if (opnd2 == 0) {
                        printf("Division by zero error!\n");
                        exit(1);
                    }
                    value = opnd1 / opnd2;
                    break;
                case '$':
                case '^':
                    value = pow(opnd1, opnd2);
                    break;
                default:
                    printf("Invalid operator encountered: %c\n", symb);
                    exit(1);
            }
            // 2.2.4. Push the result back onto the operand stack.
            push(value);
        }
        i++;
    }
    // 3. Remove and return the topmost element from the operand stack.
    return pop();
}

int main() {
    char expression[MAX];
    
    printf("Enter a postfix expression (single-digit operands, spaces optional): ");
    scanf("%s", expression);
    
    int result = evaluatePostfix(expression);
    printf("Result: %d\n", result);
    return 0;
}