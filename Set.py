from abc import ABC, abstractmethod


class Set(ABC):  # Set is a value-based (as opposed to position-based) data structure
    @abstractmethod
    def insert(self, param1):
        pass

    @abstractmethod
    def remove(self, param1):
        pass

    @abstractmethod
    def has(self, param1):
        pass
