#!/usr/bin/env python3

from collections.abc import Iterable

a = [1,2,[3,[4,5]],6,(7,8,9)]

def flatten(t):
    for x in t:
        if isinstance(x, Iterable):
            yield from flatten(x)
        else:
            yield x

print( [x for x in flatten(a)] )