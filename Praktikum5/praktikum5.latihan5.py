# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# 7.5 Studi Kasus Generator PIN
# ====================================================================
# Studi Kasus: Generator PIN
# ====================================================================


def buat_pin(panjang, hasil=""):
    # Base rekursif
    if len(hasil) == panjang:
        print("PIN :", hasil)
        return

    # Proses ulang 000
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)

buat_pin(3)

"""
Penjelasan

buat_pin(3) akan menjalankan for, pertama "0", akan menjalankan fungsi buat_pin(3, hasil="0")
----buat_pin(3, hasil="0")---
akan menjalankan for "0" juga, jadi buat_pin(3, hasil="00") 
----buat_pin(3, hasil="00")---
ini akan mengulang 3 for yaitu 1,2,3
sehingga akan menghasilkan buat_pin(3, hasil="000"), buat_pin(3, hasil="001"), dan buat_pin(3, hasil="002")
masing masing akan di print karena len(hasil) = 3. 
 
pengulangan lain juga sama. 
"""