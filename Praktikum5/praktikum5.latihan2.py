# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# 7.2 Latihan 2 Tracing rekursi | Memahami alur masuk dan keluar fungsi.
# ====================================================================
# Latihan 2 : tracing rekursi
# ====================================================================


def countdown(n):
    # base case -> menghentikan rekursi jika n = 0
    if n == 0:
        print("Selesai")
        return 

    print("Masuk :", n)  # Fase stacking

    countdown(n - 1)  # pemanggilan rekursi

    print("Keluar :", n)  # Fase Unwinding


countdown(3)

"""
Penjelasan

-----Fase Stacking-----
program akan menjalankan countdown(3) akan memprint Masuk : 3, lalu akan menjalankan countdown(3-1) yaitu countdown(2). 
fungsi countdown(2)  akan memprint Masuk : 2, dan akan menjalankan countdown(1). --> countdown(2-1) 
countdown(1) juga akan print Masuk : 1, dan akan menjalankan countdown(0). --> countdown(1-1)

-----Base case-----
nah di countdown(0) ini akan masuk ke base case yang akan print(selesai) dan akan menghentikan pengulangan. 

-----Fase unwinding-----
Setelah base case tercapai, fungsi countdown(n-1) akan kembali/selesai lalu akan menjalankan Print(Keluar : n) 
"""
