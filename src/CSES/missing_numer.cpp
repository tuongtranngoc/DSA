#include <iostream>
#include <unordered_map>

using namespace std;

int find_missing(int arr[], int n) {
    int missing_num;
    unordered_map<int, int> num_dict;
    for (int i=1;i<=n;i++) {
        num_dict[i] = 0;
    }
    for (int i=1; i<=n; i++) {
        num_dict[arr[i-1]] += 1;
    }
    for (int i=1; i<=n; i++) {
        if (num_dict[i] == 0) {
            missing_num = i;
            break;
        }
    }
    return missing_num;
}


int main() {
    int n, missing_num;
    cin >> n;
    int arr[n];
    for (int i=0; i<n-1; i++) {
        cin >> arr[i];
    }
    cout << find_missing(arr, n);

}
