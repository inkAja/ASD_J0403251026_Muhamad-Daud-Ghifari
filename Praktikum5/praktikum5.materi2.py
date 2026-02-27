# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# 6.2 Tracing rekursi (Call stack)
# ====================================================================
# Contoh Rekursif 2 : Tracing Masuk/Keluar
# ====================================================================

"""
Untuk memahami rekursi, mahasiswa perlu melihat urutan 'Masuk' (stacking) dan
'Keluar' (unwinding). Saat fungsi memanggil dirinya sendiri, call stack bertambah.
Setelah base case tercapai, fungsi kembali satu per satu.
ilustrasi
Masuk(stacking)         Keluar(unwinding)
hitung(3)                 hitung(1)
hitung(2)                 hitung(2)
hitung(1)                 hitung(3)
"""

def hitung(n):
    # Base case
    if n == 0:
        print("Selesai")
        return
    print("Masuk :", n)  # Fase stacking
    hitung(n - 1)  # Pemanggilan rekursi
    print("Keluar :", n)  # fase unwinding --> akan dijalankan ketika pemanggilan rekursi selesai
    # jadi akan print masuk terlebih dahulu hingga n = 0, baru akan menjalankan keluar


hitung(3)
