"""
Linked List Sequence Data Structure
"""


class LinkedList:
    def __init__(self, x):  # O(1)
        self.item = x
        self.next = None

    def later_node(self, i: int):  # O(i)
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)


class LinkedListSeq:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):  # O(n)
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X):  # O(n)
        for a in reversed(X):
            self.insert_first(a)

    def get_at(self, i):  # O(i)
        return self.later_node(i).item
        return node.item

    def set_at(self, i, x):  # O(i)
        self.later_node(i).item = x
        node.item = x

    def insert_first(self, x):  # O(1)
        new_node = LinkedList(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete_first(self):  # O(1)
        assert self.head
        self.head = self.head.next
        self.size -= 1

    def insert_at(self, i: int, x: int) -> None:  # O(i)
        if i == 0:
            self.insert_first(x)
            return
        else:
            new_node = LinkedList(x)
            node = self.head.later_node(i - 1)
            new_node.next = node.next
            node.next = new_node
            self.size += 1

    def delete_at(self, i: int) -> int:  # O(i)
        if i == 0:
            self.delete_first()
            return
        else:
            node = self.head.later_node(i - 1)
            x = node.next.item
            node.next = node.next.next
            self.size -= 1
            return x

    # O(n)
    def insert_last(self, x):
        self.insert_at(len(self), x)

    def delete_last(self):
        self.delete_at(len(self) - 1)


if __name__ == "__main__":
    # Write unit test for the linked list
    # Start Test here:
    pass
