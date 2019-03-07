from OrderedSet import OrderedSet


class ListOrderedSet(OrderedSet):
    # "private" helper class and functions
    class Node:
        def __init__(self):
            self.data = None
            self.prev = None
            self.next = None

    def empty(self):
        return self.head is None

    def find(self, t):
        ptr = self.head
        while ptr is not None:
            if t <= ptr.data or ptr.next is None:
                return ptr
            ptr = ptr.next
        return

    def insert_Node_middle(self, n, ptr_t):  # inserts Node* n before Node* ptr_t, which must have prev and next not nullptr
        n.next = ptr_t
        n.prev = ptr_t.prev
        ptr_t.prev.next = n
        ptr_t.prev = n

    # "public" functions
    def __init__(self):
        self.head = None

    def insert(self, t):
        if self.has(t):
            return
        n = ListOrderedSet.Node()
        n.data = t
        if self.empty():
            self.head = n
            return
        ptr_t = self.find(t)
        prev_null = ptr_t.prev is None
        next_null = ptr_t.next is None
        if not prev_null and not next_null:  # if Node with t is between head and tail (which we don't have a variable for)
            self.insert_Node_middle(n, ptr_t)
        elif not prev_null:  # if Node with t is at tail (which we don't have a variable for)
            if t < ptr_t.data:
                self.insert_Node_middle(n, ptr_t)
            else:
                n.prev = ptr_t
                ptr_t.next = n
        elif not next_null:  # if Node with t is at head
            if t < ptr_t.data:
                n.next = ptr_t
                self.head.prev = n
                self.head = n
            else:
                self.insert_Node_middle(n, ptr_t)
        else:  # if Node with t is the only Node in Set
            if t < ptr_t.data:
                n.next = self.head
                self.head = n
            else:
                n.prev = self.head
                self.head.next = n

    def remove(self, t):
        if not self.has(t):
            return
        ptr_t = self.find(t)
        prev_null = ptr_t.prev is None
        next_null = ptr_t.next is None
        if not prev_null and not next_null:  # if Node with t is between head and tail (which we don't have a variable for)
            ptr_t.prev.next = ptr_t.next
            ptr_t.next.prev = ptr_t.prev
        elif not prev_null:  # if Node with t is at tail (which we don't have a variable for)
            ptr_t.prev.next = None
        elif not next_null:  # if Node with t is at head
            self.head = ptr_t.next
            ptr_t.next.prev = None
        else:  # if Node with t is the only Node in Set
            self.head = None

    def has(self, t):
        if self.empty():
            return False
        return t == self.find(t).data

    def print(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data, " ", end="")
            ptr = ptr.next
        print()
