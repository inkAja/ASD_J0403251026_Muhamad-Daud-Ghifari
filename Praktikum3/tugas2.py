"""
Soal 2 : Buat kode Implementasikan Pencarian pada node tertentu Single Circular Linked List.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class singleCircular:
    def __init__(self):
        self.head = None
        self.tail = None

    def c(self):
        print(self)

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def insert_multiple(self, multData):
        mult = multData.strip()
        mult = multData.split(",")
        if not(mult == ['']):
            for data in mult:
                self.insert_at_end(data)

    def search(self, key):
        temp = self.head
        if self.head is None:
            print("Circular Linked List Kosong. Tidak ada elemen yang bisa dicari")
            return
        while temp:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List")
                return True
            temp = temp.next
            if temp.next == self.head and temp.data != key:
                break
        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List")
        return


cll = singleCircular()
el = input("Masukan Elemen kedalam Circular Linked List: ")
cll.insert_multiple(el)

src = input("Masukan Elemen Yang Dicari: ")
cll.search(src)
