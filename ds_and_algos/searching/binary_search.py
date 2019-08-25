

def binary_search_recursive(alist, item):
    # Time is O(log n)
    if not alist:
        # Base Case: if list is empty
        return False

    midpoint = len(alist) // 2 # floor division
    if alist[midpoint] == item: # found it
        return True
    if item < alist[midpoint]:
        binary_search_recursive(alist[:midpoint], item)
    return binary_search_recursive(alist[midpoint + 1:], item)


def binary_search_iterative(alist, item):

    left, right = 0, len(alist)-1

    while left < right:

        midpoint = left + (right - left) // 2
        if alist[midpoint] == item:
            return True
        elif alist[midpoint] < item:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return False


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search_iterative(testlist, 3))  # => False
print(binary_search_iterative(testlist, 13))  # => True