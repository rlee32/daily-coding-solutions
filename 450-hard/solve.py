#!/usr/bin/env python3

def solve(s):
    """O(n)"""
    bounds = [0, 0] # min, max bounds of left-openness (number of excess '(').
    for c in s:
        if c == '(':
            bounds[0] += 1
            bounds[1] += 1
        elif c == ')':
            bounds[0] = max(bounds[0] - 1, 0)
            bounds[1] -= 1
            if bounds[1] < 0:
                return False
        elif c == '*':
            bounds[0] = max(bounds[0] - 1, 0)
            bounds[1] += 1
        else:
            assert(False)
    print(bounds)
    return bounds[0] == 0

if __name__ == '__main__':
    print('test')
    assert(not solve(')*('))
    assert(solve('(***)'))
    assert(solve('********'))
    assert(solve('(((((*)))))'))
    assert(solve('(()(((***)))())()()(()))'))
