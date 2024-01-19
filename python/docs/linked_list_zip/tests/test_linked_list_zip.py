def test_zipLists():
    # Test Case 1
    list1 = ListNode(1, ListNode(3, ListNode(2)))
    list2 = ListNode(5, ListNode(9, ListNode(4)))
    assert str(zipLists(list1, list2)) == "1 -> 5 -> 3 -> 9 -> 2 -> 4 -> null"

    # Test Case 2
    list1 = ListNode(1, ListNode(3))
    list2 = ListNode(5, ListNode(9, ListNode(4)))
    assert str(zipLists(list1, list2)) == "1 -> 5 -> 3 -> 9 -> 4 -> null"

    # Test Case 3
    list1 = ListNode(1, ListNode(3, ListNode(2)))
    list2 = None
    assert str(zipLists(list1, list2)) == "1 -> 3 -> 2 -> null"

    # Test Case 4
    list1 = None
    list2 = ListNode(5, ListNode(9, ListNode(4)))
    assert str(zipLists(list1, list2)) == "5 -> 9 -> 4 -> null"

    # Test Case 5 (empty lists)
    list1 = None
    list2 = None
    assert str(zipLists(list1, list2)) == "null"

test_zipLists()
