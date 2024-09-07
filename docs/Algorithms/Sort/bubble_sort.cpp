#include <iostream>

using namespace std;


void bubble_sort(int arr[], int n) {
    bool is_swap;
    is_swap = false;
    for (int i=0; i<n-1; i++) {
        for (int j=i; j<n; j++) {
            if (arr[i] > arr[j]) {
                swap(arr[i], arr[j]);
                is_swap = true;
            };
        };
        if (is_swap==false) {
            break;
        };
    };

    for (int i=0; i<n; i++) {
        cout << arr[i] << " ";
    };
};


int main() {
    int arr[] = {7, 12, 9, 11, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubble_sort(arr, n);
    return 0;
};
