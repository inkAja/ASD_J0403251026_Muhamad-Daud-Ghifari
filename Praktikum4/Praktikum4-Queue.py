# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Implementasi dasar : Queue
# ======================


class Node:
    # konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self, data):
        self.data = data  # Menyimpan nilai atau data pada list
        self.next = None  # Pointer ini menunjuk ke note berikutnya (awal = none)


class queue:
    # buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None  # Node paling depan
        self.rear = None  # Node paling belakang

    def is_empty(self):
        return self.front is None

    # Membuat fungsi untuk menambah data baru di bagian paling belakang (rear)
    def enqueue(self, data):
        nodeBaru = Node(data)

        # JIka queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        # jika queue tidak kosong, maka letakan data baru ke rear
        self.rear.next = nodeBaru  # Letakan data bari setelahnya rear
        self.rear = nodeBaru  # Jadikan data baru sebagai rear

    def dequeue(self):
        if self.is_empty():
            print("queue kosong. tidak bisa dequeue")
            self.rear = None
            return None
        # menghapus data dari depan/front
        data_terhapus = self.front.data
        # geser front ke node berikutnya
        self.front = self.front.next

        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print(" Rear")


# Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
