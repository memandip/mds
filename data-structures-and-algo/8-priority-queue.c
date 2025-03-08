#include <stdio.h>

#define MAX_SIZE 10

int priorityQueue[MAX_SIZE];
int size = 0;

// Function to check if the priority queue is empty
int isEmpty() {
    return size == 0;
}

// Function to check if the priority queue is full
int isFull() {
    return size == MAX_SIZE;
}

// Function to insert a new element into the priority queue
void insert(int value) {
    if (isFull()) {
        printf("Priority queue is full. Cannot insert element.\n");
        return;
    }

    // If queue is empty, insert element at the front
    if (isEmpty()) {
        priorityQueue[0] = value;
        size++;
        return;
    }

    // Find the correct position for the new element based on priority
    int i;
    for (i = 0; i < size; i++) {
        if (value < priorityQueue[i]) {
            break;
        }
    }

    // Shift elements to the right to make space for the new element
    for (int j = size; j > i; j--) {
        priorityQueue[j] = priorityQueue[j - 1];
    }

    // Insert the new element
    priorityQueue[i] = value;
    size++;
}

// Function to delete an element from the priority queue
void deleteElement() {
    if (isEmpty()) {
        printf("Priority queue is empty. Cannot delete element.\n");
        return;
    }

    // Remove the element at the front of the queue
    for (int i = 0; i < size - 1; i++) {
        priorityQueue[i] = priorityQueue[i + 1];
    }
    size--;
}

// Function to print the priority queue
void printPriorityQueue() {
    if (isEmpty()) {
        printf("Priority queue is empty.\n");
        return;
    }

    printf("Priority Queue: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", priorityQueue[i]);
    }
    printf("\n");
}

int main() {
    int choice, value;

    while (1) {
        printf("Priority Queue Menu:\n");
        printf("1. Insert element\n");
        printf("2. Delete element\n");
        printf("3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                insert(value);
                printPriorityQueue();
                break;
            case 2:
                deleteElement();
                printPriorityQueue();
                break;
            case 3:
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}