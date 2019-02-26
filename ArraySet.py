from Set import Set


class ArraySet(Set):
    def __init__(self):
        self.capacity = 100  # will implement amortized doubling later
        self.data = [0] * self.capacity
        self.length = 0

    def insert(self, param1):
        if self.has(param1):
            return
        self.data[self.length] = param1
        self.length += 1

    def find(self, param1):  # helper function for remove(...)
        for i in range(self.length):
            if param1 == self.data[i]:
                return i
        return -1

    def remove(self, param1):
        ind_t = self.find(param1)
        if ind_t == -1:
            return
        for i in range(ind_t, self.length):
            self.data[i] = self.data[i + 1]
        self.length -= 1

    def has(self, param1):
        return self.find(param1) != -1

    def print(self):
        for i in range(self.length):
            print(self.data[i], " ", end="")
        print()
