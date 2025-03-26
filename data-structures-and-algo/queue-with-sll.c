#include<stdio.h>
#include<stdlib.h>
#define TRUE 1

struct node {
    int info;
    struct node *next;
};

struct node *front = NULL, *rear = NULL;

int isempty(){
    return front == NULL || rear == NULL;
};

// struct node* ins = (struct node*) malloc(sizeof(struct node));
// ins->info = val;
// ins->next = NULL;
// if (rear != NULL)
//     rear->next = ins;
// else
//     front = ins;
// rear = ins;
void enqueue(int val){
    struct node* ins = (struct node*)malloc(sizeof(struct node));
    ins->info = val;
    ins->next = NULL;
    if(rear != NULL)
        rear->next = ins;
    else
        front = ins;
    rear = ins;
}

void dequeue(){
    if(isempty()) {
        printf("Queue is empty.");
        return;
    }

    struct node *temp = front;
    front = front->next;
    if(front == NULL) {
        rear == NULL;
    }

    printf("Remove Element: %d", temp->info);
    free(temp);
};

void peek(){
    if(isempty()) {
        printf("Queue is empty.");
        return;
    }

    printf("Top Element: %d", rear->info);
};

void main(){
    while(TRUE) {
        int choice, val;
        printf("1. Enqueue\n");
        printf("2. Dequeue\n");
        printf("3. Peek\n");
        printf("4. Clear\n");
        printf("5. Exit\n");
        printf("Enter a choice (1-5):");
        scanf("%d", &choice);
        switch (choice)
        {
            case 1:
                printf("Enter value:");
                scanf("%d", &val);
                enqueue(val);
                break;
            case 2:
                dequeue();
                break;
            case 3:
                peek();
                break;
            case 4:
                system("clear");
                break;
            case 5:
                exit(0);
                break;
            default:
                printf("Invalid Choice.\n");
                break;
        }
    }
}

