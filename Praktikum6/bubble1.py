# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 6
# ====================================================================
# Latihan 1 : Bubble sort ascending
# ====================================================================


def bubbleSort(data):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]>data[i+1]:
                # Tukar dua data bersebelahan dengan urutannya
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

data = [54,26,93,17,77,31,44,55,20]
bubbleSort(data)
print("Bubble sort:")
print(data)

#Output
#17, 20, 26, 31, 44, 54, 55, 77, 93

def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist) -1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchange = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum - 1

alist = [20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print("")
print("Short Bubble sort:")
print(alist)

#Output
#20, 30, 40, 50, 60, 70, 80, 90, 100, 110