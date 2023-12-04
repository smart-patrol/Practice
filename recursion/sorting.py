"""Sorting implementation using recursion"""

from random import randint
from typing import List

# Merge Sort
def merge_sort(arr:List[int]) -> List[int]:
    """Sort an array in place using the Merge sort algo"""

    def _merge(left:List[int], right:List[int]) -> List[int]:
        """Merge two sorted arrays"""
        merged = []
        # two pointers, for two arrays
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # add the remaining elements
        merged += left[i:]
        merged += right[j:]
        return merged

    # base case: end of array
    if len(arr) == 0 or len(arr) == 1:
        return arr
    # recursive cases -> go left and right
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)

# Quick sort 
def quick_sort(arr:List[int]) -> List[int]:
    """Sort an array in place using the Quicksort algo"""
    def _quick_sort(arr:List[int], low:int, high:int) -> None:
        # base case: 0 or 1 item
        if low >= high:
            return
        # partitioning
        i = low
        pivot_index = randint(low, high)
        pivot_value = arr[pivot_index]
        # swap pivot with high because assumes it at end of array
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        # Iterate over the range, swapping elements that are less than or equal to the pivot value
        for j in range(low, high):
            if arr[j] <= pivot_value:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        # put the pivot on the left side
        arr[i], arr[high] = arr[high], arr[i]

        # Recursive cases
        _quick_sort(arr, low, i-1)
        _quick_sort(arr, i+1, high)

    # sort in place
    _quick_sort(arr, 0, len(arr)-1)

    return arr


def insertion_sort(arr:List[int]) -> List[int]:
    """Sort an array in place using the Insertion sort algo"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] # shift to the right
            j -= 1
        arr[j + 1] = key
    return arr



# unit test
arr = [0,7,6,3,1,2,5,4]
assert quick_sort(arr) == sorted(arr)

arr = [0,7,6,3,1,2,5,4]
assert merge_sort(arr) == sorted(arr)