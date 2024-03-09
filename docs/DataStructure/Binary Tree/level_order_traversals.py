from __future__ import division
from __future__ import print_function
from __future__ import absolute_import


class BSTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_height_tree(tree:BSTree):
    if not tree:
        return 0
    else:
        right = find_height_tree(tree.right)
        left = find_height_tree(tree.left)
        return max(right + 1, left+1)


def level_traversal(node, level):
    if node is None:
        return 
    if level == 1:
        print(node.value, end=' ')
    elif level > 1:
        level_traversal(node.left, level-1)
        level_traversal(node.right, level-1)


def naive_traversal(tree: BSTree):
    """
    Time complexity: O(N) - N is the number of nodes in the tree
    Auxiliary Space: O(1)
    """
    if tree is None:
        return 

    height = find_height_tree(tree)
    for level in range(1, height+1):
        print(f'Level {level}')
        level_traversal(tree, level)
        print()


def queue_traversal(tree:BSTree):
    """
    Time complexity: O(N)
    Auxiliary Space: O(N)
    """
    if tree is None:
        return None
    
    queue_tree = []
    queue_tree.append(tree)
    
    while(len(queue_tree) > 0):
        print(queue_tree[0].value, end=' ')
        node = queue_tree.pop(0)
        if node.left is not None:
            queue_tree.append(node.left)
        if node.right is not None:
            queue_tree.append(node.right)
    print()

        
bst = BSTree('A')
bst.left = BSTree('B')
bst.right = BSTree('C')

bst.left.left = BSTree('D')
bst.left.right = BSTree('E')

bst.left.left.left = BSTree('F')

bst.right.left = BSTree('G')
bst.right.right = BSTree('H')


queue_traversal(bst)