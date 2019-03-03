from abc import ABC, abstractmethod


class Set(ABC):  # Set is a value-based (as opposed to position-based) data structure
    @abstractmethod
    def insert(self, t):
        pass

    @abstractmethod
    def remove(self, t):
        pass

    @abstractmethod
    def has(self, t):
        pass
