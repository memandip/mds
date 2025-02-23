#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "./stack.c"
#define STACK_MAX_SIZE 10
#define TRUE 1
#define VALID_BRACKET "(){}[]"
#define SMALL_OPENING_BRACKET '('
#define SMALL_CLOSING_BRACKET ')'
#define MEDIUM_OPENING_BRACKET '{'
#define MEDIUM_CLOSING_BRACKET '}'
#define LARGE_OPENING_BRACKET '['
#define LARGE_CLOSING_BRACKET ']'

int stack[STACK_MAX_SIZE];

int main()
{
    printf("Please provide a mathematical expression");
    char math_expression[100];
    scanf("%d", &math_expression);
    for (int i = 0; i < strlen(math_expression); i++)
    {
        printf("%c", math_expression[i]);
    }
    
}