# Part 2: Big-O Notation

**Objectives**
1. To understand why algorithm analysis is important
2. To be able to use "Big-O" to describe execution time
3. To understand the "Big-O" execution time of common operations on Python Lists and Dictionaries.
4. To understand how the implementation of Python data impacts algorithm analysis
5. To understand how to benchmark simple Python programs

An algorithm is a step-by-step list of instructions for solving a problem.

Algorithm analysis is concerned with comparing algorithms based upon the amount of computing resources that each algorithm uses.
We want to be able to consider two algorithms and say that one is better than the other because it is more efficient in its use of
those resources or because it simple uses fewer. 

When we speak of computing resources this can mean two things; 
- to consider the amount of space or memory an algorithm requires to solve the problem. The amount of space is typically dictated by the problem instance itself.
- to consider the amount of time they require to execute. This is sometimes referred to as the 'execution time' or 'running time' of the algorithm. This means that we will track the actual time required for the program to compute its result.

let's consider the following code..

```python
import time

def sumOfN(n):
    start_time = time.time()
    
    theSum = 0
    for i in range(1, n+1):
        theSum += i
    end_time = time.time()
    total_time = (end_time - start_time)
    return theSum, total_time
    
for i in range(5):
    print("Sum is %d required %10.7f seconds"%sumOfN(10000))
```
The output of the above for loop prints the below after 5 iterations.

```text
Sum is 50005000 required  0.0006018 seconds
Sum is 50005000 required  0.0006011 seconds
Sum is 50005000 required  0.0007710 seconds
Sum is 50005000 required  0.0006001 seconds
Sum is 50005000 required  0.0005991 seconds
```

if we modify the above sumOfN function to compute the sum of the first n integers without iterating, will this help us to reduce the execution time?

```python
import time
def sumOfN2(n):
    start = time.time()
    answer = (n*(n+1)) / 2
    end = time.time()
    return answer, end-start
```

And apply the same benchmark measurement for the above sumOfN function, we get the following result.

```text
Sum is 50005000 required  0.0000012 seconds
Sum is 50005000 required  0.0000000 seconds
Sum is 50005000 required  0.0000000 seconds
Sum is 50005000 required  0.0000000 seconds
Sum is 50005000 required  0.0000012 seconds
```

A few things to note, that the iterative solution does take far longer than the non-iterative approach, most likely because there are some steps being repeated.
And as we increase N the iterative approach appears to increase. All of this is fine, when comparing on a single machine, using the same programming language.

However, this is most likely not always the case. We need to come up with a better solution, and a more useful measurement being independent of any particular machine, program, time of day, compiler, and programming language.

When trying to characterize an algorithms efficiency in terms of execution time, independent of any particular program or computer
it is important to quantify the number of operations or steps that the algorithm will require.
If each of these steps is considered to be a basic unit of computation, then the execution time for an algorithm can be expressed as the number of steps required to solve the problem.

**The order of magnitude** is often called **Big-O** notation for "order" and written as O(f(n)). 

It provides a useful approximation to the actual number of steps in the computation. 

Let's use the sumOfN algorithm for an example. The number of assignment statements is 1 (thSum=0) plus the
value of n (the number of times we perform theSum = theSum + i). We can denote this by a function, call it T, 
where T(n) = 1 + n. the parameter n is often referred to as the 'size of the problem'. 

As n gets large, the constant 1 becomes less and less significant to the final result. If we are looking for an approximation for T(n), 
then we can drop the 1 and simply say that the running time is O(n). 

It is very important when discussing an algorithms performance to characterize the times in terms of best case, **worst case** or
average performance. The worst case performance refers to a particular data set where as the same algorithm can be used on another data set and obtain good performance.

A number of very common order of magnitude function are shown below.

A list of the common order of magnitude functions. 

| f(n)    | Name        |
|---------|-------------|
| 1       | Constant    |
| log n   | Logarithmic |
| n       | Linear      |
| n log n | Log Linear  |
| n^2     | Quadratic   |
| n^3     | Cubic       |
| 2^n     | Exponential |
| n!      | Factorial   |

When browsing an algorithms efficiency we need to state that although algorithm speed is an important part, we should not sacrifice space in order to gain time.
This is a common occurrence, in many occasions one will need to make decisions between time and space trade-offs.

### Performance of Python Data Structures

##### Big-O Efficiency of Basic List Operations
| Operation        | Big-O Efficiency |
|------------------|------------------|
| index []         | O(1)             |
| index assignment | O(1)             |
| append           | O(1)             |
| pop()            | O(1)             |
| pop(i)           | O(n)             |
| insert(i, item)  | O(n)             |
| copy             | O(n)             |
| del operator     | O(n)             |
| iteration        | O(n)             |
| contains (in)    | O(n)             |
| get slice [x:y]  | O(k)             |
| del slice        | O(n)             |
| set slice        | O(n+k)           |
| Extend[1]        | O(k)             |
| reverse          | O(n)             |
| concatenate      | O(k)             |
| sort             | O(n log n)       |
| multiply         | O(nk)            |
| Get length       | O(1)             |

##### Big-O Efficiency of Basic Dictionary Operations
| Operation     | Big-O Efficiency |
|---------------|------------------|
| copy          | O(n)             |
| get item      | O(1)             |
| set item      | O(1)             |
| delete item   | O(1)             |
| contains (in) | O(1)             |
| iteration     | O(n)             |


