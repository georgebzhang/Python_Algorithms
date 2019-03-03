from abc import ABC, abstractmethod


class Queue(ABC):
    @abstractmethod
    def enqueue(self, t):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def front(self):
        pass

    @abstractmethod
    def empty(self):
        pass
