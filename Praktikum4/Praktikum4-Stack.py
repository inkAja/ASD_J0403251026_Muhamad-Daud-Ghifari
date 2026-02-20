# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================


# ====================================================================
# Implementasi dasar : Stack
# ====================================================================
class Node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data # Menyimpan nilai atau data pada list
        self.next = None # Pointer ini menunjuk ke note berikutnya (awal = none)


# Stack ada operasi push(Memasukan head baru) dan pop (Menghapus head)
class stack:
    def __init__(self):
        self.top = None  # top menunjuk ke node paling atas(awalnya kosong)

    def push(self, data):  # Memasukan data baru
        # 1. Membuat Node baru
        nodeBaru = Node(data)  # instantiasi/memanggil konstruktor pada clsas Node
        # 2. Node baru harus menunjuk ke top yang lama(head lama)
        nodeBaru.next = self.top
        # 3. geser top pindah ke node baru
        self.top = nodeBaru

    def is_empty(self):
        return self.top is None  # stack kosong jika top = None

    def pop(self):  # mengambil / menghapus node paling atas(top)
        if self.is_empty():
            print("Data Kosong. Tidak bisa pop")
            return None
        data_terhapus = self.top.data  # soroti bagian top dan simpan di variabel
        self.top = self.top.next  # geser top ke node berikutnya
        return data_terhapus 
    
    def peek(self):
        # melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data

    def tampilkan(self):
        current = self.top
        print("Top ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek(Lihat Top) :", s.peek())
s.pop()
s.tampilkan()
print("Peek(Lihat Top) :", s.peek())