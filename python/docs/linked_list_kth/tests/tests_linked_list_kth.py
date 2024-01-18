# Test cases
# Case 1: k is 0
ll1 = LinkedList()
ll1.head = Node(1)
ll1.head.next = Node(3)
ll1.head.next.next = Node(8)
ll1.head.next.next.next = Node(2)
assert ll1.kthFromEnd(0) == 2

# Case 2: k is 2
ll2 = LinkedList()
ll2.head = Node(1)
ll2.head.next = Node(3)
ll2.head.next.next = Node(8)
ll2.head.next.next.next = Node(2)
assert ll2.kthFromEnd(2) == 3

# Case 3: k is greater than the length of the linked list
ll3 = LinkedList()
ll3.head = Node(1)
ll3.head.next = Node(3)
ll3.head.next.next = Node(8)
ll3.head.next.next.next = Node(2)
try:
    ll3.kthFromEnd(6)
except Exception as e:
    assert str(e) == "k is greater than the length of the linked list"

# Case 4: k is not a positive integer
ll4 = LinkedList()
ll4.head = Node(1)
ll4.head.next = Node(3)
ll4.head.next.next = Node(8)
ll4.head.next.next.next = Node(2)
try:
    ll4.kthFromEnd(-1)
except Exception as e:
    assert str(e) == "Invalid value of k"

# Case 5: Linked list of size 1
ll5 = LinkedList()
ll5.head = Node(5)
assert ll5.kthFromEnd(0) == 5

# Case 6: Happy Path - k is in the middle of the linked list
ll6 = LinkedList()
ll6.head = Node(1)
ll6.head.next = Node(3)
ll6.head.next.next = Node(8)
ll6.head.next.next.next = Node(2)
assert ll6.kthFromEnd(1) == 8

print("All test cases passed!")