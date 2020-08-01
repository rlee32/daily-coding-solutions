#!/usr/bin/env python3

def solve(amount, denominations = [1, 5, 10, 25]):
    mincoins = [0] # index is amount. maps amount to minimum coin count.
    for a in range(1, amount + 1):
        minimums = []
        for d in denominations:
            if a >= d:
                minimums.append(1 + mincoins[a - d])
        mincoins.append(min(minimums))
    return mincoins[-1]

if __name__ == '__main__':
    assert(3 == solve(16))
    assert(4 == solve(17))
    assert(1 == solve(25))
    assert(2 == solve(26))
