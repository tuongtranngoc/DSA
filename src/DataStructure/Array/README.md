
<head>
    <style>
        figure{text-align: center;}
        math{text-align: center;}
    </style>
</head>


# Array-Based Sequence
In the chapter, we explore Python's various sequence classes, namely the built-in `list`, `tuple` and `str` classes. There is significant commonality between these classes, most notably: each supports indexing to access an individual element of a sequence, using a syntax such as $seq[k]$, and each uses a low-level concept known as an `array` to represent the sequence. However, there are significant differences in the abstractions that these classes represent.

### Understand to Low-Level Array
The primary memory of a computer is composed of bits of information, and those bits are typically grouped into large units that depend upon the precise system architecture (such a typical unit is a **byte**, which is equivalent to 8 **bits**).

A computer system will keep track of what information is stored in what byte of memory, the computer uses an abstractive term known as `memory address`. In effect, each byte of memory is associated with a unique number that serves as its address.

<figure>
    <img src="/images/Array/memory_address.png">
</figure>

Computer hardware is designed, in theory, so that any byte of main memory (Random Access Memory - RAM) can be effectively accessed based on its memory address. Easy to retrieve byte #2144 as it is to retrieve byte #2159 and any individual byte of memory can be stored or retrieved in $O(1)$ time.

A group of related variables can be stored in a contiguous portion of the computer's memory. For instance, a text string is stored as an ordered sequence of individual characters.

<figure>
    <img src="/images/Array/string_store.png">
</figure>

A programmer can envision a more typical high-level abstraction of an array of characters as above figure.

<figure>
    <img src="/images/Array/high-level-store.png">
</figure>









