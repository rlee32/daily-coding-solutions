#!/usr/bin/env python3

def search_after(array, index):
    minimum = array[index]
    for i in range(index, len(array)):
        if array[i] > minimum:
            return i

def search_before(array, index):
    minimum = array[index]
    for i in range(index):
        if array[i] > minimum:
            return i

def solve(array, index):
    """O(n)"""
    after = search_after(array, index)
    before = search_before(array, index)
    if after is None:
        return before
    elif before is None:
        return after
    else:
        after_distance = after - index
        before_distance = index - before
        if after_distance > before_distance:
            return before_distance
        else:
            return after_distance

def preprocess(array):
    """A 'dumb' solution would be to solve for every index and return the array,
    which would be O(n**2) in time, O(n) is space.
    There might be a way to achieve less than O(n**2) in time.
    """
    # TODO
    return None

assert(3 == solve([4, 1, 3, 5, 6], 0))

