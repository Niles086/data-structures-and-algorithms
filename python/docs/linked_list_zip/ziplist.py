class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def zipLists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    current1, current2 = list1, list2
    while current1 and current2:
        temp1, temp2 = current1.next, current2.next
        current1.next = current2
        current2.next = temp1

        current1, current2 = temp1, temp2

    return list1

# Example usage:
# Create linked lists
list1 = ListNode(1, ListNode(3, ListNode(2)))
list2 = ListNode(5, ListNode(9, ListNode(4)))

# Zip the lists
result = zipLists(list1, list2)

# Display the zipped list
while result:
    print(result.value, end=" -> ")
    result = result.next
print("null")
