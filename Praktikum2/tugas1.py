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
nama_file = "Praktikum2/stock_barang.txt" # menggunakan Praktikum2 karena membuka filenya dari folder algoritma-strukturdata jika tidak akan error


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
            file.write(f"{kode},{nama},{stok}\n") # Mengirim data baru ke file

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
    print("-"*37) # Membuat garis
    
    # Menampilkan isi
    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]['nama'] 
        stok = stok_dict[kode]['stok']
        print(f"{kode:<10} | {nama:<15} | {stok:<4}") # menampilkan data 

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

    if kode in stok_dict: # Cek apakah kode yang diinput ada di dictionary
        nama = stok_dict[kode]["nama"]
        stok = stok_dict[kode]["stok"]
        # Menampilkan data jika ditemukan
        print("===Data Barang Ditemukan===")
        print(f"Kode Barang     : {kode}")
        print(f"Nama Barang     : {nama}")
        print(f"Stok Barang     : {stok}")
    else: 
        print("Barang Tidak ditemukan. Cek apakah kode yang dimasukan benar")

# --------------------------------
# Fungsi : Tambah Barang Baru
# -------------------------------- 
def tambah_barang(stok_dict):
    """
    Menambah Barang Baru ke stok_dict
    """
    kode = input("Masukan Kode Barang Baru : ").strip()

    if kode in stok_dict:
        print("Tambah barang gagal. Kode tersebut sudah digunakan. ")
        return
    nama = input("Masukan Nama Barang : ").strip()
    nama = nama.replace(" ", "") # Menghilangkan Spasi ditengah 
    # Memastikan input bertipe integer
    try : 
        stok_pertama = int(input("Masukan Stok Barang : "))
    except ValueError:
        print("Tambah barang gagal. Mohon memasukan angka")
        return
    stok_dict[kode] = {"nama":nama,"stok":stok_pertama} # memasukan data baru ke dictionary

    # Menampilkan detail data barang yang berhasil ditambah 
    print("===Berhasil Menambahkan Barang===")
    print(f"Kode Barang : {kode}")
    print(f"Nama Barang : {nama}")
    print(f"Stok Barang : {stok_pertama}")
# --------------------------------
# Fungsi : Update Stok Barang
# --------------------------------  

def update_stok(stok_dict):
    """
    Mengubah Stok barang(menambah atau mengurangi)
    Stok barang tidak boleh negatif
    """
    kode = input("Masukan kode barang yang ingin diupdate: ").strip()

    if kode not in stok_dict:
        print("Kode Barang tidak ditemukan.")
        return
    stok_lama = stok_dict[kode]["stok"] # menyimpan stok lama
    print("Pilih jenis update:")
    print("1. Tambah Stok")
    print("2. Kurangi Stok")

    # memastikan agar user memasukan angka
    try:
        pilihan = int(input("Masukan pilihan(1/2): ").strip())
    except ValueError:
        print("Update data gagal. Mohon untuk memasukan angka. ")
        return
    # memastikan user memilih angka 1/2 saja
    if not(1<=pilihan<=2):
        print("Update gagal. Masukan hanya angka 1 atau 2 saja")
        return 
    jumlah = int(input("Masukan Jumlah: ").strip())
    # menggunakan ternary operator untuk memilih apakah akan ditambah atau dikurangi
    stok_baru = stok_lama + jumlah if pilihan == 1 else stok_lama - jumlah 
    if stok_baru <0:
        print("Update gagal. Anda mengurangi stok hingga kurang dari 0")
        return
    stok_dict[kode]["stok"] = stok_baru # mengubah jumlah stok menjadi yang baru
    print(f"Berhasil {'menambah' if pilihan ==1 else 'mengurangi'} stok dari {stok_lama} menjadi {stok_baru}") #menampilkan bahwa stok berhasil diupdate

def main():
    # Membaca data dari file saat program dimulai
    stok_barang = baca_stock(nama_file)

    while True:
        print("\n===== MENU STOK KANTIN =====")
        print("1. Tampilkan Data Semua Barang.")
        print("2. Cari Barang Berdasarkan Kode.")
        print("3. Tambah Barang Baru.")
        print("4. Update Stok Barang.")
        print("5. Simpan Ke File.")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == '1':
            tampilkan_semua(stok_barang)
        elif pilihan == '2':
            cari_barang(stok_barang)
        elif pilihan == '3':
            tambah_barang(stok_barang)
        elif pilihan == '4':
            update_stok(stok_barang)
        elif pilihan == '5':
            simpan_data(nama_file, stok_barang)
            print("Data Berhasil Disimpan")
        elif pilihan == '0':
            print("Program selesai....")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan Program Utama
if __name__ == "__main__":
    main()
