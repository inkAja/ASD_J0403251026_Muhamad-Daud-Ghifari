# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 9
# ====================================================================
# Pre-Order Traversal
# ====================================================================
# Dalam metode traversal ini, simpul akar dikunjungi terlebih dahulu, kemudian subtree kiri dan akhirnya
# subtree kanan.
# ====================================================================


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
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

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()

    # Preorder Traversal
    # Root -> left -> Right
    def preOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print(root.preOrderTraversal(root))
