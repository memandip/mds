#include<stdio.h>

int linearsearch(int arr[], int size, int target){
    for (int i = 0; i < size; i++)
    {
        if(arr[i] == target) {
            return i;
        }
    }
    
    return -1;
}

int main(){
    int a[] = {1,2,34,2,322,322,6262,234,26,26,2};
    int target;
    int idx;

    printf("Enter target value to search:");
    scanf("%d", &target);

    idx = linearsearch(a, sizeof(a), target);

    if(idx != -1) {
        printf("Target value: %d found at index %d.\n", target, idx);
    }   else    {
        printf("Target value not found in array.\n");
    }

}