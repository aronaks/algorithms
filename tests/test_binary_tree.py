from data_structures.binary_tree import BinaryTree


def test_create_binary_tree_without_root():
    my_tree = BinaryTree()
    assert my_tree.root.key is None
    assert my_tree.root.left_key is None
    assert my_tree.root.right_key is None


def test_create_binary_tree_with_root_only():
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
