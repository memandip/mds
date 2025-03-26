#include<stdio.h>

int binarysearch(int arr[], int size, int target){
    int l = 0, r = size - 1, m, count = 0;

    while(l <= r) {
        count++;
        m = (l + r) / 2;
        if(target == arr[m]){
            return m;
        }   else if(target < arr[m]) {
            r = m - 1;
        }   else    {
            l = m + 1;
        }
    }

    return -1;
}

int main(){
    int a[] = {1,2,3,4,5,6,7,11,15,18, 45, 50, 55};
    int target;
    int idx;

    printf("Enter target value to search:");
    scanf("%d", &target);

    idx = binarysearch(a, sizeof(a), target);

    if(idx != -1) {
        printf("Target value: %d found at index %d.\n", target, idx);
    }   else    {
        printf("Target value: %d not found in array.\n", target);
    }
}