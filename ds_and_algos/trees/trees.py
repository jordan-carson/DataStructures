class LinkedListNode:
    def __init__(self, data):
        self.head = data
        self.next = None


class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def insert_left(self, child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child

    def insert_right(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = self.right
            self.right = child


def insert_left(root, child_val):
    subtree = root.pop(1)
    if len(subtree) > 1:
        root.insert(1, [child_val, subtree, []])
    else:
        root.insert(1, [child_val, [], []])
    return root


def insert_right(root, child_val):
    subtree = root.pop(2)
    if len(subtree) > 1:
        root.insert(2, [child_val, [], subtree])
    else:
        root.insert(2, [child_val, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


root = [3, [], []]
insert_left(root, 4)
insert_left(root, 5)
insert_right(root, 6)
insert_right(root, 7)
left = get_left_child(root)
# left  # => [5, [4, [], []], []]
print(left)
set_root_val(left, 9)
print(root)     # => [3, [9, [4, [], []], []], [7, [], [6, [], []]]]
insert_left(left, 11)
print(root)     # => [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
print(get_right_child(get_right_child(root)))  # => [6, [], []]