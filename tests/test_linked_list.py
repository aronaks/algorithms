import pytest

from data_structures.linked_list import LinkedList


def test_create_empty_linked_list():
    my_list = LinkedList()
    assert not len(my_list)


def test_search_for_element_present():
    my_list = LinkedList()
    for i in range(5):
        my_list.insert_before(i)
        assert my_list.search(i).key == i


def test_search_for_element_absent():
    my_list = LinkedList()
    for i in range(5):
        my_list.insert_before(i)
    assert my_list.search(6) is None


def test_delete_middle_element_present():
    my_list = LinkedList()
    list_length = 5
    for i in range(list_length):
        my_list.insert_before(i)
    middle_element = 3
    my_list.delete(middle_element)
    assert my_list.search(middle_element) is None
    assert len(my_list) == (list_length - 1)


def test_delete_head():
    my_list = LinkedList()
    list_length = 5
    for i in range(list_length):
        my_list.insert_before(i)
    head = 4
    my_list.delete(head)
    assert my_list.search(head) is None
    assert len(my_list) == (list_length - 1)


def test_delete_last_element():
    my_list = LinkedList()
    list_length = 5
    for i in range(list_length):
        my_list.insert_before(i)
    last_element = 0
    my_list.delete(last_element)
    assert my_list.search(last_element) is None
    assert my_list.search(1).next_element.key is None
    assert len(my_list) == (list_length - 1)


def test_delete_element_absent():
    my_list = LinkedList()
    list_length = 5
    for i in range(list_length):
        my_list.insert_before(i)
    with pytest.raises(ValueError):
        my_list.delete(5)
    assert len(my_list) == list_length


def test_iterate_over_linked_list():
    my_list = LinkedList()
    for i in range(5):
        my_list.insert_before(i)

    for el in my_list:
        for el1 in my_list:
            print('{} {}'.format(el,el1))
