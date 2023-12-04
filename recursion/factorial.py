"""Factorial via recursion"""


def factorial_recursive(n:int) -> int:
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)

def factorial_iterative(n:int) -> int:
    out = 1
    for i in range(n):
        out *= (i+1)
    return out


assert factorial_recursive(5) == 120
assert factorial_iterative(5) == 120

