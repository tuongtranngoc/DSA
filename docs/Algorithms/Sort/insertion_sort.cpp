#include <iostream>

using namespace std;

void insertion_sort(int arr[], int n){
    for (int i = 1; i < n; i++) {
        int curr_val = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > curr_val) {
            arr[j+1] = arr[j];
            --j;
        };
        arr[j+1] = curr_val; 
    };
    for (int i=0; i<n; i++) {
        cout << arr[i] << " ";
    };
};


int main() {
    int arr[] = {7, 12, 9, 11, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    insertion_sort(arr, n);
    return 0;
};