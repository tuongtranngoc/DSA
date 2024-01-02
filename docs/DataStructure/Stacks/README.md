# Stacks

A stack is a linear data structure in which the insertion of a new element and removal of an existing element take place at the same end representing the top of the stack (**LIFO principle**). 

When using the stack, the pointer always maintains on the top of the stack, which is the position that the last element to be inserted. 

## Basic Operations

A stack is an abstract data type (ADT) such that an instance **S** supports the following methods:

+ **S.push()**: Add element **e** to the top stack **S**.
+ **S.pop()**: Remove and return the top element from the stack **S**; an error occurs if the stack is empty.
+ **S.top()**: Return a reference to the top element of stack **S**, without removing it; an error occurs if the stack is empty.
+ **S.is_empty()**: Return True if stack **S** does not contain any elements.
+ **len(S)**: Return the number of elements in stack **S**.

<p align="center">
    <img src="../../../images/Stack/Stack-660x566.png">
</p>

## Complexity Analysis

### Time Complexity

| Operations | Complexity |
| -- | -- |
| **push()** | O(1) |
| **pop()** | O(1) |
| **is_empty()** | O(1) |
| **size()** | O(1) |

