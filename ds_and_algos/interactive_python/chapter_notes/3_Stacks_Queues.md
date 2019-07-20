# Part 3
**Objectives**
1. To understand the abstract data types stack, queue, deque, and list.
2. To be able to implement the ADTs stack, queue and deque using Python lists.
3. To understand the performance of the implementations of basic linear data structures.
4. To understand prefix, infix, and postfix expression formats.
5. To use stacks to evaluate postfix expressions
6. To use stacks to convert expressions from infix to postfix
7. To use queues for basic timing simulations
8. To be able to recognize problem properties where stacks, queues, and deques are appropriate data structures.
9. To be able to implement the abstract data type list as a linked list using the node and reference pattern.
10. To be able to compare the performance of our linked list implementation with Python's list implementation.


What are linear structures?

Linear structures can be thought of as having two ends. Sometimes these ends are referred to as the 'left'
or 'right', 'top' or 'bottom', 'front' or 'rear'. What distinguishes one linear structure from another
is the way in which items are added and removed, in particular the location where these additions and removals occur.

### Stack

A stack is an ordered collection of items where the addition of new items and the removal of existing items always takes
place at the same end. This end is commonly referred to as the 'top', the opposite as the 'base'.

The base of the stack is significant since these items were inserted first and have been in the stack the longest.
The ordering principle is sometimes called **LIFO, last-in first-out**. Newer items are placed on tip, while older
items are near the base.

A very popular stack problem is converting infix mathematical notation to postfix.


### Queue

A queue is an ordered collection of items where the addition of new items happens at one end,
called the 'rear' and the removal of existing items occurs at the other end, referred to as the 'front'

As an element is entered it starts at the rear and makes its way toward the front, waiting until that time when it
is the next element to be removed.

The most recently added item in the queue must wait at the end of the collection, the item that has been in the
collection the longest is at the front. This ordering principle is sometimes called **FIFO, first-in first-out**

Example: Printing queues. When at school and waiting for a paper to be printed is based on who pressed the
print button first. And, the hot potato game.

```python
def hotPotato(alist, num):
    q = adt.Queue()
    for name in alist:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()

    return q.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],6))
```

### Deque

A deque, also known as a double-ended queue, is an ordered collection of items similar to the queue. It has two ends, a front
and a rear, and the items remain postioned in the collection. What makes this data type different is
the unrestrictive nature of adding and removing items. New items can be added at either the front
or the rear. Likewise, existing items can be removed from either end. This hybrid structure
provides all the capabilities of stacks and queues in a single data structure.


| Method Name       | Use                       | Explanation                                                          |
|-------------------|---------------------------|----------------------------------------------------------------------|
| append            | deque.append(item)        | Insert a value, to the right end of deque |
| appendleft        | deque.insert(i, item)     | Insert a value, to the left end of the deque |
| pop               | deque.pop()               | Removes and returns the last item in a list |
| popleft           | deque.popleft()           | Removes and returns the ith item in a list |
| index             | deque.index(ele, beg, end)| Returns the first index of the value, starting search from beg till end |
| insert            | deque.insert(i, a)        | Inserts the value at index (i) |
| remove         | deque.remove(val)          | Removed the first occurrence of val mentioned |
| count          | deque.count(val)              | Counts the number of occurrences of val mentioned |
| extend         | deque.extend(iterable)               | Add multiple values at the right end |
| extendleft     | deque.extend(iterable)       | Add multiple values at the left end  |
| reverse        | deque.reverse()              | Reverse the elements in the deque    |
| del            | del alist[i]          | Deletes the item in the ith position           |



#### Examples of using deque from Collections

```python
from collections import deque
deq = deque([1, 2, 3, 4, 5])            # create a deque object holding [1, 2, 3, 4, 5]

print(deq)                          # deque([1, 2, 3, 4, 5])
deq.append(6)                       # Doesn't return anything, but instead adds 6 to the right, shown below
deq.appendleft(0)                   # Doesn't return anything, but instead adds 0 to the left, shown below
print(deq)                          # returns deque([0, 1, 2, 3, 4, 5, 6])
popright = deq.pop()                # returns 6
popleft = deq.popleft()             # returns 0
print(popleft, popright)            # returns 0 6
deq.popleft()                       # returns Nothing
print(deq)                          # returns deque([2, 3, 4, 5])

# Adding more elements for use of index
deq.appendleft(4)
deq.append(4)                       #
print(deq)                          # returns deque([4, 2, 3, 4, 5, 4])
del deq[1]
print(deq)

# Rotate 3 to the left
deq.rotate(-3)                      # returns deque([5, 4, 4, 3, 4])
deq.rotate(4)                       # returns deque([5, 4, 4, 3, 4])
print(deq)
```

### Node

The basic building block for the linked list implementation is the **node**.
Each node object must hold at least two pieces of information,
1. The node must contain the list item itself, this is called the data field of the node
2. Each node must hold a reference to the next node

### Unordered List

#### Introduction
The structure of an unordered list, is a collection of items where
each item holds a relative position with respect to the others.

In order to implement an unordered list, we will construct what is
commonly known as a linked list. We need to ensure we can maintain
the relative positioning of the items. It is important to note that
the location of the first item of the list must be explicitly specified.
Once we know where the first item is, the first item can tell us where
the second is, and so on. The external reference is often referred to
as the head of the list.

#### The Unordered List Class

The unordered list will be built from a collection of nodes, each linked
to the next through explicit references. As long as we know where to find
the first node (containing the first item), each item after that can be
found by successively following the next links. Our class must make
reference to the first node. Note: each list object will maintain a single
reference to the head of the list.

**Linked List Traversal**
Traversal refers to the process of systematically visiting each node.
To do this we use an external reference that starts at the first node
in the list. As we visit each node, we move the reference to the next
node by traversing the next reference.

# TODO, add details of how this class is constructed


