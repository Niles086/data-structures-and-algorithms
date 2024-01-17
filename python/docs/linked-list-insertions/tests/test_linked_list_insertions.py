import unittest
import pytest
from linked_list_insertions import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_append(self):
        linked_list = LinkedList()
        linked_list.append(1)
        self.assertEqual(linked_list.head.value, 1)

    def test_append_multiple_nodes(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(2)
        self.assertEqual(linked_list.head.next.value, 3)
        self.assertEqual(linked_list.head.next.next.value, 2)

    def test_insert_before_middle_node(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.insert_before(3, 5)
        self.assertEqual(linked_list.head.next.value, 5)
        self.assertEqual(linked_list.head.next.next.value, 3)

    @pytest.mark.skip("pending")
    def test_insert_before_first_node(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.insert_before(1, 7)
        self.assertEqual(linked_list.head.value, 7)
        self.assertEqual(linked_list.head.next.value, 5)

    def test_insert_after_middle_node(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.insert_after(5, 9)
        self.assertEqual(linked_list.head.next.next.value, 9)
        self.assertEqual(linked_list.head.next.next.next.value, 3)

    @pytest.mark.skip("pending")
    def test_insert_after_last_node(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.insert_after(2, 11)
        self.assertEqual(linked_list.head.next.next.next.next.value, 11)

    def test_insert_after_value_not_found(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(3)
        linked_list.append(2)
        with self.assertRaises(ValueError):
            linked_list.insert_after(4, 13)

if __name__ == '__main__':
    unittest.main()
