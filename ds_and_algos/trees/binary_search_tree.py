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

    def display(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2



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


class TreeNode(object):
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def is_leaf(self):
        return not (self.right or self.left)

    def has_any_children(self):
        return self.right or self.left

    def has_both_children(self):
        return self.right and self.left

    def has_one_child(self):
        return self.has_any_children() and not self.has_both_children()

    def replace_node_data(self, key, val, left, right):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self

    def __iter__(self):
        if self is None:
            return

        if self.left:
            # `in` calls `__iter__` so is recursive
            for elem in self.left:
                yield elem

        yield self.key

        if self.right:
            # recurse again
            for elem in self.right:
                yield elem

    def find_successor(self):
        if self.right:
            return self.right.find_min()

        if self.parent is None:
            return None

        if self.is_left_child():
            return self.parent

        self.parent.right = None
        successor = self.parent.find_successor()
        self.parent.right = self
        return successor

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None

        else:
            promoted_node = self.left or self.right

            if self.is_left_child():
                self.parent.left = promoted_node
            else:
                self.parent.right = promoted_node
            promoted_node.parent = self.parent


class BinarySearchTree(object):
    TreeNodeClass = TreeNode

    def __init__(self):
        self.root = None
        self.size = 0




    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = self.TreeNodeClass(key, val)
        self.size = self.size + 1

    def _put(self, key, val, node):
        if key < node.key:
            if node.left:
                self._put(key, val, node.left)
            else:
                node.left = self.TreeNodeClass(key, val, parent=node)
        else:
            if node.right:
                self._put(key, val, node.right)
            else:
                node.right = self.TreeNodeClass(key, val, parent=node)

    def __getitem__(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.val
        raise KeyError

    def _get(self, key, node):
        if not node:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self._get(key, node.left)
        return self._get(key, node.right)

    def __contains__(self, key):
        return bool(self._get(key, self.root))

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
                return
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
            return

        raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    @staticmethod
    def remove(node):
        if node.is_leaf() and node.parent is not None:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

        elif node.has_one_child():
            promoted_node = node.left or node.right

            if node.is_left_child():
                promoted_node.parent = node.parent
                node.parent.left = promoted_node
            elif node.is_right_child():
                promoted_node.parent = node.parent
                node.parent.right = promoted_node
            else:
                node.replace_node_data(
                    promoted_node.key,
                    promoted_node.val,
                    promoted_node.left,
                    promoted_node.right
                )

        else:  # has both children
            successor = node.find_successor()
            if successor:
                successor.splice_out()
                node.key = successor.key
                node.val = successor.val
