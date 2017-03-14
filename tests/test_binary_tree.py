from data_structures.binary_tree import BinaryTree


def test_insert_element_into_binary_tree():
    my_tree = BinaryTree()
    for i in range(5):
        my_tree.insert_key(i)
    assert my_tree.search_tree(1).key == 1
    assert my_tree.search_tree(11) is None


def test_find_min():
    my_tree = BinaryTree()
    for i in range(5):
        my_tree.insert_key(i)
    min_item = my_tree.find_min()
    assert 0 == min_item


def test_find_max():
    my_tree = BinaryTree()
    for i in range(5):
        my_tree.insert_key(i)
    max_item = my_tree.find_max()
    assert 4 == max_item


def test_traversing():
    my_tree = BinaryTree()
    for i in range(5):
        my_tree.insert_key(i)
    expected_res = 0
    tree = my_tree.traverse_tree()
    for n in tree:
        assert expected_res == n
        expected_res += 1
