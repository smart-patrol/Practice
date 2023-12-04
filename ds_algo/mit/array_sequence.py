"""
        Array Sequence Implementation
"""


class Array_Seq:
    def __init__(self):  # O(1)
        self.A = []
        self.size = 0

    def build(self, X):  # O(n)
        self.A = [a for a in X]
        self.size = len(self.A)

    def __len__(self):
        return self.size  # O(1)

    def __iter__(self):
        yield from self.A  # O(n) iter_seq

    def get_at(self, i: int) -> int:  # O(1)
        return self.A[i]

    def set_at(self, i: int, x: int) -> None:  # O(1)
        self.A[i] = x

    def _copy_forward(self, i: int, n: int, A: list, j: int) -> None:  # O(N)
        for k in range(n):
            A[j + k] = self.A[i + k]

    def _copy_backward(self, i: int, n: int, A: list, j: int) -> None:  # O(N)
        for k in range(n - 1, -1, -1):
            A[j + k] = self.A[i + k]

    def insert_at(self, i: int, x: int) -> None:  # O(N)
        n = len(self)
        A = [None] * (n + 1)
        self._copy_forward(0, i, A, 0)
        A[i] = x
        self._copy_forward(i, n - i, A, i + 1)
        self.build(A)

    def delete_at(self, i: int) -> int:  # O(N)
        n = len(self)
        A = [None] * (n - 1)
        self._copy_forward(0, i, A, 0)
        x = self.A[i]
        self._copy_forward(i + 1, n - i - 1, A, i)
        self.build(A)
        return x

    def insert_last(self, x: int) -> None:
        self.insert_at(len(self), x)

    def delete_last(self) -> None:
        self.delete_at(len(self) - 1)

    def insert_first(self, x: int) -> None:
        self.insert_at(0, x)

    def delete_first(self) -> None:
        self.delete_at(0)


if __name__ == "__main__":
    # Here is a unit test for the code
    # Unit Test Start
    A = Array_Seq()
    A.build([1, 2, 3, 4, 5])
    # Run operations on the array
    A.insert_at(3, 6)
    A.insert_first(5)
    A.insert_last(10)

    assert A.A == [5, 1, 2, 3, 6, 4, 5, 10]

    A.delete_at(3)
    A.delete_last()
    A.delete_first()

    assert A.A == [1, 2, 6, 4, 5]
