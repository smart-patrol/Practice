from typing import List
import array as arr


def recursive_insertion_sort(A: List[int], i=None) -> None:
    """Sort A[:i+1]"""
    if i is None:
        i = len(A) - 1
    if i > 0:
        insertion_sort(A, i - 1)
        insert_last(A, i)


def insert_last(A: List[int], i: int) -> None:
    """Sort A[:i+1] assuming sorted A[:i]"""
    if i > 0 and A[i] < A[i - 1]:
        A[i], A[i - 1] = A[i - 1], A[i]
        insert_last(A, i - 1)


def iterative_insertion_sort(A: List[int]) -> None:
    """Sort A[:i+1] in place"""
    for i, key in enumerate(A):
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    iterative_insertion_sort(arr)
    print(arr)
    assert arr == [5, 6, 11, 12, 13]
