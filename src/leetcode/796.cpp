// https://leetcode.com/problems/rotate-string

#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    bool rotateString(string s, string goal) {
        int n = s.length();
        int m = s.length();
        if (n != m) {
            return false;
        }

        for (int i = 0; i < n; i++) {
            string si = s.substr(i) + s.substr(0, i);
            if (si == goal) {
                return true;
            }
        }
        return false;
    }
};

int main() {
    Solution sol;
    string s;
    string goal;
    cin >> s >> goal;
    cout << sol.rotateString(s, goal) << endl;
}