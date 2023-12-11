
# Array-Based Sequence
In the chapter, we explore Python's various sequence classes, namely the built-in `list`, `tuple` and `str` classes. There is significant commonality between these classes, most notably: each supports indexing to access an individual element of a sequence, using a syntax such as $seq[k]$, and each uses a low-level concept known as an `array` to represent the sequence. However, there are significant differences in the abstractions that these classes represent.

### Understand to Low-Level Array
The primary memory of a computer is composed of bits of information, and those bits are typically grouped into large units that depend upon the precise system architecture (such a typical unit is a **byte**, which is equivalent to 8 **bits**).

A computer system will keep track of what information is stored in what byte of memory, the computer uses an abstractive term known as `memory address`. In effect, each byte of memory is associated with a unique number that serves as its address.

<p align="center">
    <img src="/images/Array/memory_address.png">
</p>

Computer hardware is designed, in theory, so that any byte of main memory (Random Access Memory - RAM) can be effectively accessed based on its memory address. Easy to retrieve byte #2144 as it is to retrieve byte #2159 and any individual byte of memory can be stored or retrieved in $O(1)$ time.

A group of related variables can be stored in a contiguous portion of the computer's memory. For instance, a text string is stored as an ordered sequence of individual characters.

<p align="center">
    <img src="/images/Array/string_store.png">
</p>

A programmer can envision a more typical high-level abstraction of an array of characters as above figure.

<p align="center">
    <img src="/images/Array/high-level-store.png">
</p>

## Referential Arrays

Python represents a list or tuple instance using an internal storage mechanism of an array of object `references`. Although the relative size of the individual elements may vary, the number of bits used to store the memory address of each is fixed. In this way, Python can support constant-time access to a list or tuple elements based on its index.

## Dynamic Array
Although a list has a particular length when constructed, the list class allows us to add to the list without an apparent limit on the overall capacity of the list. Python uses an algorithmic sleight of hand known as a `dynamic array`.

Algorithm:
1. Allocate a new array B with a larger capacity.
2. Set $B[i] = A[i], \forall i=0, ..., n-1$, where $n$ denotes current number of items.
3. Set $A=B$, that is, we use $B$ as the array supporting the list.
4. Insert the new element in a new array.

<p align="center">
    <img src="/images/Array/dymamic_array.png">
</p>

## Asymptotic Analysis

Asymptotic of performance the **list** class:

<p align="center">
    <img src="/images/Array/Asymptotic_list.png">
</p>

