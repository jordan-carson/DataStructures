class Node:
    """
    Simple class definition for a Node, in case of trees where nodes may have more
    than two children, a `children` list could be used to contain these references instead.

    The important thing to note about this representation is that the attributes
    `left` and `right` will become references to other instances of the `Node` class.

    For example, when we insert a new left child into the tree we create another
    instance of `Node` and modify `self.left` in the root to reference the new
    subtree.
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def get_children(self):
        children = list()
        if self.left is not None:
            children.append(self.left)
        if self.right is not None:
            children.append(self.right)
        return children


class BST:
    def __init__(self):
        self.root = None

    def set_root(self, val):
        self.root = Node(val)

    def insert(self, val):
        if self.root is None:
            self.set_root(val)
        else:
            self.insert_node(self.root, val)

    def insert_node(self, current_node, val):
        if val <= current_node.val:
            if current_node.left:
                self.insert_node(current_node.left, val)
            else:
                current_node.left = Node(val)

        elif val > current_node.val:
            if current_node.right:
                self.insert_node(current_node.right, val)
            else:
                current_node.right = Node(val)

    def find(self, val):
        return self.find_node(self.root, val)

    def find_node(self, current_node, val):
        if current_node is None:
            return False
        elif val == current_node.val:
            return True
        elif val < current_node.val:
            return self.find_node(current_node.left, val)
        else:
            return self.find_node(current_node.right, val)


