class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def find_maximum_value(self):
        return self._find_maximum_value_recursive(self.root)

    def _find_maximum_value_recursive(self, node):
        if node is None:
            return float('-inf')  # Return negative infinity for empty nodes

        max_value = node.value
        left_max = self._find_maximum_value_recursive(node.left)
        right_max = self._find_maximum_value_recursive(node.right)

        max_value = max(max_value, left_max, right_max)
        return max_value

# Example usage:
# Create a binary tree
example_tree = BinaryTree(5)
example_tree.root.left = TreeNode(3)
example_tree.root.right = TreeNode(7)
example_tree.root.left.left = TreeNode(2)
example_tree.root.left.right = TreeNode(4)
example_tree.root.right.left = TreeNode(6)
example_tree.root.right.right = TreeNode(11)

# Find the maximum value in the tree
max_value = example_tree.find_maximum_value()
print(max_value)  # Output: 11
