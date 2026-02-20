#====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026 
# Kelas : TPL A2 
#====================================================================

#====================================================================
# Implementasi dasar : Node pada Linked List
#====================================================================
class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data # Menyimpan nilai atau data pada list
        self.next = None # Pointer ini menunjuk ke note berikutnya (awal = none)

# 1. Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2. Mendefinisikan head dan Menghubungkan Node : A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC
# 4. Traversal : Menelusuri Node dari head sampai ke None
current = head
while current is not None:
    print(current.data) # Menampikan data pada node saat ini
    current = current.next # Pindah ke Node berikutnya

