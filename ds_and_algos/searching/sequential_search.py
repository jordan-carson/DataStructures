def sequential_search(alist, item):

    position = 0

    while position < len(alist):
        if alist[position] == item:
            return True
        position += 1

    return False