from PriorityQueue import PriorityQueue


class BinaryHeapPriorityQueue(PriorityQueue):
    # "private" helper functions
    def swap(self, ind_1, ind_2):
        self.data[ind_1], self.data[ind_2] = self.data[ind_2], self.data[ind_1]

    def percolate_up(self):
        i = len(self)
        while i // 2 > 0:
            if self.data[i] < self.data[i // 2]:  # < for min heap, > for max heap
                self.swap(i, i // 2)
            else:
                return  # no need to keep percolating up, since higher priority items already satisfy heap order property
            i = i // 2

    def prior_child(self, i):  # returns index of higher priority child of parent with index i
        ind_left_child = 2 * i
        ind_right_child = ind_left_child + 1
        if ind_right_child > len(self):
            return ind_left_child
        if self.data[ind_left_child] < self.data[ind_right_child]:
            return ind_left_child
        # else
        return ind_right_child

    def percolate_down(self, i):
        while 2 * i <= len(self):
            ind_prior_child = self.prior_child(i)
            if self.data[i] > self.data[ind_prior_child]:
                self.swap(i, ind_prior_child)
            else:
                return  # no need to keep percolating down, since lower priority items already satisfy heap order property
            i = ind_prior_child

    # "public" functions
    def __init__(self):
        self.data = [0]  # ignore index 0 and start at index 1 for simpler parent-child math

    def __len__(self):
        return len(self.data) - 1  # no need to keep track of length ourselves with list append below

    def insert(self, t):
        self.data.append(t)  # no need to implement amortized doubling ourselves with list append
        self.percolate_up()

    def remove(self):
        return_t = self.data[1]
        self.data[1] = self.data[len(self)]  # replace highest priority item with lowest priority item
        self.data.pop()  # remove lowest priority item and reduce length by 1
        self.percolate_down(1)
        return return_t

    def top(self):
        return self.data[0]

    def empty(self):
        return len(self) == 0

    def print(self):
        for i in range(1, len(self) + 1):
            print(self.data[i], " ", end="")
        print()
