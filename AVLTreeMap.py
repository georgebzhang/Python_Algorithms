from Map import Map


class AVLTreeMap(Map):
    # "private" class and functions
    class Node:
        def __init__(self, k, v):
            self.key = k
            self.value = v
            self.left = None
            self.right = None

    def find(self, k):
        pass

    def print_inorder(self, n):
        if n is not None:
            self.print_inorder(n.left)
            print('[k: ' + str(n.key) + ', v: ' + str(n.value) + ']')
            self.print_inorder(n.right)

    # "public" functions
    def __init__(self):
        self.root = None

    def insert(self, k, v):
        pass

    def remove(self, k):
        pass

    def put(self, k, v):
        pass

    def get(self, k):
        pass

    def has(self, k):
        pass

    def print(self):
        self.print_inorder(self.root)
        print()

