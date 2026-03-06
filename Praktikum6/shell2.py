# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 6
# ====================================================================
# Latihan 1 : Shell sort Descending
# ====================================================================


def shellSortDescending(data):
    sublistcount = len(data) // 2
    while sublistcount > 0:

        for starposition in range(sublistcount):
            gapInsertionSort(data, starposition, sublistcount)
        print("After increments of size ", sublistcount, "The list is", data)
        sublistcount = sublistcount // 2


def gapInsertionSort(data, start, gap):
    for i in range(start + gap, len(data), gap):
        currentValue = data[i]
        position = i
        while position >= gap and data[position - gap] < currentValue:
            data[position] = data[position - gap]
            position = position - gap
        data[position] = currentValue


data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSortDescending(data)
print("Shell Sort Descending:")
print(data)
