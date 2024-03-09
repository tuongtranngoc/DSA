from __future__ import division
from __future__ import print_function
from __future__ import absolute_import


class BSTree:
    def __init__(self, value, left=None, right=None):
        self.value = value  
        self.left = left
        self.right = right


def levelorder_insert(tree, value):
    if tree is None:
        tree = BSTree(value)
        return
    else:
        queue_tree = []
        queue_tree.append(tree)

        while (len(queue_tree)>0):
            tree = queue_tree[0]
            queue_tree.pop(0)

            if tree.left is None:
                tree.left = BSTree(value)
                break
            else:
                queue_tree.append(tree.left)

            if tree.right is None:
                tree.right = BSTree(value)
                break
            else:
                queue_tree.append(tree.right)


def printTree(tree):
    if tree is None:
        return
    printTree(tree.left)
    print(tree.value, end=' ')
    printTree(tree.right)
        


bst = BSTree('A')
bst.left = BSTree('B')
bst.right = BSTree('C')

bst.left.left = BSTree('D')
bst.left.right = BSTree('E')

bst.left.left.left = BSTree('F')

bst.right.left = BSTree('G')
bst.right.right = BSTree('H')

printTree(bst)
print()
levelorder_insert(bst, 'inserted')
printTree(bst)
print()
