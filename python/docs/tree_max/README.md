# Tree Max
Write the following method for the Binary Tree class

find maximum value
Arguments: none
Returns: number
Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process
![whiteboard](./whiteboard16.png)

## Approach & Efficiency
Approach:

The approach used in the provided code is a recursive depth-first traversal of the binary tree. The method _find_maximum_value_recursive is a helper function that explores the tree in a depth-first manner, visiting each node and comparing the values to find the maximum. The algorithm follows these steps:

If the current node is None, return negative infinity (float('-inf')) to indicate an empty node.
Initialize max_value with the value of the current node.
Recursively call the method on the left subtree and right subtree.
Update max_value by taking the maximum of the current node's value, the maximum value from the left subtree, and the maximum value from the right subtree.
Return the updated max_value.
Efficiency:

Time Complexity:

The time complexity of the algorithm is O(N), where N is the number of nodes in the binary tree.
This is because in the worst case, the algorithm needs to visit every node in the tree once to find the maximum value.
Space Complexity:

The space complexity is O(H), where H is the height of the binary tree.
This is due to the recursive nature of the algorithm, and the maximum recursion depth is determined by the height of the tree.
In the worst case, for a skewed tree, the height can be equal to the number of nodes, resulting in O(N) space complexity.
For a balanced tree, the height is logarithmic, resulting in better space efficiency (O(log N)).

## Solution
<!-- Show how to run your code, and examples of it in action -->
