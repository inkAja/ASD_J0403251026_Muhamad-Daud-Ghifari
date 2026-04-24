# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 9
# ====================================================================
# Tugas
# ====================================================================
# 1. Membuat struktur data Binary Search Tree.
# 2. Menambahkan data ke dalam tree menggunakan fungsi insert().
# 3. Menampilkan hasil traversal:
# - In-order
# - Pre-order
# - Post-order
# 4. Menampilkan hasil akhir dalam bentuk list.
# 5. Memberikan penjelasan singkat dari output yang dihasilkan.
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

    def inorderTraversal(self,root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
    
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res
    
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res
    
root = Node(26)

root.insert(6)  # - 20
root.insert(46) # + 20
root.insert(46) # - 30 + 50 = + 20
root.insert(16) # - 10
root.insert(36) # + 10
root.insert(56) # + 30
root.insert(11) # - 15

print("Nama     : Muhamad Daud Ghifari")
print("NIM      : J0403251026")
print("=======================================================")
print(f"In-order Reversal   : {root.inorderTraversal(root)}")
print(f"Pre-order Reversal  : {root.preorderTraversal(root)}")
print(f"Post-order Reversal : {root.postorderTraversal(root)}")