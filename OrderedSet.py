from abc import ABC, abstractmethod


class OrderedSet(ABC):
    @abstractmethod
    def insert(self, t):
        pass

    @abstractmethod
    def remove(self, t):
        pass

    @abstractmethod
    def has(self, t):
        pass
