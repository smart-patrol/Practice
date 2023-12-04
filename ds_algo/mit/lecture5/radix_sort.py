"""
source: https://www.lewuathe.com/radix-sort-in-python.html
"""

from typing import List, Callable


def counting_sort(arr: List[int], max_value: int, get_index: Callable) -> List[int]:
    counts = [0] * (max_value + 1)
    # Counting - O(n)
    for a in arr:
        counts[get_index(a)] += 1

    # Accumulating - O(k)
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    # Calculating start index - O(k)
    for i in range(len(counts) - 1):
        if i == 0:
            counts[i] = 0
        counts[i + 1] = counts[i]

    ret = [None] * len(arr)
    # Sorting - O(n)
    for a in arr:
        index = counts[get_index(a)]
        ret[index] = a
        counts[get_index(a)] += 1

    return ret


def get_digit(n, d):
    for i in range(d - 1):
        n //= 10
    return n % 10


def get_num_difit(n):
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i


def radix_sort(arr, max_value):
    num_digits = get_num_difit(max_value)
    # O(k(n+k))
    for d in range(num_digits):
        # Counting sort takes O(n+k)
        arr = counting_sort(arr, max_value, lambda a: get_digit(a, d + 1))
    return arr


if __name__ == "__main__":
    arr = [1, 3, 5, 6, 1, 3, 5]
    new_arr = radix_sort(arr, max(arr))
    new_arr == [1, 1, 3, 3, 5, 5, 6]
