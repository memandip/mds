#include<stdio.h>
#include<stdlib.h>
#define TRUE 1
// hashing

int num[10] = {};

int hash(int key){
    return key % 10;
}

void insert(int value){
    int index = hash(value);
    for(int i = 0; i < 10; i++){
        if(!num[index]){
            num[index] = value;
            printf("Element %d inserted at index %d\n", value, index);
            break;
        }
        index = (index + 1) % 10;
    }
    printf("Hash table is full\n");
}

int search(int value){
    int index = hash(value);
    for(int i = 0; i < 10; i++){
        if(num[index] == value){
            printf("Element %d found at index %d\n", value, index);
            return index;
        }
        index = (index + 1) % 10;
    }
    printf("Element %d not found\n", value);
    return -1;
}

void delete(int value){
    int index = search(value);

    if(index == -1){
        printf("Element not found\n");
        return;
    }

    num[index] = -1;
    printf("Element deleted at index %d\n", index);
}

int main(){
    // insert(10);
    // insert(15);
    // insert(89);
    // insert(18);
    // insert(49);
    // insert(58);
    // insert(69);
    // insert(5);

    // search(15);
    // search(5);

    while(TRUE){
        int choice, value;
        printf("1. Insert\n");
        printf("2. Search\n");
        printf("3. Delete\n");
        printf("4. Clear\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice){
            case 1:
                printf("Enter value to insert: ");
                scanf("%d", &value);
                insert(value);
                break;
            case 2:
                printf("Enter value to search: ");
                scanf("%d", &value);
                search(value);
                break;
            case 3:
                printf("Enter value to delete: ");
                scanf("%d", &value);
                delete(value);
                break;
            case 4:
                system("clear");
                break;
            case 5:
                exit(0);
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}