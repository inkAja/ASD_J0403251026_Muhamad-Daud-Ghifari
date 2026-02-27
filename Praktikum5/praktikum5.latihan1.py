# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# 7.1 Latihan 1 Rekursi dasar | Memahami base case dan recursive case.
# ====================================================================
# Latihan 1 : Rekursi pangkat
# ====================================================================


def pangkat(a, n):
    # Base case
    if n == 0:
        return 1

    # Recursive case
    return a * pangkat(a, n - 1) # akan menjalankan pangkat(a,n-1) hingga n = 0 yang mereturn 1.


print(pangkat(2, 4)) # output 16

"""
Penjelasan

ketika pangkat(2,4)  dijalankan akan mereturn 2 * pangkat(2, 4-1) yaitu pangkat(2, 3) sehingga menjalankan 2 * pangkat(2, 3-1). 
begitu seterusnya hingga n=0 yang merupakan base case dan return 1.

ketika pangkat(n) 0 akan return 1, 
ketika pangkat(n) 1 akan return 2 * 1 = 2   #1 merupakan hasil return pangkat 0,
ketika pangkat(n) 2 akan return 2 * 2 = 4, 
ketika pangkat(n) 3 akan return 2 * 4 = 8
ketika pangkat(n) 4 akan return 2 * 8 = 16
"""
