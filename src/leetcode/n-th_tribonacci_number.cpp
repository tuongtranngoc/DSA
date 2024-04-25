#include <iostream>

using namespace std;


int main() {
    int n;
    cin >> n;
    if (n==0) {
        cout << 0 << '\n';
    }
    else if (n==1 | n==2) {
        cout << 1 << '\n';
    }
    else {
        int t0 = 0;
        int t1 = 1;
        int t2 = 1;
        for (int i=3; i<=n; i++) {
            int prev = t0 + t1 + t2;
            t0 = t1;
            t1 = t2;
            t2 = prev;
        };
        cout << t2 << '\n';
    }
}