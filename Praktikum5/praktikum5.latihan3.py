# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Latihan 3 Rekursi pada List |Mengolah struktur data menggunakan rekursi.
# ====================================================================
# Latihan 3: Mencari Nilai Maksimum
# ====================================================================


def cari_maks(data, index=0):
    # Base case --> harus index = lenght data - 1. karena index dimulai dari 0 sedangkan len(data) itu menghitung jumlah data. yang pasti akan lebih 1 dari index
    if index == len(data) - 1:
        return data[index]

    # Recursive case : mengambil data dari index + 1
    maks_sisa = cari_maks(data, index + 1)

    # Setelah mengambil maks_sisa akan membandingkan dengan data saat ini. jika lebih besar akan return data,
    # jika lebih kecil akan return maks sisa
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa


angka = [3, 7, 2, 9, 5]
print("Nilai Maksimum :", cari_maks(angka))

"""
Penjelasan

cari_maks([3,7,2,9,5]) akan dijalankan akan merekursif dalam variabel maks_sisa--> cari_maks(data, index+1) 
------dalam variabel Cari maks------
cari_maks akan terus mengulang hingga kondisi base rekursif tercapai(index = len(data)-1) yang akan mereturn 5.
akan kembali ke angka 9/index ke-3, variabel maks_sisanya adalah 5(base rekursif), dan akan menjalankan perbandingan di baris 24 (if data[index] > maks_sisa)
karena 9 > 5 maka akan return 9.
lanjut ke angka 2/index ke-2, variabel maks_sisa = 9 (return dari 9 > 5). dan akan membandingkannya lagi data[index] yaitu 2 
dengan maks_sisa yaitu 9. begitu seterusnya hingga kembali ke index 0.
"""
