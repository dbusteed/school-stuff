#!/usr/bin/python3

# profiling two different methods of doing factorials
#   1) using recursion
#   2) using a for-loop

try:
    import cProfile as profile
except ImportError:
    import profile


def recursive_fact(n):
    if n == 0:
        return 1
    else:
        return n * recursive_fact(n-1)

def looping_fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def recursion_test():
    for i in range(50000):
        recursive_fact(5)

def looping_test():
    for i in range(50000):
        looping_fact(5)


print('using recursion')
prof = profile.Profile()
prof.runcall(recursion_test)
prof.print_stats()

print('using for loop')
prof = profile.Profile()
prof.runcall(looping_test)
prof.print_stats()
