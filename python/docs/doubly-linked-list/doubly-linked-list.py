import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        result = ""
        current = self.head
        while current:
            result += f"{{ {current.value} }} -> "
            current = current.next
        return result + "NULL"

class TestLinkedListMethods(unittest.TestCase):
    def test_instantiate_empty_linked_list(self):
        ll = LinkedList()
        self.assertIsNone(ll.head)

    def test_insert_into_linked_list(self):
        ll = LinkedList()
        ll.insert(10)
        self.assertEqual(ll.head.value, 10)

    def test_head_points_to_first_node(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        self.assertEqual(ll.head.value, 20)

    def test_insert_multiple_nodes(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        ll.insert(30)
        self.assertEqual(ll.head.value, 30)

    def test_find_existing_value(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        ll.insert(30)
        self.assertTrue(ll.includes(20))

    def test_find_nonexistent_value(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        ll.insert(30)
        self.assertFalse(ll.includes(40))

    def test_return_all_values_in_linked_list(self):
        ll = LinkedList()
        ll.insert(10)
        ll.insert(20)
        ll.insert(30)
        self.assertEqual(ll.to_string(), "{ 30 } -> { 20 } -> { 10 } -> NULL")

if __name__ == '__main__':
    unittest.main()
