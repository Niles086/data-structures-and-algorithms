class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def kthFromEnd(self, k):
        if self.head is None or k < 0:
            raise Exception("Invalid value of k")

        # Use two pointers to find the kth node from the end
        slow_ptr = fast_ptr = self.head

        # Move fast_ptr k nodes ahead
        for _ in range(k):
            if fast_ptr is None:
                raise Exception("k is greater than the length of the linked list")
            fast_ptr = fast_ptr.next

        # Move both pointers until fast_ptr reaches the end
        while fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        return slow_ptr.value
