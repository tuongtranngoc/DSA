# Linked List - Data Structure

### Linked List and Array

**Advantage and disadvantage**

| Array | Linked List |
|---|---|
| Arrays are stored in contiguous location | Linked lists are not stored in contiguous location |
| Fixed in size | Dynamic in size |
| Memory is allocated at complie time | Memory is allocated at run time |
| Uses less memory than linked lists | Uses more memory because it stores both data and the address of next node |
| Elements can be accessed easily | Element accessing requires the traversal of whole linked list |
| Insertion and deletion operation takes time | Insertion and deletion operation is faster |

**Time Complexity**

| Operation | Linked List | Array |
|--|--|--|
| Random Access | $O(N)$ | $O(1)$ |
| Insertion and deletion at beginning| $O(1)$ | $O(N)$ |
| Insertion and deletion at end| $O(N)$ | $O(1)$ |
| Insertion and deletion at random position| $O(N)$ | $O(N)$ |
