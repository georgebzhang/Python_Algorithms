from OrderedSet import OrderedSet


class ListOrderedSet(OrderedSet):
    # helper classes and functions
    class Node:
        def __init__(self):
            self.data = None
            self.prev = None
            self.next = None

    def empty(self):
        return self.head is None

    def find(self, t):
        pass

    # "public" functions
    def __init__(self):
        self.head = None

    def insert(self, t):
        pass

    def remove(self, t):
        pass

    def has(self, t):
        pass

    def print(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data, " ", end="")
        print()
