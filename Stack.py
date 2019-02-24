from abc import ABC, abstractmethod


class Stack(ABC):
    @abstractmethod
    def push(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def top(self):
        pass

    @abstractmethod
    def empty(self):
        pass
