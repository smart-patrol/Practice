""" Calculate exponents """


def exponent_iterative(a:int, n:int) -> int:
    """ Calculate exponents iteratively """
    result = 1
    for i in range(n):
        result *= a
    return result

def exponent_recursive(a:int, n:int) -> int:
    """ Calculate exponents recursively """
    if n == 0:
        return 1
    elif n % 2 == 0:
        out = exponent_recursive(a, n//2)
        return out * out
    elif n % 2 == 1:
        out = exponent_recursive(a, (n-1)//2)
        return out * out * a


# Log N time
def expo_stack(a:int, n:int) -> int:
    out = 1
    while n > 0:
        if n % 2 == 1:
            out *= a
        a *= a
        n //= 2
    return out


assert exponent_iterative(2,3) == 8
assert exponent_recursive(2,3) == 8
assert exponent_iterative(2,0) == 1
assert exponent_recursive(2,0) == 1
assert exponent_recursive(17,10) == 2015993900449
assert expo_stack(2,3) == 8