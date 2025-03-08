#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_SIZE 100
#define SMALL_OPENING_BRACKET '('
#define SMALL_CLOSING_BRACKET ')'
#define MEDIUM_OPENING_BRACKET '{'
#define MEDIUM_CLOSING_BRACKET '}'
#define LARGE_OPENING_BRACKET '['
#define LARGE_CLOSING_BRACKET ']'

// Global variables at the top
char stack[MAX_SIZE];  // Stack array
int top = -1;         // Stack top pointer

// Stack operations
bool isEmpty() {
    return top == -1;
}

bool isFull() {
    return top == MAX_SIZE - 1;
}

void push(char item) {
    if (!isFull()) {
        stack[++top] = item;
    }
}

char pop() {
    if (!isEmpty()) {
        return stack[top--];
    }
    return NULL;
}

char peek() {
    if (!isEmpty()) {
        return stack[top];
    }
    return NULL;
}

// Bracket matching helper functions
bool isOpeningBracket(char c) {
    return c == SMALL_OPENING_BRACKET || 
           c == MEDIUM_OPENING_BRACKET || 
           c == LARGE_OPENING_BRACKET;
}

bool isClosingBracket(char c) {
    return c == SMALL_CLOSING_BRACKET || 
           c == MEDIUM_CLOSING_BRACKET || 
           c == LARGE_CLOSING_BRACKET;
}

bool isMatchingPair(char opening, char closing) {
    return (opening == SMALL_OPENING_BRACKET && closing == SMALL_CLOSING_BRACKET) ||
           (opening == MEDIUM_OPENING_BRACKET && closing == MEDIUM_CLOSING_BRACKET) ||
           (opening == LARGE_OPENING_BRACKET && closing == LARGE_CLOSING_BRACKET);
}

// Main bracket matching function
bool areBracketsBalanced(const char* expr) {
    // Reset stack for new expression
    top = -1;
    
    for (int i = 0; expr[i] != NULL; i++) {
        if (isOpeningBracket(expr[i])) {
            push(expr[i]);
        } else if (isClosingBracket(expr[i])) {
            // If we find a closing bracket but stack is empty
            if (isEmpty()) {
                return false;
            }
            
            // If the closing bracket doesn't match the corresponding opening bracket
            char last_opening = pop();
            if (!isMatchingPair(last_opening, expr[i])) {
                return false;
            }
        }
    }
    
    // Check if there are any remaining opening brackets
    return isEmpty();
}

int main() {
    char expr[MAX_SIZE];
    printf("Enter an expression with brackets (max %d characters): ", MAX_SIZE-1);
    scanf("%s", expr);
    
    if (areBracketsBalanced(expr)) {
        printf("Brackets are balanced\n");
    } else {
        printf("Brackets are NOT balanced\n");
    }
    
    return 0;
}
