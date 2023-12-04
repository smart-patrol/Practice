""" Reverse a string """

from time_it import time_it

@time_it
def reverse_string(s:str) -> str:
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

@time_it
def reverse_string_iterative(s:str) -> str:
    s = list(s)
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

assert reverse_string("hello") == "olleh"
assert reverse_string("a") == "a"

assert reverse_string_iterative("hello") == "olleh"
assert reverse_string_iterative("a") == "a"