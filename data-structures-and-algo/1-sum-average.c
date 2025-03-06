// 1. Write a program to find sum and average of n numbers using malloc(), calloc(), realloc(), and free() in C.
#include<stdio.h>
#include<stdlib.h>

int main(){
    int sum = 0, n, *ptr;
    printf("Enter a numbers: ");
    scanf("%d", &n);

    // This will allocate a block of memory that can hold n integers, 
    // and the address of the starting element will be stored in the ptr variable.

    printf("Enter 1 for malloc, 2 for calloc:");
    int choice;
    scanf("%d", &choice);

    switch(choice){
        case 1:
            ptr = (int*)malloc(n * sizeof(int));
            break;
        case 2:
            ptr = (int*)calloc(n, sizeof(int));
            break;
        // case 3:
        //     ptr = (int*)realloc(ptr, n * sizeof(int));
        //     break;
        default:
            printf("Invalid choice. Using default MALLOC.\n");
            ptr = (int*)malloc(n * sizeof(int));
            exit(0);
    }

    printf("POINTER: %p\n", ptr);
    
    // if memory cannot be allocated
    if(ptr == NULL) {
        printf("Error! memory not allocated.");
        exit(0);
    }

    for (int i = 0; i < n; ++i)
    {
        printf("Enter number %d: ", i + 1);
        scanf("%d", ptr + i);
        sum += *(ptr + i);
    }
    printf("Sum: %d\n", sum);

    float avg = (float)sum / n;
    printf("Average: %.2f\n", avg);

    free(ptr);
    return 0;
}