from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

'''Doubly Linked List

Head --> [prev, data, next] --> [prev, data, next] --> ... --> Null
Null <--                    <--                    <--      
     
'''


class Node:
    def __init__(self, data=None, prev=None, next=None) -> None:
        self.prev = prev
        self.next = next
        self.data = data

    
class Begin_DLL:
    """Add a node at begin of the list
    Time Complexity: O(1)
    Auxiliary Space: O(1)
    """
    def __init__(self) -> None:
        self.head = None

    def begin_push(self, new_data):
        new_node = Node(data=new_data)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def end_push(self, new_data):
        new_node = Node(data=new_data)
        last = self.head
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        
        while last.next is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last






