# linked-list-insertions
Write the following methods for the Linked List class:

append
arguments: new value
adds a new node with the given value to the end of the list
insert before
arguments: value, new value
adds a new node with the given new value immediately before the first node that has the value specified
insert after
arguments: value, new value
adds a new node with the given new value immediately after the first node that has the value specified
## Whiteboard Process
![whiteboard](./whiteboard6.png)

## Approach & Efficiency
Time and complexity 

Append (append method):
Time Complexity: O(n), where n is the number of nodes in the linked list.
In the worst case, it iterates through the entire list to find the last node.
Insert Before (insert_before method):
Time Complexity: O(n), where n is the number of nodes in the linked list.
In the worst case, it iterates through the entire list to find the node with the specified value.
Insert After (insert_after method):
Time Complexity: O(n), where n is the number of nodes in the linked list.
In the worst case, it iterates through the entire list to find the node with the specified value.


## Solution
Append Method:

Adds a new value to the end of the list.
Creates a new node with the given value.
If the list is empty, the new node becomes the head of the list.
Otherwise, it traverses the list to find the last node and appends the new node to it.
Insert Before Method:

Inserts a new value immediately before the first node with a specified value.
Creates a new node with the given new value.
If the list is empty, it raises an error.
If the specified value matches the value of the head node, the new node becomes the new head.
Otherwise, it traverses the list to find the node with the specified value and inserts the new node before it.
Insert After Method:

Inserts a new value immediately after the first node with a specified value.
Creates a new node with the given new value.
If the list is empty, it raises an error.
Traverses the list to find the node with the specified value.
Inserts the new node after the found node.