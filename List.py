from abc import ABC, abstractmethod


class List(ABC):
    @abstractmethod
    def insert_front(self, t):
        pass

    @abstractmethod
    def insert_back(self, t):
        pass

    @abstractmethod
    def remove_front(self):
        pass

    @abstractmethod
    def remove_back(self):
        pass

    @abstractmethod
    def insert(self, index, t):
        pass

    @abstractmethod
    def remove(self, index):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def empty(self):
        pass
