from Queue import Queue


class ListQueue(Queue):

    class Node:
        def __init__(self):  # unnecessary
            self.data = None
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, t):
        n = ListQueue.Node()
        n.data = t
        if self.empty():
            self.first = n
            self.last = n
        else:
            self.last.next = n
            self.last = n

    def dequeue(self):
        if self.empty():
            raise Exception('Queue is empty')
        elif self.first is self.last:  # if queue has 1 element
            self.first = None
            self.last = None
        else:
            self.first = self.first.next

    def front(self):
        if self.empty():
            raise Exception('Queue is empty')
        else:
            return self.first.data

    def empty(self):
        return self.first is None and self.last is None
