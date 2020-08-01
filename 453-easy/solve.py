#!/usr/bin/env python3

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def make_left(self, value):
        self.left = Node(value)
        return self.left
    def make_right(self, value):
        self.right = Node(value)
        return self.right

def find_node(node, value):
    if node is None:
        return None
    if node.value == value:
        return node
    elif value > node.value:
        return find_node(node.right, value)
    else:
        return find_node(node.left, value)

def attempt(root, K, node):
    if node is None:
        return None
    k = K - node.value
    other = find_node(root, k)
    if other is None:
        return None
    if node == other:
        if node.right and node.right.value == k:
            return [node, other]
        else:
            return None
    return [node, other]

def solve(root, K, node):
    """worst case O(n * log(n)): at each node attempt to search for other number."""
    if node is None:
        return None
    soln = attempt(root, K, node)
    if soln:
        return soln
    for n in [node.left, node.right]:
        soln = solve(root, K, n)
        if soln:
            return soln

def check(a ,b):
    assert(len(a) == len(b))
    for i in a:
        assert(i in b)

if __name__ == '__main__':
    print('test')
    root = Node(10)
    left = root.make_left(5)
    right = root.make_right(15)
    right.make_left(11)
    right.make_right(15)
    soln = solve(root, 20, root)
    check([x.value for x in soln], [5, 15])
    soln = solve(root, 16, root)
    check([x.value for x in soln], [5, 11])
