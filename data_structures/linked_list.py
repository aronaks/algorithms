class Element(object):

    def __init__(self, key):
        self.key = key
        self.next_element = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        self.size = 1 if head else 0

    def __len__(self):
        return self.size

    def search(self, k):
        x = self.head
        while x and x.key != k:
            x = x.next_element
        return x

    def insert_before(self, x):
        new_element = Element(x)
        new_element.next_element = self.head
        self.head = new_element
        self.size += 1

    def delete(self, x):
        element = self.search(x)
        if element:
            new_next_element = element.next_element
            if new_next_element:
                element.key = new_next_element.key
                element.next_element = new_next_element.next_element
            self.size -= 1
        else:
            raise ValueError('Element is not present in the list, thus can not be removed')
