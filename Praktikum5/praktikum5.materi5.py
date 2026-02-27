# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# 6.5 Backtracking dengan Pruning (Pemangkasan)
# ====================================================================
# Contoh Backtracking 2 : Kombinasi biner dengan batas '1' (prunning)
# ====================================================================

"""
Pruning adalah strategi untuk menghentikan eksplorasi cabang yang pasti tidak
memenuhi syarat, sehingga pencarian menjadi lebih efisien
"""


def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Prunning : jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas:
        return

    # Base case
    if len(hasil) == n:
        print(hasil)
        return

    # Pilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # Pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)


biner_batas(4,2)
