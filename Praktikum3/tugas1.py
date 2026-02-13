"""
Soal 1 : Implementasikan fungsi	untuk menghapus	node dengan	nilai tertentu
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # Jika linked list kosong
            self.head = new_node
            self.tail = new_node  # Tail juga menunjuk ke node pertama
        else:
            self.tail.next = new_node  # Sambungkan tail ke node baru
            new_node.prev = self.tail
            self.tail = new_node  # Update tail ke node baru

    def display_forward(self):
        print("\nTraversing Forward: ")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")

    def delete_node(self, key):
        temp = self.head
        prev = None
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return
        prev.next = temp.next
        temp = None


dll = DoubleLinkedList()
dll.insert_at_end(3)
dll.insert_at_end(5)
dll.insert_at_end(13)
dll.insert_at_end(2)
dll.display_forward()

p = int(input("Masukan Elemen Yang Ingin dihapus: "))
print("\nSetelah dihapus: ")
dll.delete_node(p)
dll.display_forward()
