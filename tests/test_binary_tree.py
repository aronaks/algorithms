from data_structures.binary_tree import BinaryTree


def test_create_binary_tree_without_root():
    my_tree = BinaryTree()
    assert my_tree.root is None


def test_insert_element_into_binary_tree():
    my_tree = BinaryTree()
    my_tree.insert_key(10)
    assert my_tree.search_tree(10).key == 10
    assert my_tree.search_tree(11) is None
