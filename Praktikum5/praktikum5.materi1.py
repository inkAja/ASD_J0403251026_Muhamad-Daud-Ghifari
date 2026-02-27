# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# 6.1 Konsep Dasar Rekursif
# ====================================================================
# Contoh Rekursif 1 : Faktorial
# ====================================================================
"""
Fungsi rekursif adalah fungsi yang memanggil dirinya sendiri untuk menyelesaikan
masalah yang lebih kecil hingga mencapai kondisi berhenti.
Setiap fungsi rekursif harus memiliki dua komponen utama:
1. Base Case
Kondisi berhenti agar fungsi tidak berjalan terus-menerus.
2. Recursive Case
Pemanggilan fungsi ke dirinya sendiri dengan ukuran masalah yang lebih kecil.
Tanpa base case, program akan mengalami infinite recursion.. 

illustrasi pemanggilan rekursif:
f(3) --> f(2) --> f(1) -> f(0)/base case
"""

def faktorial(n):
    # Base case : berhenti ketika n = 0
    if n == 0:
        return 1

    # Recursive case : masalah diperkecil menjadi faktorial(n-1)
    return n * faktorial(n - 1)


print(faktorial(5))
