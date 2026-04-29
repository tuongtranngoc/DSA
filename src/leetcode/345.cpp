// https://leetcode.com/problems/reverse-vowels-of-a-string

#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    string reverseVowels(string s) {
        unordered_set<char> vowels = {
            'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
        };
        int left = 0;
        int right = s.size() - 1;

        while (left < right) {
            while (left < right && !vowels.count(s[left])) left++;
            while (left < right && !vowels.count(s[right])) right--;
            if (left < right) swap(s[left++], s[right--]);
        }
        return s;
    }
};

int main() {
    Solution sol;
    string s;
    cin >> s;
    cout << sol.reverseVowels(s) << endl;
}