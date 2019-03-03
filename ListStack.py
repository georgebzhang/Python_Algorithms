from Stack import Stack


class ListStack(Stack):
    class Node:  # unnecessary
        def __init__(self):
            self.data = None
            self.next = None

    def __init__(self):
        self.head = None

    def push(self, t):
        n = ListStack.Node()
        n.data = t
        n.next = self.head
        self.head = n

    def pop(self):
        if self.empty():
            raise Exception('Stack is empty')
        else:
            self.head = self.head.next

    def top(self):
        if self.empty():
            raise Exception('Stack is empty')
        else:
            return self.head.data

    def empty(self):
        return self.head is None
