from Stack import Stack


class ArrayStack(Stack):
    MAX_CAPACITY = 100

    def __init__(self):
        self.data = [0] * ArrayStack.MAX_CAPACITY
        self.length = 0

    def push(self, param1):
        self.data[self.length] = param1
        self.length += 1

    def pop(self):
        if self.empty():
            print("Stack is empty")
        else:
            self.length -= 1;

    def top(self):
        if self.empty():
            print("Stack is empty")
        else:
            return self.data[self.length - 1]

    def empty(self):
        return self.length == 0
