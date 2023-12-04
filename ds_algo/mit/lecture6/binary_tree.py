from binary_node import Binary_Node


class Binary_Tree:
    def __init__(T, node_type=Binary_Node):
        T.root = None
        T.node_type = node_type
        T.size = 0

    def __len__(T):
        return T.size

    def __iter__(T):
        if T.root:
            for A in T.root.subtree_iter():
                yield A.item

    def build(T, X):
        A = [x for x in X]

        def build_subtree(A, i, j):
            if i > j:
                return None
            c = (i + j) // 2
            root = T.node_type(A[c])
            if i < c:
                root.left = build_subtree(A, i, c - 1)
                root.left.parent = root
            if c < j:
                root.right = build_subtree(A, c + 1, j)
                root.right.parent = root
            return root

        T.root = build_subtree(A, 0, len(A) - 1)
        T.size = len(A)

    def tree_iter(T):
        node = T.subtree_first()
        while node:
            yield node
            node = node.successor()


if __name__ == "__main__":
    T = Binary_Tree()
    nums = [1, 2, 3, 4, 5, 6, 7]
    T.build(nums)
    for i, A in enumerate(T):
        assert A == nums[i]
