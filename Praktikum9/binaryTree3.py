# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 9
# ====================================================================
# In-Order Traversal
# ====================================================================
# Dalam metode traversal ini, subtree kiri dikunjungi terlebih dahulu, kemudian root dan kemudian subtree kanan. Kita harus
# selalu ingat bahwa setiap node dapat mewakili subtree itu sendiri.
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
    # In-Order Traversal
    # Left -> Root -> Right
    def inorderTraversal(self,root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
    

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print(root.inorderTraversal(root))