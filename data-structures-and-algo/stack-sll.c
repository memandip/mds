#include<stdio.h>
#include<stdlib.h>
struct node
{
    int info;
    struct node* next;
};
struct node* top = NULL;

int isempty(){
    return top == NULL ? 1 : 0;
}

void peek(){
    if(isempty()) {
        printf("Stack is empty.\n");
        return;
    }

    printf("Top Element: %d\n", top->info);
}

void push(int val)
{
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    temp->info = val;
    temp->next = top;
    top = temp;
}
void pop()
{
    if(isempty()) {
        printf("Stack is empty.\n");
        return;
    }
    struct node* temp = top;

    printf("Removed element is %d.\n", temp->info);

    top = temp->next;
    free(temp);
}

void display()
{
    struct node* temp = top;
    while(temp != NULL) {
        printf("%d\t", temp->info);
        temp = temp->next;
    }
    printf("\n");
}

int main(){
    while(1){
        int choice, val;
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Peek\n");
        printf("5. Clear\n");
        printf("6. Exit\n");
        printf("Enter a choice (1-5):");
        scanf("%d", &choice);
        switch(choice){
            case 1:
                printf("Enter a value to push:");
                scanf("%d", &val);
                push(val);
                break;
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                peek();
                break;
            case 5:
                system("clear");
                break;
            case 6:
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }
}