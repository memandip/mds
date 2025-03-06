// 7. Write a program to implement Circular Queue using array data structure.
#include<stdio.h>
#include<stdlib.h>

#define MAX 5
int queue[MAX];
int front = -1, rear = -1;

void enqueue(int value){
    if((front == 0 && rear == MAX - 1) || front == rear + 1){
        printf("Queue is full\n");
        return;
    }

    if(front == -1){
        front = 0;
    }

    if(rear == MAX - 1){
        rear = 0;
    } else {
        rear++;
    }

    queue[rear] = value;
    printf("Enqueued %d\n", value);
}

void dequeue(){
    if(front == -1){
        printf("Queue is empty\n");
        front = -1;
        rear = -1;
        return;
    }
    printf("Dequeued %d\n", queue[front]);
    if(front == rear){
        front = -1;
        rear = -1;
    } else if(front == MAX - 1) {
        front = 0;
    } else {
        front++;
    }
}

int main(){
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);
    enqueue(5);
    enqueue(6);
    enqueue(7);
    dequeue();
    dequeue();
    enqueue(8);
    enqueue(9);
    enqueue(10);
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    dequeue();
    enqueue(8);
    enqueue(9);
    enqueue(10);
    return 0;
}