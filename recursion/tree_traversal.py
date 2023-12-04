# tree data structure in python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode, vals: list) -> list:
    """Access data in parent nodes before child nodes"""
    # root > left > right
    # note: left to right traversal down the tree, starting at root
    if root:
        vals.append(root.val)
        preorder_traversal(root.left,vals)
        preorder_traversal(root.right,vals)
        return vals

def postorder_traversal(root: TreeNode, vals: list) -> list:
    """Access the child node data before the parent node"""
    # left > right > root
    # note: will display left before right, bottom before top
    if root:
        postorder_traversal(root.left,vals)
        postorder_traversal(root.right,vals)
        vals.append(root.val)
        return vals

def inorder_traversal(root: TreeNode, vals: list) -> list:
    """Access the data in the parent node between the left and right child nodes"""
    # left > root > right
    # note: commonly used to retrieve the nodes of a binary tree in sorted order
    if root:
        inorder_traversal(root.left,vals)
        vals.append(root.val)
        inorder_traversal(root.right,vals)
        return vals

def get_depth(root: TreeNode, depth:int) -> int:
    """Get the depth of a tree using recursion"""
    if root is None:
        return depth
    if root:
        left_depth = get_depth(root.left, depth+1)
        right_depth = get_depth(root.right, depth+1)
        return max(left_depth, right_depth)



# Create the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(preorder_traversal(root,[]))
print(postorder_traversal(root,[]))
print(inorder_traversal(root,[]))


get_depth(root, 0)

