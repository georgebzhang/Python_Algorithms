from abc import ABC, abstractmethod


class PriorityQueue(ABC):
    @abstractmethod
    def insert(self, t):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def top(self):
        pass

    @abstractmethod
    def empty(self):
        pass
