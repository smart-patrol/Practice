"""
Set Implementation in python
https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/mit6_006s20_r02/
"""
from array_sequence import Array_Seq


class SetFromSeq(Array_Seq):
    def __init__(self):
        self.S = Array_Seq()

    def __len__(self):
        return len(self.S)

    def __iter__(self):
        yield from self.S

    def build(self, A):
        self.S.build(A)

    def insert(self, x: int):
        """add x to set (replace item with key x.key if one already exists)"""
        for i in range(len(self.S)):
            if self.S.get_at(i).key == x.key:
                self.S.set_at(i, x)
                return
            self.S.insert_last(x)

    def delete(self, k):
        for i in range(len(self.S)):
            if self.S.get_at(i).key == k:
                return self.delete_at(i)

    def find(self, k):  # k=key
        """return the stored item with key k"""
        if x in self.S:
            if x.key == k:
                return x
        else:
            return None

    def find_min(self):
        """return the stored item with smallest key"""
        out = None
        for x in self:
            if (out is None) or (x.key < out.key):
                out = x
        return out

    def find_max(self):
        """return the stored item with largest key"""
        out = None
        for x in self:
            if (out is None) or (x.key > out.key):
                out = x
        return out

    def find_next(self, k):
        """return the stored item with smallest key larger than k"""
        out = None
        for x in self:
            if x.key > k:
                if (out is None) or (x.key < out.key):
                    out = x
        return out

    def find_prev(self, k):
        """return the stored item with largets key larger than k"""
        out = None
        for x in self:
            if x.key < k:
                if (out is None) or (x.key > out.key):
                    out = x
        return out

    def iter_ord(self):
        """return the stored items one-by-one in key order"""
        x = self.find_min()
        while x:
            yield x
            x = self.find_next(x.key)


if __name__ == "__main__":
    # Create unit test on the next line
    # Unit test start:
    S = SetFromSeq()
    S.build([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    for i in S:
        print(i)
