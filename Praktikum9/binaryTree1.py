# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 9
# ====================================================================
# Mempelajari Binary Tree
# ====================================================================

# Membuat root
class Node:
    def __init__(self, data):
        self.left = None # < parent
        self.right = None # > parent
        self.data = data
    # Print data
    def PrintTree(self):
        print(self.data)


root = Node(10)

root.PrintTree()
