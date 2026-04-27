#include <bits/stdc++.h>
#include <set>
using namespace std;


int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

bool is_divisor_string(const string& x, const string& y) {
    if (x.length() % y.length() != 0) {
        return false;
    }

    int d = x.length() / y.length();
    for (int i = 0; i < d; i++) {
        if (x.substr(i * y.length(), y.length()) != y) {
            return false;
        }
    }
    return true;
}

int main() {
    string a, b;
    cin >> a >> b;
    int m = a.length();
    int n = b.length();
    int g = gcd(m, n);
    
    int result = 0;

    set<int> gs;
    for (int i = 1; i <= g; i++) {
        if (g % i == 0) {
            string c = a.substr(0, i);
            if (is_divisor_string(a, c) && is_divisor_string(b, c)) {
                result++;
            }
        }
    }
    cout << result;
}