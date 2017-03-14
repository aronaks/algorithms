class Node:
    def __init__(self, key):
        self.parent_key = None
        self.left_key = None
        self.right_key = None
        self.key = key


class BinaryTree:

    def __init__(self, key=None):
        self.root = Node(key)

    def __search_impl(self, node, x):
        if not node:
            return None
        elif node.key == x:
            return node

        if x < node.key:
            return self.__search_impl(node.left_key, x)
        else:
            return self.__search_impl(node.right_key, x)

    def __find_min(self, node):
        if not node:
            return None
        minimum = node.key
        while node.left_key:
            minimum = node.left_key
        return minimum

    def search_tree(self, x):
        return self.__search_impl(self.root, x)

    def find_minimum(self):
        self.__find_min(self.root)
