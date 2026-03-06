# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 6
# ====================================================================
# Latihan 1 : Bubble sort descending
# ====================================================================


def bubbleSort(data):
    for passum in range(len(data) - 1, 0, -1):
        for i in range(passum):
            if (
                data[i] < data[i + 1]
            ):  # Ini yang diubah agar menjadi descending, membalikan jika data lebih kecil maka mengubah indeksnya menjadi i + 1
                # Tukar dua data bersebelahan dengan urutannya
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp


data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Bubble sort Descending:")
bubbleSort(data)
print(data)

# Output
# 17, 20, 26, 31, 44, 54, 55, 77, 93
# 93, 77, 55, 54, 44, 31, 26, 20, 17


def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] < alist[i + 1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum = passnum - 1


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist)
print("")
print("Short Bubble sort Descending:")
print(alist)
