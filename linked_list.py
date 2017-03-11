class Element(object):

    def __init__(self, key):
        self.key = key
        self.next_element = None


class LinkedList(object):

    def __init__(self, key=None):
        self.head = Element(key)

    def search(self, k):
        x = self.head
        while x and x.key != k:
            x = x.next_element
        return x

    def insert(self, x):
        new_element = Element(x)
        new_element.next_element = self.head
        self.head = new_element

    def delete(self, x):
        element = self.search(x)
        if element:
            self.head = element.next_element
