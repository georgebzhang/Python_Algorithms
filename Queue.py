from abc import ABC, abstractmethod


class Queue(ABC):
    @abstractmethod
    def enqueue(self, param1):
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
