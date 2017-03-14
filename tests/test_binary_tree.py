from data_structures.binary_tree import BinaryTree


def test_create_linked_list_with_root_only():
    root = 2
    my_tree = BinaryTree(root)
    assert my_tree.root.key == root


def test_search_for_element_present():
    root = 8
    my_tree = BinaryTree(root)
    assert my_tree.search_tree(8).key == root


def test_search_for_element_absent():
    my_tree = BinaryTree(10)
    assert my_tree.search_tree(19) is None
