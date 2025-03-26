#include<stdio.h>

long facto(int n, long a){
    if(n == 0){
        return a;
    }
    return facto(n - 1, n * a);
}

int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("%d! = %ld\n", n, facto(n, 1));
    return 0;
}