# Asymptotic Notation and Analysis (Based on input size) in Complexity Analysis of Algorithms

In Asymptotic Analysis, to evaluate the performance of an algorithm (do not measure the actual running time). We calculate, how the time (or space) taken by an algorithm increases  with the input size.

`Asymptotic Notation` is a way to describe the running time or space complexity of an algorithm based on the input size. There are three commonly used notations: Big-O ($O$), Big-Omega ($\Omega$), Big-Theta ($\Theta$).

<p>
    <image src="/images/Algorithmic-complexity-BigO-Asymptotic-Analysis/asymptotic.png">
</p>

## Big-O notation

Let $f(n)$ and $g(n)$ be functions mapping positive integers to positive real numbers. We say that $f(n)$ is $O(g(n))$ if there is a real constant $c$ > 0 and integer constant $n_0 >= 1$ such that 
$$f(n) <= c. g(n), \forall n >= n_0$$

**Example**:  The function $25n + 97$ = $O(n)$

**Justification**: By the Big-O definition ,
$$25n + 97 <= c.n, \forall n>=n_0$$

We can choice $n_0=1, c=125$ to satisfy the above inequality.

## Big-Omega notation

Let $f(n)$ and $g(n)$ be functions mapping positive integers to positive real numbers. We say that $f(n)$ is $\Omega(g(n))$ if $g(n)$ is $O(f(n))$, that is, there is a real constant $c > 0$ and an integer constant $n_0>=1$ such that

$$f(n) >= cg(n), \forall n>=n_0$$


## Big-Theta notation

Let $f(n)$ and $g(n)$ be functions mapping positive integers to positive real numers. We say that $f(n)$ is $\Theta(g(n))$ if $f(n)$ is $O(g(n))$ and $f(n)$ is $\Omega(g(n))$ that is, there is a real constants $c'>0, c'' > 0$, and an integer constant $n_0>=1$ such that

$$c'g(n) <= f(n) <= c''g(n), \forall n>=n_0$$

## Some classes of functions
+ $O(1)$: constant
+ $O(log \space n)$: logarithmic
+ $O(n)$: linear
+ $O(n \space log \space n)$: superlinear
+ $O(n^2)$: quadratic
+ $O(n^3)$: cubic
+ $O(n^k)$: polynomial $k>=1$
+ $O(a^n)$: exponential $a >1$