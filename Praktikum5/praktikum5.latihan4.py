# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# 7.4 Latihan 4 Backtracking Dasar | Memahami pola choose dan explore.
# ====================================================================
# Latihan 4: Kombinasi Huruf
# ====================================================================


def kombinasi(n, hasil=""):
    # Base rekursif -> ketika len(hasil) = n
    if len(hasil) == n:
        print(hasil)
        return

    # Choose + explore a
    kombinasi(n, hasil + "A")
    # Choose + explore b
    kombinasi(n, hasil + "B")


kombinasi(2)

"""
Penjelasan

kombinasi(2) dijalankan akan ada 2 kombinasi yang dijalankan yaitu kombinasi(n, hasil + "A") dan kombinasi(n, hasil + "B")
    1. kombinasi(n, hasil + "A")
        ketika ini dijalankan akan menjalankan kombinasi(2, hasil="A"), 
        ini akan menjalankan 2 kombinasi juga yaitu kombinasi(n, hasil + "A") dan kombinasi(n, hasil + "B")

    1.1. kombinasi(n, hasil ="A") + kombinasi(n, hasil + "A") 
        ini akan menghasilkan kombinasi(2, hasil="AA")
        nah karena len dari hasil = 2, maka akan mencapai base rekursif akan print hasilnya yaitu "AA", lalu berhenti
    1.2 kombinasi(n, hasil = "A") + kombinasi(n, hasil + "B") 
        ini akan menghasilkan kombinasi(2, hasil="AB")
        sama seperti 1.1 ini akan mencapai base rekursif akan print hasilnya yaitu "AB", lalu berhenti

yang bagian B juga sama.
"""