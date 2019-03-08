from abc import ABC, abstractmethod


class OrderedMap(ABC):
    @abstractmethod
    # inserts unique key k with value v
    def insert(self, k, v):
        pass

    @abstractmethod
    def remove(self, k):
        pass

    @abstractmethod
    # updates value v of existing key k
    def put(self, k, v):
        pass

    @abstractmethod
    def get(self, k):
        pass

    @abstractmethod
    def has(self, k):
        pass
