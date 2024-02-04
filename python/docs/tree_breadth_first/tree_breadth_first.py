import unittest

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def breadth_first(tree):
    result = []
    if not tree:
        return result
    
    # Use a queue to perform breadth-first traversal
    queue = [tree]

    while queue:
        current_node = queue.pop(0)  # Dequeue the front node
        result.append(current_node.value)

        # Enqueue left and right children if they exist
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result
class TestBreadthFirst(unittest.TestCase):
    def setUp(self):
# Construct the example tree
        self.example_tree = TreeNode(2)
        self.example_tree.left = TreeNode(7)
        self.example_tree.right = TreeNode(5)
        self.example_tree.left.left = TreeNode(2)
        self.example_tree.left.right = TreeNode(6)
        self.example_tree.right.right = TreeNode(9)
        self.example_tree.right.right.left = TreeNode(5)
        self.example_tree.right.right.right = TreeNode(11)
        self.example_tree.left.left.left = TreeNode(4)


def test_breadth_first(self):
        result = breadth_first(self.example_tree)
        expected_output = [2, 7, 5, 2, 6, 9, 5, 11, 4]
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
    
# Call the breadth_first function
output = breadth_first(example)
print(output)
