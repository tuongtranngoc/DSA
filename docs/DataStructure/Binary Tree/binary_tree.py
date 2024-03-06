from __future__ import division
from __future__ import print_function
from __future__ import absolute_import


class BSTree:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def traversal_inorder(bst: BSTree):
    if bst:
        traversal_inorder(bst.left)
        print(bst.value, end='-')
        traversal_inorder(bst.right)


def traversal_preorder(bst: BSTree):
    if bst:
        print(bst.value, end='-')
        traversal_preorder(bst.left)
        traversal_preorder(bst.right)


def traversal_postorder(bst: BSTree):
    if bst:
        traversal_postorder(bst.left)
        traversal_postorder(bst.right)
        print(bst.value, end='-')


bst = BSTree('A')
bst.left = BSTree('B')
bst.right = BSTree('C')

bst.left.left = BSTree('D')
bst.left.right = BSTree('E')

bst.left.left.left = BSTree('F')

traversal_inorder(bst)
print()
traversal_preorder(bst)
print()
traversal_postorder(bst)
print()