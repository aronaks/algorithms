import unittest

from data_structures.linked_list import Element, LinkedList


class TesLinkedList(unittest.TestCase):

    def test_create_empty_linked_list(self):
        my_list = LinkedList()
        self.assertIsNone(my_list.head)
        self.assertFalse(len(my_list))

    def test_create_linked_list_with_head_only(self):
        head = Element(2)
        my_list = LinkedList(head)
        self.assertEqual(my_list.head, head)
        self.assertEqual(len(my_list), 1)

    def test_insert_element_before(self):
        my_list = LinkedList()
        first_element = 0
        my_list.insert_before(first_element)
        self.assertEqual(my_list.head.key, first_element)
        self.assertIsNone(my_list.head.next_element)
        for i in range(1, 5):
            my_list.insert_before(i)
            self.assertEqual(my_list.head.key, i)
            self.assertEqual(my_list.head.next_element.key, i - 1)

    def test_search_for_element_present(self):
        my_list = LinkedList()
        for i in range(5):
            my_list.insert_before(i)
            self.assertEqual(my_list.search(i).key, i)

    def test_search_for_element_absent(self):
        my_list = LinkedList()
        for i in range(5):
            my_list.insert_before(i)
        self.assertIsNone(my_list.search(6))

    def test_delete_middle_element_present(self):
        my_list = LinkedList()
        list_length = 5
        for i in range(list_length):
            my_list.insert_before(i)
        middle_element = 3
        my_list.delete(middle_element)
        self.assertIsNone(my_list.search(middle_element))
        self.assertEqual(len(my_list), list_length - 1)

    def test_delete_head(self):
        my_list = LinkedList()
        list_length = 5
        for i in range(list_length):
            my_list.insert_before(i)
        head = 4
        my_list.delete(head)
        self.assertIsNone(my_list.search(head))
        self.assertEqual(my_list.head.key, 3)
        self.assertEqual(my_list.head.next_element.key, 2)
        self.assertEqual(len(my_list), list_length - 1)

    def test_delete_last_element(self):
        my_list = LinkedList()
        list_length = 5
        for i in range(list_length):
            my_list.insert_before(i)
        last_element = 0
        my_list.delete(last_element)
        self.assertIsNone(my_list.search(last_element))
        self.assertIsNone(my_list.search(1).next_element.key)
        self.assertEqual(len(my_list), list_length - 1)

    def test_delete_element_absent(self):
        my_list = LinkedList()
        list_length = 5
        for i in range(list_length):
            my_list.insert_before(i)
        with self.assertRaises(ValueError):
            my_list.delete(5)
        self.assertEqual(len(my_list), list_length)
