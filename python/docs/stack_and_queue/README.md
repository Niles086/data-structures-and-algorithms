# stack_and_queue
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Whiteboard Process

Below

## Approach & Efficiency

Below 

## Solution

Below

Stack:
push Method:
Create a new node with the given value.
Set the next pointer of the new node to the current top of the stack.
Update the top to point to the new node.
Time Complexity: O(1) - Constant time, as the operation involves a fixed number of steps regardless of the size of the stack.

pop Method:
Check if the stack is empty.
Retrieve the value from the top node.
Update the top to point to the next node.
Time Complexity: O(1) - Constant time, as the operation involves a fixed number of steps regardless of the size of the stack.

peek Method:
Check if the stack is empty.
Return the value from the top node without removing it.
Time Complexity: O(1) - Constant time, as the operation involves a fixed number of steps regardless of the size of the stack.

is_empty Method:
Check if the top is None.
Time Complexity: O(1) - Constant time, as it involves a single check.

Queue:
enqueue Method:
Create a new node with the given value.
If the queue is empty, set the front to the new node.
Otherwise, traverse the queue to find the last node and append the new node.
Time Complexity: O(1) - Constant time for the best case (enqueue to an empty queue). In the worst case (enqueue to a non-empty queue), it's O(n) where n is the number of nodes in the queue.

dequeue Method:
Check if the queue is empty.
Retrieve the value from the front node.
Update the front to point to the next node.
Time Complexity: O(1) - Constant time, as the operation involves a fixed number of steps regardless of the size of the queue.

peek Method:
Check if the queue is empty.
Return the value from the front node without removing it.
Time Complexity: O(1) - Constant time, as the operation involves a fixed number of steps regardless of the size of the queue.

is_empty Method:
Check if the front is None.
Time Complexity: O(1) - Constant time, as it involves a single check.

