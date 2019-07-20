# Sorting and Search

##  Objectives of this Module
1. To be able to explain and implement sequential search and binary search
2. To be able to explain and implement select sort, bubble sort, merge sort, quick sort, insertion sort, and shell sort.
3. To understand the idea of hashing as a search technique
4. To introduce the map data type
5. To implement the map abstract data type using hashing.

### Introduction

Searching is the algorithmic process of finding a particular item in a collection of items. it typically answers True or False as to whether the item is present.
On occasion it may be modified to return where the item is found. for simplicity, take a look at the example below.

```python
print(15 in [1,2,3,4])  # returns False
print(4 in [1,2,3,4])   # returns True
```

When data items are stored in a collection such as a list, we say that they have a linear or sequential
relationship. Each data is stored in a position relative to others. In Python lists, these relative positions
are the index value of the individual items. Since these index values are ordered, it is possible for us to visit
them in sequence. This process gives rise to our first searching technique, the sequential search.

### Sequential Search

We start at the first item in the list, and simply move item to item, following the underlying sequential ordering
until we either find what we are looking for or run out of items, if we run out of items, we have discovered
that the item we are searching for is not present. to implement a sequential search, we need an array and the item.

```python
def seqentialSearchPractice(arr, item):
    isFound = False
    pos = 0
    while pos < len(arr) and not isFound:
        if arr[pos] == item:
            isFound = True
        else:
            pos += 1
    return isFound
```

#### Analysis of the above code
First we initialize a boolean variable called isFound and position of index (we are going to search from left to right) we then use a while loop which will return to True if our condition is met.

#### Analysis of searching algorithms
to analyze searching algorithms, we need to decide on a basic unit of computation. Recall that this is typically the common step that must be repeated in order to solve the problem. In search, it makes sense to count the number of comparisons performed. Each comparison may or may not discover the item we are looking for.

The list of items is not ordered in any way, and have been placed randomly into the list. Thus, the probability
that the item we are looking for is in any particular position is exactly the same for each position of the list.

If the item is not in the list, the only way to know it is to compare it against every item present.
If there are n items, then the sequential search requires n comparisons to discover that the item is not there.
in the case where the item is in the list, the analysis is not so straightforward. There are actually three different
scenarios that can occur. In the best case we will find the item in the first place we look, at the beginning of the list
We will only need one comparison, in the worst case, we will not discover the item until the very last comparison, the
nth comparison.

What if we change the above problem, with an array that has been sorted for us prior to our algorithm. What would this change?
the items are now in ascending order, from low to high.

```python
def orderedSequentialSearch(arr, item):
    pos = 0
    isFound = False
    isStop = False

    while pos < len(arr) and not isFound and not isStop:
        if arr[pos] == item:
            isFound = True
        else:
            if arr[pos] > item:
                isStop = True
            else:
                pos += 1
    return isFound

```

A sequential search is improved by ordering the list only in the case where
we do not find the item. 


### Binary Search

It is possible to take greater advantage of the ordered list if we are clever with out comparisons. 
In the sequential search, when we compare against the first item, there are at most n - 1 more items to look
through if the first item is not what we are looking for. Instead of searching the list in sequence, a binary
search will start by examining the middle item. If that is the one we are searching for, we are done.
If it is not the correct item, we can use the ordered nature of the list to eliminate half of the remaining items.
if the item we are searching for is greater than the middle item, we know that the entire lower half of the
list as well as the middle item can be eliminated from further consideration. The item, if its in the list, 
must be in the upper half. 

We then repeat the process with the upper half. Start at the middle and compare it against what we are
looking for, again, we either find it or split the list in half, therefore eliminating a large part of our 
possible search space. 

```python
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if first < last:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
```

This algorithm is a great example of a divide-and-conquer strategy. Divide the problem into smaller pieces,
solve the smaller pieces, and then reassemble the whole problem to get the result we want.

We do binary search over and over until we retrieve the result we want. We can rewrite the above 
function to a recursive solution:

```python
def binarySearch_recursive(arr, item):
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if arr[midpoint] == item:
            found = True
        else:
            if item < arr[midpoint]:
                return binarySearch_recursive(arr[:midpoint], item)
            else:
                return binarySearch_recursive(arr[midpoint:], item)

    return found

```

The results of the timer show that the recursive solution takes longer than the iterative.

```text
Binary Search 2 search recursive  0.0035475490149110556 milliseconds
Binary Search 2 search iterative  0.0025773500092327595 milliseconds
```

**Another example from Udacity**
```python
#!\usr\bin\Python2
def binary_search(input_array, value):
    """Your code goes here."""
    first = 0
    last = len(input_array) - 1
    isFound = False
    
    while first <= last and not isFound:
        midpoint = (first + last) // 2
        if input_array[midpoint] == value:
            isFound = True
            return midpoint
        elif input_array[midpoint] < value:
            first = midpoint + 1
        else: 
            last = midpoint - 1
        isFound = False
    if isFound:
        return midpoint
    else:
        return -1
    # return midpoint

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
```


### Hashing

So far we have been able to make improvements in our search algorithms by taking advantage of info
about where items are stored in the collection with respect to one another. By knowing if a list
is ordered, we can search in logarithmic time using binary search. We are going to take this one step
further by building a data structure that can be searched in O(1) time. This concept is known as **hashing**.

In order to do this, we will need to know even more about where the items might be when we go to 
look for them in the collection. If every item is where it should be, then the search can use a single comparison 
to discover the presence of an item. We will see, however, that this is typically not the case.

a **hash table** is a collection of items which are stored in such a way as to make it easy to find them later.
each position of the hash table, often called a **slot**, can hold an item and is named by an integer value
starting at 0. For example, we will have a slot named 0, a slot named 1, 2, and so on. Initially, the
hash table contains no items so every slot is empty. We can implement a hash table by using a list with 
each element initialized to the special Python value None. 


| 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 |
|----|----|----|----|----|----|----|----|----|----|----|
|None|None|None|None|None|None|None|None|None|None|None|


The mapping between an item and the slot where that item belongs in the hash
table is called the **hash function**. The hash function will take any item in the collection and
return an integer in the range of slot names, between 0 and _m_-1. Assume that we have the set of integer
items 54, 26, 93, 17, 77, and 31. Our first hash function, sometimes referred to as the "remainder method"
simply takes an item and divides it by the table size, returning the remainder as its hash value 
> h(item) = item % 11 

Once the hash values have been computed, we can insert each item into the hash table at the designated
position. Once we start loading the items into our hash table, the **load factor** will tell us the percentage
of occupancy (i.e. numberOfItems / tableSize)

Now when we want to search fo an item, we simply use the hash function to compute the slot name
for the item and then check the hash table to see if it is present. This searching operation is O(1),
since a constant amount of time is required to compute the hash value and then index the hash table
at that location. If everything is where it should be, we have found a constant time search algorithm. 

Now lets say, we have two items that map to the same location in the hash table. For example, if the item
33 or 44, both of these would map to the location 0 as 33 % 11 == 0, and 44 % 11 == 0. According to the hash function, 
two or more items would need to be in the same slot. This is referred to as a **collision**. Clearly, collisions create
problems for the hashing technique. 


### Sorting

Before we get into specific algorithms, we should think about the operations that can be used to
analyze a sorting process.
- First, it will be necessary to compare two values to see which is smaller (or larger). In order to sort
a collection, it will be necessary to have some systematic way to compare values to see if they are
out of order. 

#### Bubble Sort

The **bubble sort** makes multiple passes through a list, it compares adjacent items and exchanges those
that are out of order. Each pass through the list places the next largest value in its proper place.
In essence, each item 'bubbles' up to the location where it belongs.

In each pass, we place the next largest value in its place, the total number of 






