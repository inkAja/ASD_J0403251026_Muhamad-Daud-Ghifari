# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 6
# ====================================================================
# Latihan 1 : Insertion sort Descending
# ====================================================================


def insertionSortDescending(data):
    for index in range(1, len(data)):

        currentValue = data[index]
        position = index
        while position > 0 and data[position - 1] < currentValue:
            data[position] = data[position - 1]
            position = position - 1
            data[position] = currentValue


data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSortDescending(data)
print("Insertion Sort Descending:")
print(data)
