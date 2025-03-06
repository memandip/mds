// 10. Write a recursive program to solve Tower of Hanoi (TOH) problem and hence count the number of moves required.
#include<stdio.h>
#include<stdlib.h>

void towerOfHanoi(int n, char from_rod, char to_rod, char aux_rod){
    if(n == 1){
        printf("Move disk 1 from rod %c to rod %c\n", from_rod, to_rod);
        return;
    }
    towerOfHanoi(n - 1, from_rod, aux_rod, to_rod);
    printf("Move disk %d from rod %c to rod %c\n", n, from_rod, to_rod);
    towerOfHanoi(n - 1, aux_rod, to_rod, from_rod);
}

int main(){
    int n;
    printf("Enter number of disks: ");
    scanf("%d", &n);
    towerOfHanoi(n, 'A', 'C', 'B');
    // count the number of moves
    printf("Number of disks: %d\n", n);
    // 1 << n results in 2^n, while 2 << n results in 2^(n+1).
    int moves = (1 << n) - 1;
    printf("Number of moves: %d\n", moves);
    return 0;
}