#======================================================================
# Praktikum 2   : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 1     : Membuat Fungsi Load Data dari File
#======================================================================

# Variabel menyimpan data file 
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} # inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() # ambil data per baris dan hilangkan new line
            nim,nama,nilai = baris.split(",") # ambil data per item
            data_dict[nim] = {
                "nama": nama,
                "nilai": int(nilai)
            } # masukan data kedalam variabel data_dict
    return data_dict

# buka_data = baca_data(nama_file) # memanggil fungsi load data dan menyimpannya ke variabel
# print("Jumlah data terbaca :", len(buka_data), "data") # Melihat berapa data yang diload

#======================================================================
# Praktikum 2   : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 2     : Membuat Fungsi Menampilkan Data
#======================================================================

def tampilkan_data(data_dict):
    # Membuat header tabel
    print("\n======== Daftar Mahasiswa ========")
    print(f"{'NIM':<10} | {'Nama':<12} | {'Nilai':>5}") #Mengatur ukuran kolom
    print('-'*32) # Membuat garis
    '''
    untuk tampilan yang rapi, atur lebar kolom 
    {'NIM' :<10} artinya NIM rata kiri dengan lebar kolom 10 karakter
    {'Nama' :<10} artinya Nama rata kiri dengan lebar kolom 12 karakter
    {'Nilai' :>5} artinya Nilai rata kanan dengan lebar kolom 5 karakter
    '''
    # Menampilkan isi data
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]['nama']
        nilai = data_dict[nim]['nilai']
        print(f"{nim:<10} | {nama:<12} | {int(nilai):>5}")
    print("\n")
# tampilkan_data(buka_data) # memanggil fungsi untuk menampilkan data 

#======================================================================
# Praktikum 2   : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 3     : Membuat Fungsi Mencari Data
#======================================================================

# Membuat fungsi pencarian data
def cari_data(data_dict):
    # pencarian data berdasarkan nim sebagai key dictionary
    # membuat input nim mahasiswa yang akan dicari
    nim_cari = input("Masukan NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]['nama']
        nilai = data_dict[nim_cari]['nilai']
        print("===== Data Mahasiswa Ditemukan =====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan, Pastikan NIM yang dimasukan benar")
    print("\n")
# Memanggil fungsi cari data
# cari_data(buka_data)

#======================================================================
# Praktikum 2   : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 4     : Membuat Fungsi Update Data
#======================================================================

# Membuat Fungsi update data
def ubah_data(data_dict):
    # awali dulu dengan mencari nim / data yang ingin diupdate
    nim = input("Masukan Nim mahasiswa yang ingin diubah datanya: ").strip()
    if nim not in data_dict:
        print("NIM tidak ditemukan. Update dibatalkan")
        return 
    
    try:
        nilai_baru = int(input("Masukan nilai baru 0-100: ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai Harus antara 0 sampai 100. Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. NIlai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")
    print("\n")

#memanggil fungsi ubah data
# ubah_data(buka_data)


#======================================================================
# Praktikum 2   : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 5     : Membuat Fungsi Menyimpan Data pada File
#======================================================================

# Membuat fungsi menyimpan data ke File
def simpan_data(nama_file,data_dict):
    with open(nama_file,"w",encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

# simpan_data(nama_file,buka_data)
# print("\nData Berhasil Disimpan ke File: ", nama_file)


#======================================================================
# Praktikum 2   : Konsep ADT dan File Handling (Studi Kasus)
# Latihan 6     : Membuat Menu Interaktif
#======================================================================

def main():
    # load data otomatis saat program dimulai
    buka_data = baca_data(nama_file)

    while True: 
        print("===MENU DATA MAHASISWA===")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data) # Memanggil fs 2 menampilkan data
        elif pilihan == "2":
            cari_data(buka_data) # Memanggil fs 3 mencari data
        elif pilihan == "3":
            ubah_data(buka_data) # Memanggil fs 4 mengubah data
        elif pilihan == "4":
            simpan_data(nama_file,buka_data) # Memanggil fs 5 menyimpan data ke file
            print("Data Berhasil Disimpan")
        elif pilihan == "0":
            print("Program Selesai.") # 
            break
        else:
            print("Pilihan tidak valid. Silahkan Coba Lagi")

if __name__ == "__main__":
    main()        