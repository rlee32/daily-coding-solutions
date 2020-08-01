#!/usr/bin/env python3

def string_sort(string):
    string = [x for x in string]
    string.sort()
    return ''.join(string)

def solve_suboptimal(string, word):
    """O(S * W * log(W))"""
    word = string_sort(word)
    matches = []
    for i in range(len(string)):
        candidate = string_sort(string[i : i + len(word)])
        if candidate == word:
            matches.append(i)
    return matches

def count_characters(string):
    count = {}
    for c in string:
        if c not in count:
            count[c] = 0
        count[c] += 1
    return count

def compare_counts(count1, count2):
    if len(count1) != len(count2):
        return False
    for c in count1:
        if c not in count2:
            return False
        if count1[c] != count2[c]:
            return False
    return True

def solve_better(string, word):
    """O(S * W)"""
    word = count_characters(word)
    window = count_characters(string[:len(word)])
    matches = []
    for i in range(len(string)):
        if compare_counts(word, window):
            matches.append(i)
        j = i + len(word) - 1
        if j >= len(string) - 1:
            break
        first = string[i]
        last = string[j + 1]
        window[first] -= 1
        if window[first] == 0:
            del window[first]
        if last not in window:
            window[last] = 0
        window[last] += 1
    return matches

def count_diff(word, window):
    diff = {} # negative value means window does not have what word has.
    for c in window:
        delta = window[c] - word.get(c, 0)
        if delta != 0:
            diff[c] = delta
    for c in word:
        delta = window.get(c, 0) - word[c]
        if delta != 0:
            diff[c] = delta
    return diff

def increment_dict(d, k, i):
    if k not in d:
        d[k] = 0
    d[k] += i
    if d[k] == 0:
        del d[k]

def solve(string, word):
    """O(S)"""
    word = count_characters(word)
    window = count_characters(string[:len(word)])
    diff = count_diff(word, window)
    matches = []
    for i in range(len(string)):
        if not diff:
            matches.append(i)
        j = i + len(word) - 1
        if j >= len(string) - 1:
            break
        first = string[i]
        last = string[j + 1]
        increment_dict(diff, first, -1)
        increment_dict(diff, last, 1)
    return matches


def check(a ,b):
    assert(len(a) == len(b))
    for i in a:
        assert(i in b)

if __name__ == '__main__':
    print('test')
    check(solve('abxaba', 'ab'), [0, 3, 4])
