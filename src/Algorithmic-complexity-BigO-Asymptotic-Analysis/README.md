# Asymptotic Notation and Analysis (Based on input size) in Complexity Analysis of Algorithms

In Asymptotic Analysis, to evaluate the performance of an  algorithm (do not measure the actual running time). We calculate, how the time (or space) taken by an algorithm increases  with the input size.

`Asymptotic Notation` is a way to describe the running time or space complexity of an algorithm based on the input size. There are three commonly used notations: BigO ($O$), Omega ($\Omega$), Theta ($\Theta$).

## Big O notation ($O$)

Let $f(n)$ and $g(n)$ be functions mapping positive integers to positive real numbers. We say that $f(n)$ is $O(g(n))$ if there is a real constant $c$ > 0 and integer constant $n_0 >= 1$ such that 
$$f(n) <= c. g(n), \forall n >= n_0$$

<p>
    <image src="../../images/BigO.png">
</p>

**Example**:  The function $25n + 97$ is $O(n)$

**Justification**: By the Big-O definition,  