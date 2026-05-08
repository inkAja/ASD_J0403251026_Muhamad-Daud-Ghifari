# ====================================================================
# Nama  : Muhamad Daud Ghifari
# NIM   : J0403251026
# Kelas : TPL A2
# ====================================================================

# ====================================================================
# Praktikum 11
# ====================================================================
# Tugas Praktikum 3 - Konversi Matrix ke List
# matriks = [
# [0,1,1,0],
# [1,0,1,0],
# [1,1,0,1],
# [0,0,1,0] ]
# ====================================================================


def konversi(matriks):
    panjang_matriks = len(matriks)

    # buat listnya berdasarkan panjang matriks
    adj = [[] for _ in range(panjang_matriks)]

    for i in range(panjang_matriks):
        for j in range(panjang_matriks):
            # mengirimkan nilai ke variabel adj jika nilai di dalam matriks adalah 1
            if matriks[i][j] == 1:
                adj[i].append(j)
    return adj


if __name__ == "__main__":
    matriks = [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 0]]
    adj = konversi(matriks)
    print("Representasi matriks dalam bentuk Adjacency List: ")
    for i in range(len(matriks)):
        print(f"{i}:", end=" ")
        for j in adj[i]:
            print(f"{j}", end=" ")
        print()
