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

The **bubble sort** makes multiple passes through a list, it compares
adjacent items and exchanges those that are out of order. Each pass
through the list places the next largest value in its proper place.
In essence, each item 'bubbles' up to the location where it belongs.

In each pass, we place the next largest value in its place, the total
number of passes necessary will be n - 1. After completing n - 1
passes, the smallest item must be in the correct position with no further
processing required.

The exchange operation is sometimes called a swap, and in Python
is slightly different because you can perform simultaneous assignment.
The statement:
```python
a, b = b, a

alist = [1, 2, 3, 4]

def swap(alist):
    for i in range(len(alist)):
        alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist
```

will result in two assignment statements being done at the same time.
Using simultaneous assignment, the exchange operation can be done in
one statement.

Bubble sort takes advantage of this exchange operation

```python
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
```

To analyze bubble sort, we should note that regardless of how the items
are arranged in the initial list, n - 1 passes will be made to sort a list
of size n. The total number of comparisons is the sum of the first n - 1
integers. Recall that the sum of the first n integers is 1/2n^2 + 1/2n
The sum of the first n - 1 integers is 1/2n^2 + 1/2n - n, which is
1/2n^2 - 1/2n. This is still O(n^2) comparisons. In the best case,
if the list is already ordered no exchanges can be made. However, in the worst
case, every comparison will cause an exchange. On average, we exchange half
of the time.

A bubble sort is often considered the most **inefficient** sorting method
since it must exchange items before the final location is known.
These wasted exchanges are very costly, however, because the bubble sort
makes passes through the entire unsorted portion of the list, it has
the capability to do something must sorting algorithms cannot.
In particular, if during a pass there are no exchanges, then we know that
the list must be sorted. A bubble sort can be modified to stop early if
it finds that the list has become sorted. This means that for lists
that require just a few passes, a bubble sort may have an advantage
in that it will recognize the sorted list and stop

A shortened version of the Bubble Sort
```python
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)

```

#### Selection Sort

The selection sort improves on the bubble sort by making only one
exchange for every pass through the list. In order to do this, a selection sort looks for the largest value
as it makes a pass and, after completing the pass, places it in the proper
location. As with a bubble sort, after the first pass, the largest
item is in the correct place. After the second pass, the next largest
is in place. This process continues and requires n - 1 passes to sort
n items, since the final item must be in place after the (n -1) pass.

Example:
```python
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
```

This sorting method makes the same number of comparisons as the bubble
sort and is therefore also O(n^2). However due to the reduction in
the number of exchanges, the selection sort typically executes faster
in benchmark studies. In fact, for our list, the bubble sort makes 20 exchanges,
while the selection sort makes only


#### Insertion Sort

The insertion sort, although still O(n^2) works in a slightly different
way. It always maintains a sorted sublist in the lower positions of the list.
Each new item is then inserted back into the previous sublist
such that the sorted sublist is one item larger.

We begin by assuming that a list with one item (postition 0) is already
sorted. On each pass, one for each item 1 through n - 1, the current
item is checked against those in the already sorted sublist. As we look
back into the already sorted sublist we shift those items that are greater
to the right. When we reach a smaller item or the end of the sublist,
the current item can be inserted.

The maximum number of comparisons for an insertion sort is the sum of the
first n - 1 integers. Again, this is O(n^2). However, in the best case,
only one comparison needs to be done on each pass. This would be the case
for an already sorted list.

One note about shifting versus exchanging is also important. In general,
a shift operation requires approximately a third of the processing work
of an exchange since only one assignment is performed. In benchmark studies,
insertion sort will show very good performance.

Example below:

```python
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

```

#### Shell Sort

The shell sort, sometimes called the diminishing increment sort, improves
on the insertion sort by breaking the original list into a number of
smaller sublists, each of which is sorted using an insertion sort.
The unique way that these sublists are chosen is the key to the shell
sort. Instead of breaking the list into sublists of contiguous items,
the shell sort uses an increment i, sometimes called the gap, to create
a sublist by choosing all items that are i items apart.

```python
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

```

At first glance you may think that a shell sort cannot be better than
an insertion sort, since it does a complete insertion sort as the last step.
It turns out, however, that this final insertion sort does not need to do
very many comparisons (or shifts) since the list has been pre-sorted by
earlier incremental insertion sorts, as described above. In other words,
each pass produces a list that is "most sorted" than the previous one.
This makes the final pass very efficient.

Although a general analysis of the shell sort is well beyond the scope of this
text, we can say that it tends to fall somewhere between O(n) and O(n^2)
based on the behavior described above. changing the increment, using
2^k - 1 (1, 3, 7, 15, 31, and so on) a shell sort can perform at O(n^3/2)

#### Merge Sort

We now turn our attention to using a divide and conquer strategy as a
way to improve the performance of sorting algorithms. The first
algorithm we will study is the **merge sort**. Merge sort is a recursive
algorithm that continually splits a list in half. If the list is empty
or has one item, it is sorted by definition (the base case). If the
list has more than one item, we split the list and recursively invoke
a merge sort on both halves. Once the two halves are sorted, the fundamental
operation, called a merge is performed. Merging is the process of taking
two smaller sorted lists and combining them together into a single, sorted,
new list.

The mergeSort function below begins by asking the base case question.
If the length of the list is less than or equal to one, then we
already have a sorted list and no more processing is necessary. If,
on the other hand, the length is greater than one, then we use the slice
operation to extract the left and right halves. It is important
to note that the list may not have an even number of items. That does
not matter, as the lengths will differ by at most one.

```python
def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
```

Once the mergeSort function is invoked on the left half and the right
half, it is assumed they are sorted. The rest of the function is
responsible for merging the two smaller sorted lists into a larger
sorted list. Notice that the merge operation takes places the items back
into the original list (alist) one at a time by repeatedly taking the
smallest item from the sorted lists.

Analyzing the mergeSort function, we need to consider the two distinct
processes that make up its implementation. First, the list is split
into halves. We already computed (in a binary search) that we can divide
a list in half log n times where n is the length of the list. The second
process is the merge. Each item in the list will eventually be processed
and placed on the sorted list. So the merge operation which
results in a list of size n requires n operations. The result of this analysis
is that log n splits, each of which costs n for a total of n log n operations
a merge sort is a O(n log n) algorithm.

Recall, that the slicing operator is a O(k) where k is the size of the slice
In order to guarantee that mergeSort O(n log n) we need to remove the slice
operator, this is possible if we simply pass the starting and ending indices
along with the list when we make the recursive call.


#### Quick Sort

Uses a divide and conquer to gain the same advantages as the merge sort,
while not using the additional storage. As a trade-off, however,
it is possible that the list may not be divided in half. When this
happens, we will see that performance is diminished.

A quick sort first selects a value, which is called the **pivot value**.
Although there are many different ways to choose the pivot value,
we will simply use the first item in the list. The role of the pivot
value is to assist with splitting the list. The actual position where
the pivot value belongs in the final sorted list, commonly called
the **split point**, will be used to divide the list for subsequent
calls to the quick sort.

```python
[54, 26, 93, 17, 77, 31, 44, 55, 20]
```
Using the example above again, 54 will serve as our first pivot value.
Since we have looked at this example a few times already, we know that
54 will eventually end up in the position currently holding 31.
the **partition** process will happen next. It will find the split point
and at the same time move other items to the appropriate side of the list
either less than or greater than the pivot value.

Partitioning begins by locating two position markers - lets call them
leftmark and rightmark - at the beginning and end of the remaining items
in the list (positions 1 and 8) the goal of the partition process is
to move items that are on the wrong side with respect to the pivot value
while also converging on the split point. See below image as we locate
the position of 54.

![Figure 1:](quick_sort_1.png "Figure 1")

We begin my incrementing leftmark until we locate a value that is greater
than the pivot value. We then decrement rightmark until we find a value
that is less than the pivot value. At this point we have discovered
two items that are out of place with respect to the eventual split point.
For our example, this occurs at 93 and 20. Now we can exchange these two
items and then repeat the process again.

At the point where rightmark becomes less than leftmark, we stop. The
position of rightmark is now the split point. The pivot value can be
exchanged with the contents of the split point and the pivot value
is now in place. In addition, all the items to the left of the split point
are less than the pivot value, and all the items to the right of the
split point are greater than the pivot value. The list can now be
divided at the split point and the quick sort can be invoked recursively
on the two halves.

```python
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
```

The above code invokes a recursive function, quickSortHelper.
QuickSortHelper begins with the same base case as the merge sort.
If the length of the list is less than or equal to one, it is already sorted.
If it is greater, then it can be partitioned and recursively sorted.
The partition function implements the process described above.

To analyze the quick sort function, note that for a list of length n,
if the partition always occurs in the middle of the list, there will
again be log n divisions. In order to find the split point, each of
the n items needs to be checked against the pivot value. The result
is n log n. In addition, there is no need for additional memory
as in the merge sort process.

Unfortunately, in the worst case, the split points may be in the middle
and can be very skewed to the left or the right, leave a very uneven
division. In this case, sorting a list of n items divides into sorting
a list of 0 items and a list of n - 1 items. Then sorting a list of n - 1
divides a list of size 0 and a list of size n - 2 and so on.
The result is an O(n^2) sort with all of the overhead that recursion requires.

We mentioned earlier that there are different ways to choose the pivot
value. In particular, we can attempt to alleviate some of the potential for
an uneven division by using a technique called median of three. To choose
the pivot value, we will consider the first, the middle, and the last
element in the list. In our example, those 54, 77, and 20. Now pick the
median value, in our case 54, and use it for the pivot value (of course,
that was the pivot value we used originally). The idea is that in the case where
the item in the list does not belong toward the middle of the list, the median
of three will choose a better 'middle' value. This will be particularly
useful when the original list is somewhat sorted to begin with. We leave
the implementation of this pivot value selection as an exercise.

### Summary

A sequential search is O(n) for ordered and unordered lists.
A binary search of an ordered list is O(log n) in the worst case.
Hash tables can provide constant time searching.
A bubble sort, a selection sort, and an insertion sort are O(n2) algorithms.
A shell sort improves on the insertion sort by sorting incremental sublists. It falls between O(n)
and O(n2).
A merge sort is O(n log n), but requires additional space for the merging process.
A quick sort is O(n log n), but may degrade to O(n2) if the split points are not near the middle of the list. It does not require additional space.

# https://chrisalbon.com/python/basics/sort_a_list_of_strings_by_length/
