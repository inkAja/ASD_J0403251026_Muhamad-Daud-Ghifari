# ====================================================================
# Praktikum 6
# ====================================================================
# Soal : Merge sort ascending
# Pak Budi adalah seorang manager sumber daya manusia di suatu perusahaan. Ia
# saat ini harus menseleksi pelamar kerja berdasarkan skor tes potensi akademik
# mereka. Skor tersebut disajikan dalam bentuk list dengan rentang nilai 0 - 100.
# Berikut adalah data hasil tes potensi akademik yang tersedia:
# [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]
# ====================================================================

# ====================================================================
# Soal:
# 1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah
# skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
# 2. Kandidat berapa saja yang lolos?
# ====================================================================


def insertionSort(data):

    data_index = []  # untuk menyimpan nomor urut dan nilai
    for i in range(len(data)):
        data_index.append((data[i], i + 1))  # Masukan ke list dalam bentuk tuple

    for index in range(1, len(data_index)):
        currentValue = data_index[index]

        position = index
        while position > 0 and data_index[position - 1] < currentValue:
            data_index[position] = data_index[position - 1]
            position = position - 1
            data_index[position] = currentValue
    return data_index[:5]


data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
kandidat = insertionSort(data)

nilai_kandidat = [
    item[0] for item in kandidat
]  # ambil item index ke 0 dari tuple dalam list
# Soal 1
print("Skor kandidat tertinggi hingga terendah:")
print(nilai_kandidat)

nomor_kandidat = [
    item[1] for item in kandidat
]  # ambil item index ke 1 dari tuple dalam list
# Soal 2
print("Kandidat ke berapa saja yang lolos:")
print(nomor_kandidat)
