class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
            raise ValueError("List is empty, cannot insert before.")
        
        # Handle insertion before the head separately
        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if not current.next:
            raise ValueError("Value not found in the list, cannot insert before.")

        new_node.next = current.next
        current.next = new_node
    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
            raise ValueError("List is empty, cannot insert after.")
        
        current = self.head
        while current and current.value != value:
            current = current.next

        if not current:
            raise ValueError("Value not found in the list, cannot insert after.")

        new_node.next = current.next
        current.next = new_node