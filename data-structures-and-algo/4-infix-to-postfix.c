#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX 100  // Maximum size for stack and expression

// Stack definition for characters
char stack[MAX];
int top = -1;

// Function to push an element to the stack
void push(char c) {
    if (top < MAX - 1) {
        stack[++top] = c;
    } else {
        printf("Stack overflow!\n");
        exit(1);
    }
}

// Function to pop an element from the stack
char pop() {
    if (top >= 0) {
        return stack[top--];
    } else {
        printf("Stack underflow!\n");
        exit(1);
    }
}

// Function to return the top element of the stack without popping it
char peek() {
    if (top >= 0)
        return stack[top];
    else
        return '\0';
}

// Function to check if a character is an operator
int isOperator(char c) {
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^' || c == '$');
}

// Function to return the precedence of an operator
int precedence(char op) {
    switch(op) {
        case '^': 
        case '$': return 3; // Both ^ and $ have the highest precedence
        case '*': 
        case '/': return 2;
        case '+': 
        case '-': return 1;
        default: return 0;
    }
}

// Function that converts an infix expression to a postfix expression
void infixToPostfix(char infix[], char postfix[]) {
    int i, j = 0;
    char c;
    
    for (i = 0; infix[i] != '\0'; i++) {
        c = infix[i];
        
        // If the character is an operand, add it to the postfix expression
        if (isalnum(c)) { 
            postfix[j++] = c;
        }
        // If the character is an opening parenthesis, push it on the stack
        else if (c == '(') {
            push(c);
        }
        // If the character is a closing parenthesis, pop until an opening parenthesis is encountered
        else if (c == ')') {
            while (top != -1 && peek() != '(') {
                postfix[j++] = pop();
            }
            // Pop the '(' from the stack
            if (top != -1 && peek() == '(')
                pop();
        }
        // If the character is an operator
        else if (isOperator(c)) {
            // Pop operators from the stack with higher or equal precedence.
            // For right-associative operators (^ and $), do not pop on equal precedence.
            while (top != -1 && isOperator(peek()) &&
                   ((precedence(peek()) > precedence(c)) ||
                   (precedence(peek()) == precedence(c) && (c != '^' && c != '$')))) {
                postfix[j++] = pop();
            }
            push(c);
        }
    }
    
    // Pop any remaining operators from the stack
    while (top != -1) {
        postfix[j++] = pop();
    }
    postfix[j] = '\0'; // Null-terminate the postfix expression
}

int main() {
    char infix[MAX], postfix[MAX];
    
    printf("Enter an infix expression (no spaces): ");
    scanf("%s", infix);
    
    infixToPostfix(infix, postfix);
    
    printf("Postfix Expression: %s\n", postfix);
    return 0;
}

// INFIX: A+B$C-D$E, POSTFIX: ABC$+DE$-
