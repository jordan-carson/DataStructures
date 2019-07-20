# Trees and Tree Algorithms

**Objectives**
- To understand what a tree data structure is and how it's used
- To see how trees can be used to implement a map data structure
- To implement trees using a list
- To implement trees using classes and references
- To implement trees as a recursive data structure
- To implement a priority queue using a heap


### Examples of Trees

Trees are a non-linear data structure different than stacks, queues
and are used in many areas of computer science, including operating
systems, graphics, database systems, and computer networking.

A tree data structure has a root, branches, and leaves. The difference
between a tree in nature and a tree in computer science is that
a tree data structure has its root at the top and its leaves at the bottom
Trees are hierarchical, we mean that trees are structured in layers
with the more general things near the top and the more specific 
things near the bottom. The top of the hierarchy is the Parent,
the next layer are its children, then so on.

All children of one node are independent of the children of another node.
Another important property of trees, is that you can move entire
sections of a tree to a different position in the tree without affecting
the lower levels of the hierarchy. 

Examples:

British Royal Family Tree

Plant Genealogy


### Vocabulary and Definitions
Now that we have looked at examples of trees, let's define key words that will be used for our
formal definition of what a tree is exactly.

**Node**
A node is a fundamental part of a tree. It can have a name, 
which we call the "key". A node may also have additional
information. We call this additional information the "payload".
While the payload information is not central to many tree
algorithms, it is often critical in applications that make
use of trees.

**Edge**
An edge is another fundamental part of a tree. An edge connects
two nodes to show that there is a relationship between them.
Every node (except the root) is connected by exactly one
incoming edge from another node. Each node may have several 
outgoing edges.

**Root**
The root of the tree is the only node in the tree that has no
incoming edges. 

**Path**
A path is an ordered list of nodes that are connected by edges.
Mammal -> Carnivora -> Felidae -> Felis -> Domestica

**Children**
The set of nodes c that have incoming edges from the same
node to are said to be children of that node.

**Parent**
A node is the parent of all the nodes it connects to with 
outgoing edges. 

**Sibling**
Nodes in the tree that are children of the same parent are said
to be siblings

**Subtree**
A subtree is a set of nodes and edges comprised of a parent and all the
descendants of that parent.

**Leaf Node**
A leaf node is a node that has no children. 

**Level**
The level of a node n is the number of edges on the path from
the root node to n. By definition, the level of the root node 
is zero. 

**Height**
The height of a tree is equal to the maximum level of any node
in the tree. 

#### **Definitions of a Tree**

With the basic vocabulary now defined, we can move on to a formal
definition of a tree. In fact, we will provide two definitions of a tree.
One definition involves nodes and edges. The second definition, which will
prove to be very useful, is a recursive definition

_Definition one_: A tree consists of a set of nodes and a set 
of edges that connect pairs of nodes. A tree has the following
properties:

- One node of the tree is designated as the root node
- Every node n, except the root node, is connected by an edge
from exactly one other node p, where p is the parent of n.
- A unique path traverses from the root to each node.
- If each node in the tree has a maximum of two children, we 
say that the tree is a binary tree.

_Definition two_: A tree is either empty of consists of a root
and zero or more subtrees, each of which is also a tree. The
root of each subtree is connected to the root of the parent tree
by an edge. 

### Priority Queues with Binary Heaps

In earlier sections, we learned about the first-in first-out data structure called a queue. One
important variation of a queue is a **priority queue**. A priority queue acts like a queue in that
you deque an item by removing it from the front. However, in a priority queue the logical order of
items inside a queue is determined by their priority. The highest priority items are at the front
of the queue and the lowest priority items are at the back. Thus when you enqueue an item on a
priority queue, the new ite may move all the way to the front. We will see that the priority queue
is a useful data structure for some of the graph algorithms we will study in the next chapter. 

You can probably think of a couple of easy ways to implement a priority queue using sorting functions
and lists. However, inserting into a list is O(n) and sorting a list is O(n log n). We can do better.
The classic way to implement a priority queue is using a data structure called a **binary heap**. 
A binary heap will allow us both enqueue and dequeue items in O(log n).

The binary heap is interesting to study because when we diagram the heap it looks a lot like a tree,
but when we implement it we use only a single least as an internal representation. The binary
heap has two common variations: the **min heap**, in which the smallest key is always at the front, and
the **max heap**, in which the largest key value is always at the front. In this section we will implement
the min heap. We leave a max heap implementation as an exercise. 

In order to make our heap work efficiently, we will take advantage of the logarithmic nature
of the binary tree to represent our heap. In order to guarantee logarithmic performance, we must
keep our tree balanced. A balanced binary tree has roughly the same number of nodes in the left
and right subtrees of the root. A balanced binary tree has roughly the same number of nodes in the
left and right subtrees of the root. In our heap implementation we keep the tree balanced
by creating a **complete binary tree**. A complete binary tree is a tree in which each level has all of
its nodes. The exception to this is the bottom level of the tree, which we fill in from left to right. 

Another interesting property of a complete tree is that we can represent it using a single list. 
We do not need to use nodes and references or even lists of lists. Because the tree is complete, the
left child of a parent (at position p) is the node that is found in position 2p in the list. 
Similarly, the right child of the parent is at position 2p + 1 in the list. To find the parent of any node in the tree, 
we can simply use Pythons integer division. Given that a node is at position n in the list, the parent is at position
n/2. The list below shows a list representation of the tree, note the 2p and 2p + 1 relationship between
parent and children. The list representation of the tree, along with the full structure property, 
allows us to efficiently traverse a complete binary tree using only a few simple mathematical operations.
We will see that this also leads to an efficient implementation of our binary heap. 
```python
[0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
```

The method that we will use to store items in a heap relies on maintaining the heap order property.
The **heap order property** is as follows: In a heap, for every node x with parent p, the key in p
is smaller than or equal to the key in x. 

We begin our implementation of a binary heap with the constructor. You will notice that an empty binary
heap has a single zero as the first element of heapList and that this zero is not used, but is there
so that simple integer division can be used in later methods.

```python
class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
```

The next method we will implement is insert. The easiest, and most efficient, way to add an item to a list
is to simply append the item to the end of the list. The good news about appending is that
it guarantees that we will maintain the complete tree property. The bad news about appending
is that we will very likely violate the heap structure property. However, it is possible
to write a method that will allow up to regain the heap structure property by comparing the newly
added item with its parent. If the newly added item is less than its parent, than we can swap the item 
with its parent. 

When we percolate an item up, we are restoring the heap property between the newly added item
and its parent. We are also preserving the heap property for any siblings. Of course,
if the newly added item is very small, we may still need to swap it up another level. In fact,
we may need to keep swapping until we get to the top of the tree. The below method shows the percUp
which percolates a new item as far up in the tree as it needs to go to maintain the heap property. Here
is where our wasted element in heapList is important. Notice that we can compute the parent of 
any node by using simple integer division. The parent of the current node can be computed by dividing
the index of the current node by 2.

We are now ready to create the insert method. Most of the work in the insert method is really done
by percUp. Once a new item is appended to the tree, percUp takes over and positions the new item
properly. 

```python
def percUp(self, i):
    while i // 2 > 0:
        if self.heapList[i] < self.heapList[i // 2]:
            tmp = self.heapList[i // 2]
            self.heapList[i // 2] = self.heapList[i]
            self.heapList[i] = tmp
        i = i // 2

def insert(self, k):
    self.heapList.append(k)
    self.currentSize = self.currentSize + 1
    self.percUp(self.currentSize)
```

with the insert method properly defined above, we can now look at the delMin method. Since the heap
property requires that the root of the tree be the smallest item in the tree, finding the minimum 
item is easy. The hard part of delMin is restoring full compliance with the heap structure and heap
order properties after the root has been removed. We can restore our heap in two steps. First,
we will restore the root item by taking the last item in the list and moving it to the root position.
Moving the last item maintains our heal structure property. However, we have probably destroyed
the heap order property of our binary heap. Second, we will restore the heap order property
by pushing the new root node down the tree to its proper position. 

In order to maintain the heap order property, all we need to do is swap the root with its smallest
child less than the root. After the initial swap, we may repeat the swapping process with a node and its children
until the node is swapped into a position on the tree where it is already less than both children.
The code for percolating a node down the tree is found in the percDown and minChild methods.

```python
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
            
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
```

The code for delMin operation is below, notice again that all the hard word is done through
a helper function, in this case percDown.

To finish our discussion of binary heaps, we will look at a method to build an entire heap
from a list of keys. The first method you might think of may be like the following. Given
a list of keys, you could easily build a heap by inserting each key one at a time. Since
you are starting with a list of one item, the list is sorted and you could use binary search
to find the right position to insert the next key at a cost of approximately O(log n) operations.
However, remember that inserting an item in the middle of a list may require O(n) operations to shift
the rest of the list over to make room for the new key. Therefore, to insert n keys into the heap
would require a total of O(n log n) operations. However, if we start with an entire list than 
we can build the whole heap in O(n) operations. Below shows the code to build the entire heap.



#### Binary Search Trees

We have already seen two different ways to get key-value pairs in a collection. Recall that these
collections implement the map abstract data type. The two implementations of a map ADT we discussed
were binary search on a list and hash tables. In this section we will study **binary search trees**
as yet another way to map from a key to a value. In this case we are not interested in the exact 
placement of items in the tree, but we are interested in using the binary tree structure to provide
for efficient searching. 

A binary search tree relxies on the property that keys that are less than the parent
are found in the left subtree, and keys that are greater than the parent are found in the right subtree.
We will call this the **bst property**. As we implement the Map interface as described above, the bst
property will guide our implementation. All of the keys in the left subtree are less than the key in the root. 
All of the keys in the right subtree are greater than the root.

Now lets look at how to construct a binary search tree.
The search tree in Figure 1 represents the nodes that exist after we have inserted the following 
keys in the order shown: 70,31,93,94,14,23,73. Since 70 was the first key inserted into the tree, 
it is the root. Next, 31 is less than 70, so it becomes the left child of 70. Next, 93 is greater than 70, 
so it becomes the right child of 70. Now we have two levels of the tree filled, so the next key is going to 
be the left or right child of either 31 or 93. Since 94 is greater than 70 and 93, it becomes the right child of 
93. Similarly 14 is less than 70 and 31, so it becomes the left child of 31. 23 is also less than 31, 
so it must be in the left subtree of 31. However, it is greater than 14, so it becomes the right child of 14.

To implement the binary search tree, we will use the nodes and references approach similar to the one we used
to implement the linked list, and the expression tree. However, because we must be able to create and work
with a binary search tree that is empty, our implementation will use two classes. The first class we will
call BinarySearchTree, and the second class we will call TreeNode. The BinarySearchTree class has a reference
to the TreeNode that is the root of the binary search tree. In most cases the external methods defined in the
outer class simply check to see if the tree is empty. If there are nodes in the tree, the request is just
passed on to a private method defined in the BinarySearchTree class that it takes the root as the parameter. 
In the case where the tree is empty or we want to delete the key at the root of the tree, we must take
special action. The code for the BinarySearchTree class constructor along with a few other miscellaneous functions is
shown below:

```python
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
        
    def length(self):
        return self.size
```

The TreeNode class provides many helper functions that make the work done in the BinarySearchTree class methods
much easier. The constructor for a TreeNode, along with these helper functions, is shown below. As you can
see in the listing many of these helper functions help to classify a node according to its own position as a child,
(left or right) and the kind of children the node has. The TreeNode class will also explicitly keep track
of the parent as an attribute of each node. You will see why this is important when we discuss the implementation
for the del operator. 






























