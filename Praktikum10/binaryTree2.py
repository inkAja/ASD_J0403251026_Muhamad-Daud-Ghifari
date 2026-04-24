# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 9
# ====================================================================
# Memasukan data ke python/node
# ====================================================================


class Node:
    def __init__(self, data):
        self.left = None # < parent
        self.right = None # > parent
        self.data = data

    # Memasukan data ke python
    def insert(self, data):
        # Membandingkan data dengan parent
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    # Print data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


root = Node(10) # Object root

root.insert(11)
root.insert(2)
root.insert(5)
root.insert(43)
root.insert(9)
root.insert(12)
root.PrintTree()