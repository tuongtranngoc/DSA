from __future__ import division
from __future__ import print_function
from __future__ import absolute_import


class BSTree:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None


def DFS(tree: BSTree):
    if tree is None:
        return 0
    else:
        left = DFS(tree.left)
        right = DFS(tree.right)

        return max(left + 1, right + 1)


def level_order_traversal(tree: BSTree):
    l_depth = 0
    r_depth = 0
    if tree is None:
        return 0
    else:
        queue_tree = []
        queue_tree.append(tree)

        while (len(queue_tree)>0):
            node = queue_tree.pop(0)
            if node.left is not None:
                queue_tree.append(node.left)
                l_depth += 1
            if node.right is not None:
                queue_tree.append(node.right)
                r_depth += 1
        return max(r_depth, l_depth)


bst = BSTree('A')
bst.left = BSTree('B')
bst.right = BSTree('C')

bst.left.left = BSTree('D')
bst.left.right = BSTree('E')

bst.left.left.left = BSTree('F')

bst.right.left = BSTree('G')
bst.right.right = BSTree('H')

print(DFS(bst))
print(level_order_traversal(bst))
