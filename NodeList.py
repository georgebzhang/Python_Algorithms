from List import List


class NodeList(List):
    class Node:
        def __init__(self):
            self.data = None
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert_front(self, t):
        n = NodeList.Node()
        n.data = t
        if self.empty():
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n
        self.length += 1

    def insert_back(self, t):
        n = NodeList.Node()
        n.data = t
        if self.empty():
            self.head = n
            self.tail = n
        else:
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
        self.length += 1

    def remove_front(self):
        if self.empty():
            raise Exception('List is empty')
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1

    def remove_back(self):
        if self.empty():
            raise Exception('List is empty')
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
        self.length -= 1

    def find(self, index):
        ptr = self.head
        for i in range(index):
            ptr = ptr.next
        return ptr

    def insert(self, index, t):
        if index > self.length:
            raise Exception('Index exceeds length')
        if index == 0:
            self.insert_front(t)
        elif index == self.length:
            self.insert_back(t)
        else:
            n = NodeList.Node()
            n.data = t
            n_index = self.find(index)
            n_index.prev.next = n
            n.prev = n_index.prev
            n.next = n_index;
            n_index.prev = n
            self.length += 1

    def remove(self, index):
        if self.empty():
            raise Exception('List is empty')
        if index >= self.length:
            raise Exception('Index exceeds length')
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            n_index = self.find(index)
            n_index.prev.next = n_index.next
            n_index.next.prev = n_index.prev
            self.length -= 1

    def size(self):
        return self.length

    def empty(self):
        return self.length == 0

    def print(self):
        if self.empty():
            print('List is empty')
        elif self.length == 1:
            print(self.head.data)
        else:
            ptr = self.head
            for i in range(self.length):
                print(ptr.data, " ", end="")
                ptr = ptr.next
            print()
