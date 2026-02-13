"""
Soal 4 : Buat metode untuk menggabungkan dua single linked list menjadi satu linked list baru
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_multiple(self, multData):
        mult = multData.strip()
        mult = multData.split(",")
        if not (mult == [""]):
            for data in mult:
                self.insert_at_end(data)

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")

    def combine_lists(self, list2):
        if self.head:
            self.tail.next = list2.head
            if list2.tail:
                self.tail = list2.tail
        else:
            self.head = list2.head
            self.tail = list2.tail


ll1 = LinkedList()
val1 = input("Masukan Elemen Untuk Linked list pertama: ")
ll1.insert_multiple(val1)

ll2 = LinkedList()
val2 = input("Masukan Elemen Untuk Linked list kedua: ")
ll2.insert_multiple(val2)

print("Linked List  1: ", end=" ")
ll1.display()
print("Linked List  2: ", end=" ")
ll2.display()
ll1.combine_lists(ll2)
print("Linked List  gabungan: ", end=" ")
ll1.display()
