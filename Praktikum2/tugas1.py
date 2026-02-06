#======================================================================
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin(Berbasis File .txt)
#
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
#======================================================================

# --------------------------------
# Konstanta Nama File
# --------------------------------
nama_file = "Pertemuan2/stock_barang.txt"


# --------------------------------
# Fungsi : Membaca data dari file 
# --------------------------------
def baca_stock(nama_file):
    """
    Membaca data stock dari file text.
    Format per baris: KodeBarang,NamaBarang,Stok

    Output :
    - stok_dict(dictionary)
    key = kode_barang
    value = {"nama" : nama, "stok" : stok_int}
    """

    stok_dict = {} # inisialisasi stok dictioary
    with open(nama_file, "r",encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() # menghilangkan \n pada file txt
            kode,nama,stok = baris.split(",") # memisahkan data berdasarkan , dan memasukannya ke variabel
            stok_dict[kode] = {"nama": nama, "stok": int(stok)} # menyimpan data ke dictionary
        return stok_dict
    
# --------------------------------
# Fungsi : Menyimpan data ke file
# --------------------------------
def simpan_data(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file text 
    Format per baris : KodeBarang,NamaBarang,Stok 
    """
    with open(nama_file,"w",encoding="utf-8") as file :
        for kode in sorted(stok_dict.keys()):
            nama = stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

# --------------------------------
# Fungsi : Menampilkan semua data
# --------------------------------

def tampilkan_semua(stok_dict):
    """
    Menampilkan semua data di stok_dict.
    """
    # Jika kosong, tampilkan pesan stok kosong 
    # Tampilkan dengan format rapi : Kode | Nama | Stok

    # Membuat Header Tabel
    print("===== Daftar Stok Barang Kantin =====")
    print(f"{'Kode':<10} | {'Nama':<15} | {'Stok':>4}") # Mengatur ukuran kolom
    print("-"*32) # Membuat garis
    
    # Menampilkan isi
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]['nama'] 
        stok = stok_dict[kode]['stok']
        print(f"{kode:<10} | {nama:<15} | {stok:<4}")
    print('') # Membuat Baris Baru 

# --------------------------------
# Fungsi : Mencari data berdasarkan Kode Barang
# --------------------------------
def cari_barang(stok_dict):
    """
    Mencari barang berdasarkan kode barang
    """
    # Jika tidak ada akan menampilkan pesan barang tidak ditemukan
    # Jika ada akan menampilkan detail barang 
    # Cek apakah kode ada dalam dictionary
    kode = input("Masukan Kode Barang: ").strip()

    if kode in stok_dict:
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        print(f"Kode Barang")