# Implementation of binary tree using array - Python

binary_tree = [None] * 100

def root_tree(value):
    if binary_tree[0] is None:
        binary_tree[0] = value
    else:
        print('Binary tree already had value of root')


def set_left_node(parent, value):
    if binary_tree[parent] is not None:
        binary_tree[2*parent + 1] = value
    else:
        print('Node is not exist, can not set left value of node')


def set_right_node(parent, value):
    if binary_tree[parent] is not None:
        binary_tree[2*parent+2] = value
    else:
        print('Node is not exist, can not set right value of node')


def visualize_binary_tree():
    """
         A(0)    
        /   \
        B(1)  C(2)  
    /   \      \
    D(3)  E(4)   F(6) 
    
    """

