from Set import Set


class ArraySet(Set):
    def __init__(self):
        self.capacity = 100  # TODO: implement amortized doubling
        self.data = [0] * self.capacity
        self.length = 0

    def insert(self, t):
        if self.has(t):
            return
        self.data[self.length] = t
        self.length += 1

    def find(self, t):  # helper function for remove(...)
        for i in range(self.length):
            if t == self.data[i]:
                return i
        return -1

    def remove(self, t):
        ind_t = self.find(t)
        if ind_t == -1:
            return
        for i in range(ind_t, self.length):
            self.data[i] = self.data[i + 1]
        self.length -= 1

    def has(self, t):
        return self.find(t) != -1

    def print(self):
        for i in range(self.length):
            print(self.data[i], " ", end="")
        print()
