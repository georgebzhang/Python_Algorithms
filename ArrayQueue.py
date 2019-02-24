from Queue import Queue


class ArrayQueue(Queue):
    MAX_CAPACITY = 100

    def __init__(self):
        self.data = [0] * ArrayQueue.MAX_CAPACITY
        self.ind_front = 0
        self.ind_back = 0

    def enqueue(self, param1):
        self.data[self.ind_back] = param1
        self.ind_back = (self.ind_back + 1) % ArrayQueue.MAX_CAPACITY

    def dequeue(self):
        if self.empty():
            raise Exception('Queue is empty')
        else:
            self.ind_front = (self.ind_front + 1) % ArrayQueue.MAX_CAPACITY

    def front(self):
        if self.empty():
            raise Exception('Queue is empty')
        else:
            return self.data[self.ind_front]

    def empty(self):
        return self.ind_front == self.ind_back
