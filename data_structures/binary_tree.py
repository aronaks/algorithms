class Node:
    def __init__(self, key=None):
        self.parent_key = None
        self.left_key = None
        self.right_key = None
        self.key = key


class BinaryTree:

    def __init__(self):
        self.root = None

    def __search_impl(self, node, x):
        if not node:
            return None
        elif node.key == x:
            return node

        if x < node.key:
            return self.__search_impl(node.left_key, x)
        else:
            return self.__search_impl(node.right_key, x)

    @staticmethod
    def __find_min(node):
        if not node:
            return None
        minimum = node.key
        while node.left_key:
            minimum = node.left_key
        return minimum

    def __insert_impl(self, node, x, parent):

        if not node:
            self.root = Node(x)
            self.root.parent_key = parent
            return

        if x < node.key:
            self.__insert_impl(node.left_key, x, node)
        else:
            self.__insert_impl(node.right_key, x, node)

    def insert_key(self, x):
        self.__insert_impl(self.root, x, None)

    def search_tree(self, x):
        return self.__search_impl(self.root, x)

    def find_minimum(self):
        self.__find_min(self.root)
