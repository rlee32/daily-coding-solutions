#!/usr/bin/env python3

class Node:
    def __init__(self, index):
        self.index = index
        self.next = None

    def append_new(self):
        new_tail = Node(self.index + 1)
        self.next = new_tail
        return new_tail

def create_list(size):
    head = Node(0)
    tail = head
    for i in range(1, size):
        tail = tail.append_new()
    return head

def check_reverse(head):
    i = head.index
    print(f'head index: {i}')
    current = head
    while current:
        assert(current.index == i)
        i -= 1
        current = current.next
    assert(i == -1)

def reverse(node):
    if node.next is None:
        # tail, make this new head.
        return node
    new_head = reverse(node.next)
    node.next.next = node
    return new_head

def solve(head):
    new_head = reverse(head)
    head.next = None # old head is new tail
    return new_head

if __name__ == '__main__':
    print('test')
    for n in [1, 10, 20]:
        head = create_list(n)
        new_head = solve(head)
        check_reverse(new_head)
