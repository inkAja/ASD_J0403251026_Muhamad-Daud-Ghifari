# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 6
# ====================================================================
# Latihan 1 : Selection sort Descending
# ====================================================================


def selectionSortDecending(data):
    for fillslot in range(len(data) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if data[location] < data[positionOfMax]:
                positionOfMax = location

        # Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp


data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSortDecending(data)
print("Selection Sort: ")
print(data)
