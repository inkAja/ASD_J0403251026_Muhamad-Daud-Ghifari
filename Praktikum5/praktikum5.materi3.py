# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# 6.3 Rekursi pada data list
# ====================================================================
# Contoh Rekursi 3 : Menjumlahkan elemen list
# ====================================================================

"""
Rekursi dapat digunakan untuk memproses data list secara bertahap, misalnya
menjumlahkan elemen list dengan menggeser indeks (index) dari 0 hingga akhir list.
Contoh 3: Menjumlahkan elemen list secara rekursif
"""

def jumlah_list(data, index = 0):
    # Base case : Jika index sudah mencapai panjang list
    if index == len(data):
        return 0
    
    # Recursive case: elemen sekarang + jumlah elemen setelahnya
    return data[index] + jumlah_list(data, index + 1)

print(jumlah_list([2,4,6,8])) # Output 20