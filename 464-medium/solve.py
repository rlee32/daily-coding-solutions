#!/usr/bin/env python3

"""O(n^2)"""

def match(i, j):
    return max(i, j) % min(i, j) == 0

def match_set(number_set, candidate):
    for i in number_set:
        if not match(candidate, i):
            return False
    return True

def extract_set(numbers):
    new_set = set([numbers.pop()])
    for i in numbers:
        if match_set(new_set, i):
            new_set.add(i)
    for i in new_set:
        if i in numbers:
            numbers.remove(i)
    return new_set

def solve(numbers):
    sets = []
    while numbers:
        sets.append(extract_set(numbers))
    max_set_index = 0
    max_set_length = 0
    for i in range(len(sets)):
        if len(sets[i]) > max_set_length:
            max_set_index = i
            max_set_length = len(sets[i])
    return sets[max_set_index]

def check(a ,b):
    assert(len(a) == len(b))
    for i in a:
        assert(i in b)

if __name__ == '__main__':
    print('test')
    check(solve(set([3, 5, 10, 20, 21])), [5, 10, 20])
    check(solve(set([1, 3, 6, 24])), [1, 3, 6, 24])
    check(solve(set([2, 5, 7, 19])), [2])
