# linked-list-zip
Write a function called zip lists
Arguments: 2 linked lists
Return: New Linked List, zipped as noted below
Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
Try and keep additional space down to O(1)
You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
## Whiteboard Process
![whiteboard](./whiteboard8.png)

## Approach & Efficiency
Time Complexity: O(min(m, n)), where m and n are the lengths of list1 and list2. The algorithm runs in linear time, iterating through the shorter of the two lists.

Space Complexity: O(1). The algorithm uses a constant amount of extra space regardless of the input size. It modifies the input lists in place without using additional data structures.

## Solution
list1 = 1 -> 3 -> 2 -> null
list2 = 5 -> 9 -> 4 -> null


Initialize pointers current1 and current2 at the heads.
Iteration 1:
current1.next = list2 (1 -> 5 -> ...)
current2.next = temp1 (3 -> ...)
Move current1 to temp1 and current2 to temp2.
Iteration 2:
current1.next = list2 (1 -> 5 -> 3 -> 9 -> ...)
current2.next = temp1 (2 -> ...)
Move current1 to temp1 and current2 to temp2.
Iteration 3:
current1.next = list2 (1 -> 5 -> 3 -> 9 -> 2 -> ...)
current2.next = temp1 (null)
Move current1 to temp1 and current2 to temp2.
Result: 1 -> 5 -> 3 -> 9 -> 2 -> 4 -> null
The algorithm alternates between nodes of list1 and list2, modifying list1 in place. The time complexity is linear, and the space complexity is constant.