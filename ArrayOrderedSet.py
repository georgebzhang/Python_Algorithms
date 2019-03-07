from OrderedSet import OrderedSet


class ArrayOrderedSet(OrderedSet):
    # helper functions
    def grow(self):
        print('Growing array')
        self.capacity *= 2
        data_new = [0] * self.capacity
        for i in range(self.length):
            data_new[i] = self.data[i]
        self.data = data_new

    def empty(self):
        return self.length == 0

    def find(self, t):
        if self.empty():
            return 0
        ind_left = 0
        ind_right = self.length - 1
        while ind_left <= ind_right:
            ind_mid = (ind_left + ind_right) // 2
            val_mid = self.data[ind_mid]
            if t < val_mid:
                ind_right = ind_mid - 1
            elif t > val_mid:
                ind_left = ind_mid + 1
            else:
                return ind_mid
        return ind_left

    # "public" functions
    def __init__(self):
        self.capacity = 2
        self.data = [0] * self.capacity
        self.length = 0

    def insert(self, t):
        if self.has(t):
            return
        if self.length == self.capacity:
            self.grow()
        ind_t = self.find(t)
        for i in range(self.length - 1, ind_t - 1, -1):  # must iterate backwards or else data is lost
            self.data[i + 1] = self.data[i]
        self.data[ind_t] = t
        self.length += 1

    def remove(self, t):
        if not self.has(t):
            return
        ind_t = self.find(t)
        for i in range(ind_t, self.length):
            self.data[i] = self.data[i + 1]
        self.length -= 1

    def has(self, t):
        return t == self.data[self.find(t)]

    def print(self):
        for i in range(self.length):
            print(self.data[i], " ", end="")
        print()
