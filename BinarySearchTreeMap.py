from Map import Map
from ArrayQueue import ArrayQueue  # for level order traversal


class BinarySearchTreeMap(Map):
    # "private" helper class and functions
    class Node:
        def __init__(self, k, v):
            self.key = k
            self.value = v
            self.left = None
            self.right = None

    def find(self, k):
        n = self.root
        while n is not None:
            if k < n.key:
                n = n.left
            elif k > n.key:
                n = n.right
            else:
                return n
        return None

    def find_for_sure(self, k):  # returns Node with key k or raises exception if no Node is found
        n = self.find(k)
        if n is None:
            raise Exception('Key does not exist')
        return n

    def insert_rec(self, n, k, v):  # recursive helper function for insert(k, v)
        if n is None:
            return BinarySearchTreeMap.Node(k, v)
        if k < n.key:
            n.left = self.insert_rec(n.left, k, v)
        elif k > n.key:
            n.right = self.insert_rec(n.right, k, v)
        else:
            raise Exception('Map already has key')
        return n

    def max_Node(self, n):
        while n.right is not None:
            n = n.right
        return n

    def remove_max_Node(self, n):
        if n.right is None:
            return n.left
        n.right = self.remove_max_Node(n.right)
        return n

    def remove_Node(self, n):
        # 0 or 1 child
        if n.left is None:
            return n.right
        if n.right is None:
            return n.left
        # 2 children
        pred = self.max_Node(n.left)  # find predecessor of n
        n.left = self.remove_max_Node(n.left)
        n.key = pred.key
        n.value = pred.value
        return n

    def remove_rec(self, n, k):
        if n is None:
            raise Exception('Key does not exist')
        if k < n.key:
            n.left = self.remove_rec(n.left, k)
        elif k > n.key:
            n.right = self.remove_rec(n.right, k)
        else:
            n = self.remove_Node(n)
        return n

    def print_inorder(self, n):
        if n is not None:
            self.print_inorder(n.left)
            print('[k: ' + str(n.key) + ', v: ' + str(n.value) + ']')
            self.print_inorder(n.right)

    # "public" functions
    def __init__(self):
        self.root = None

    def insert(self, k, v):
        self.root = self.insert_rec(self.root, k, v)

    def remove(self, k):
        v = self.get(k)
        self.remove_rec(self.root, k)
        return v

    def put(self, k, v):
        n = self.find_for_sure(k)
        n.value = v

    def get(self, k):
        n = self.find_for_sure(k)
        return n.value

    def has(self, k):
        return self.find(k) is not None

    def print(self):
        self.print_inorder(self.root)
        print()

    def print_tree(self):
        q = ArrayQueue()
        q.enqueue(self.root)
        while not q.empty():
            n = q.dequeue()
            print('[k: ' + str(n.key) + ', v: ' + str(n.value) + ']')
            if n.left is not None:
                q.enqueue(n.left)
            if n.right is not None:
                q.enqueue(n.right)
