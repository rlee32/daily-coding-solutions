#!/usr/bin/env python3

class Node:
    def __init__(self, parent = None):
        self.children = []
        self.is_locked = False
        self.locked_descendants = 0
        self.parent = parent

    def locked_ancestor(self):
        if not self.parent:
            return False
        if self.parent.is_locked:
            return True
        return self.parent.locked_ancestor()

    def lockable(self):
        return not self.is_locked and self.locked_descendants == 0 and not self.locked_ancestor()
    def unlockable(self):
        return self.is_locked and self.locked_descendants == 0 and not self.locked_ancestor()

    def lock(self):
        if not self.lockable():
            return False
        self.is_locked = True
        if self.parent:
            self.parent.add_locked_descendant()
        return True

    def unlock(self):
        if not self.unlockable():
            return False
        self.is_locked = False
        if self.parent:
            self.parent.remove_locked_descendant()
        return True

    def add_locked_descendant(self):
        self.locked_descendants += 1
        if self.parent:
            self.parent.add_locked_descendant()

    def remove_locked_descendant(self):
        self.locked_descendants -= 1
        assert(self.locked_descendants >= 0)
        if self.parent:
            self.parent.remove_locked_descendant()

    def make_child(self):
        child = Node(self)
        self.children.append(child)
        return child

if __name__ == '__main__':
    root = Node()
    child = root.make_child()
    assert(child.lock())
    assert(not root.lock())
    assert(not root.unlock())
    assert(child.unlock())
    assert(root.lock())
    assert(not child.lock())
    grandchild = child.make_child()
    assert(not grandchild.lock())
    assert(root.unlock())
    other_child = root.make_child()
    assert(other_child.lock())
    assert(child.lock())
    assert(not root.lock())
    assert(other_child.unlock())
    assert(child.unlock())
    assert(root.lock())
