#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    result = 1
    negative = False
    if b < 0:
        negative = True
        b = -b
    for _ in range(b):
        result *= a
    if negative:
        return 1 / result
    return result
