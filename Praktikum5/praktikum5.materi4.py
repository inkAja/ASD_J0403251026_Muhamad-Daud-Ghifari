# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# 6.4 Konsep dasar Backtracking
# ====================================================================
# Contoh Backtracking 1 : Kombinasi biner
# ====================================================================

"""
Backtracking adalah teknik pencarian solusi dengan mencoba berbagai kemungkinan.
Jika suatu pilihan membuat solusi tidak mungkin, program 'mundur' (backtrack) dan
mencoba pilihan lain. Pola umum: Choose ➔ Explore ➔ Unchoose.
"""

def biner(n, hasil=""):
    # Base case : jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    # Choose + explore : tambah '0'
    biner(n, hasil + "0")
    # Choose + explore : tambah '1'
    biner(n, hasil + "1")

biner(3)
