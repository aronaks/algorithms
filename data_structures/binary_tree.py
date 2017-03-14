class Node:
    def __init__(self, key=None):
        self.parent_key = None
        self.left_key = None
        self.right_key = None
        self.key = key


class BinaryTree:

    def __init__(self):
        self.__root = None

    def __search_impl(self, node, x):
        if not node:
            return None
        elif node.key == x:
            return node

        if x < node.key:
            return self.__search_impl(node.left_key, x)
        else:
            return self.__search_impl(node.right_key, x)

    def insert_key(self, z):
        parent = None
        current = self.__root
        z = Node(z)
        while current:
            parent = current
            if z.key < current.key:
                current = current.left_key
            else:
                current = current.right_key
        z.parent_key = parent
        if not parent:
            self.__root = z
        elif z.key < parent.key:
            parent.left_key = z
        else:
            parent.right_key = z

    def search_tree(self, x):
        return self.__search_impl(self.__root, x)

    def find_min(self):
        if not self.__root:
            return None
        min_item = self.__root
        while min_item.left_key:
            min_item = min_item.left_key
        return min_item.key

    def find_max(self):
        if not self.__root:
            return None
        max_item = self.__root
        while max_item.right_key:
            max_item = max_item.right_key
        return max_item.key
