#include<bits/stdc++.h>

using namespace std;

char binary_tree[10];

int root_tree(char value) {
    if (binary_tree[0] == '\0')
        binary_tree[0] = value;
    else
        cout << "Binary tree already had value of root";
}


int set_left_node(char value, int node) {
    if (binary_tree[node] == '\0')
        binary_tree[2*node+1] = value;
    else
        cout << "";
}


int set_right_node(char value, int node) {
    if (binary_tree[node] == '\0')
        binary_tree[2*node+2] = value;
    else
        cout << "";
}


int main() {
    
}