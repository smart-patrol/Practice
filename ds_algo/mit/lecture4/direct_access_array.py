# bin/usr/python3
# endcoding=utf8

"""
Direct access array implementation of the `Array` interface.
"""


class DirectAccessArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity

    def find(self, k: int) -> int:
        return self.data[k]

    def insert(self, x: int) -> None:
        self.data[x.key] = x

    def delete(self, k: int) -> None:
        self.data[k] = None

    def find_next(self, k: int) -> int:
        for i in range(k + 1, len(self.data)):
            if self.data[i] is not None:
                return self.data[i]
        return -1

    def find_max(self) -> int:
        for i in range(len(self.data) - 1, -1, -1):  # O(N)
            if self.data[i] is not None:
                return self.data[i]

    def delete_max(self) -> int:
        for i in range(len(self.data) - 1, -1, -1):  # O(N)
            if self.data[i] is not None:
                self.data[i] = None
                return self.data[i]


if __name__ == "__main__":
    # unit tests for the DirectAccessArray class
    A = DirectAccessArray(capacity=10)
    A.data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(A.find(5))
    A.insert(11)
    print(A.data)
