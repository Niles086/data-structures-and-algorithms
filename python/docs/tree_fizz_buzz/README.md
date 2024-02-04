# tree fizz buzz
<!-- Description of the challenge -->

## Whiteboard Process
![whiteboard](./whiteboard.png)

## Approach & Efficiency
As for space complexity, the main factor is the recursive call stack during the tree traversal. The space complexity is O(H), where H is the height of the k-ary tree. In the worst case, when the tree is linear (each node has only one child), H is equal to N, making the space complexity O(N). However, for more balanced k-ary trees, the space complexity would be less than O(N). The additional space required for the new k-ary tree is also O(N) since each node is visited and transformed.

In terms of efficiency, the code is quite efficient as it processes each node exactly once, and the Fizz Buzz transformation is performed in constant time. The recursive approach simplifies the implementation and readability.






## Solution
<!-- Show how to run your code, and examples of it in action -->
