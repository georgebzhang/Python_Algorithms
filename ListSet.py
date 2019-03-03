from Set import Set


class ListSet(Set):
    class Node:
        def __init__(self):
            self.data = None
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None

    def insert(self, t):
        if self.has(t):
            return
        n = ListSet.Node()
        n.data = t
        n.next = self.head
        if not self.empty():
            self.head.prev = n
        self.head = n

    def find(self, t):  # helper function for remove()
        ptr = self.head
        while ptr is not None:
            if ptr.data == t:
                return ptr
            ptr = ptr.next
        return None

    def remove(self, t):
        ptr_t = self.find(t)
        if ptr_t is None:
            return
        prev_null = ptr_t.prev is None
        next_null = ptr_t.next is None
        if not prev_null and not next_null:  # if Node with t is between head and tail (which doesn't exist)
            ptr_t.prev.next = ptr_t.next
            ptr_t.next.prev = ptr_t.prev
        elif not prev_null:  # if Node with t is at tail (which doesn't exist)
            ptr_t.prev.next = None
        elif not next_null:  # if Node with t is at head
            self.head = ptr_t.next  # Node at head being removed
            ptr_t.next.prev = None
        else:  # if Node with t is the only Node in Set
            self.head = None

    def has(self, t):
        ptr = self.head
        while ptr is not None:
            if ptr.data == t:
                return True
            ptr = ptr.next
        return False

    def print(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data, " ", end="")
            ptr = ptr.next
        print()