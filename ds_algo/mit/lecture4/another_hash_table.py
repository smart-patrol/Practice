class HashEntry:
    def __init__(self, key, data):
        # key of the entry
        self.key = key
        # data to be stored
        self.value = data
        # reference to new entry
        self.nxt = None

    def __str__(self):
        return str(entry.key) + ", " + entry.value


class HashTable:
    # Constructor
    def __init__(self):
        # Size of the HashTable
        self.slots = 10
        # Current entries in the table
        # Used while resizing the table when half of the table gets filled
        self.size = 0
        # List of HashEntry objects (by default all None)
        self.bucket = [None] * self.slots

    # Helper Functions

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.get_size() == 0

    # Hash Function
    def get_index(self, key):
        # hash is a built in function in Python
        hash_code = hash(key)
        index = hash_code % self.slots
        return index

    # we will make sure that the hash table doesn’t get loaded up beyond a certain threshold
    def resize(self):
        new_slots = self.slots * 2
        new_bucket = [None] * new_slots
        # rehash all items into new slots
        for item in self.bucket:
            head = item
            while head is not None:
                new_index = hash(head.key) % new_slots
                if new_bucket[new_index] is None:
                    new_bucket[new_index] = HashEntry(head.key, head.value)
                else:
                    node = new_bucket[new_index]
                    while node is not None:
                        if node.key is head.key:
                            node.value = head.value
                            node = None
                        elif node.nxt is None:
                            node.nxt = HashEntry(head.key, head.value)
                            node = None
                        else:
                            node = node.nxt
                head = head.nxt
        self.bucket = new_bucket
        self.slots = new_slots


if __name__ == "__main__":

    ht = HashTable()
    ht.insert(2, "London")
    # Collides with (2, "London") - Added next to it at the same index
    ht.insert(12, "Moscow")
    ht.insert(7, "Paris")

    print("Size of the list: " + str(ht.size))
