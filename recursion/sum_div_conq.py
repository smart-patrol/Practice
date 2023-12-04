""" Summing numbers in an array using divide and conquer"""

from typing import List


def sum_div_conq(arr:List[int]) -> List[int]:
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr)//2
        return sum_div_conq(arr[:mid]) + sum_div_conq(arr[mid:])


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert sum_div_conq(arr) == 55