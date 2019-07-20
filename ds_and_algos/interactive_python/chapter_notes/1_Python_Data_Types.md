# Introduction (Part 1)
## Python Data Types

This is the introduction to a course in algorithms and data structures
using the below link.

The solutions to problems and test cases will be written solely in Python 3 (3.6)

Author: Jordan Carson

[Algorithms & Data Structures Course](http://interactivepython.org/runestone/static/pythonds/Introduction/toctree.html)

##### Table 1: Relational and logical operators with examples shown below
| Operation Name        | Operator | Explanation                                                     |
|-----------------------|----------|-----------------------------------------------------------------|
| less than             | <        | Less than operator                                              |
| greater than          | >        | Greater than operator                                           |
| less than or equal    | <=       | Less than or equal to operator                                  |
| greater than or equal | >=       | Greater than or equal to operator                               |
| equal                 | ==       | Equality operator                                               |
| not equal             | !=       | Not equal operator                                              |
| logical and           | and      | Both operands True for result to be True                        |
| logical or            | or       | One or the other operand is True for the best result to be True |
| logical not           | not      | Negates the truth value, False becomes True, True becomes False |

Below shows implementation of Logical Operators:

```python
print(5 == 10)                  # returns False
print(10 > 5)                   # returns True
print((5 >= 1) and (5 <= 10))   # returns True
```

Python has a number of very powerful built-in collection classes. Lists, strings,
and tuples are ordered collections that are very similar in structure but
have specific differences that must be understood for them to be used properly.
Sets and dictionaries are **unordered** collections.

## Lists

A **list** is an ordered collection of zero or more references to Python data objects.
Lists are written as comma-separaed values enclosed in square brackets. Shown Below:

```python
[1, 3, True, 18.18]
alist = [1, 3, True, 18.18]
print(alist)                # returns [1, 3, True, 18.18]
```

Since lists are considered to be sequentially ordered, they support a number
of operations that can be applied to any Python sequence.

| Operation Name | Operator | Explanation                            |
|----------------|----------|----------------------------------------|
| indexing       | []       | Access an element of a sequence        |
| concatenation  | |        | Combine sequences together             |
| repetition     | *        | Concatenate a repeated number of times |
| membership     | in       | Ask whether an item is in a sequence   |
| length         | len      | Ask the number of items in a sequence  |
| slicing        | [:]      | Extract a part of a sequence           |


Lists support a number of methods that will be used to build data
structures

##### Lists Methods to build Data Structures
| Method Name | Use                   | Explanation                                       |
|-------------|-----------------------|---------------------------------------------------|
| append      | alist.append(item)    | Adds a new item to the end of a list              |
| insert      | alist.insert(i, item) | Inserts an item at the ith position in a list     |
| pop         | alist.pop()           | Removes and returns the last item in a list       |
| pop         | alist.pop(i)          | Removes and returns the ith item in a list        |
| sort        | alist.sort()          | Modifies a list to be sorted                      |
| reverse     | alist.reverse()       | Modifies a list to be in reverse order            |
| del         | del alist[i]          | Deletes the item in the ith position              |
| index       | alist.index(item)     | Returns the index of the first occurrence of item |
| count       | alist.count(item)     | Returns the number of occurrences of item         |
| remove      | alist.remove(item)    | Removes the first occurrence of item              |

#### Full Table of Lists Methods

| Method Name | Use                   | Explanation                                       |
|-------------|-----------------------|---------------------------------------------------|
| append        | alist.append(item)    | Adds a new item to the end of a list              |
| insert        | alist.insert(i, item) | Inserts an item at the ith position in a list     |
| pop           | alist.pop()           | Removes and returns the last item in a list       |
| pop           | alist.pop(i)          | Removes and returns the ith item in a list        |
| sort          | alist.sort()          | Modifies a list to be sorted                      |
| reverse       | alist.reverse()       | Modifies a list to be in reverse order            |
| del           | del alist[i]          | Deletes the item in the ith position              |
| index         | alist.index(item)     | Returns the index of the first occurrence of item |
| count         | alist.count(item)     | Returns the number of occurrences of item         |
| remove        | alist.remove(item)    | Removes the first occurrence of item              |
| extend        | alist.extend(another_list) | Add elements of one list to another list     |
| copy          | newlist = alist.copy()    | Copy a list                                   |
| clear         | alist.clear()             | Clear a list, removing all elements           |
| any           | any(alist)                | returns True if any element of an iterable is True, if not returns False |
| all           | all(alist)        | returns True if all elements of an iterable are True, otherwise False |
| ascii         | ascii(alist) | returns the printable representation of an Object      |
| bool          | bool(alist)  | returns a Boolean on whether the value passed is a bool |
| enumerate     | enumerate(alist) | takes two params; iterable (i.e. list), start, this method adds a counter to an iterable and returns it |
| filter        | filter(func, alist) | takes two params; function, and iterable, function is used to filter the iterable |
| iter          | iter(alist)         | returns an iterator object (you can use next()) for the given object that loops through each element |
| list          | list(iterable)      | returns a list of the value provided (i.e. string) |
| len           | len(alist)          | returns the number of elements in the sequence object |
| max | max(alist)                    | returns the maximum value from the sequence provided, if no sequence one must pass two values |
| min | min(alist)                      | returns the minimum value from the sequence provided, if no sequence one must pass two values |
| map | map(function, iterable) | Applies a given function to each item of an iterable(list, tuple etc.) and returns a list of the results |
| reversed | reversed(alist)    | returns the reversed iterator of the given sequence |
| slice     | slice(start, stop, step) | returns a slice constructor (similar to a list slice) representing the set of indices specified by range(start, stop, step) |
| sorted    | sorted(alist)             | returns a sorted iterator of the given sequence |
| sum       | sum(alist)                | returns the summation of an iterable |
| zip   | zip(alist, otherlist)         | takes iterables, makes iterator that aggregates elements based on the iterables passed, and returns an iterator of tuples |



There are a number of methods that return a value and also modify the list
Others, simply modify the list with no return value.

Below is sample code using Python lists methods

```python
# Sample number array
a_array_of_numbers = [1, 2, 3, 4, 5]

# Define list
alist = ['Jordan', 'Carson', 26, 'New York, NY']

# Append a value
alist.append('Engineer')        # returns ['Jordan', 'Carson', 26, 'New York, NY', 'Engineer']
alist.append(False)             # returns ['Jordan', 'Carson', 26, 'New York, NY', 'Engineer', False]
alist.append(True)              # returns ['Jordan', 'Carson', 26, 'New York, NY', 'Engineer', False, True]
# Remove a value
alist.pop()                     # returns ['Jordan', 'Carson', 26, 'New York, NY', 'Engineer', False]
alist.pop(2)                    # returns ['Jordan', 'Carson', 'New York, NY', 'Engineer', False]
# Sort a list
alist.pop()                     # must have similar types to sort
alist.sort()                    # returns TypeError: unorderable types: bool() < str()
                                # returns ['Carson', 'Engineer', 'Jordan', 'New York, NY']
# Reverse a list
alist.reverse()                 # returns ['New York, NY', 'Jordan', 'Engineer', 'Carson']
# Count a specific item
print(alist.count('Jordan'))    # returns 1
# Find the index of a specific item
print(alist.index('Carson'))    # returns 3
# Remove an item by name
alist.remove('New York, NY')    # returns ['Jordan', 'Engineer', 'Carson']
# Remove an item by position
del alist[1]                    # returns ['Jordan', 'Carson']
```

Python also has a built-in range object, which is often used and discussed
in conjunction with lists. range produces a range object that represents
a sequence of values. While using the list function, it is possible to see
the value of the range object as a list, illustrated below:

```python
print(range(10))                # returns range(0, 10)
print(list(range(10)))          # returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(range(5, 10))             # returns range(5, 10)
print(list(range(5, 10)))       # returns [5, 6, 7, 8, 9]
print(list(range(5, 10, 2)))    # returns [5, 7, 9]
print(list(range(10, 1, -1)))   # returns [10, 9, 8, 7, 6, 5, 4, 3, 2]
```

From the above examples, we can see that range(start, stop, increment)
the range object will start **start** and end before it reaches **stop**
by one value.

## Strings

Strings are another sequential data collection, they can consist of zero or
more letters, numbers and sympbols. Literal string values are differentiated
from identifiers by using quotation marks (single or double), illustrated below:

```python
myName = 'Jordan'
print(myName[0])                # returns J
print(myName[-1])               # returns n

print(len(myName))              # returns 5
```

Since strings are sequences, all of the sequence operations described
above work as you would expect.
In addition, strings have a number of methods,

##### String Methods (outside of sequence operations above)

| Method Name | Use                  | Explanation                                             |
|-------------|----------------------|---------------------------------------------------------|
| center      | astring.center(w)    | Returns a string centered in a field of size w          |
| count       | astring.count(item)  | Returns the number of occurrences of item in the string |
| ljust       | astring.ljust(w)     | Returns a string left-justified in a field of size w    |
| lower       | astring.lower()      | Returns a string in all lowercase                       |
| rjust       | astring.rjust(w)     | Returns a string right-justified in a field of size w   |
| find        | astring.find(item)   | Returns the index of the first occurrence of item       |
| split       | astring.split(schar) | Splits a string into substrings at schar                |

##### Full Table of String Methods

| Method Name | Use                  | Explanation                                              |
|-------------|----------------------|----------------------------------------------------------|
| capitalize  | astring.capitalize()    | Returns a string with the first letter capitalized    |
| center      | astring.center(w)       | Returns a string centered in a field of size w           |
| casefold      | astring.casefold()    | Returns a string used for caseless matching           |
| count       | astring.count(item)  | Returns the number of occurrences of item in the string  |
| endswith      | astring.endswith(suffix)  | Checks if the string ends with the specified suffix, if it does, returns True, if not, returns False |
| expandtabs    | astring.expandtabs(tabsize) | Returns a copy of string with all tab characters '\t' replaced with whitespace characters |
| encode        | astring.encode(encoding='UTF-8', errors='string') | Returns encoded version of the given string |
| find        | astring.find(item)   | Returns the index of the first occurrence of item        |
| format    | astring.format(x, ..., xn) | Method formats the given string into a nicer output |
| index     | astring.index(substring[, start[, end]])  | Returns the index of a substring inside the string (if found) |
| isalnum   | astring.isalnum() | Returns True if all characters in the string are alphanumeric, if not, False |
| isalpha   | astring.isalpha() | Returns True if all characters in the string are alphabets, if not, False |
| isdecimal | astring.isdecimal() | Returns True if all characters in the string are decimal characters, if not, False |
| isdigit   | astring.isdigit()   | Returns True if all characters in the string are digits, if not, False |
| islower   | astring.islower() | Returns True if all alphabets in the string are lowercase, if not, False |
| isnumeric | astring.isnumeric()   | Returns True if all characters in the string are numeric characters, if not, False |
| isprintable | astring.isprintable() | Returns True if all characters in the string are printable or the string is empty, if not, False |
| isspace     | astring.isspace()   | Returns True if all characters in the string are whitespace characters, if not, False |
| istitle   | astring.istitle()     | Returns True if the string is titlecased string, if not, False |
| isupper   | astring.isupper()     | Returns True if all alphabets in the string are uppercase, if not, False |
| join      | astring.join(iterable) | Method which returns a string concatenated with the elements of an iterable |
| ljust       | astring.ljust(w)     | Returns a string left-justified in a field of size w     |
| rjust       | astring.rjust(w)     | Returns a string right-justified in a field of size w    |
| lower       | astring.lower()      | Returns a string in all lowercase                        |
| upper     | astring.upper()       | Returns a string in all uppercase |
| swapcase  | asring.swapcase()     | Returns a string with each characters case swapped, if uppercase then lowercase, if lowercase then uppercase |
| lstrip    | astring.lstrip()      | Returns a string with the leading characters removed |
| rstrip    | astring.rstrip()      | Returns a string with the trailing characters removed |
| strip     | astring.strip()       | Returns a string with both leading and trailing characters removed |
| partition | astring.parition(sep) | Returns a 3-tuple containing the part before the parameter, the separator parameter, and the part after the separator if the separator is found in the string |
| rpartition | astring.rpartition(sep) | Returns a 3-tuple containing the part before the separator, separator parameter, and the part after the separator if the separator parameter is found in the string |
| replace   | astring.replace(old, new, count) | Returns a string where all occurrences of a substring is replaced with another substring |
| rfind     | astring.rfind(item, start, end) | Returns the highest index of the substring (if found), if not, returns -1 |
| rindex    | astring.rindex(substring[, start[, end]]) | Returns the highest index of the substring inside the string (if found), if not, raises an exception |
| split       | astring.split(schar) | Splits a string into substrings at schar                 |
| rsplit    | astring.rsplit(sep)    | Splits a string from the right at the specified separator and returns a list of strings |
| splitlines    | astring.splitlines() | Splits a string at line breaks and returns a list of lines in the string, optional - passing True will keep the ends in the output |
| startswith    | astring.startswith(prefix) | Returns True if a string starts with the specified prefix, if not, False |
| title         | astring.title()           | Returns a string with first letter of each word capitalized |
| zfill         | astring.zfill(width)      | Returns a string of specified width with '0' digits filled to the left, if the width is more than the string |

__Note: functions .maketrans(), .translation() are missing from above.__


Below implementation of string methods.

```python
print(myName*3)                 # returns JordanJordanJordan
print(myName)                   # returns Jordan
print(myName.upper())           # returns JORDAN

# Returns the string centered in a field of size 10
print(myName.center(10))        # returns '  Jordan  '

# Returns the index of the string based on the string searched
print(myName.find('J'))         # returns 0

# Takes a string and return a list of strings using the split character as a division point.
print(myName.split('o'))        # returns ['J', 'rdan']
```

**Major Difference**
A major difference between lists and strings are that lists can be
modified while strings cannot. This is referred to as **mutability**.
**Lists are mutable, strings are immutable**. For example, you can
change an item in a list by using indexing and assignment. With a string
that change is not allowed.

If you try to run the below code it will return a
TypeError: 'str' object does not support item assignment

```python
myName = 'Jordan'
myName[0] = 'C'
```

## Tuples

Tuples are very similar to lists in that they are heterogeneous sequences of data.
The difference is that a tuple is immutable, like a string. A tuple
cannot be changed. Tuples are written as comma-separated values
enclosed in parentheses. As sequences, they can use a operation described
above.

```python
aTuple = ('Jordan', 'Carson', 26)
print(len(aTuple))              # returns 3
```

## Sets

Sets are an unordered collection type of zero or more immutable python
data objects. Sets do not allow duplicates and are written as
comma-delimited values enclosed in curly braces. The empty set
is represented by set(). Sets are also heterogeneous and
the collection can be assigned to a variable shown below.

```python
aSet = {26, 'Jordan', 'Carson')
print(len(set))                 # returns 3
```

Although sets are not considered to be sequential, they do support a few
of the familiar operations presented earlier. The table below reviews
these operations.

| Method Name | Use              | Explanation                                                       |
|-------------|------------------|-------------------------------------------------------------------|
| membership  | in               | Set membership                                                    |
| length      | len              | Returns the cardinality of the set                                |
| &#x7c;      | aset &#x7c; otherset  | Returns a new set with all elements from both sets                |
| &           | aset & otherset  | Returns a new set with only those elements common to both sets    |
| -           | aset - otherset  | Returns a new set with all items from the first set not in second |
| <=          | aset <= otherset | Asks whether all elements of the first set are in the second      |



```python
aset = {26, 'Jordan', 'Carson'}
print(len(aset))                                    # returns 3
aset_2 = {26, 'Steve', 'Smith'}

a_combined_set = aset | aset_2                      # returns {'Carson', 'Jordan', 'Smith', 26, 'Steve'}
print(a_combined_set)

a_common_set = aset & aset_2                        # returns {26}
print(a_common_set)

a_first_set_not_in_second = aset - aset_2           # returns {'Carson', 'Jordan'}
print(a_first_set_not_in_second)

first_set_in_second_boolean = aset <= aset_2        # returns False
print(first_set_in_second_boolean)
```

Sets support a number of methods that should be familiar to those in
mathematics.


| Operation Name | Use                         | Explanation                                                    |
|----------------|-----------------------------|----------------------------------------------------------------|
| union          | aset.union(otherset)        | Returns a new set with all elements from both sets             |
| intersection   | aset.intersection(otherset) | Returns a new set with only those elements common to both sets |
| difference     | aset.difference(otherset)   | Returns a new set with all items from first set not in second  |
| issubset       | aset.issubset(otherset)     | Asks whether all elements of one set are in the other          |
| add            | aset.add(item)              | Adds item to the set                                           |
| remove         | aset.remove(item)           | Removes item from the set                                      |
| pop            | aset.pop()                  | Removes an arbitrary element from the set                      |
| clear          | aset.clear()                | Removes all elements from the set                              |


```python
print(aset)

new_set = {'26', 26, False, 'JC'}

# Combining sets together
print(aset.union(new_set))                  # returns {False, 'JC', 'Jordan', 'Carson', '26', 26}
print(aset | new_set)                       # returns {False, '26', 'JC', 'Carson', 26, 'Jordan'}

# Intersecting sets
print(aset.intersection(new_set))           # returns {26}
print(aset & new_set)                       # returns {26}

# Difference sets
print(aset.difference(new_set))             # returns {'Carson', 'Jordan'}
print(aset - new_set)                       # returns {'Carson', 'Jordan'}

# Subset sets
print(aset.issubset(new_set))               # returns False
print(aset <= new_set)                      # returns False

# add a item
aset.add('Louis')                           # return {'Jordan', 26, 'Louis', 'Carson'}
print(aset)

# remove an arbitrary item
aset.pop()                                  # returns {'Louis', 'Jordan', 'Carson'}
print(aset)

aset.clear()                                # returns set()
print(aset)
```

## Dictionary

Dictionaries are one of Pythons most powerful and useful data types as
one can manipulate a dictionary by accessing a value via key or
by adding another key-value pair.

The syntax for access looks much like a sequence access except that instead
of using the index of the item we use the key value, and add value is similar.

```python
names = {'first': 'Jordan', 'last': 'Carson'}
print(names['first'])                       # returns Jordan
print(names['last'])                        # returns Carson

names['first'] = 'Gordan'
names['last'] = 'Geko'

print(names)                                # returns {'first': 'Gordan', 'last': 'Geko'}
names['middle'] = 'G'
print(len(names))                           # returns 3

for k in names:
    print(names[k], ' Is the name of ', k)  # returns 1. Geko  Is the name of  last
                                            # returns 2. G  Is the name of  middle
                                            # returns 3. Gordan  Is the name of  first
```

##### Dictionary operations and explanations of use
| Operator | Use            | Explanation                                                 |
|----------|----------------|-------------------------------------------------------------|
| []       | myDict[k]      | Returns the value associated with k, otherwise its an error |
| in       | key in adict   | Returns True if key is in the dictionary, False otherwise   |
| del      | del adict[key] | removed the entry from the dictionary                       |


##### Dictionary methods and explanations of use
| Method Name | Use               | Explanation                                                  |
|-------------|-------------------|--------------------------------------------------------------|
| keys        | adict.keys()      | Returns the keys of the dictionary in a dict_keys object     |
| values      | adict.values()    | Returns the values of the dictionary in a dict_values object |
| items       | adict.items()     | Returns the key-value pairs in a dict_items objects          |
| get         | adict.get(k)      | Returns the value associated with k, None otherwise          |
| get         | adict.get(k, alt) | Returns the value associated with k, alt otherwise           |

See below implementation of above dictionary methods.

```python
phoneext = {'work': 3584, 'cell': 7518}
print(phoneext)

print(phoneext.keys())                      # returns dict_keys(['cell', 'work'])
print(list(phoneext.keys()))                # returns ['cell', 'work']
print(phoneext.values())                    # returns dict_values([7518, 3584])
print(list(phoneext.values()))              # returns [7518, 3584]

print(phoneext.items())                     # returns dict_items([('work', 3584), ('cell', 7518)])
print(phoneext.get('work'))                 # returns 3584
```

