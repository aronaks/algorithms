class Element:

    def __init__(self, key):
        self.key = key
        self.next_element = None


class LinkedListIter:

    def __init__(self, element):
        self.__element = element

    def __iter__(self):
        return self

    def __next__(self):
        if self.__element:
            res = self.__element.key
            self.__element = self.__element.next_element
            return res
        else:
            raise StopIteration


class LinkedList:

    def __init__(self):
        self.__head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return LinkedListIter(self.__head)

    def search(self, k):
        x = self.__head
        while x and x.key != k:
            x = x.next_element
        return x

    def insert_before(self, x):
        new_element = Element(x)
        new_element.next_element = self.__head
        self.__head = new_element
        self.size += 1

    def delete(self, x):
        element = self.search(x)
        if element:
            new_next_element = element.next_element
            if new_next_element:
                element.key = new_next_element.key
                element.next_element = new_next_element.next_element
            else:
                element.key = element.next_element
                element.next_element = None
            self.size -= 1
        else:
            raise ValueError('Element is not present in the list, thus can not be removed')
