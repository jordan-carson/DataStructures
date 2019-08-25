def preorder(node):
    if node:
        print(node['val'])
        preorder(node.get('left'))
        preorder(node.get('right'))


def postorder(node):
    if node:
        postorder(node.get('left'))
        postorder(node.get('right'))
        print(node['val'])


def inorder(node):
    if node:
        inorder(node.get('left'))
        print(node['val'])
        inorder(node.get('right'))


def construct_expression(parse_tree):
    if parse_tree is None:
        return ''

    left = construct_expression(parse_tree.get('left'))
    right = construct_expression(parse_tree.get('right'))
    val = parse_tree['val']

    if left and right:
        return '({}{}{})'.format(left, val, right)

    return val