#include <iostream>

using namespace std;


void selection_sort(int arr[], int n) {
    for (int i=0; i<n-1; i++) {
        int swap_idx = i;
        for (int j=i+1; j<n; j++) {
            if (arr[swap_idx] > arr[j])
                swap_idx = j;
        };
        swap(arr[swap_idx], arr[i]);
    };

    for (int k=0; k<n; k++) {
        cout << arr[k] << " ";
    };
};


int main() {
    int arr[] = {7, 12, 9, 11, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    selection_sort(arr, n);
    return 0;
};