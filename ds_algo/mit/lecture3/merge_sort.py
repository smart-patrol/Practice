from typing import List


def merge(
    left: List[int], right: List[int], A: List[int], i: int, j: int, l: int, r: int
) -> None:
    """Merge left and right into A[a:b]."""
    if l < r:
        # right array is not null and left array is not null
        # set array to the smaller of the two
        if (j <= 0) or (i > 0 and left[i - 1] > right[j - 1]):
            A[r - 1] = left[i - 1]
            i -= 1
        else:
            # otherwise right is the smallest, set it to right
            A[r - 1] = right[j - 1]
            j -= 1
        merge(left, right, A, i, j, l, r - 1)


def merge_sort(A: List[int], l: int = 0, r: int = None) -> None:
    """Sort A[a:b] in place using merge sort."""
    if r is None:
        r = len(A)
    if 1 < r - l:
        mid = (l + r + 1) // 2
        merge_sort(A, l, mid)
        merge_sort(A, mid, r)
        left, right = A[l:mid], A[mid:r]
        merge(left, right, A, len(left), len(right), l, r)


def merge_back(
    left_list: List[int],
    right_list: List[int],
    result_list: List[int],
    left_index: int,
    right_index: int,
) -> None:
    """Merge left_list and right_list into result_list."""
    left_len = len(left_list)
    right_len = len(right_list)
    i, j, k = 0, 0, 0

    # Merge the two lists in ot result in ascending order
    while i < left_len and j < right_len:
        if left_list[i] <= right_list[j]:
            result_list[k] = left_list[i]
            i += 1
        else:
            result_list[k] = right_list[j]
            j += 1
        k += 1
    # Add any remaining elements from the left list
    while i < left_len:
        result_list[k] = left_list[i]
        i += 1
        k += 1
    # Add any remaining elements from the right list
    while j < right_len:
        result_list[k] = right_list[j]
        j += 1
        k += 1


def iterative_merge_sort(A: List[int]) -> None:
    """Sort input in place using merge sort"""
    ln = len(A)
    # Base case: list is already sorted if 1 or 0
    if ln <= 1:
        return
    # Divide the list into two halves and sort each half using recurions
    mid = ln // 2
    left_list = A[:mid]
    right_list = A[mid:]
    iterative_merge_sort(left_list)
    iterative_merge_sort(right_list)

    # Merge the sorted havles back into the original
    merge_back(left_list, right_list, A, mid, ln - mid)


if __name__ == "__main__":
    A = [5, 2, 4, 6, 1, 3]
    merge_sort(A)
    print(A)
    assert A == [1, 2, 3, 4, 5, 6]

    A = [5, 2, 4, 6, 1, 3]
    iterative_merge_sort(A)
    print(A)
    assert A == [1, 2, 3, 4, 5, 6]
