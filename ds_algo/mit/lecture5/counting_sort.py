"""
MIT 6006 Counting Sort
"""

from typing import List


def counting_sort_two(A: List[int]) -> None:
    """
    The algorithm loops over the items, computing a histogram of each key’s number of times within the input collection.
    It then performs a prefix sum computation to determine, for each key, the starting position in the output array of the items having that key.
    Finally, it loops over the items again, moving each item into its sorted position in the output array.

    Source: https://www.techiedelight.com/counting-sort-algorithm-implementation/
    Args:
        A (List[int]): _description_
    """
    k = max(A)
    freq = [0] * (k + 1)
    for i in A:
        freq[i] += 1
    # overwrite the input list with sorted order
    index = 0
    for i in range(k + 1):
        # freq[i] always stores the next position in the output array
        # into which an item with key i should be stored
        #  so each item is moved to its correct position in the output array.
        while freq[i] > 0:
            A[index] = i
            index += 1
            freq[i] -= 1


def counting_sort(A):
    """Sort A assuming items have non-negative keys"""
    u = max(A) + 1  # O(n) find maximum key
    D = [0] * u  # O(u) direct access array of counts
    for x in A:  # O(n) count occurrences of each key
        D[x] += 1
    i = 0
    for key in range(u):  # O(u) read out items in order
        for j in range(D[key]):
            A[i] = key
            i += 1
    return A


if __name__ == "__main__":
    A = [5, 2, 4, 6, 1, 3]
    counting_sort(A)
    print(A)
    assert A == [1, 2, 3, 4, 5, 6]
