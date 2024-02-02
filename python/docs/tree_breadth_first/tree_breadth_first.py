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

# Example usage:
# Construct the tree
example = TreeNode(2)
example.left = TreeNode(7)
example.right = TreeNode(5)
example.left.left = TreeNode(2)
example.left.right = TreeNode(6)
example.right.right = TreeNode(9)
example.right.right.left = TreeNode(5)
example.right.right.right = TreeNode(11)
example.left.left.left = TreeNode(4)

# Call the breadth_first function
output = breadth_first(example)
print(output)
