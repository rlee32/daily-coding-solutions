#!/usr/bin/env python3


def solve(a):
    """a is an array of elements whose values are in [1, len(a) - 1]"""
    n = len(a) - 1
    seen = set()
    for i in a:
        if i in seen:
            return i
        seen.add(i)

if __name__ == '__main__':
    dup = solve([2, 3, 1, 3])
    assert(dup == 3)
