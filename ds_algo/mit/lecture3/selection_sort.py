from typing import List


def prefix_max(A: List[int], i: int) -> int:
    """Return index of maximum in A[:i+1]"""
    if i > 0:
        # biggest element between A and i-1
        j = prefix_max(A, i - 1)
        if A[i] < A[j]:
            return j
    # this is the base case
    return i


def recursive_selection_sort(A: List[int], i: int = None) -> None:
    """recurisve selection sort from A[:i+1]"""
    # base case
    if i is None:
        i = len(A) - 1
    # recursive case
    if i > 0:
        # find the biggest point in the Array
        j = prefix_max(A, i)
        if j != i:
            A[i], A[j] = A[j], A[i]
        recursive_selection_sort(A, i - 1)


def iterative_selection_sort(A: List[int]) -> None:
    """iterative selection sort from A"""
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]


if __name__ == "__main__":
    A = [5, 2, 4, 6, 1, 3]
    recursive_selection_sort(A)
    print(f"sorted A={A}\n")
    assert A == [1, 2, 3, 4, 5, 6], f"A={A} should be [1,2,3,4,5,6]\n"
    A = [1, 2, 3, 4, 5, 6]
    recursive_selection_sort(A)
    print(f"sorted A={A}\n")
    assert A == [1, 2, 3, 4, 5, 6], f"A={A} should be [1,2,3,4,5,6]\n"
    A = [6, 5, 4, 3, 2, 1]
    recursive_selection_sort(A)
    print(f"sorted A={A}\n")
    assert A == [1, 2, 3, 4, 5, 6], f"A={A} should be [1,2,3,4,5,6]\n"
