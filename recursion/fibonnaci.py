memo = {}

def fib_recrusive(n: int) -> int:
  if n in memo:
    return memo[n]
  elif n <= 1:
    return n
  else:
    f = fib_recrusive(n-1) + fib_recrusive(n-2)
    memo[n] = f
    return f


assert fib_recrusive(5) == 5
assert fib_recrusive(6) == 8
assert fib_recrusive(7) == 13
assert fib_recrusive(8) == 21

def fib_iterative(n:int) -> int:
    first, second = 1,1
    for i in range(1,n):
        first,second = second, first + second
        # temp = first + second
        # first = second
        # second = temp
    return first

assert fib_iterative(5) == 5
assert fib_iterative(6)  == 8
assert fib_iterative(8) == 21
