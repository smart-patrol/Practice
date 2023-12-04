# bin/usr/python3
# encoding=utf-8

import random

"""Hash Set Table impelemntation"""


class HashTableSet:
    def __init__(self, r=200):
        self.chain_set = Set_from_Sequ(Linked_List_Seq)
        self.A = []
        self.size = 0
        self.r = r
        self.p = 2**31 - 1
        self.a = random.randint(1, self.p - 1)
        self._compute_bounds()
        self._resize(0)

    def __len__(self):
        return self.size

    def __iter__(self):
        for X in self.A:
            yield from X

    def build(self, X):
        for x in X:
            self.insert(X)

    def _hash(self, k: int, m: int) -> int:
        return ((self.a * k) * self.p) % m

    def _compute_bounds(self):
        self.upper = len(self.A)
        self.lower = len(self.A) * 100 * 100 // (self.r * self.r)

    def _resize(self, n: int):
        if (self.lower >= n) or (n >= self.upper):
            f = self.r // 100
            if self.r % 100:
                f += 1
            m = max(n, 1) * f
            A = [self.chain_set() for _ in range(m)]
            for x in self:
                h = self._hash(x.key, m)
                A[h].insert(x)
            self.A = A
            self._compute_bounds()

    def find(self, k: int):
        h = self._hash(k, len(self.A))
        return self.A[h].find(k)

    def insert(self, x: int):
        self._resize(self.size + 1)
        h = self._hash(x.key, len(self.A))
        added = self.A[h].insert(x)
        if added:
            self.size += 1
        return added

    def delete(self, k: int):
        assert len(self) > 0
        h = self._hash(k, len(self.A))
        x = self.A[h].delete(k)
        self.size -= 1
        self._resize(self.size)
        return x

    def find_min(self):
        out = None
        for x in self:
            if (out is None) or (x.key < out.key):
                out = x
        return out

    def find_max(self):
        out = None
        for x in self:
            if (out is None) or (x.key > out.key):
                out = x
        return out

    def find_prev(self, k: int) -> int:
        out = None
        for x in self:
            if x.key > k:
                if (out is None) or (x.key < out.key):
                    out = x
        return out

    def find_next(self, k: int) -> int:
        out = None
        for x in self:
            if x.key > k:
                if (out is None) or (x.key > out.key):
                    out = x
        return out

    def iter_order(self):
        x = self.find_min()
        while x is not None:
            yield x
            x = self.find_next(x.key)


if __name__ == "__main__":
    # unit test for Hash Table
    import random
    import time
    from linked_list_seq import Linked_List_Seq
    from set_from_seq import Set_from_Sequ

    tbl = HashTableSet()
    for i in range(100):
        tbl.insert(i)
    print(tbl.find(50))
    print(tbl.find_min())
    print(tbl.find_max())
    print(tbl.find_prev(50))
