class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def preorder_traversal(self, node, result=[]):
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        return result

    def inorder_traversal(self, node, result=[]):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result

    def postorder_traversal(self, node, result=[]):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
        return result


class BinarySearchTree(BinaryTree):
    def add(self, value):
        self.root = self._add(self.root, value)

    def _add(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._add(node.left, value)
        elif value > node.value:
            node.right = self._add(node.right, value)

        return node

    def contains(self, value):
        return self._contains(self.root, value)

    def _contains(self, node, value):
        if not node:
            return False

        if value == node.value:
            return True
        elif value < node.value:
            return self._contains(node.left, value)
        else:
            return self._contains(node.right, value)


# Testing
# 1. Instantiate an empty tree
empty_tree = BinaryTree()
print(empty_tree.preorder_traversal(empty_tree.root))  # Output: []

# 2. Instantiate a tree with a single root node
single_node_tree = BinaryTree(Node(10))
print(single_node_tree.preorder_traversal(single_node_tree.root))  # Output: [10]

# 3. Add left and right child to a node in Binary Search Tree
bst = BinarySearchTree(Node(10))
bst.add(5)
bst.add(15)
print(bst.preorder_traversal(bst.root))  # Output: [10, 5, 15]

# 4. Traversal collections
print(bst.preorder_traversal(bst.root))  # Output: [10, 5, 15]
print(bst.inorder_traversal(bst.root))   # Output: [5, 10, 15]
print(bst.postorder_traversal(bst.root)) # Output: [5, 15, 10]

# 5. Contains method
print(bst.contains(5))   # Output: True
print(bst.contains(8))   # Output: False
