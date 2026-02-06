#===================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca seluruh isi file data
#===================================================

print("====Membuka file dalam satu string====")
with open("data_mahasiswa.txt", "r",encoding="utf-8")  as file:
    isi_file = file.read()
print(isi_file)    
print("tipe data: ", type(isi_file))
print("====Membuka file per baris====")
jumlah_baris =0 #inisialisasi variabel untuk menghitung jumlah baris
with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris +1
        baris = baris.strip() #menghilangkan karakter baris baru
        print("Baris ke-", jumlah_baris)
        print("isinya : ", baris)

#===================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : Parsing Data
#===================================================
#Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom2 data

with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim,nama,nilai = baris.split(',') # Memecah data menjadi satuan dan simpan ke variabel
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai) # menampilkan satuan data dalam bentuk kolom

#================================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca data dan Menyimpannya ke Struktur Data List
#================================================================================

data_list = [] # inisialisasi variable

with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim,nama,nilai = baris.split(',') # Memecah data menjadi satuan dan simpan ke variabel
        data_list.append([nim,nama,int(nilai)]) #Menyimpan data ke List
print("==Menampilkan List==")
print(data_list)
print("Contoh record ke 1 :",data_list[0])
print("Contoh record ke 2 :",data_list[1])
print("Jumlah record :", len(data_list) )
#================================================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca data dan Menyimpannya ke Struktur Data Dictionary
#================================================================================
data_dict = {} # inisialisasi variabel dictionary

with open("data_mahasiswa.txt", "r",encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter baris baru
        nim,nama,nilai = baris.split(',') # Memecah data menjadi satuan dan simpan ke variabel
        # Simpan data ke dictionary
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : nilai
        }
print("==Menampilkan Data Dictionary==")
print(data_dict)