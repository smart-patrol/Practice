"""
    Introduction to Algorithms: 6.006
    Massachusetts Institute of Technology 
    Recitation 3
    https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/mit6_006s20_r03/_
"""

from array_sequence import Array_Seq
from merge_sort import merge_sort, merge
from timer import timer
from random import randint


class Sorted_Array_Set:
    def __init__(self):
        self.A = Array_Seq()  # O(1)

    def __len__(self):
        return len(self.A)  # O(1)

    def __iter__(self):
        yield from self.A  # O(n)

    def iter_order(self):
        yield from self  # O(n)

    def build(self, X, sort_type="merge"):  # O(?)
        self.A.build(X)
        self._sort(sort_type)

    @timer
    def _sort(self, sort_type: str):
        if sort_type == "selection":  # O(N^2)
            for i in range(len(self)):
                min_index = i
                for j in range(i + 1, len(self)):
                    if self.A.get_at(j) < self.A.get_at(min_index):
                        min_index = j
                A, B = self.A.get_at(i), self.A.get_at(min_index)
                self.A.set_at(i, B)
                self.A.set_at(min_index, A)

        elif sort_type == "insertion":  # O(N^2)
            for i in range(len(self) - 1):
                key = self.A.get_at(i)
                j = i - 1
                while j >= 0 and key < self.A.get_at(j):
                    self.A.set_at(j + 1, self.A.get_at(j))
                    j -= 1
                self.A.set_at(j + 1, key)
        else:  # merge sort O(NlogN)
            merge_sort(self.A.A)

    def _binary_search(self, k, i, j):  # O(log n)
        if i >= j:
            return i
        m = (i + j) // 2
        x = self.A.get_at(m)
        if x.key > k:
            return self._binary_search(k, i, m - 1)
        if x.key < k:
            return self._binary_search(k, m + 1, j)
        return m

    def find_min(self):  # O(1)
        if len(self) > 0:
            return self.A.get_at(0)
        else:
            return None

    def find_max(self):  # O(1)
        if len(self) > 0:
            return self.A.get_at(len(self) - 1)
        else:
            return None

    def find(self, k):  # O(log n)
        if len(self) == 0:
            return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key == k:
            return x
        else:
            return None

    def find_next(self, k):  # O(log n)
        if len(self) == 0:
            return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key > k:
            return x
        if i + 1 < len(self):
            return self.A.get_at(i + 1)
        else:
            return None

    def find_prev(self, k):  # O(log n)
        if len(self) == 0:
            return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key < k:
            return x
        if i > 0:
            return self.A.get_at(i - 1)
        else:
            return None

    def insert(self, x):  # O(n)
        if len(self.A) == 0:
            self.A.insert_first(x)
        else:
            i = self._binary_search(x.key, 0, len(self.A) - 1)
            k = self.A.get_at(i).key
            if k == x.key:
                self.A.set_at(i, x)
                return False
            if k > x.key:
                self.A.insert_at(i, x)
            else:
                self.A.insert_at(i + 1, x)
            return True

    def delete(self, k):  # O(n)
        i = self._binary_search(k, 0, len(self.A) - 1)
        assert self.A.get_at(i).key == k
        return self.A.delete_at(i)


if __name__ == "__main__":
    # Unit test of the code
    sorts = ["merge sort", "insertion", "selection"]
    for sort in sorts:
        print(sort)
        S = Sorted_Array_Set()
        S.build([3, 1, 4, 5, 2, 6, 7], sort_type=sort)
        print(S.A.A)
        assert S.A.A == [1, 2, 3, 4, 5, 6, 7]

    for sort in sorts:
        print(f"{sort} sort speed is...")
        S = Sorted_Array_Set()
        X = [randint(0, 100) for _ in range(1000)]
        S.build(X, sort_type=sort)
