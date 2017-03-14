from data_structures.binary_tree import BinaryTree


def test_insert_element_into_binary_tree():
    my_tree = BinaryTree()
    for i in range(5):
        my_tree.insert_key(i)
    assert my_tree.search_tree(1).key == 1
    assert my_tree.search_tree(11) is None
